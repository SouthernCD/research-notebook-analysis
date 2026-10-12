# Troubleshooting

For ordinary startup, begin with the project-root private `JUPYTER_START.md` or `JUPYTER_START.zh-CN.md`. These files should reflect the current `config/project.yaml` and machine profile. If they contain placeholders, stale paths, or an obsolete SSH topology, repair both language versions and the root `.gitignore` before diagnosing the runtime service.

Use this guide to diagnose the local VS Code to remote Jupyter workflow. Gather evidence from the least invasive layer first; do not change remote state merely to test a theory.

## 1. Establish Context

Read `config/project.yaml` and the selected `remote-hpc-operator` machine profile. Confirm:

- local workspace and notebook;
- machine profile and SSH alias;
- remote project root;
- Jupyter node and remote/local ports;
- Jupyter server environment and selected kernelspec;
- scheduler and active allocation;
- VS Code sync task label.

Separate verified facts, profile facts, project configuration, and inference.

## 2. Connection Layers

Diagnose in this order:

1. **SSH:** authentication, MFA, alias expansion, ProxyJump, and compute-node reachability.
2. **Allocation:** interactive allocation still exists, Jupyter node is correct, and the allocation has not expired.
3. **Jupyter process:** server is running on the expected node and port and listens only on `127.0.0.1`.
4. **Tunnel:** local port is free, forwarding targets the actual Jupyter node/port, and the tunnel remains alive.
5. **VS Code:** Existing Jupyter Server URL uses the local port and current token.
6. **Kernel:** selected kernelspec points to the intended environment and kernel remains alive.

Use the connection topology from the machine profile. Do not guess whether the login node can reach compute-node loopback or invent a ProxyJump route.

Typical symptom mapping:

- connection refused: Jupyter stopped, wrong node/port, or tunnel target mismatch;
- local bind failure: local port already occupied;
- token rejection: stale URL/token or a different server instance;
- kernel disappears: allocation expired, kernel crashed, or environment is broken;
- works initially then drops: SSH/tunnel interruption, server exit, or scheduler timeout.

Before changing anything, locate the exact Jupyter run/process and tunnel created for this session. Never use a broad `pkill jupyter` or cancel an unrelated allocation.

Additional startup checks:

- Jupyter command missing: verify the configured server activation script and environment metadata; request environment selection or installation authorization rather than installing silently.
- Server exits immediately: inspect its recorded stdout/stderr for an invalid environment, occupied remote port, unwritable runtime directory, quota, or scheduler termination.
- No token/URL in output: confirm the server is still starting, inspect the actual run log, and use the server's supported listing command inside the same environment. Do not disable authentication.
- Interactive allocation unavailable: report the scheduler reason and stop; do not fall back to the login node.
- Tunnel exits immediately: inspect local port conflicts, SSH authentication, ProxyJump, final target node, and `ExitOnForwardFailure` output.
- VS Code accepts the URL but shows the wrong Python: select the configured kernelspec and verify `sys.executable` and the environment prefix in the initialization cell.

## 3. Project and Synchronization

If imports or configuration appear stale:

1. verify the user ran the named VS Code sync task after the latest local edit;
2. inspect rsync output for authentication, missing destination, permissions, and transferred filenames;
3. verify the remote project root exists and contains the expected updated file;
4. confirm notebook cwd equals the remote project root;
5. confirm `src/` is on `sys.path` when needed;
6. rerun the import/call cell with `%autoreload 2` enabled;
7. use `importlib.reload()` or restart the kernel only when module state requires it.

Do not solve a sync failure by broadening the task to data/results or adding `--delete`.

Common import causes:

- wrong remote cwd;
- `src/` not on `sys.path`;
- sync task not run or failed;
- wrong kernelspec/environment;
- dependency absent from the documented environment;
- package state incompatible with autoreload.

If results seem stale despite successful synchronization, inspect the expected output paths and the cache-reuse branch. Verify required files/columns and available input/parameter metadata. Distinguish stale results from stale source code; identify which outputs need explicit recomputation and downstream reruns, without deleting them or launching computation as a diagnostic shortcut.

Any dependency installation or environment repair must follow `remote-hpc-operator` software policy.

## 4. Scheduler and Resource Failures

Confirm scheduler type and commands from the machine profile, not from the project example.

- Pending allocation/job: inspect scheduler reason, account, partition/queue, requested resources, and policy limits.
- Immediate failure: inspect scheduler log, environment activation, working directory, missing inputs, and command path.
- Out-of-memory or timeout: use recorded resource evidence before proposing a larger request.
- Large work on a login node: stop planning direct execution and prepare an interactive allocation or batch job instead.

Project-specific resources may be adjusted to the analysis, but they must remain within cluster policy. Do not submit, cancel, or resubmit unless the user explicitly asks.

## 5. Old HPC Systems

This workflow intentionally avoids dependence on VS Code Server, modern remote Node.js, or remote glibc compatibility. Keep VS Code and notebooks local, use standard SSH forwarding, and run Jupyter/Python inside an environment allowed by the target machine profile.

Do not attempt to repair an old system by replacing system libraries. Follow the documented user-space software policy through `remote-hpc-operator`.

## Diagnostic Handoff

Report:

- the failing layer;
- evidence already verified;
- the smallest next check or user action;
- whether sync or notebook rerun is needed;
- any command's required execution context.

For an active or failed Jupyter setup, also report the verified node, allocation/run ID, logs, local/remote ports, whether the tunnel is alive, and the exact safe stop procedure.

Do not claim a fix until the relevant observable behavior has been rechecked by the user or through explicitly authorized execution.
