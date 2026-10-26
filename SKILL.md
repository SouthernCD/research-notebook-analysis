---
name: research-notebook-analysis
description: Assist with local scientific Jupyter notebooks whose kernels, data, and results live on remote HPC systems. Use for notebook-centered research projects, local-to-HPC source synchronization through VS Code tasks, remote Jupyter workflows, and preparing analysis code or scheduler jobs for the user to run. Pair with remote-hpc-operator for any actual remote access, software, environment, node, or scheduler work.
---

# Research Notebook Analysis

## Core Philosophy

Act as a scientific notebook copilot. Prepare, edit, explain, and hand work back to the user; let the user run it and judge the scientific result.

The notebook is the complete, readable entry point for reproducing the project's defined analysis scope. A reader should see every step, its inputs/outputs and key scientific/resource parameters, and launch it from cells. `src/` and optional `tools/<tool-name>/` hold implementation; the project workflow remains launchable from notebook cells. External tools and scheduler jobs may be launched explicitly from notebook cells; only specifically justified or user-requested exceptions require an outside-notebook analysis action. This design goal does not authorize the agent to execute those cells.

By default:

- Inspect the existing notebook, its saved outputs, and nearby project files.
- Edit or add notebook Markdown/code cells and place project helpers under `src/` or a coherent independent analysis tool under `tools/<tool-name>/`.
- Prepare configuration, source implementations, external-tool launch cells, and scheduler files without executing them as the agent.
- Do not execute notebook cells, submit jobs, start large analyses, or infer permission to run from a request to write, fix, diagnose, or explain.
- Prefer static checks and a precise manual run handoff over executing code for verification.

Run a notebook only when the user explicitly asks to run the entire named notebook. Before remote execution, confirm the notebook, kernel, remote project root, execution node, and resource policy. For HPC execution, follow the remote integration rules below.

Focused regression checks prepared for a style-unification stage may also run when the user explicitly authorizes those checks and their execution context. This exception does not authorize arbitrary cell execution or large workloads. Keep code-editing, service-management, notebook-execution, and comparison-test permissions distinct.

Remote Jupyter is user-managed by default. After project configuration is complete, create a private, project-specific bilingual startup guide at the project root so the user can start Jupyter and its SSH tunnel without asking Codex each time. Start or manage the service directly only when the user explicitly requests that remote action; such authorization never extends to notebook cells, pipelines, or batch jobs.

## Scope and Boundaries

Use this skill for notebook-centered scientific analysis where:

- notebooks are edited and retained locally;
- the selected Jupyter kernel executes on a remote HPC system;
- human-written source and configuration are synchronized manually;
- large data, intermediate products, and result files normally remain remote;
- figures, tables, and text outputs return through the Jupyter protocol for local display.

Do not use it for unrelated software engineering or for building an automated workflow platform. Do not recreate Jupyter, VS Code Remote SSH, a file-watching sync daemon, or a project-management CLI.

## New User Guidance

When the user says they are new, asks how to begin, or needs help understanding the local-notebook/remote-kernel workflow, read [references/new-user-guidance.md](references/new-user-guidance.md). Briefly explain the collaboration model, then help clarify the research question, available data, and desired first deliverable. Ask only the next necessary questions, using supplied context instead of repeating them. Missing configuration alone does not imply inexperience.

Accept an incomplete research plan. Help identify one feasible first step without inventing methods or findings. Start with file locations, formats, identifiers, processing history, and small examples rather than asking for full large datasets. Introduce environment, synchronization, and startup details when the work reaches that stage. Experienced users with a concrete request can proceed directly; onboarding does not expand scope or execution permission.

## New Project Initialization

When the user asks to start a new research project with this skill, read [references/project-setup.md](references/project-setup.md) before creating files. Establish the research question, available inputs and reproducibility starting point, local location, and first meaningful analysis step. Ask only for missing information that affects current work; do not invent later analyses, parameters, or findings.

