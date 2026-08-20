---
name: research-notebook-analysis
description: Assist with local scientific Jupyter notebooks whose kernels, data, and results live on remote HPC systems. Use for notebook-centered research projects, local-to-HPC source synchronization through VS Code tasks, remote Jupyter workflows, and preparing analysis code or scheduler jobs for the user to run. Pair with remote-hpc-operator for any actual remote access, software, environment, node, or scheduler work.
---

# Research Notebook Analysis

## Core Philosophy

Act as a scientific notebook copilot. Prepare, edit, explain, and hand work back to the user; let the user run it and judge the scientific result.

By default:

- Inspect the existing notebook, its saved outputs, and nearby project files.
- Edit or add notebook Markdown/code cells and place necessary reusable files under `src/`.
- Prepare configuration, shell commands, and scheduler job files without running them.
- Do not execute notebook cells, submit jobs, start large analyses, or infer permission to run from a request to write, fix, diagnose, or explain.
- Prefer static checks and a precise manual run handoff over executing code for verification.

Run a notebook only when the user explicitly asks to run the entire named notebook. Before remote execution, confirm the notebook, kernel, remote project root, execution node, and resource policy. For HPC execution, follow the remote integration rules below.

Remote Jupyter infrastructure is a separate opt-in action: after project configuration is complete, offer once to start Jupyter and establish the SSH tunnel. A user's confirmation authorizes only the exact machine, environment, node role, resources, and ports shown in that offer; it does not authorize notebook cells, pipelines, or batch jobs.

## Scope and Boundaries

Use this skill for notebook-centered scientific analysis where:

- notebooks are edited and retained locally;
- the selected Jupyter kernel executes on a remote HPC system;
- human-written source and configuration are synchronized manually;
- large data, intermediate products, and result files normally remain remote;
- figures, tables, and text outputs return through the Jupyter protocol for local display.

Do not use it for unrelated software engineering or for building an automated workflow platform. Do not recreate Jupyter, VS Code Remote SSH, a file-watching sync daemon, or a project-management CLI.

## Remote HPC Integration

Any task involving SSH, remote inspection, transfer, Jupyter startup, software, environments, nodes, allocations, or scheduler operations must also use `remote-hpc-operator`.

Apply this authority order:

1. The target machine profile defines SSH topology, authentication, node roles, allowed storage roots, software root, environment policy, scheduler, queues, and cluster limits.
2. This project's `config/project.yaml` selects the project root, Jupyter/kernel settings, and requested resources within those limits.
3. If project configuration conflicts with the machine profile, stop and report the conflict. Do not silently substitute a path, node, environment, or resource request.

Software discovery, reuse, installation, micromamba environments, activation scripts, `AGENT_SOFTWARE.md`, and network-node selection must strictly follow `remote-hpc-operator`. Do not install reusable software into the project directory or scratch space merely for convenience.

Never assume a login node permits scientific computation. Use an allowed interactive compute allocation for lightweight interactive analysis and scheduler batch jobs for large work. Do not automatically run large bioinformatics tools, assemblies, mapping pipelines, pangenome analyses, or machine-learning workloads.

Label runnable commands by execution context:

- `[LOCAL]`
- `[REMOTE LOGIN]`
- `[REMOTE COMPUTE]`
- `[SCHEDULER JOB]`

## Project Readiness Gate

When initializing a project or first opening an existing project, inspect `config/project.yaml` before preparing remote-dependent code. Treat missing fields, empty values, and angle-bracket template placeholders as unset.

Do not proceed with remote setup until the user has explicitly chosen:

- the `remote-hpc-operator` machine profile;
- the absolute remote project root;
- the micromamba, conda, module, or other documented environment used by the Jupyter server;
- the environment and kernelspec used by the notebook kernel;
- whether the server and kernel intentionally share one environment.

Read the remote machine index and selected profile before presenting machine, path, environment, node, or scheduler choices. Never reuse a previous machine as a default. Record confirmed project choices in `config/project.yaml`; keep SSH topology and machine-wide policy in the private machine profile.

For every environment, record its manager, human-readable name, and profile-compliant activation script. If an environment or Jupyter is missing, ask whether to select another documented environment or install/repair it. Installation requires separate authorization and must follow `remote-hpc-operator` software-root and metadata rules.

Validate that the remote root and requested resources are allowed by the machine profile. If the directory does not exist, report that fact and obtain authorization before creating it. Stop on profile/config conflicts rather than filling an assumed value.

Read [references/project-setup.md](references/project-setup.md) for the completeness checklist and template workflow.

## Remote Jupyter Session

