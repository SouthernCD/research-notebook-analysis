# Project Setup

Use this guide when initializing or reorganizing a notebook-centered research project.

## Initialization Sequence

Inspect the user's existing files first. Preserve useful structure and do not force a migration merely to match the template.

When the user needs help framing their first project or understanding the workflow, use [new-user-guidance.md](new-user-guidance.md) before asking for all technical settings. Establish one useful research step and introduce setup details as needed. In paired READMEs, adapt the template's short Getting started section to the actual inputs, first notebook, and inspection goal; do not create an additional beginner manual by default.

An explicit request to unify the entire existing repository's style follows [project-style-unification.md](project-style-unification.md), including Git snapshots and one-notebook execution/review gates. Do not treat ordinary setup or a small edit as authorization for that migration.

For a new project, aim for the smallest usable research starting point, not a complete anticipated pipeline:

1. Establish the research question, available inputs/formats/provenance, reproducibility starting point (raw or analysis-ready data), local project location, and the first meaningful analysis. Inspect supplied files before asking questions. Bundle only missing choices that affect the current step; do not invent hypotheses, later notebooks, thresholds, or results.
2. Read the remote machine index/profile and confirm project-specific machine, absolute remote root, server/kernel environments, node/resources, and ports. Record stable choices in `config/project.yaml` and validate them through the configuration-readiness procedure below. A missing remote directory, environment, or package requires the corresponding explicit authorization; initialization is not installation or remote execution.
3. Create paired `README.md` and `README.zh-CN.md`, `.gitignore`, project configuration, and manual `.vscode/tasks.json`. Describe the research objective, actual notebook inventory, source/result roles, environment, reproducibility boundary, and manual workflow. Label genuinely known later stages as planned, without generating their files by default.
4. Prepare the first useful numbered notebook, such as input audit, data preparation, or the first justified analysis. Read the notebook/source style references. Follow the first-notebook requirements below; create additional notebooks only when already needed by the current request.
5. Add only required long/reusable source functions. If a complete independent analysis tool is needed, use `tools/<tool-name>/` following [project-tools.md](project-tools.md); do not create an empty tools scaffold. Adopt `src/plot_style.py` when plotting is needed. Do not create placeholder modules, copy the agent-reference examples, or add a test/package/workflow framework by default.
6. Use logical `data/source/` and `data/results/` locations, normally remote; create local directories only when a small local file needs them, without `.gitkeep`. Do not download large data or populate the whole data tree merely to demonstrate the structure.
7. After remote configuration passes readiness, generate project-specific `JUPYTER_START.md` and `JUPYTER_START.zh-CN.md` and ignore both guides plus `/runs/jupyter/`. The user starts the service manually unless explicitly requesting otherwise.
8. Perform static checks, establish the initial local Git snapshot as described below, and hand off the exact sync task, startup guides, first cells to run, expected checks, and outstanding manual operations. Do not run the notebook just to validate initialization.

If necessary input or remote choices are pending, continue independent local planning or documentation but do not prepare runnable remote-dependent code using guessed values. Keep unfinished configuration clearly pending; do not generate placeholder-filled startup guides or report the scaffold ready. Previously confirmed choices for this same project need not be reconfirmed, but another project's settings are not defaults.

The reusable starting files are under `assets/project-template/`, and the private Jupyter guide sources are under `assets/jupyter-start/`. Adapt placeholders to the current project; never treat example values as verified machine facts or leave placeholders in a generated project guide.

`assets/project-template/src/style_examples.py` is an agent-only style reference. Read it when writing Python source, but do not copy the example module or create `src/` merely because it exists in the template. Create only source files required by the actual analysis.

Likewise, `assets/project-template/notebooks/style_example.ipynb` is an unexecuted writing reference, not a research stage to add to the project's notebook inventory. Use [authoring-examples.md](authoring-examples.md) to select its relevant cell and caption patterns when authoring notebooks; do not copy the template directory wholesale or leave its example paths and inputs in a working project.