Confirm the project's remote choices through the readiness gate, then build the minimum project and its first useful notebook, with source only where needed. Read the writing examples rather than copying them into the project; adopt the shared plotting module when figures are needed. Set up manual synchronization and generate private bilingual startup guides only after remote configuration is verified. Finish with static checks, a precise manual handoff, and a local Git initialization snapshot of shareable code/documentation unless the user chooses otherwise. Do not push or silently install software, create remote directories, start services, or run analysis.

Initialization is complete when the project organization, confirmed environment, first notebook, and startup/sync instructions are ready for the user to work. It is not completion or execution of the whole research workflow. If necessary choices remain missing, report a partial scaffold and the exact pending decisions, rather than calling it ready.

## Existing Projects and Style Unification

Default to incremental editing: apply these conventions to new or modified portions and necessary dependencies, preserving the rest of the existing project. Invoking the skill alone does not authorize a repository-wide rewrite.

When the user explicitly requests whole-project style unification, read [references/project-style-unification.md](references/project-style-unification.md) before editing. Work one notebook and its necessary source dependencies at a time: preserve a Git baseline, prepare the changes and result comparisons, obtain authorization to run the named notebook on the configured HPC, verify behavior and scientific results, request user inspection, then commit the accepted stage before starting the next notebook. Do not finish the entire repository in one sweep or advance past unresolved differences or pending user review. Existing-project preservation rules do not exempt the current authorized notebook from style unification; scientific behavior remains the priority.

An explicit style-unification request includes the local Git snapshots required by this workflow, but does not itself authorize remote execution. An explicit user approval to run the entire named notebook satisfies the execution requirement below; do not ask again for an unchanged execution already authorized. Human acceptance of the current notebook is required before committing its accepted stage and moving on.

## Remote HPC Integration

Any task involving SSH, remote inspection, transfer, Jupyter startup, software, environments, nodes, allocations, or scheduler operations must also use `remote-hpc-operator`.

Apply this authority order:

1. The target machine profile defines SSH topology, authentication, node roles, allowed storage roots, software root, environment policy, scheduler, queues, and cluster limits.
2. This project's `config/project.yaml` selects the project root, Jupyter/kernel settings, and requested resources within those limits.
3. If project configuration conflicts with the machine profile, stop and report the conflict. Do not silently substitute a path, node, environment, or resource request.

Software discovery, reuse, installation, micromamba environments, activation scripts, `AGENT_SOFTWARE.md`, and network-node selection must strictly follow `remote-hpc-operator`. Do not install reusable software into the project directory or scratch space merely for convenience.

Never assume a login node permits scientific computation. Use an allowed interactive compute allocation for lightweight interactive analysis and scheduler batch jobs for large work. The agent must not run large bioinformatics tools or other workloads without execution authorization. Preparing an explicit notebook cell that the user can run to invoke such work is allowed and expected when it belongs to the analysis.

Label runnable commands by execution context:

- `[LOCAL]`
- `[REMOTE LOGIN]`
- `[REMOTE COMPUTE]`
- `[SCHEDULER JOB]`

## Project Readiness Gate

When initializing a project or first opening an existing project, inspect `config/project.yaml` before preparing remote-dependent code. Treat missing fields, empty values, and angle-bracket template placeholders as unset.

This gate controls remote setup and execution, not independent local edits. For a small notebook/source edit, preserve available project configuration and continue changes that do not depend on missing choices; do not launch SSH checks or demand full environment selection merely to polish prose, plot styling, or a self-contained function. Ask only when the current work actually depends on an unresolved path/environment/resource choice.

Do not proceed with remote setup until the user has explicitly chosen:

- the `remote-hpc-operator` machine profile;
- the absolute remote project root;
- the micromamba, conda, module, or other documented environment used by the Jupyter server;
- the environment and kernelspec used by the notebook kernel;
- whether the server and kernel intentionally share one environment.

Read the remote machine index and selected profile before presenting machine, path, environment, node, or scheduler choices. Never reuse a previous machine as a default. Record confirmed project choices in `config/project.yaml`; keep SSH topology and machine-wide policy in the private machine profile.

