# Project Setup

Use this guide when initializing or reorganizing a notebook-centered research project.

## Initialization Sequence

Inspect the user's existing files first. Preserve useful structure and do not force a migration merely to match the template.

For a new project:

1. Create concise paired READMEs: `README.md` in English and `README.zh-CN.md` in Chinese. Give them the same structure and facts, link them to each other, and cover the research objective, notebook order, local/remote file semantics, environment, and manual workflow.
2. Create only the notebooks justified by known research steps. Use numbered filenames when an execution or narrative order exists.
3. Add `src/` files only for already-known reusable or long logic. Do not create placeholder modules.
4. Create `config/project.yaml` with project-specific remote and resource settings.
5. Create `.vscode/tasks.json` with a manually triggered sync task.
6. Treat `data/` and `results/` as logical locations. Create them only when a local small file needs them; do not add `.gitkeep`.
7. Complete and validate the remote project configuration with the user before offering a Jupyter session.

The reusable starting files are under `assets/project-template/`. Adapt placeholders to the current project; never treat example values as verified machine facts.

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

## VS Code Sync Task

The template task uses an `rsync` shell command assembled as a JSON argument array. Keep source selection explicit: `README.md`, `README.zh-CN.md`, `src/`, and `config/`. This avoids scanning or transferring the whole workspace and naturally leaves local notebooks behind.

When either README changes, update its language partner in the same task. Preserve matching heading order, facts, paths, environment names, resource values, notebook order, and caveats. Natural phrasing may differ between languages; semantic content must not.

Apply the same `<name>.md` / `<name>.zh-CN.md` pairing and cross-linking to any other standalone prose document that the research project actually needs. Do not create extra documentation solely to demonstrate the convention. If such a document must be available remotely, add both language files to the manual VS Code sync task together.

Adapt these placeholders:

- task label;
- SSH alias;
- absolute remote project root.

The task must remain manual. Do not add background watching, automatic execution on save, or `--delete`. The remote project root should already exist unless the user explicitly asks Codex to create it through `remote-hpc-operator`.

After editing `src/` or remote-consumed configuration, the handoff should say, for example:

> 请先在 VS Code 运行任务 `Sync <project> to <machine>`，确认 rsync 成功后，再重新运行 notebook 中“导入分析函数”和后续调用单元格。

## Jupyter Session Offer

After configuration becomes ready, summarize the chosen machine, remote root, server environment, kernel, node role, resources, and ports. Ask whether the user wants Codex to start Jupyter Lab and establish the SSH tunnel now.

Ask once per project work stage when no connection has been verified. A decline means continue preparing the notebook without remote action; do not repeatedly prompt. A confirmation authorizes the displayed Jupyter infrastructure setup, not notebook execution.

For the actual startup, tunnel, VS Code connection, and shutdown procedure, read [remote-jupyter.md](remote-jupyter.md).
