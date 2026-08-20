# <Project title>

[中文说明](README.zh-CN.md)

## Research objective

Briefly describe the scientific question addressed by this project. Leave unknown details as explicit open items rather than inventing hypotheses or conclusions.

## Notebook order

1. `notebooks/01_<step>.ipynb` — Current research step and expected output.

List only notebooks that are already justified by the research plan.

## Local and remote files

- Local: `README.md`, `README.zh-CN.md`, `notebooks/`, `src/`, `config/`, and `.vscode/tasks.json`.
- Remote: synchronized `src/` and `config/`, plus large `data/` and `results/` files.
- Notebooks remain local, while their Python code runs through the selected remote Jupyter kernel.
- Figures, tables, and text displays return through Jupyter; files written to disk remain remote by default.

## Environment and execution

- Machine profile: `<machine-id>`
- Remote project root: `<absolute-remote-project-root>`
- Jupyter server environment: `<jupyter-server-environment-name>`
- Notebook kernel: `<kernel-display-name>` (`<notebook-kernel-environment-name>`)
- Scheduler: `<scheduler-type>`

Remote machine, software, and scheduler rules come from the corresponding `remote-hpc-operator` machine profile.

## Manual workflow

1. Edit notebooks, `src/`, or `config/` locally.
2. After changing `src/` or remote-consumed configuration, run `Sync <project> to <machine>` in VS Code.
3. Select the remote kernel connected through the SSH tunnel in the local notebook.
4. Manually run the cells identified in the Codex handoff and inspect their outputs.
5. Submit large workloads manually through the scheduler allowed by the target cluster.

After project configuration is complete, Codex will ask whether to start remote Jupyter Lab and establish the local SSH tunnel. If confirmed, Codex should return a verified VS Code Existing Jupyter Server URL, kernel choice, and safe shutdown procedure.