For every environment, record its manager, human-readable name, and profile-compliant activation script. If an environment or Jupyter is missing, ask whether to select another documented environment or install/repair it. Installation requires separate authorization and must follow `remote-hpc-operator` software-root and metadata rules.

Validate that the remote root and requested resources are allowed by the machine profile. If the directory does not exist, report that fact and obtain authorization before creating it. Stop on profile/config conflicts rather than filling an assumed value.

After the stable configuration is confirmed, create or refresh `JUPYTER_START.md` and `JUPYTER_START.zh-CN.md` at the project root. Render real project-specific commands from `config/project.yaml` and the selected machine profile; do not leave template placeholders in a working project. Ensure the root `.gitignore` ignores both private guides and `/runs/jupyter/`. Preserve existing ignore rules. The guides must not contain a token, password, private key, or transient PID/allocation value.

Read [references/project-setup.md](references/project-setup.md) for the completeness checklist and template workflow.

## Remote Jupyter Session

Once the readiness gate passes, point the user to the generated private startup guide instead of proactively offering to start Jupyter. The normal handoff is for the user to follow its `[REMOTE LOGIN]`, `[REMOTE COMPUTE]`, and `[LOCAL]` commands, then connect VS Code to the Existing Jupyter Server URL obtained from the runtime log.

If the user explicitly asks Codex to start, reconnect, diagnose, or stop the service, use `remote-hpc-operator` to perform and verify that exact action. Do not silently install Jupyter, fall back to a login node, disable token authentication, or expose the server on a non-loopback interface.

Read [references/remote-jupyter.md](references/remote-jupyter.md) completely before starting, checking, reconnecting, or stopping a remote Jupyter session.

## Lightweight Project Shape

Keep the directory tree shallow and organized by research role. Add a directory or configuration file only for a current concrete need; do not create one per cell, figure, or minor operation. Number notebooks by scientific stage and dependency order, name source modules by analysis domain, and describe their producer/consumer relationships in the paired READMEs. Do not copy a reference project's exact notebook count or topics.

For a new project, start with this minimal research-oriented structure. The notebook name and source files reflect actual needs, not files to generate literally:

```text
project/
├── README.md
├── README.zh-CN.md
├── JUPYTER_START.md          # private, project-specific, gitignored
├── JUPYTER_START.zh-CN.md    # private, project-specific, gitignored
├── .gitignore
├── notebooks/
│   └── 01_<first-step>.ipynb
├── src/
│   └── plot_style.py        # when figures are needed; other source only as required
├── tools/                  # optional; only for a concrete independent analysis tool
│   └── <tool-name>/
├── config/
│   └── project.yaml
├── data/
│   ├── source/              # externally supplied inputs
│   └── results/             # analysis products, including intermediates
└── .vscode/
    └── tasks.json
```

The notebook is the primary research record, presentation surface, and analysis launcher. Keep short, one-off analysis code in the notebook. Move project-specific code to `src/` when it is long, reused, easier to review separately, or represents a shell/batch operation; keep its explicit invocation and key parameters in a notebook cell. Python, shell, and scheduler files may coexist in `src/`; do not add a separate project-root `scripts/` tree by default. A complete analysis tool with defined inputs/outputs and an independent interface belongs in optional `tools/<tool-name>/`, rather than being forced into project-root `src/`. Read [references/project-tools.md](references/project-tools.md) before creating, restructuring, or integrating such a tool. Its internal package, CLI, tests, and dependency files are allowed when useful; do not generate them automatically. Keep scientific choices and explicit launches in the notebook.

Preserve an existing project's data layout. For a new project, `data/source/` and `data/results/` are a useful convention: source inputs may already be analysis-ready; results include intermediates, models, figure data, and final outputs. These are logical remote locations, not directories to populate locally by default.

