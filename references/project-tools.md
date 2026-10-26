# Project Tools

Read this guide when creating, restructuring, or integrating a project-local tool under `tools/`. It supplements the notebook/source conventions; tool development remains within the current research task.

## Placement and boundaries

- `notebooks/`: research questions, input selection, scientific parameters, explicit launches, and result interpretation.
- Project-root `src/`: project-specific analysis helpers, shared plotting, and thin integration code.
- `tools/<tool-name>/`: an analysis tool with a coherent purpose, defined inputs/outputs, and an interface that can run independently of the notebook.

Choose `tools/` for a complete analysis capability that needs its own internal organization or maintenance boundary. Reuse across projects is not a prerequisite; line count alone is not a reason to extract a tool. Do not create this directory until a concrete tool is needed, or move working code solely to match the convention.

Use one descriptive lowercase directory name per tool, such as `variant_context`. Keep the default project repository as the source of truth; do not initialize nested Git repositories or add submodules without a concrete user request. A tool can move to its own repository later when independent reuse or releases justify that change.

## Internal structure

Choose the smallest structure that fits the tool. A single implementation file and paired README files may be sufficient. A Python tool with several modules might grow into:

```text
tools/
└── variant_context/
    ├── README.md
    ├── README.zh-CN.md
    ├── pyproject.toml          # only when packaging/dependency declaration is useful
    ├── src/
    │   └── variant_context/
    │       ├── __init__.py
    │       └── ...             # actual implementation modules
    └── tests/                 # when meaningful core-behavior checks are needed
```

This is an illustration, not a scaffold to generate wholesale. A tool may have its own CLI, shell scripts, scheduler templates, configuration defaults, or build files where required. Existing language/tool conventions take precedence over forcing Python packaging. The project-root preference against extra package/test/script trees does not prohibit necessary structure inside a tool.

Keep the tool independent of the containing project's private state. Pass paths, data, parameters, and resources explicitly. Do not import project-root `src/`, rely on the caller's working directory, read private `config/project.yaml` implicitly, or hard-code machine paths inside the tool. Project integration code may call the tool; dependencies should flow in that direction. Reuse an existing tool before introducing a second implementation of the same method.

The source readability, scientific-validation, and interface-documentation principles in [notebook-authoring.md](notebook-authoring.md) also apply to tool code. Its storage formats, internal APIs, and implementation language may follow actual tool requirements; project-facing statistics and figure exports retain the project's conventions. A tool must not depend on project-root plotting code for independence: project presentation normally belongs in the notebook or project `src/`, where the shared plotting style is applied.

## Interface and research integration

Provide a documented Python API, CLI, or other appropriate invocation interface. Imports must not run analyses. A CLI is allowed and can be used independently; the project's defined research workflow must still be launchable from explicit notebook cells unless the user chooses an outside-notebook action or a concrete limitation requires it.

The notebook selects scientific parameters, input/output paths, and resource requests at their point of use, then passes them to the tool. Tool defaults may exist, but scientifically important choices must remain visible in the notebook. Avoid conflicting notebook/tool configuration copies or wrappers that hide major analysis stages. Keep result reuse and completion checks at the layer owning each output rather than duplicating them in the notebook, integration helper, and tool.

For Python imports, document the actual package resolution: an already authorized installed package or an explicit tool source path in notebook setup. Do not assume adding the project root makes a tool's nested `src/` importable. For CLI calls, make the executable/interpreter and environment explicit; a tool in another environment requires an explicit subprocess or scheduler launch rather than an import into the notebook kernel. Synchronizing code does not install a package or refresh an installed non-editable copy.

Keep existing notebook rules for expensive work and jobs: visible invocation/resources, propagated failures, log/status inspection, recorded job identity, no duplicate submissions after restart, and a completion check before downstream analysis. Tool placement grants no extra execution permission.

## Documentation, dependencies, and outputs

Maintain cross-linked English/Chinese README files describing purpose, input/output contracts (including relevant identifiers, coordinates, and units), invocation, dependencies, and scientifically important defaults. Keep project-specific sample choices and conclusions in the research notebook. Add further documentation only when needed; code comments and interface docstrings remain English by default.

Declare dependencies when useful, and document whether the tool uses the notebook kernel environment or another confirmed environment. Do not generate a separate environment per tool automatically. All remote environment creation, package installation, builds, and software placement follow `remote-hpc-operator`; source preparation does not authorize installation. `tools/` holds project-authored source, not reusable third-party software installations or environment directories.

Write analysis products to `data/results/<analysis-or-tool>/` or the established project result layout, and runtime logs/state to `runs/<tool>/` or existing runtime locations. Make these destinations explicit arguments. Keep real datasets, caches, logs, environments, and build artifacts outside tool source. Small synthetic fixtures for meaningful tests may live with the tool and be tracked; they must not contain private research data.

Add focused tests when the tool's algorithms or interfaces need them; do not create an empty test tree or tests that merely mirror the implementation. Local synthetic checks may run when they need no remote access, dependency installation, or scientific workload; these are distinct from notebook execution. Remote checks and scientific comparisons require their applicable execution authorization. Report the checks actually performed and their limits.

## Synchronization and handoff

Include existing `tools/` source and its necessary documentation/dependency files in the project's manual VS Code sync task. Do not add a source operand for an absent directory. Exclude environments (`.venv/`, `venv/`, `.env/`, `env/`), caches (`__pycache__/`, `.pytest_cache/`, `.mypy_cache/`, `.ruff_cache/`), build/install artifacts (`build/`, `dist/`, `*.egg-info/`), data, results, logs, and runtime state at any tool depth. Keep required source and small synthetic fixtures transferable; adapt broad scientific-file exclusions narrowly if they would hide a required fixture.

Preserve directory paths on the remote side. A renamed or removed source file can remain remotely because synchronization does not use `--delete`; identify the exact stale path and its impact, and prepare a scoped cleanup for user action or explicit authorization rather than broad deletion.

After tool edits, name the exact sync task, the tool/interface changed, the notebook launch/continuation cells, and any separate installation/build step still needed. Do not claim a source sync updates the active package without checking how it is loaded.
