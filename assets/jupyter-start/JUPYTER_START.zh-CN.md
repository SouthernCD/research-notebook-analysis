# 为本项目启动 Jupyter Lab

[English](JUPYTER_START.md)

本文件包含项目专用的私有远端连接信息。它由 `.gitignore` 忽略，不得提交。不要把 Jupyter token、密码、私钥、当前 PID 或 allocation ID 写入本文件。

以下值和命令是模板。初始化项目时，Codex 必须根据 `config/project.yaml` 和选定的 `remote-hpc-operator` 机器 profile 验证并替换所有尖括号占位符。

## 1. 到达允许的执行节点

按照机器 profile 规定的 SSH 和 scheduler 拓扑操作。除非 profile 明确允许，否则不要在 login node 上运行 Jupyter 计算。

**[LOCAL]**

```bash
<ssh-login-command>
```

**[REMOTE LOGIN]**

```bash
<interactive-allocation-or-compute-node-command>
```

如果 profile 允许直接 SSH 到执行节点，生成的指南可以把上述命令替换为经过验证的直接连接路径。

## 2. 启动 Jupyter Lab

在将要持有 Jupyter loopback socket 的节点上运行：

下方 `nohup` 示例仅在选定机器 profile 允许这种持久运行方式时适用。对于 scheduler 管理的会话，生成项目指南前应替换为该机器规定的 allocation/session 生命周期方式；`nohup` 不能维持已到期的 allocation。

**[REMOTE COMPUTE]**

```bash
PROJECT_ROOT="<absolute-remote-project-root>"
ACTIVATE="<jupyter-server-activation-script>"
REMOTE_PORT=<remote-port>

cd "$PROJECT_ROOT"
source "$ACTIVATE"
mkdir -p runs/jupyter

STAMP="$(date +%Y%m%d-%H%M%S)"
LOG="$PROJECT_ROOT/runs/jupyter/jupyter-$STAMP.log"
PIDFILE="$PROJECT_ROOT/runs/jupyter/jupyter-$STAMP.pid"

nohup <jupyter-server-command> \
  --no-browser \
  --ip=127.0.0.1 \
  --port="$REMOTE_PORT" \
  --ServerApp.port_retries=0 \
  --ServerApp.open_browser=False \
  >"$LOG" 2>&1 </dev/null &

SERVER_PID=$!
printf '%s\n' "$SERVER_PID" >"$PIDFILE"
printf '%s\n' "$LOG" >runs/jupyter/current.log
printf '%s\n' "$PIDFILE" >runs/jupyter/current.pidfile

sleep 3
ps -p "$SERVER_PID" -o pid=,stat=,cmd=
grep -E 'http://127\.0\.0\.1:|token=' "$LOG" | tail -n 5
```

如果进程退出，先检查显示的日志，再建立 tunnel。不要关闭 token authentication。如果端口已被占用，应先确认它是否为预期的现有服务；否则选择空闲端口，并同步更新项目配置和 tunnel 命令。

## 3. 打开本地 SSH tunnel

在独立的本地终端中保持此前台命令运行；结束时使用 `Ctrl-C`。

**[LOCAL]**

```bash
<profile-derived-loopback-tunnel-command>
```

生成的命令必须把 `127.0.0.1:<local-port>` 转发到执行节点的 `127.0.0.1:<remote-port>`，包含 `ExitOnForwardFailure=yes` 和 keepalive 选项。ProxyJump 或嵌套跳转必须来自机器 profile。

## 4. 在 VS Code 中连接

从远端日志读取当前带 token 的 URL；不要把它复制到本文件：

**[REMOTE COMPUTE]**

```bash
PROJECT_ROOT="<absolute-remote-project-root>"
LOG="$(cat "$PROJECT_ROOT/runs/jupyter/current.log")"
grep -E 'http://127\.0\.0\.1:|token=' "$LOG" | tail -n 5
```

把运行时 URL 中的远端端口替换为配置的本地端口，得到：

```text
http://127.0.0.1:<local-port>/?token=<current-runtime-token>
```

在 VS Code 中：

1. 打开本地 notebook 及其 **Kernel Picker**。
2. 选择 **Select Another Kernel**。
3. 选择 **Existing Jupyter Server**。
4. 输入当前本地 URL。
5. 选择 `<kernel-display-name>`。
6. 只运行初始化 cell，确认 hostname、工作目录、`sys.executable` 和环境前缀后再开始分析。

## 5. 安全停止本次会话

先用 `Ctrl-C` 停止本地 tunnel，再只停止为本项目精确记录的 Jupyter PID：

**[REMOTE COMPUTE]**

```bash
PROJECT_ROOT="<absolute-remote-project-root>"
PIDFILE="$(cat "$PROJECT_ROOT/runs/jupyter/current.pidfile")"
SERVER_PID="$(cat "$PIDFILE")"

case "$SERVER_PID" in
  ''|*[!0-9]*) echo "Invalid recorded PID" >&2; exit 1 ;;
esac

ps -p "$SERVER_PID" -o pid=,stat=,cmd=
kill "$SERVER_PID"
```

如果本次会话创建了 interactive allocation，应在 Jupyter 停止后，仅使用机器 profile 规定的命令释放该精确 allocation。绝不使用 `pkill jupyter`，也不要取消可能包含其他工作的 allocation。