Keep frequently adjusted scientific parameters visible at their point of use in the notebook. Shared context definitions or comparison catalogs may live in configuration when reused across analyses; identify their authoritative source and avoid conflicting notebook/config copies. Keep machine-specific configuration private and provide sanitized examples when the project is intended for sharing.

At project root, avoid adding `tests/`, `docs/`, `lib/`, `bin/`, `workflow/`, `pipelines/`, packaging metadata, CI, containers, or placeholder modules unless the research task actually requires them. Do not create empty directories with `.gitkeep`.

## Notebook Authoring

The conventions below are the user's default authoring requirements, not optional inspiration. Apply them to new work and the portions touched by an edit, unless the user explicitly requests a different approach. Preserve unrelated existing code and structure. Examples illustrate these requirements; project-specific inputs, parameters, and findings must come from the actual project.

Treat each notebook as a readable, operable lab record. Open with its scientific scope and organize sections by scientific question, analysis object, or research stage, with focused operations beneath them. Keep the visible order aligned with the analysis dependencies; avoid a structure driven by helper names, file formats, or software plumbing. Keep ordinary explanations short; expand scientific rationale, coordinate conventions, denominators, filtering, or uncertainty where they affect interpretation. Concision must not omit definitions needed to understand a result: define derived metrics, comparison/reference populations, window/anchor conventions, and consequential missing-data or tie handling where relevant. Put each definition near its first scientific use and explain complex figures in their captions without repeating the full methods. Do not impose a repeated purpose/input/method/output template on every cell.

Use this default presentation pattern: paired scientific headings, a brief explanation or operation cue, focused calculation/plotting cells, and paired figure captions after the displayed figure. Ordinary narrative usually needs only one or two sentences. Number scientific sections with matching Markdown depth (`## 1`, `### 1.1`, `#### 1.1.1`); describe smaller operations with a short bullet or standalone phrase rather than another numbered heading. Avoid repeating the parent section's title in its child. Put essential reading guidance in the caption when that avoids a separate repetitive interpretation section.

Give principal figures consecutive numbers within each notebook. Place an English caption cell immediately after the plotting cell and its Chinese partner immediately after it. Use a bold figure number and short title, followed only by the explanation needed to read the figure; complex figures may need panel/track order, symbols, units and displayed thresholds. Do not invent results or translate project-specific scientific choices into skill defaults.

Notebook Markdown is for biology readers and reviewers. Keep only the research purpose, analysis content, necessary methodological definitions, and the meaning of figures/results. Use concise, accessible language to explain what is done, why, and how to interpret it, rather than how the code runs.

- Do not describe result reuse, file-existence checks, caches, skipping, forced recomputation, modification-time checks, or other program control logic in Markdown.
- Keep threads, memory, concurrency, invocation details, and other runtime settings in code, not repeated in Markdown.
- Include scientific parameters only when they affect biological interpretation, such as window scale, whether Genic includes flanks, a density denominator, or the meaning of merged intervals in a figure. Do not enumerate code arguments.
- Keep modification logs, refactoring/verification status, synchronization, and task lists in the conversation or Git history. This also applies to code comments/docstrings and printed messages about the agent's edit. Minimal cell-target markers remain locating aids only.
- Apply the same content boundary to both languages. Keep genuine scientific limitations and relevant provenance without generic editing disclaimers.

Make the research purpose, analysis stages, and important output interpretation easy to locate. Put initialization, invocation, resource settings, progress, and resumption logic in code cells; interface docstrings can explain implementation contracts. Preserve established section numbering and expose meaningful scientific stages without technical detail piling up in Markdown.

Keep inputs, output paths, analysis selections, scientific parameters, and actual calls visible in the relevant notebook section. Define shared calculation/plotting settings once in a nearby setup cell; do not hide important scientific choices behind helper defaults or a distant global block. After initialization and section setup, plotting must load saved statistics without requiring the expensive calculation cell or its in-memory objects.

