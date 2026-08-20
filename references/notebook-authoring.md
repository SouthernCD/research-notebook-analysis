# Notebook Authoring

Use this guide when creating or editing notebooks and their nearby `src/` files.

## Research Record

Prefer a small sequence of meaningful Markdown and code cells over a software-style abstraction layer.

- Before code, state the scientific question or operation.
- After important code, explain how the user should interpret the expected output.
- Record biological or technical reasons for filtering and parameter choices.
- Preserve uncertainty and say what observation would resolve it.
- Keep saved outputs when they remain consistent with the code.
- When code changes make an old output misleading, clear only the affected output or tell the user to rerun that cell; do not imply the new output already exists.

## Bilingual Narrative Cells

All newly created or modified notebook narrative must use two consecutive Markdown cells:

1. English first;
2. equivalent Chinese immediately after;
3. then the associated code cell, when any.

Do not combine both languages into one Markdown cell. Code cells, generated outputs, and code identifiers remain single; do not duplicate code merely to create a bilingual presentation.

Keep each pair semantically aligned:

- use corresponding heading levels and section numbers;
- preserve the same scientific claims, uncertainty, parameters, paths, filenames, variable names, and warnings;
- translate prose naturally rather than mechanically, without adding facts to only one language;
- update both cells whenever either member's meaning changes.

For an existing monolingual notebook, create the missing language partner next to each Markdown cell touched by the current request. Preserve untouched historical cells unless the user asks to convert the whole notebook.

## Remote Initialization Cell

Adapt this pattern to the project configuration:

```python
from pathlib import Path
import os
import socket
import sys

%load_ext autoreload
%autoreload 2

PROJECT_ROOT = Path("/absolute/remote/project/root")
assert PROJECT_ROOT.is_dir(), f"Remote project does not exist: {PROJECT_ROOT}"

os.chdir(PROJECT_ROOT)

print(f"Host: {socket.gethostname()}")
print(f"Working directory: {Path.cwd()}")
print(f"Python executable: {sys.executable}")
print(f"Environment prefix: {os.environ.get('CONDA_PREFIX', '<not set>')}")
```

The path is interpreted by the remote kernel. The user should verify that hostname is an allowed remote node, cwd equals the configured remote project root, and the Python executable/environment matches the configured kernel environment. A mismatched kernel is a configuration or VS Code selection problem, not a reason to silently install packages into the active environment.

If `src/` is not importable through the chosen project layout, add the minimum explicit path setup:

```python
import sys

SRC_DIR = PROJECT_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))
```

Do not build or install a Python package merely to avoid this small notebook-local setup.

## Notebook Versus `src/`

Keep code in the notebook when it is short, specific to one analysis step, and improves the visible reasoning trail.

Use `src/` when code is:

- reused by more than one cell or notebook;
- long enough to obscure the scientific flow;
- easier to test or review as a function;
- a shell pipeline, scheduler job, or other command that should not execute accidentally inside a cell.

Functions imported from `src/*.py` must not perform work at import time. After a local edit, the user must run the VS Code sync task before rerunning the import/call cell. `%autoreload 2` normally reloads changed modules; use explicit `importlib.reload()` only when autoreload is unsuitable for the package.

Do not use `subprocess.run`, `!cmd`, or shell magics for substantial, file-changing, or long-running HPC commands. Put them in a descriptive `src/*.sh` or scheduler file with Chinese comments covering purpose, inputs, outputs, environment, resources, and manual invocation.

## Precise Cell Targeting

Use an AI task marker when the user wants a change in one exact cell. Do not ask the user to count cells or rely on a position that will drift when cells are inserted, deleted, or moved.

For a code cell, the user places this as its first non-empty line:

```python
# ai todo cell
```

For a Markdown cell, use an HTML comment so the marker does not become a rendered heading:

```markdown
<!-- ai todo cell -->
```

The marker locates the primary target cell. The accompanying user request supplies the task. Do not infer the requested change from the marker alone.

For a bilingual narrative task, place the marker in the English Markdown cell. Treat the immediately following Chinese Markdown cell as part of the same target, update both together, and keep the completion marker only in the English cell. If the Chinese partner is absent, create it as part of the requested edit.

### Resolution Rules

1. Inspect the named notebook and search cell sources for an exact todo marker on the first non-empty line.
2. Require exactly one unfinished marker:
   - zero: ask the user to place and save the appropriate marker;
   - more than one: list each marker's cell type and a short nearby source preview, then ask the user to leave only the intended marker;
   - one: use that cell as the primary edit target.
3. Keep edits scoped to the marked cell and the smallest necessary nearby cells or `src/` files. A bilingual Markdown partner is required scope, not an unrelated expansion. Disclose every additional edit in the handoff.
4. If the result requires splitting or inserting cells, put the done marker on the primary resulting cell and identify the other inserted cells by heading or purpose.
5. Convert the marker only after the requested file edit is complete. If blocked, ambiguous, or partially implemented, preserve the todo marker.

### Completion Marker

Replace the code marker with:

```python
# ai done: qc-missingness-plot
```

For Markdown:

```markdown
<!-- ai done: explain-missingness-threshold -->
```

Choose a short lowercase kebab-case slug that describes the cell's scientific role. Check existing `ai done` markers in the same notebook and make the slug unique by adding meaningful context rather than relying on cell position.

Keep completed markers in place as lightweight, stable references. A user can request later work by naming the slug or by changing that marker back to the corresponding todo form.

`ai done` records editing status only. It does not mean:

- the cell was executed;
- remote files were synchronized;
- outputs were regenerated;
- the scientific result was verified.

State those statuses separately in the handoff.

## Outputs

Remote execution can return rich display data to the local notebook without transferring the underlying dataset:

- `DataFrame` previews and text are rendered locally through Jupyter;
- Matplotlib figures are computed remotely and displayed locally;
- files written to `data/`, `results/`, or other remote paths remain remote unless the user explicitly requests a download.

Do not assume a remote result exists locally or that a local file exists remotely.

## Whole-Notebook Execution

Do not run individual cells or the notebook by default. Only enter execution mode when the user explicitly asks to run the entire named notebook.

Before execution:

1. confirm the exact notebook path;
2. confirm the intended remote kernelspec and environment;
3. confirm the configured remote project root;
4. verify the execution node and resource policy through `remote-hpc-operator`;
5. ensure required `src/` and `config/` changes were synchronized;
6. identify whether execution will overwrite remote result files.

After execution, report whether the notebook completed, the first failing cell if any, and where executed notebook outputs and remote result files were written. Never report scientific conclusions beyond what the actual outputs support.

## Required Handoff

Use a compact form such as:

```text
改动：notebooks/01_qc.ipynb 的 qc-missingness-plot。
定位：# ai done: qc-missingness-plot
同步：不需要；本次只修改 notebook。
运行：请重新运行该 cell。
检查：确认图例按 population 分组，样本数与上一单元格一致。
手动命令：无。
```

If `src/` or remote-consumed `config/` also changed, replace the sync line with the exact VS Code task and tell the user to sync before rerunning the marked cell. Omit irrelevant lines only when the remaining handoff is still unambiguous. Explicitly state when no sync or run is needed.
