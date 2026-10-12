# Existing-Project Style Unification

Read this guide only when the user explicitly asks to unify an existing project's
style across notebooks and source. Ordinary small edits remain incremental.

The objective is consistent, readable research code with preserved scientific
results. Process one notebook at a time; speed of repository-wide completion is
secondary to verified behavior and human acceptance.

## 1. Preserve the starting point

Inspect Git status, existing staged changes, ignore rules, and the research files
before edits. Create a local baseline commit containing the relevant current
notebooks, source, and shareable documentation/configuration, including existing
research edits needed to reconstruct the starting point. Review the file list;
do not blindly stage the entire directory, disturb unrelated staged work, force-add
ignored data, or commit private configuration, tokens, logs, or startup guides.
If the relevant state is already committed, record its commit ID as the baseline.

The unification request authorizes these local snapshots. It does not authorize
pushing, destructive Git operations, or publishing. If no Git repository exists,
ask how the user wants to establish the archive before beginning migration.
If a snapshot cannot be created, preserve current files and report the obstacle
rather than proceeding with an unprotected rewrite.

Git records code, not ignored remote results. Locate the current notebook outputs
and reusable result files separately. Record the baseline commit ID and result
locations in the handoff; do not pretend a Git commit backs up large remote data.

Keep this migration record in the conversation and Git history. Do not insert
baseline commit IDs, preservation promises, verification/backup tasks, or pending
acceptance into notebook Markdown, code comments, or printed messages. The notebook
explains research purpose, methods, and results to biology readers and reviewers.
Keep resumption/cache logic and runtime settings in code; Markdown mentions
scientific parameters only when needed for biological interpretation. Relevant scientific
provenance and specific interpretation limits still belong there. Flag stale or
unverified outputs in the handoff, omit unsupported conclusions, and arrange a rerun
or clear misleading affected outputs as appropriate; an editing disclaimer is not
a substitute for keeping the research presentation accurate.

## 2. Choose one notebook and establish its baseline

Honor a user-selected notebook. Otherwise choose the earliest meaningful notebook
in dependency order and explain the choice; do not require another selection when
the order is clear. Inspect its full narrative, code, saved outputs, imports, and
the source functions it actually uses. Identify other notebooks consuming those
functions, but do not start their migrations yet.

Identify scientific invariants before editing: inputs, sample/variant identities
and order, coordinate systems, filtering, thresholds, models, random seeds,
intermediate table meaning, and final plotted values. Preserve available baseline
results without overwriting them. If no baseline exists, report that limitation;
a successful run alone cannot demonstrate equality to a previous result.

Prepare a small comparison plan using existing outputs where available. Favor
checks with scientific meaning: table dimensions, identifiers and alignment,
context membership/counts, and numeric values in the actual analysis/plot tables.
Use exact comparisons for discrete deterministic results; use a justified
tolerance for floating-point results. Do not reduce verification to file
existence, a success message, or image pixel equality when styling is changing.

## 3. Unify the notebook and its necessary source

Read the notebook and Python style examples and apply the user's current
conventions to this notebook: bilingual narrative, compact source, clear important
interfaces, string paths, pandas persistence, cell-level resumption, progress,
separate calculation/plotting cells, shared plotting style, and compressed figure
data exports. Read [notebook-authoring.md](notebook-authoring.md) for implementation details.

Refactor only source dependencies necessary for this notebook. Keep public
interfaces compatible where possible. If changing a shared interface is necessary,
inspect its callers and make the smallest compatibility edits, disclose them,
and check the affected calls; this does not authorize stylistically rewriting
every consuming notebook. Preserve scientific parameters and methods, and keep
unrelated scientific corrections separate from the style work.

Retain compatible existing result files and formats when useful; adopting new
output conventions is not a reason to convert or regenerate all historical data.
If a path/format must change, update its consumers and explain reuse/migration.
Preserve saved notebook outputs when still consistent; identify outputs requiring
rerun instead of claiming new results already exist.

Perform static checks and prepare only the focused tests needed to compare actual
behavior. Use small standalone checks or an appropriate existing test location;
do not build a test framework merely for this migration.

## 4. Obtain authorization, synchronize, and verify on HPC

After the current notebook and dependency edits are ready for review, show the
concrete change scope and proposed verification. Ask for authorization to run the
entire named notebook on the configured HPC, including the intended baseline
comparisons. Follow `remote-hpc-operator` and confirm the notebook, server/kernel
environment, remote root, allowed node/allocation/resources, required inputs,
and whether outputs will be written or overwritten. Installation/repair and
unrelated jobs remain outside that authorization. Reuse sufficient prior explicit
authorization rather than asking repeatedly.

Follow the manual VS Code synchronization rule: name the exact task and wait for
the user to synchronize required source/configuration before executing. Direct
transfer requires a separate explicit request and the remote operator workflow.

Once authorized and synchronized, run the whole notebook in order, using its
normal cell-level result reuse. A notebook that only loads caches verifies the
load/display path, not changed computation. For changed scientific functions,
also use authorized small recomputations against baseline data, or an agreed
separate output destination, to exercise the changed logic without replacing
trusted results. Do not delete caches to force recomputation.

Use existing actual outputs as comparison baselines where available. Compare
analysis and plot-data tables as appropriate; document what ran, what was reused,
and which functions were exercised. Do not claim unchanged scientific results
solely because a cached file was loaded. If results differ, diagnose within this
notebook's scope and revalidate; do not accept unexplained differences as styling.
If remote access or execution is blocked, stop at the prepared notebook and
report the limitation instead of migrating the next one.

## 5. Human inspection, accepted snapshot, next notebook

After technical verification, present the current notebook for user inspection.
Give a concise account of changed sections/source, execution completion or first
failure, comparison outcomes and limits, saved result/figure-data paths, and what
the user should inspect. Ask the user to confirm the notebook's presentation and
scientific results are acceptable. This review is distinct from execution approval.

Wait for explicit acceptance; silence is not approval. Address requested changes
and rerun affected checks when necessary. After acceptance, create a local commit
of this stage's notebook and dependency edits, recording the accepted notebook in
the commit message. Include scientifically useful saved notebook outputs according
to existing repository practice; keep large data and private runtime state ignored.
Do not accidentally include unrelated changes.

Only after acceptance and a successful snapshot, advance to the next notebook in
the user-authorized project scope and repeat the process. Preserve a compact
handoff of the active notebook, baseline/accepted commit IDs, edits, verification,
pending approval, and next notebook so the workflow can resume across chats.
Do not add a separate management CLI or documentation tree for this state.

The phases are: baseline archived -> one notebook prepared -> execution authorized
-> execution/comparisons verified -> user accepted -> accepted stage archived
-> next notebook. Do not merge these milestones or report the project unified
while later notebooks or the current user review remain pending.