For reusable computations, define expected outputs and reuse complete, compatible results before recomputing. Keep output and cache checks at the layer responsible for the result rather than repeating them throughout the call chain. File existence alone does not establish compatibility with current inputs or parameters. Separate expensive calculation from plotting so display changes can reuse statistical results. Cache handling never authorizes Codex to execute cells or large workloads.

Preserve the user's existing narrative, numbering, and useful saved outputs. Do not invent hypotheses, inputs, results, or interpretations.

Write all newly created or modified narrative material bilingually:

- In notebooks, place an English Markdown cell first and its equivalent Chinese Markdown cell immediately after it. Keep code cells single and untranslated; use English for new code comments, identifiers, table labels, and figure labels unless the user requests another convention.
- Keep paired Markdown cells aligned in heading level, section number, scientific meaning, parameters, paths, identifiers, and caveats.
- When the user revises Chinese prose and selects it as the standard, use its content scope, tone and level of detail to align the English; remove English-only explanations the user removed. Translate naturally, use established English scientific terms, and do not retain editorial terminology hints as parenthetical prose. Preserve genuine scientific constraints and flag factual conflicts rather than silently changing analytical meaning.
- For existing notebooks, add or repair the bilingual pair for Markdown touched by the current task. Do not translate all untouched historical cells unless the user asks for a full migration.
- At project root, maintain `README.md` in English and `README.zh-CN.md` in Chinese with the same structure and facts; link the two files to each other.
- If another standalone prose document is genuinely needed, use `<name>.md` for English and `<name>.zh-CN.md` for Chinese, keep them semantically aligned, and cross-link them. Do not create extra documentation files or a `docs/` tree without a research need.

During analysis, debugging, and revision, retain one working notebook per stage with adjacent English/Chinese Markdown pairs and a single shared set of code cells. Only at final publication preparation, suggest optional language-specific copies such as `notebooks/` and `notebooks.zh-CN/`; do not create or maintain separate language trees during ongoing work. Carry out a split only when the user chooses it as part of final publication preparation. Follow the publication-copy checks in [references/notebook-authoring.md](references/notebook-authoring.md).

Assume notebook Python runs in the remote kernel. Begin new initialization cells with `import warnings` and `warnings.filterwarnings('ignore')`, then imports and setup. Make the remote project root explicit near the top, verify hostname and working directory, and enable `%autoreload 2` for synchronized modules. Do not hide local/remote path assumptions inside helpers.

For detailed notebook patterns, source-file decisions, and whole-notebook execution rules, read [references/notebook-authoring.md](references/notebook-authoring.md).

Before creating a notebook or substantially revising its narrative/cell organization, read [references/authoring-examples.md](references/authoring-examples.md), then inspect the matching sections of [assets/project-template/notebooks/style_example.ipynb](assets/project-template/notebooks/style_example.ipynb) as writing references. The index maps simple operation cues, compact methods, detailed metric definitions, table previews, calculation/plotting cells, external launches, and minimal through complex or statistical captions. For a small targeted edit, consult only the relevant example; choose its level of detail rather than adding every pattern to the notebook. Follow its concise paired narrative, restrained heading hierarchy, bilingual figure captions, explicit local parameters, result reuse, and separate plotting while preserving the user's established structure. Adapt the pattern, not its scientific thresholds, inputs, or headings. This unexecuted agent reference and its companion source module are not files to copy into every project.

## Python Source Style

Follow the user's preferred research idioms in new notebook and source code: string paths with `os` and f-strings (`data_dir = f'{project_dir}/data'`), pandas tables, small tabular outputs as `.csv.gz`, and large tables as one `.h5` file per table with key `'df'`. Keep the confirmed remote root explicit before deriving paths from `os.getcwd()`; preserve conventions outside the requested edits.

