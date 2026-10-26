# <Project title>

[中文说明](README.zh-CN.md)

## Research objective

Briefly describe the scientific question addressed by this project. Leave unknown details as explicit open items rather than inventing hypotheses or conclusions.

## Getting started

Start with the current research question, available input paths/formats and identifiers, and the first table, figure, or check you want to inspect. A full analysis plan is not required. File descriptions and small examples are usually enough to begin; do not copy large datasets locally just to open the project.

Identify this project's first notebook and its input preparation here. State which cells to run first, what output to inspect, and any choices still pending. After remote setup is confirmed, follow the private `JUPYTER_START.md` guide to connect. Synchronize source changes with the named VS Code task before running their import/call cells. The agent prepares code; analysis is not run automatically.

## Notebook order

1. `notebooks/01_<step>.ipynb` — Current research step and expected output.

List only notebooks that are already justified by the research plan. Number them by scientific stage and dependency order; keep the directory tree shallow and add files only for current needs.

During analysis and debugging, each working notebook contains adjacent English/Chinese narrative cells and one shared set of code cells. Only at final publication preparation may separate language directories be useful; they are optional publication copies derived from the same finalized bilingual source, with identical code and corresponding sections/figures.

## Data and reproducibility boundary

- `data/source/`: externally supplied, read-only inputs, which may include documented analysis-ready derivatives.
- `data/results/`: analysis products, including intermediate tables, models, external-program outputs, figure data, and final outputs.

Describe the actual source inputs, their provenance and acquisition, the starting point for reproduction, and upstream processing outside this project. Preserve an established data layout instead of migrating it just to match this example.

Scientific parameters are normally stated near their use in notebooks. Shared definitions may live in `config/` when reused across analyses; document their authoritative source.

## Analysis implementation

Keep short analysis code in notebooks and project-specific helpers or plotting in project-root `src/`. When a complete analysis tool needs an independent interface and internal structure, place it under `tools/<tool-name>/`. Create only the structure it needs; packaging, a CLI, and focused tests are optional. Maintain paired tool READMEs for inputs, outputs, invocation, and dependencies. Pass project paths and parameters explicitly; tool code does not import project-root `src/`. Keep analysis products and runtime files in the project data/runtime layout. Notebook cells expose the research choices and launch the tool. Include existing tool source in the manual sync task, excluding environments, caches, and build/runtime artifacts; syncing source does not install a package.

### Optional tool layout

For example, a standalone window-summary tool could use this small layout. This is a style illustration; create it only when the project needs such a tool.

```text
tools/
└── window_summary/
    ├── README.md
    ├── README.zh-CN.md
    └── main.py
```

The paired tool READMEs describe its scientific purpose, input columns and coordinates, output columns, dependencies, and invocation. `main.py` provides the tool interface and implementation without importing project-root `src/`. Add a package layout, dependency file, or focused tests only as the tool needs them.

For a CLI using the notebook kernel's environment, a notebook calculation cell might call the interface below. The tool and flags are illustrative and must be implemented/documented before use:

```python
import subprocess
import sys

input_file = f'{source_dir}/variants.csv'
window_size = 500
output_file = f'{results_dir}/variant_windows.b{window_size}.csv.gz'
subprocess.run([
    sys.executable, f'{project_dir}/tools/window_summary/main.py',
    '--input', input_file, '--output', output_file,
    '--window-size', str(window_size),
], check=True)
```

The notebook owns the research choices; the tool owns calculation and output completion. A later plotting cell loads `output_file` and applies the shared plotting style. Keep outputs outside the tool directory. Add `${workspaceFolder}/tools` to the manual sync task only once the directory exists; transfer source and documentation while excluding environments and build/runtime artifacts. A different tool environment needs its own confirmed interpreter or launcher.

## Local and remote files

- Local: `README.md`, `README.zh-CN.md`, `notebooks/`, `src/`, optional `tools/`, `config/`, and `.vscode/tasks.json`.
- Private local guides: `JUPYTER_START.md` and `JUPYTER_START.zh-CN.md`; both are project-specific and ignored by Git.
- Remote: synchronized `src/`, existing `tools/`, and `config/`, plus large source inputs and analysis products under `data/` (or the project's established layout).
- Notebooks remain local, while their Python code runs through the selected remote Jupyter kernel.
- Figures, tables, and text displays return through Jupyter; files written to disk remain remote by default.

## Environment and execution

- Machine profile: `<machine-id>`
- Remote project root: `<absolute-remote-project-root>`
- Jupyter server environment: `<jupyter-server-environment-name>`
- Notebook kernel: `<kernel-display-name>` (`<notebook-kernel-environment-name>`)
- Scheduler: `<scheduler-type>`

Remote machine, software, and scheduler rules come from the corresponding `remote-hpc-operator` machine profile.

## Notebook workflow

1. Edit notebooks, `src/`, existing `tools/`, or `config/` locally.
2. After changing `src/`, `tools/`, or remote-consumed configuration, run `Sync <project> to <machine>` in VS Code.
3. Follow `JUPYTER_START.md` to start Jupyter on the allowed remote node and open the local SSH tunnel.
4. In VS Code, connect to the Existing Jupyter Server URL and select the configured kernel.
5. Manually run the cells identified in the Codex handoff and inspect their outputs.
6. Launch external tools or large scheduler-backed analyses from their explicit notebook cells; inspect logs/job status and confirm completion before downstream cells.

Reusable steps define expected outputs and load complete, compatible results when available. Display reused paths and relevant metadata; file existence alone does not establish compatibility with current inputs and parameters. Identify affected outputs before intentionally repeating a step. Substantial calculation cells save reusable results so later notebook sessions can skip completed steps. Cell-internal loops normally show progress only; finer checkpoints are optional when needed. Use pandas with `.csv.gz` for small tables and one `.h5` file per large table (key `df`). Build paths with `os` and f-strings. Calculation and plotting use separate cells; plotting reads saved statistics and always exports its actual data as `.csv.gz` for publication inspection. Multi-step work reports timestamps and elapsed time; substantial loops use `tqdm` for progress and rate. The notebook is the complete entry point for the defined analysis: source files contain implementation, while cells expose and launch each step with its key parameters. Outside-notebook analysis actions require a stated exception.

For a shared repository, provide sanitized project and sync-task examples while keeping real machine-specific settings private.

The project-specific startup guides are generated after remote configuration is verified. Codex starts or manages the service only when explicitly asked.

Project figures use `src/plot_style.py`; call `set_plot_style()` in notebook initialization. Individual figures may vary in size and layout while retaining the shared typography and line widths.
