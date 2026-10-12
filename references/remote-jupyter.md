# Remote Jupyter Session

Read this guide completely before starting, reconnecting, diagnosing, or stopping remote Jupyter. Use `remote-hpc-operator` throughout; its machine profile and software policy are authoritative.

This is the escalation path for an explicitly requested agent-operated action. The normal project workflow is user-managed: project setup generates private bilingual `JUPYTER_START` guides containing the verified startup, tunnel, VS Code, and shutdown commands. Do not proactively launch a service when those guides are sufficient.

## Preconditions and Authorization

Do not start until `config/project.yaml` passes the readiness gate in [project-setup.md](project-setup.md).

When the user explicitly asks Codex to establish the connection, show and confirm:

- machine profile and remote project root;
- Jupyter server environment and command;
- notebook kernelspec and environment;
- target node role and direct/interactive mode;
- scheduler resources when applicable;
- local and remote ports.

The user's confirmation authorizes this exact infrastructure setup. It does not authorize notebook cells, analysis commands, pipelines, or batch jobs. If the user does not explicitly request startup, provide or update the private guide and continue preparation without remote changes.

## Verified Startup Sequence

1. Read the remote machine index, selected profile, software-root index, and relevant environment documentation.
2. Verify SSH access, the allowed project path, activation scripts, Jupyter executable, intended kernelspec, scheduler mode, and node role using minimal read-only checks.
3. If the project directory is absent, stop for creation authorization. If Jupyter or an environment is absent or incomplete, stop for environment selection or installation/repair authorization.
4. If the profile requires an interactive allocation, obtain it using the configured project resources and record its allocation ID and assigned node. Do not substitute a login node when allocation fails.
5. Start the server on the verified node, from the remote project root, inside the configured server environment:

   ```text
   jupyter lab --no-browser --ip=127.0.0.1 --port=<remote-port>
   ```

   Keep token authentication enabled. Add only profile- or version-required arguments; never bind to `0.0.0.0`.
6. Prefer `remote-hpc-operator` long-task tooling when it is compatible with the verified direct/compute-node topology. For scheduler-owned interactive sessions, use the profile's persistent execution method. Record the exact run/allocation ID, process identity, stdout/stderr location, node, and remote port.
7. Read the actual server log to confirm the process remains alive and obtain its loopback URL/token. Do not write the token or temporary URL into tracked project files.
8. Build the SSH forwarding route from the machine profile. The final SSH endpoint must be the node whose loopback interface owns Jupyter. Use the topology-equivalent form of:

   ```text
   ssh -N -o ExitOnForwardFailure=yes -o ServerAliveInterval=30 \
     -L <local-port>:127.0.0.1:<remote-port> <verified-final-target>
   ```

   Add ProxyJump or nested-hop behavior only as documented by the profile. Bind the local listener to loopback and keep the tunnel in a managed long-lived local PTY/session.
9. Verify that the tunnel remains alive, the local port is listening, and `http://127.0.0.1:<local-port>/` reaches the Jupyter server before declaring success.

If any layer fails, stop the later steps, retain exact logs, and diagnose that layer. Do not disable authentication, choose an arbitrary port without updating the project configuration, or fall back to a forbidden node.

## VS Code Connection

After verification, give the user the current connection URL without persisting it:

```text
http://127.0.0.1:<local-port>/?token=<current-token>
```

Guide the user through:

1. open the local notebook in VS Code;
2. open **Kernel Picker**;
3. choose **Select Another Kernel**;
4. choose **Existing Jupyter Server**;
5. enter the verified URL;
6. select the configured kernelspec/display name;
7. run only the notebook initialization/verification cell when ready.

Ask the user to confirm that hostname, working directory, `sys.executable`, and environment prefix match the verified node, project root, and configured kernel. Do not run further cells unless the user explicitly asks to run the entire notebook.

## Session Handoff and Shutdown

Report:

- verified Jupyter node;
- allocation and/or remote run ID;
- server stdout/stderr log location;
- server environment and selected kernelspec;
- local and remote ports;
- whether the local tunnel is currently alive;
- the VS Code URL containing the current token;
- exact steps to stop this tunnel, this Jupyter process, and its allocation when applicable.

Stop only identifiers created for this session. Use `remote-hpc-operator` task checking to recover the exact recorded PID/run metadata, then stop that PID and the exact allocation ID when applicable. Never use broad process matching such as `pkill jupyter`, and never cancel an allocation that may contain unrelated work.

Tunnel shutdown must target the exact managed local PTY/process. Stopping the tunnel does not stop Jupyter; stopping Jupyter does not automatically release a scheduler allocation. State each lifecycle action separately.