Default to cell-level resumption: save reusable results of substantial calculation cells so later notebook sessions can load completed steps instead of recalculating them. Cell-internal loops normally need progress display only, not per-iteration files. Add finer checkpoints only when the actual cost or user request warrants them; do not require every trivial cell to save a file. In notebooks, use separate calculation and plotting code cells by default: calculation saves statistics; plotting reads them from disk without triggering expensive calculation. Add concise timestamped stage messages and elapsed time for multi-step work; use `tqdm.auto` for substantial loops with a meaningful description and unit. Prefer simple prints/progress bars over a logging framework. Always export the actual data used for each scientific figure as `.csv.gz` for publication inspection, independently of larger HDF intermediates. These conventions do not authorize executing analyses.

Write `src/` Python for the current research inputs and reproducible analysis, prioritizing a visible data flow over general-purpose infrastructure. Trust documented input contracts and let ordinary missing-file, missing-column, and invalid-format errors surface naturally. Add targeted checks where violations could silently corrupt scientific results, such as sample alignment or coordinate/units mismatches; do not turn every documented assumption into validation code.

Encapsulate meaningful analysis steps without mechanically splitting one-use operations into helpers or introducing classes, compatibility branches, or configuration frameworks. Keep meaningful intermediate variables, concise calls on one line, and blank lines only between logical stages. Use grouped wrapping for long calls; do not impose a function-length limit or compress complicated operations into dense expressions.

Document important interfaces clearly: functions called directly by notebooks or reused by other functions should explain inputs, assumptions, parameters, returns, and relevant file/cache side effects in English NumPy-style docstrings. Multi-stage functions should also outline their workflow. Simple internal helpers need only a short docstring, or none when self-evident. Comments explain scientific rationale and non-obvious implementation choices. Preserve existing style outside the requested edits; do not refactor the project merely to enforce these conventions.

Read the Python source style and interface examples in [references/notebook-authoring.md](references/notebook-authoring.md) when creating or modifying `src/*.py`.

Use [assets/project-template/src/plot_style.py](assets/project-template/src/plot_style.py) as the user's shared Matplotlib base style. In projects with figures, place this reusable implementation in `src/plot_style.py` (or integrate with the established shared plotting module) and call `set_plot_style()` explicitly during notebook initialization before creating figures. All project figures should build on these defaults; adjust individual sizes and layouts where needed without resetting typography and line styling. Avoid competing global styles that overwrite the defaults. The style module is a usable project asset, unlike the agent-only examples.

Before creating or substantially changing `src/*.py`, read the relevant functions in [assets/project-template/src/style_examples.py](assets/project-template/src/style_examples.py): a short helper, a multi-stage analysis interface, a sample-alignment check, and plotting separated from computation. For a small edit, consult the relevant pattern as needed. Read `plot_style.py` when adding or modifying figure initialization. Reuse references already read in the current task rather than repeatedly loading them. The style examples are agent reference material, not a module to copy into every generated project.

## Authoring Self-Review

Before handing off notebook/source edits, review the changed portions against the following requirements and repair applicable deviations. Use static inspection by default; this is not permission to execute notebook cells, install dependencies, or launch scientific workloads. Keep this review internal rather than adding a checklist to every notebook or user-facing response.

- Organization: shallow directories justified by current needs, numbered notebooks following scientific stages/dependencies, domain-based source modules, and no automatic language split during development.
- Narrative: concise biology-reader/reviewer-facing sections explaining what, why, and interpretation, with sufficient local definitions for metrics, references, coordinates, and consequential edge cases; Chinese-led alignment when requested; aligned English/Chinese headings and consecutive bilingual figure captions; no program control logic, repeated runtime settings, argument inventories, task lists, or editing records. Scientific parameters appear only when needed for interpretation; no invented inputs or findings.
- Initialization and paths: warning suppression, explicit remote root, `os`/f-string paths, autoreload, and an explicit shared-style call before plotting, where initialization is in scope.
- Tables and resumption: cell-level saved results for substantial steps, progress-only loops by default, `.csv.gz` for small tables, one `.h5` per large table with key `'df'`, and one responsible layer for reuse checks. Input/parameter changes identify affected outputs without building a general cache framework.
- Workflow and plotting: every included analysis step is visible and launchable in notebook cells with key parameters; external/job steps expose status/completion before continuation. Keep separate calculation and plotting cells, disk-backed statistics, no expensive cache-miss analysis in plotting, shared style retained, and actual plotted values exported to `.csv.gz`. Shared analysis parameters/output paths have one visible nearby definition rather than independent copies in calculation and plotting cells. Plotting works from initialization, section setup, and saved statistics without rerunning expensive calculations.
- Source and progress: direct readable data flow, only meaningful abstractions and scientific checks, compact formatting, appropriate interface docstrings, and timestamps/elapsed time or tqdm for multi-step work.
- Scope and handoff: no automatic copying of reference examples, unrelated refactoring, implicit execution, or forgotten sync instructions. Tools retain independent interfaces without imports from project-root `src/`; code sync is distinct from package installation. Identify saved outputs and the smallest cells to rerun.