For projects that create figures, `assets/project-template/src/plot_style.py` is a reusable implementation to adopt or merge into the existing shared plotting module. It is not an agent-only example. Initialize this style explicitly in each notebook so project figures inherit the same defaults.

## First Notebook Requirements

Use the scientific purpose to select the first step; a generic empty notebook is not a useful deliverable. Prepare only code and explanations supported by the known inputs and agreed method. Follow [notebook-authoring.md](notebook-authoring.md) and its linked example:

- Adjacent English/Chinese narrative for biology readers and reviewers: purpose, analysis, necessary method definitions, and interpretation only. Keep runtime settings and resumption logic in code.
- Initialization beginning with warning suppression, explicit confirmed remote root, `os`/f-string paths, kernel/host display, autoreload, and shared plotting-style initialization when relevant.
- Known input paths, their expected meaning/format, and current scientific parameters at their point of use.
- Substantial calculation cells with saved reusable outputs and cell-level reuse; loops show progress without default per-iteration checkpoints.
- Separate plotting cells that load saved statistics and export actual plot data as `.csv.gz`.
- Useful interface docstrings for required `src/` functions, without speculative abstractions or defensive checks.
- Explicit launch/continuation cells and what the user should inspect, without fabricated findings.

If heavy external tools are needed, prepare explicit notebook launch cells that show key parameters/resources and invoke the implementation in `src/` or `tools/<tool-name>/` when appropriate. Include logs/status and completion/continuation handling so readers can reproduce the analysis from the notebook. Expensive work and scheduler submission must be visible, not hidden behind imports or unexplained convenience calls. Do not require outside-notebook script execution unless the user chooses it or a concrete limitation requires it.

## Initial Git Snapshot and Completion

For a genuinely new project, the initialization request authorizes creating a local Git repository and initial commit unless the user specifies otherwise. Check for an existing repository or enclosing repository first; do not create an accidental nested repository or change unrelated repository settings.

Review the candidate files and ignore rules before staging. Commit shareable code, notebooks, documentation, and sanitized configuration/task examples as needed. Exclude real private machine settings, Jupyter startup guides/runtime state, credentials, large scientific inputs/results, and caches. Generate sanitized `config/project.example.yaml` and `.vscode/tasks.example.json` from the actual structure when real settings are ignored. Do not blindly stage the full directory, force-add ignored files, overwrite the user's staged work, invent Git identity settings, create a remote, or push. Report the initial commit ID; if Git setup/commit is blocked, preserve the prepared files and report the missing archive separately.

Use the template `.gitignore` as the starting point: ignore all of `/data/` (both source and results, regardless of file size), optional top-level `/results/`, `/logs/`, `/runs/`, `.venv/`, Python/notebook caches, private project/task settings, and both startup guides. Git is for code and shareable research documentation, not scientific data or runtime artifacts. If any such paths are already tracked in an existing project, report them; ignore rules do not untrack files, and index changes require user authorization.

Before handoff, check notebook JSON/schema and unexecuted cell status, source syntax, imports/file references that can be verified locally, paired documentation, and configuration/task consistency. These are static checks; do not claim remote scientific results are verified. Apply the authoring self-review in `SKILL.md`.

State what was created, the confirmed machine/root/kernel, initial Git snapshot status, exact VS Code sync task, private startup guides, first cells to run, outputs to inspect, and commands still manual. Clearly distinguish confirmed facts from pending choices.

Call initialization complete only when the research starting point and project organization are clear, remote configuration is ready, the first meaningful notebook is prepared, and the startup/sync handoff is usable. Git snapshot status must also be reported; a blocked snapshot is outstanding work, not a reason to lose or discard the project. Completion does not imply a full pipeline, executed analysis, or verified scientific findings.

## Research Organization and Reproducibility Boundary

Use a shallow directory tree organized by research role, with numbered notebooks following scientific stages and their dependencies and source modules named for analysis domains. Keep one bilingual working notebook per stage; add another notebook for a meaningful research boundary rather than every operation or figure. Create directories/configuration only for current needs. The example project's five stages are not a universal scaffold. Optional independent tools follow [project-tools.md](project-tools.md).

