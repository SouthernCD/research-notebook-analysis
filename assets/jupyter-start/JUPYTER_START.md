# Start Jupyter Lab for this project

[中文说明](JUPYTER_START.zh-CN.md)

This file contains private, project-specific remote connection details. It is ignored by `.gitignore` and must not be committed. Never paste a Jupyter token, password, private key, current PID, or allocation ID into this file.

The values and commands below are templates. During project initialization, Codex must replace every angle-bracket placeholder with values verified from `config/project.yaml` and the selected `remote-hpc-operator` machine profile.

## 1. Reach the allowed execution node

Follow the machine profile's SSH and scheduler topology. Do not run Jupyter computation on a login node unless that profile explicitly permits it.

**[LOCAL]**

```bash
<ssh-login-command>
```

**[REMOTE LOGIN]**

```bash
<interactive-allocation-or-compute-node-command>
```

If the profile permits direct SSH to the execution node, the generated guide may replace these commands with that verified route.

## 2. Start Jupyter Lab

Run this on the node that will own the Jupyter loopback socket.

The `nohup` example below is usable only when the selected machine profile permits this persistence method. For scheduler-owned sessions, replace it with the documented allocation/session lifetime method before generating the project guide; `nohup` does not keep an expired allocation alive.

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

If the process exits, inspect the displayed log before opening a tunnel. Do not disable token authentication. If the port is already in use, first check whether it is the intended existing service; otherwise choose a free port and update both the project configuration and tunnel command consistently.

## 3. Open the local SSH tunnel

Keep this foreground command running in a dedicated local terminal. Stop it later with `Ctrl-C`.

**[LOCAL]**

```bash
<profile-derived-loopback-tunnel-command>
```

The generated command must bind `127.0.0.1:<local-port>` to the execution node's `127.0.0.1:<remote-port>`, include `ExitOnForwardFailure=yes`, and use keepalive options. ProxyJump or nested hops must come from the machine profile.

## 4. Connect from VS Code

Read the current token-bearing URL from the remote log; do not copy it into this file:

**[REMOTE COMPUTE]**

```bash
PROJECT_ROOT="<absolute-remote-project-root>"
LOG="$(cat "$PROJECT_ROOT/runs/jupyter/current.log")"
grep -E 'http://127\.0\.0\.1:|token=' "$LOG" | tail -n 5
```

Replace the remote port in that runtime URL with the configured local port, producing:

```text
http://127.0.0.1:<local-port>/?token=<current-runtime-token>
```

In VS Code:

1. Open the local notebook and its **Kernel Picker**.
2. Choose **Select Another Kernel**.
3. Choose **Existing Jupyter Server**.
4. Enter the current local URL.
5. Select `<kernel-display-name>`.
6. Run only the initialization cell and confirm hostname, working directory, `sys.executable`, and environment prefix before analysis.

## 5. Stop this session safely

First stop the local tunnel with `Ctrl-C`. Then stop only the exact Jupyter PID recorded for this project:

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

If an interactive allocation was created for this session, release that exact allocation using the machine profile's documented command only after Jupyter has stopped. Never use `pkill jupyter` or cancel an allocation that may contain unrelated work.