## AI Task Markers

When the user wants a precise edit in one notebook cell, use a visible task marker instead of a positional cell number.

- Code cell: the first non-empty line is exactly `# ai todo cell`.
- Markdown cell: the first non-empty line is exactly `<!-- ai todo cell -->`.
- The user's request defines what to do; the marker defines where to do it.
- Require exactly one unfinished marker in the named notebook. If none exists, ask the user to add and save it. If several exist, report their nearby context and ask the user to leave one; do not guess.
- After the requested edit is fully prepared, replace the todo marker with `# ai done: <semantic-slug>` or `<!-- ai done: <semantic-slug> -->`.
- Keep the done marker as a stable human-visible reference. `done` means the edit is prepared, not that the cell ran or its scientific result was verified.
- If work is blocked or incomplete, leave the todo marker unchanged.

Generate a concise, unique, lowercase kebab-case slug from the cell's scientific purpose, such as `qc-missingness-plot`. The user may later refer to that slug or change its done marker back to todo for follow-up work.

For a bilingual narrative edit, place the todo marker in the English Markdown cell. Update that cell and the immediately following Chinese partner together; keep the done marker in the English cell as the pair's stable reference.

## Manual Synchronization

Project synchronization uses only `.vscode/tasks.json`. Do not create a sync script, Python sync CLI, file watcher, or save hook.

- Use `${workspaceFolder}` rather than a hard-coded local path.
- Synchronize `README.md`, `README.zh-CN.md`, `src/`, `config/`, and existing `tools/` source to the configured remote project root. Select only existing directories; omit absent optional operands.
- Exclude notebooks, `.git`, `.vscode`, environments, caches, build/install artifacts, data, results, logs, runtime state, and common large scientific files, including nested tool artifacts. See [references/project-tools.md](references/project-tools.md) for tool exclusions and package-loading checks.
- Never add `rsync --delete` by default.
- The user triggers the named task through VS Code **Run Build Task** or **Run Task** and reviews its terminal output.

After changing `src/`, `tools/`, or remote-consumed `config/`, explicitly tell the user to run the exact VS Code sync task before rerunning the relevant cell or job. A notebook-only edit does not require notebook synchronization because its cell code is sent directly to the remote kernel.

## Copilot Handoff

End every project-editing interaction with a short handoff that states:

- what notebook sections/cells and files changed;
- the completed AI task slug and exact done marker when a task marker was used;
- whether a VS Code sync task is required, and its exact label;
- which notebook cells the user should run next, identified by heading, order, or distinctive content;
- what output or condition the user should inspect;
- which cells launch external tools/jobs, their resources and completion/continuation checks, and any justified outside-notebook exceptions.

For ordinary project setup, identify the private Jupyter startup guides and state that the user starts the service manually. When Codex explicitly started a Jupyter session, also report its verified node, allocation/run ID when applicable, log location, local port, VS Code connection URL, and exact stop procedure. Never store the token or transient process information in tracked project configuration.

If no sync or execution is needed, say so explicitly. Do not claim that unexecuted code or a remote result was verified.

For connection, sync, import, kernel, allocation, and scheduler failures, read [references/troubleshooting.md](references/troubleshooting.md).