In paired READMEs, describe the actual notebook order, each notebook's purpose and major output, and important producer/consumer dependencies. Keep the inventory aligned with files that exist; label planned stages as planned instead of presenting them as completed notebooks.

Define data roles rather than forcing a directory migration:

- `source`: externally supplied inputs, including documented analysis-ready derivatives. Treat these as read-only inputs.
- `results`: analysis products, including intermediate tables, models, external-program outputs, figure data, figures, and final tables. Organize by analysis when useful, without inventing extra data classes.

State where reproduction begins, which upstream processing is outside project scope, and how source inputs are obtained. Add a file manifest only when the project needs one, recording locations and known provenance rather than copying paths into several competing registries. Do not invent download URLs, publication status, or reproducibility claims.

Keep scientific parameters near their notebook use. Shared scientific catalogs may be stored in configuration when several analyses consume them; distinguish executable definitions from descriptive metadata and avoid conflicting duplicate values.

For shareable repositories, provide sanitized `config/project.example.yaml` and `.vscode/tasks.example.json` alongside private real settings when needed. Generate examples from the templates and confirmed structure without publishing machine-specific routes or paths. Preserve existing ignore rules and ignore the real `config/project.yaml` and `.vscode/tasks.json` when they contain private machine settings. Inspect tracking state first; adding ignore rules does not remove tracked files.

