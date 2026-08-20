# <项目标题>

[English](README.md)

## 研究目标

简要说明本项目要回答的科研问题。未知内容应明确保留为待解决事项，不提前编造研究假设或结论。

## Notebook 顺序

1. `notebooks/01_<step>.ipynb` — 当前研究步骤和预期产出。

只列出当前研究计划已经明确需要的 notebook。

## 本地与远端文件

- 本地：`README.md`、`README.zh-CN.md`、`notebooks/`、`src/`、`config/` 和 `.vscode/tasks.json`。
- 远端：同步后的 `src/` 和 `config/`，以及大型 `data/` 和 `results/` 文件。
- Notebook 保存在本地，其中的 Python 代码通过所选远端 Jupyter kernel 运行。
- 图、表和文字显示通过 Jupyter 返回；写入磁盘的文件默认仍保存在远端。

## 环境与执行

- Machine profile：`<machine-id>`
- 远端项目根目录：`<absolute-remote-project-root>`
- Jupyter server 环境：`<jupyter-server-environment-name>`
- Notebook kernel：`<kernel-display-name>`（`<notebook-kernel-environment-name>`）
- Scheduler：`<scheduler-type>`

远端机器、软件和 scheduler 规则来自 `remote-hpc-operator` 中对应的机器 profile。

## 手动工作流

1. 在本地编辑 notebook、`src/` 或 `config/`。
2. 修改 `src/` 或远端需要读取的配置后，在 VS Code 中运行 `Sync <project> to <machine>`。
3. 在本地 notebook 中选择通过 SSH tunnel 连接的远端 kernel。
4. 手动运行 Codex 交接中指定的单元格，并检查其输出。
5. 大型任务通过目标集群允许的 scheduler 手动提交。

项目配置完成后，Codex 会询问是否需要启动远端 Jupyter Lab 并建立本地 SSH tunnel。用户确认后，Codex 应返回经过验证的 VS Code Existing Jupyter Server URL、kernel 选择和安全停止方法。