Once the readiness gate passes, and no Jupyter connection has been verified in the current project session, ask once whether the user wants Codex to start remote Jupyter Lab and establish the local SSH tunnel. Summarize the exact machine, project root, server environment, kernel, node role, resource request, and local/remote ports in the question.

If the user declines, continue notebook preparation without remote actions and do not ask again during the same work stage. If the user confirms, use `remote-hpc-operator` to perform and verify the setup. Do not silently install Jupyter, fall back to a login node, disable token authentication, or expose the server on a non-loopback interface.

Read [references/remote-jupyter.md](references/remote-jupyter.md) completely before starting, checking, reconnecting, or stopping a remote Jupyter session.

## Lightweight Project Shape

Prefer this research-oriented structure:

```text
project/
├── README.md
├── README.zh-CN.md
├── notebooks/
│   ├── 01_qc.ipynb
│   ├── 02_mapping.ipynb
│   └── 03_analysis.ipynb
├── src/
│   ├── mapping.py
│   └── utils.py
├── config/
│   └── project.yaml
├── results/
├── data/
└── .vscode/
    └── tasks.json
```

The notebook is the primary research record and presentation surface. Keep short, one-off analysis code in the notebook. Move code to `src/` only when it is long, reused, easier to review separately, or represents a shell/batch operation. Python, shell, and scheduler files may coexist in `src/`; do not add a separate `scripts/` tree by default.

Avoid adding `tests/`, `docs/`, `lib/`, `bin/`, `workflow/`, `pipelines/`, packaging metadata, CI, containers, or placeholder modules unless the research task actually requires them. Do not create empty directories with `.gitkeep`.

## Notebook Authoring

Treat each notebook as a readable lab record:

1. title and research purpose;
2. remote environment and working-directory setup;
3. input data description;
4. alternating explanation and focused analysis cells;
5. interpretation of important outputs;
6. manual shell or scheduler steps;
7. caveats and open questions.

Preserve the user's existing narrative, numbering, and useful saved outputs. Do not invent hypotheses, inputs, results, or interpretations.

Write all newly created or modified narrative material bilingually:

- In notebooks, place an English Markdown cell first and its equivalent Chinese Markdown cell immediately after it. Keep code cells single and untranslated.
- Keep paired Markdown cells aligned in heading level, section number, scientific meaning, parameters, paths, identifiers, and caveats.
- For existing notebooks, add or repair the bilingual pair for Markdown touched by the current task. Do not translate all untouched historical cells unless the user asks for a full migration.
- At project root, maintain `README.md` in English and `README.zh-CN.md` in Chinese with the same structure and facts; link the two files to each other.
- If another standalone prose document is genuinely needed, use `<name>.md` for English and `<name>.zh-CN.md` for Chinese, keep them semantically aligned, and cross-link them. Do not create extra documentation files or a `docs/` tree without a research need.

Assume notebook Python runs in the remote kernel. Make the remote project root explicit near the top, verify hostname and working directory, and enable `%autoreload 2` for synchronized modules. Do not hide local/remote path assumptions inside helpers.

For detailed notebook patterns, source-file decisions, and whole-notebook execution rules, read [references/notebook-authoring.md](references/notebook-authoring.md).

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
- Synchronize `README.md`, `README.zh-CN.md`, `src/`, and `config/` to the configured remote project root.
- Exclude notebooks, `.git`, `.vscode`, caches, data, results, and common large scientific files.
- Never add `rsync --delete` by default.
- The user triggers the named task through VS Code **Run Build Task** or **Run Task** and reviews its terminal output.

After changing `src/` or remote-consumed `config/`, explicitly tell the user to run the exact VS Code sync task before rerunning the relevant cell or job. A notebook-only edit does not require notebook synchronization because its cell code is sent directly to the remote kernel.

## Copilot Handoff

End every project-editing interaction with a short handoff that states:

- what notebook sections/cells and files changed;
- the completed AI task slug and exact done marker when a task marker was used;
- whether a VS Code sync task is required, and its exact label;
- which notebook cells the user should run next, identified by heading, order, or distinctive content;
- what output or condition the user should inspect;
- which shell or scheduler commands remain for manual execution.

When Codex started a Jupyter session, also report its verified node, allocation/run ID when applicable, log location, local port, VS Code connection URL, and exact stop procedure. Never store the token or transient process information in tracked project configuration.

If no sync or execution is needed, say so explicitly. Do not claim that unexecuted code or a remote result was verified.

For connection, sync, import, kernel, allocation, and scheduler failures, read [references/troubleshooting.md](references/troubleshooting.md).