Separate language notebook directories are an optional final-publication arrangement only. Keep English/Chinese cells together throughout development and debugging. At final publication preparation, offer the option and follow [notebook-authoring.md](notebook-authoring.md#final-publication-copies) if the user chooses it; ordinary setup or cleanup must not create parallel language trees.

## Project Configuration

`config/project.yaml` is a human- and Codex-readable project record, not an API that requires a parser. Keep these concerns separate:

- project identity;
- `remote-hpc-operator` machine profile ID;
- remote project root;
- Jupyter server settings;
- notebook kernel environment and kernelspec;
- scheduler and project resource request;
- synchronization task label.

Do not store passwords, private keys, Jupyter tokens, or real authentication material. SSH aliases, ProxyJump, software roots, node roles, and cluster-wide limits belong to the private machine profile rather than this project file.

The project may request a concrete work path and resources, but confirm that they are allowed by the selected machine profile before remote work.

## Configuration Readiness

Run this check when initializing a project and when first encountering an existing project. A field containing an angle-bracket placeholder is incomplete, not a default.

For small existing-project edits, inspect what is available but do not block independent local work on completing unrelated remote settings. Full readiness is required before remote setup/execution and new runnable remote-dependent setup, not before every prose or source-style change. Confirm scheduler/allocation fields only when applicable; document unused settings as not applicable rather than inventing values.

Required user-confirmed choices are:

- `remote.machine_profile`;
- `remote.project_root`;
- Jupyter server environment manager, name, and activation script;
- notebook kernel environment manager, name, activation script, and kernelspec;
- whether server and kernel environments are intentionally the same;
- Jupyter local and remote ports;
- scheduler execution mode and project resource request when an allocation is required.

Use the machine index/profile to present verified options, but require the user to choose the machine, environment, and project root. Do not infer these choices from a previous project or conversation.

Validate confirmed values through `remote-hpc-operator`:

1. the machine profile exists;
2. the project root is within an allowed work root;
3. the activation script follows the machine software-root policy and its environment metadata is complete;
4. the server environment provides Jupyter and the kernel environment provides its kernelspec requirements;
5. the requested node role and scheduler resources are allowed.

If the project directory is absent, ask before creating it. If the environment or Jupyter is absent, ask the user to choose another documented environment or explicitly authorize installation/repair. Never install as an implicit part of project initialization.

Write only stable choices to `config/project.yaml`. Do not write the allocated compute node, allocation/job ID, Jupyter PID, token, temporary URL, or tunnel PID.

## Private Jupyter Startup Guide

Create or update both of these root-level files after configuration readiness succeeds:

- `JUPYTER_START.md` in English;
- `JUPYTER_START.zh-CN.md` in Chinese.

Keep their headings, facts, commands, warnings, and stop procedure semantically aligned and cross-link them. They are project-local operational guides, not tracked documentation. Each generated guide must contain usable project-specific values derived from `config/project.yaml` and the selected machine profile:

- the documented SSH route and the required login/compute transition;
- the remote project root;
- the Jupyter server activation script and command;
- the configured remote and local ports;
- the scheduler or interactive-allocation step when required;
- a loopback-only Jupyter command with token authentication retained;
- a loopback-only SSH tunnel with forwarding-failure detection and keepalive;
- the runtime log/PID location under `runs/jupyter/`;
- VS Code **Existing Jupyter Server** and kernelspec selection steps;
- exact shutdown instructions for the recorded PID/task/allocation only.

Never put a token, password, private key, current compute node, PID, allocation ID, or temporary URL in these files. Explain how the user reads the current token-bearing URL from the runtime log instead. Never use broad shutdown commands such as `pkill jupyter`.

Update the existing root `.gitignore` non-destructively. Preserve all user rules and add this section when missing:

```gitignore
# Private local Jupyter startup instructions and runtime state
/JUPYTER_START.md
/JUPYTER_START.zh-CN.md
/runs/jupyter/
```

If either guide is already tracked, `.gitignore` alone will not untrack it. Report that condition and obtain permission before changing the Git index. Do not silently remove a tracked file.

When adopting an old project, inspect any existing Jupyter instructions before replacing them. Preserve working project-specific topology and scheduler details that agree with the current machine profile, repair unsafe or stale commands, create the missing language partner, and ensure the ignore rules are present.

## VS Code Sync Task

The template task uses `"type": "process"` to pass an `rsync` argument array directly, avoiding shell quoting for ordinary paths. Use a shell task only when the verified SSH setup genuinely requires shell behavior. Keep source selection explicit: `README.md`, `README.zh-CN.md`, and the existing `src/`, `config/`, and `tools/` directories. The template has no `tools/` operand until an actual tool exists; add it when creating the first tool, and omit any absent source directories. Include tool documentation/dependency files, exclude nested environments, caches, build/install artifacts, logs and runtime state, and follow [project-tools.md](project-tools.md) for details. This avoids scanning or transferring the whole workspace and naturally leaves local notebooks behind.

When either README changes, update its language partner in the same task. Preserve matching heading order, facts, paths, environment names, resource values, notebook order, and caveats. Natural phrasing may differ between languages; semantic content must not.

Apply the same `<name>.md` / `<name>.zh-CN.md` pairing and cross-linking to any other standalone prose document that the research project actually needs. Do not create extra documentation solely to demonstrate the convention. If such a document must be available remotely, add both language files to the manual VS Code sync task together.

Adapt these placeholders:

- task label;
- SSH alias;
- absolute remote project root.

The task must remain manual. Do not add background watching, automatic execution on save, or `--delete`. The remote project root should already exist unless the user explicitly asks Codex to create it through `remote-hpc-operator`.

After editing `src/`, `tools/`, or remote-consumed configuration, the handoff should say, for example:

> 请先在 VS Code 运行任务 `Sync <project> to <machine>`，确认 rsync 成功后，再重新运行 notebook 中“导入分析函数”和后续调用单元格。

## Jupyter Startup Handoff

After configuration becomes ready, summarize the chosen machine, remote root, server environment, kernel, node role, resources, and ports. Tell the user that the private root-level Jupyter guide now contains the manual startup, tunnel, VS Code connection, and shutdown steps.

Do not proactively ask to launch the service and do not start it merely to validate notebook edits. The user may follow the guide whenever a session is needed. If the user explicitly asks Codex to start or troubleshoot Jupyter, that request authorizes only the displayed infrastructure action, not notebook execution.

For an explicitly requested agent-operated startup, tunnel, diagnosis, or shutdown, read [remote-jupyter.md](remote-jupyter.md).
