# New User Guidance

Use this guide when a user asks how to start, explicitly says they are new, or
needs help with the local notebook / remote computation model. Do not infer
inexperience from an empty project or missing configuration. Use the user's
language and technical level; do not repeat an introduction they already know.

## Explain the collaboration briefly

Begin with a short explanation, adapted rather than pasted verbatim:

> 我可以帮你把研究问题组织成 notebook，准备分析代码、结果保存和绘图。
> Notebook 在本地编辑，数据和计算通常在远端；代码准备好后，默认由你运行
> 并检查结果。我们先完成一个明确步骤，再逐步扩展项目。

Distinguish editing from running, and displayed figures from files saved remotely.
Explain that the notebook displays and launches the complete defined analysis,
including external-tool steps implemented in `src/` or `tools/`; separate terminal analysis
scripts are not the default reproduction path.
Do not start with a list of every configuration field, a large directory tree, or
all the skill's restrictions. Explain terms such as kernel, synchronization, and
scheduler only when relevant, using concrete actions rather than jargon.

## Clarify the question, data, and expected outcome

Read the user's existing explanation and supplied artifacts first. Ask only what
the next decision needs, normally one to three short questions at a time. A user
does not need a complete hypothesis, pipeline, or chosen method to begin.

- Research: what question do they want to explore, and what observation would
  help them understand it? Keep a vague idea explicit instead of manufacturing
  a hypothesis or claiming that the data support a conclusion.
- Data: what is available, where is it located, and which processing steps are
  already complete? Distinguish raw inputs from analysis-ready derivatives.
- Expectations: are they exploring data, reproducing a method, organizing work
  already done, or preparing publication figures? Identify the next useful
  deliverable and how the user will inspect it.

For example, when none of this is known:

> 先告诉我你最想回答的问题、已有的数据及其位置，以及当前最希望得到的
> 一张图、一个表或一项检查。方法还没确定也可以，我们先从现有数据判断
> 哪一步最值得做。

Offer a small number of grounded starting options when helpful, with their purpose
and required inputs. Do not propose every possible analysis or promise a full
paper from limited information. Record agreed choices in the project narrative;
label suggested methods and unresolved choices as such.

## Help the user describe and prepare data

Initially, a file list, column description, or a few representative rows may be
enough. Do not demand upload, copying, or downloading of the entire dataset.
Inspect accessible local artifacts before asking the user to restate their contents;
actual remote inspection requires `remote-hpc-operator` and its access rules.

Help establish the information relevant to the first step:

- Machine/path, file format, approximate size, and what each row/file represents.
- Key identifiers and relationships between inputs: sample IDs, gene IDs, variant
  IDs, or equivalent domain identifiers. Explain how tables will align.
- Prior processing, units, reference/coordinate conventions, and known omissions
  when they matter to the analysis. Do not require irrelevant metadata.
- Source/provenance and whether the current inputs are sufficient for the chosen
  starting point. Missing data can become a concrete prerequisite, not invented
  placeholder observations.

Explain the default data roles: `data/source/` holds externally supplied read-only
inputs; `data/results/` holds generated analysis products. Both are excluded from
Git regardless of size. Preserve an existing layout; do not move data merely to
match the convention or confuse Git archiving with data backup.

If only raw data are available, clarify what preparation belongs to the project's
defined reproduction scope. Included preprocessing should have explicit notebook
launch cells, even when implemented with external tools or scheduler files in
`src/` or `tools/`. Explain required resources and completion checks. Onboarding itself does
not authorize the agent to execute a pipeline or install its dependencies.

## Agree on one concrete first step

Translate the initial discussion into a minimal research starting point:

1. Which known inputs will be used?
2. What will be checked or calculated first?
3. What table/result will be saved, and is a figure useful?
4. What will the user inspect to decide whether the step is sound?

For example, an input audit may check alignment between sample metadata and a
genotype dataset before association analysis. Choose this only when relevant to
the actual inputs; do not force all projects through the same audit notebook.

If the method remains undecided, continue grounded discussion or data inspection.
Do not generate executable scientific choices as though the user had agreed to
them. Once the first step is clear, use [project-setup.md](project-setup.md) for new
projects, or incremental editing for existing ones. Read the authoring examples
when preparing actual notebooks/source.

## Introduce technical setup when needed

When the first step needs a remote kernel, explain the confirmed machine/root,
server versus kernel environment where relevant, and the required node/resources.
Present verified options from the machine profile; do not reuse another project's
settings. Missing choices should not block independent research discussion or
documentation, but must not be guessed in runnable setup.

At connection time, point to the private project startup guide and explain the
next action: start the permitted Jupyter session, open the local SSH tunnel,
choose Existing Jupyter Server, then verify the initialization cell. Do not
proactively start the service or run analysis merely to demonstrate the workflow.

At source-edit handoff, name the exact VS Code sync task and say why it is needed:
local `src/` or `tools/` changes must reach the remote kernel. Notebook-only edits need no
notebook synchronization. Keep detailed startup/shutdown commands in the project
guide rather than restating all infrastructure steps every turn.

## Set expectations and hand off a manageable action

The agent prepares clear notebooks, readable source, result persistence and plots;
explains scientific choices and checks; and states what remains unexecuted or
uncertain. The user supplies research context, confirms scientific choices, and
inspects real outputs. Neither a prepared cell nor an existing file is proof of a
scientific conclusion. Execution and remote changes retain their normal
authorization boundaries.

The first handoff should emphasize the next smallest useful action and its check,
including prerequisites such as sync only when relevant. Identify the cell by
heading/purpose, the output to inspect, and the decision that follows. Do not
overload the user with the entire future pipeline.

Use a short project-specific "Getting started" section in paired READMEs to
record the first step and relevant data preparation. The guide here is agent
instruction, not an extra beginner manual to copy into every project. Do not
create a separate documentation tree by default or force experienced users to
repeat onboarding.
