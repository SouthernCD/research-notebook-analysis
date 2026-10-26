# Notebook Authoring

Use this guide when creating or editing notebooks and their nearby `src/` files. For independent analysis tools in `tools/`, also read [project-tools.md](project-tools.md).

For explicit whole-project style unification, also read [project-style-unification.md](project-style-unification.md): migrate one notebook and its source dependencies, then verify and obtain user acceptance before committing and advancing. Ordinary edits do not trigger that workflow.

For notebook creation or substantial structural edits, first read [authoring-examples.md](authoring-examples.md) and inspect the matching sections of [style_example.ipynb](../assets/project-template/notebooks/style_example.ipynb). The index calibrates heading-only operations, compact methods, detailed metric definitions, independent calculation/plotting, and captions ranging from one sentence to complex multi-panel or statistical explanations. The notebook demonstrates these patterns with paired English/Chinese narrative and visible local parameters, without invented findings. It has no executed outputs. Use relevant sections for small edits; preserve unrelated existing style and never execute or copy the example automatically. Apply the user's conventions to the changed portions, then perform the authoring self-review in `SKILL.md` before handoff.

## Research Record

### Write for research readers

Notebook Markdown addresses biology readers and reviewers. Limit it to research purpose, analysis content, necessary methodological definitions, and the meaning of figures/results. Explain what is done, why, and how to understand the output in concise, accessible language.

Do not describe how code runs: result reuse, file-existence checks, caches, skipping, forced recomputation, modification-time checks, or other program control logic. Runtime settings (threads, memory, concurrency, invocation details) belong in code, not repeated in Markdown. Keep resumption/progress logic in code and relevant interface contracts in docstrings; these implementation conventions still apply even though the prose does not narrate them.

Mention scientific parameters only when they affect biological understanding: window scale, whether Genic includes flanks, density denominators, coordinate/overlap conventions, or what merged intervals in a figure represent. Do not list arguments or paraphrase assignments. Relevant data provenance and specific scientific limitations belong next to the methods or interpretation they clarify.

For example, avoid “Load the cache if it exists; otherwise compute using eight threads, then skip completed chromosomes.” Write “Variants with MAF ≥ 0.05 are summarized in 500 bp windows. Mean MAF is calculated over retained variants; windows without retained variants are omitted,” when supported by the project.

Keep modification logs, refactoring baseline commits, verification status, synchronization, and pending tasks in the conversation or Git history, not Notebook Markdown. Do not insert editing records into code comments/docstrings or printed messages either. Never present unverified outputs as verified findings; flag affected outputs and execution limits in the handoff, omit unsupported conclusions, and handle misleading saved outputs explicitly. Minimal task markers remain locating aids only. Both languages follow the same restrictions and convey the same scientific meaning.

Prefer a small sequence of meaningful Markdown and code cells over a software-style abstraction layer.

- Organize major sections by scientific question, analysis object, or research stage; use operation-level subsections that readers can find independently.
- Before code, briefly state the scientific question or operation. A heading may be sufficient for an obvious routine step; do not repeat a full purpose/input/method/output template for every cell.
- Expand explanations where scientific meaning depends on coordinate systems, units, denominators, overlap handling, missing data, filtering, or parameter rationale. Define a derived metric with its formula or an equally precise definition, specify its reference/background and interpretation, and describe consequential low-count, zero-denominator, or tie rules when applicable. Distinguish a per-variant mean from a per-base density, and a complete background from a foreground-excluded control pool when relevant. Put definitions at first scientific use; captions may refer back rather than repeating the methods. Cite supplied provenance near the relevant input; do not invent sources. These are criteria for what needs explanation, not a checklist to repeat for every cell.
- Keep heading levels and numbering consistent with neighboring sections when inserting or splitting material.
- After important plots, explain how to read the figure in its bilingual caption. Add a separate interpretation paragraph only when it contributes scientific reasoning beyond the caption; ordinary calculation cells do not require a repeated explanation.
- Explain filtering and parameter choices only where needed to understand the biological analysis; do not narrate implementation settings.
- Preserve uncertainty and say what observation would resolve it.
- Keep saved outputs when they remain consistent with the code.
- When code changes make an old output misleading, clear only the affected output or tell the user to rerun that cell; do not imply the new output already exists.

### Section hierarchy and operation cues

Start with a title and a brief statement of the notebook's scientific scope. Arrange numbered sections in the order a reader needs to understand and perform the analysis: establish inputs and definitions, perform the scientific comparisons, then present results. Adapt the stages to the actual research; do not require a fixed stage list. Keep setup before the scientific stages when useful, and do not make helper names, file loading, caching, or export mechanics the main outline.

Use `#` for the notebook title, `## 1` for a major scientific section, `### 1.1` for its subsection, and `#### 1.1.1` when a further scientific subdivision helps navigation. Increase heading depth with numbering depth, keep English/Chinese pairs identical in level and number, and avoid parent/child titles that repeat the same topic. Unnumbered setup headings may stand before the numbered scientific sections.

Within a scientific subsection, prefer a short bullet such as `- LD-pruned SNP panel` or a standalone cue such as `Calculate statistics in 500 bp windows`. These are operations, not mandatory new subsections. Do not create a heading for every parameter definition, result load or plotting call. Introduce each operation only as much as a research reader needs; one or two sentences are normally enough.

### Figure captions

Use the sequence: English/Chinese scientific heading and brief purpose, calculation cells, plotting cell with displayed output, English figure caption, Chinese figure caption. Simple load-and-plot operations may use one plotting cell. Keep caption pairs immediately after the relevant plotting cell, with separate Markdown cells and matching figure numbers.

Number principal figures consecutively within the notebook. A caption starts with a bold number and concise scientific title, for example `**Figure 1. Chromosomal distribution of nucleotide diversity.**` and `**图 1. 核苷酸多样性沿染色体的分布。**`. Simple figures may need only that sentence. Explain panel or track order, colors, symbols, units, denominators or thresholds for more complex figures when they are needed to read them. Describe what is plotted rather than restating the calculation pipeline. Captions can carry the essential reading guidance instead of a separate "Reading the figure" subsection.

Use natural scientific terminology in each language. Parentheses introduce useful abbreviations or definitions, not editing hints; for example use `Kinship` in English and `亲缘关系` in Chinese. Omit generic caveats and repeated technical detail, while retaining limitations or definitions that materially change interpretation. Figure captions and short narrative do not replace the required export of actual plotted data.

## Bilingual Narrative Cells

All newly created or modified notebook narrative must use two consecutive Markdown cells:

1. English first;
2. equivalent Chinese immediately after;
3. then the associated code cell, when any.

Do not combine both languages into one Markdown cell. Code cells and generated outputs remain single; do not duplicate code merely to create a bilingual presentation. Use English for new code comments, identifiers, table labels, and figure labels unless the user requests another convention. Preserve existing labels and comments outside the requested edit.

Keep each pair semantically aligned:

- use corresponding heading levels and section numbers;
- preserve the same scientific claims, uncertainty, relevant scientific parameters, methodological definitions, and interpretation; do not add implementation details in either language;
- translate prose naturally rather than mechanically, without adding facts to only one language;
- update both cells whenever either member's meaning changes.

When the user edits Chinese Markdown and names it as the standard, treat that text as authoritative for scope, tone and detail. Revise the English to match additions and deletions, including headings and figure captions; do not preserve English-only explanations from an older draft. A natural translation need not mirror word order. If the requested wording conflicts with known scientific inputs or behavior, identify the conflict and make the smallest necessary correction without inventing findings.

For an existing monolingual notebook, create the missing language partner next to each Markdown cell touched by the current request. Preserve untouched historical cells unless the user asks to convert the whole notebook.

### Final publication copies

During project work, keep adjacent English/Chinese narrative cells in the same notebook and only one copy of its analysis code. Do not split languages for ordinary cleanup, debugging, style unification, or manuscript drafting. When the user is preparing the final publication/release, offer separate English and Chinese notebook directories as an optional reading convenience, for example `notebooks/` and `notebooks.zh-CN/`. A suggestion does not authorize restructuring; make the copies only when the user chooses this final-publication option.

For an authorized split, derive both versions from the same finalized bilingual notebook, retaining only the selected language's narrative while preserving identical code, code order, scientific parameters, relevant saved outputs, and corresponding section/figure numbers. Check that the retained language reads coherently, notebook paths/imports and project-root assumptions remain usable, and both README inventories explain which version to choose. Keep any retained working bilingual copy's role clear and avoid three competing editable versions. Do not rerun analyses, regenerate scientific outputs, or redesign the project merely to split narrative languages; validate notebook structure and code equivalence statically. If analysis resumes, use one bilingual working source rather than editing the publication copies independently.

## Remote Initialization Cell

Adapt this pattern to the project configuration. Start the initialization cell with the user's preferred warning suppression, then imports and remote setup.

```python
import warnings
warnings.filterwarnings('ignore')

import os
import socket
import sys

%load_ext autoreload
%autoreload 2

project_dir = '/absolute/remote/project/root'  # Confirmed config/project.yaml path.
os.chdir(project_dir)
project_dir = os.getcwd()
data_dir = f'{project_dir}/data'
source_dir = f'{data_dir}/source'
results_dir = f'{data_dir}/results'

os.makedirs(source_dir, exist_ok=True)
os.makedirs(results_dir, exist_ok=True)
if project_dir not in sys.path:
    sys.path.insert(0, project_dir)

from src.plot_style import set_plot_style
set_plot_style()

print(f"Host: {socket.gethostname()}")
print(f"Working directory: {os.getcwd()}")
print(f"Python executable: {sys.executable}")
print(f"Environment prefix: {os.environ.get('CONDA_PREFIX', '<not set>')}")
```

The path is interpreted by the remote kernel. The user should verify that hostname is an allowed remote node, cwd equals the configured remote project root, and the Python executable/environment matches the configured kernel environment. A mismatched kernel is a configuration or VS Code selection problem, not a reason to silently install packages into the active environment.

For `from src.module import ...`, the project root must be on `sys.path`, as above. If the existing project instead imports source modules directly (`from module import ...`), use its established convention and add the source directory when needed:

```python
import sys

src_dir = f'{project_dir}/src'
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)
```

Do not build or install a Python package merely to avoid this small notebook-local setup.

## Local Parameters and Focused Cells

For each scientific operation, keep its input/output paths, selected samples/features/contrasts, scientific parameters, and actual analysis call visible in the relevant notebook section. A useful cell shape is: relevant imports, explicit input/output paths, this step's parameters, computation or result loading, and a focused display or save operation. Adapt it to the established notebook rather than imposing a fixed skeleton or cell-length limit.

Keep scientific choices visible: thresholds, window sizes, analysis populations, random seeds, and frequently adjusted plotting settings should normally be set near the call that uses them. `src/` or `tools/` implements the operation; the notebook shows the choices and their rationale. Pass scientifically important values explicitly or visibly select/load their authoritative configuration; do not hide the research design inside an opaque runner. Avoid a distant global parameter block or hidden helper defaults for choices that materially affect interpretation.

When calculation and plotting share parameters/output paths, define them once in a short setup cell immediately before that analysis section. Both cells use those definitions; plotting reads saved statistics after lightweight initialization/setup, without needing to run the calculation cell. Keep plotting-only choices in the plotting cell. Do not independently repeat scientific parameter values merely to make a plotting cell appear self-contained.

Shared context definitions, named contrasts, or other catalogs used by several analyses can live in `config/`. State whether that catalog supplies executable values or documents notebook-defined values. Maintain one authoritative definition; pass notebook values explicitly or load catalog values explicitly instead of maintaining conflicting copies. Technical paths and remote settings remain project configuration.

## Reusable Results and Incremental Work

The core notebook philosophy is to resume the notebook at approximately cell granularity: substantial calculation cells save reusable results, so after restarting the computer or kernel, completed steps can be loaded and skipped. Cell-internal loops normally display progress without saving each iteration. If interrupted mid-cell, rerunning that cell from its beginning is acceptable. Use finer-grained checkpoints only when the workload actually justifies them or the user asks; avoid a checkpoint framework and do not force trivial setup/display cells to produce files.

For a reusable calculation, identify its expected output before the calculation and load it when complete and compatible. Otherwise prepare the calculation and save step for the user to run. Keep this logic per analysis step; do not introduce a global run mode or checkpoint framework by default.

- Put file and cache checks at the notebook or entry point that owns the result. Do not repeat the same checks in every helper. A helper that independently owns an output may manage that output's reuse.
- For multiple required outputs, check the complete set. For incremental annotation tables, check required columns or keys and add missing components without rebuilding unrelated annotations.
- When reusing results, display the path and relevant available metadata, such as dimensions, required columns, population, resolution, or recorded parameters. Check input/parameter compatibility using existing metadata when available. If compatibility cannot be established, state that limitation instead of declaring the cache valid.
- Keep compatibility handling proportional: meaningful filenames, existing metadata, and explicit reuse assumptions are normally sufficient for project-specific examples. Do not introduce hashing registries, schema validators, versioned cache managers, or pervasive input checks merely to enforce these conventions.
- A parameter change may require a different output name or explicit recomputation. Identify the affected outputs and downstream steps; do not silently overwrite unrelated or incompatible results. Moving or deleting outputs remains a user action unless explicitly requested.
- A cached result does not make a call harmless: inspect the cache-miss branch and keep its operations explicit in code. External tools and pipelines belong in explicit launch cells with visible key parameters, outputs and resource requirements; a `JOB` or `.run()` wrapper must not conceal those stages. The user running that cell may launch the analysis; the agent still needs execution authorization.

## Calculation and Figure Editing

Use the shared [plot_style.py](../assets/project-template/src/plot_style.py) implementation for the user's baseline typography, figure size, and line widths. Call `from src.plot_style import set_plot_style` and `set_plot_style()` once in the initialization cell after remote path/import setup, before creating figures. Keep import free of style-changing side effects. For an existing project, integrate with its shared plotting module rather than maintaining two competing style functions.

All figures start from this baseline, including those made by `src/` helpers. Per-figure `figsize`, layout, data colors, and scientifically necessary axis settings can vary; avoid blanket `plt.style.use`, Seaborn theme resets, or helper-level rcParams changes that silently replace the shared style. After editing the shared style, sync `src/` and rerun its initialization call before rerunning plotting cells; autoreload alone does not reapply rcParams. Arial availability is a kernel-environment fact, not a reason to install fonts or silently change the requested style.

By default, put substantive statistical calculation and plotting in separate code cells. The calculation cell saves its intermediate table; the plotting cell loads that saved table and contains only plot-data selection/transformation, figure styling, and exports. This allows rerunning plots without expensive recalculation or relying on the calculation cell's in-memory state. A short load-and-plot cell is appropriate, but do not hide expensive cache-miss computation inside it. If saved statistics are absent, report the missing input and identify the calculation cell to run; do not fall back to computation. Plotting may select, reshape, scale, or aggregate the saved statistics for display, but model fitting, permutations, genotype processing, or new scientific estimation belongs in calculation cells. A small calculation-stage preview table is useful and does not require an artificial extra plotting cell. When reviewing the edit statically, trace plotting inputs back to disk and section setup to catch dependencies on objects created only by the expensive calculation cell. Consult the separate calculation and plotting cells in the notebook example before authoring this pattern.

Prefer plotting helpers that accept existing tables and return figure/axes for further adjustment. Display important figures inline and save suitable export formats. Always save the actual figure data as `.csv.gz` using pandas for publication inspection, including the selected rows and transformed/aggregated values used by the plot. Export relevant series/panels with clear identifiers, either together or as separate compressed tables. A large HDF intermediate does not replace this export. Name outputs consistently with the analysis and relevant parameters; do not hard-code paper-specific figure numbers into the generic skill.

Use diagnostic panels when they help evaluate a result, rather than copying a particular project's colors or panel layout universally.

## Notebook, `src/`, and `tools/`

Keep code in the notebook when it is short, specific to one analysis step, and improves the visible reasoning trail.

Use `src/` when code is:

- reused by more than one cell or notebook;
- long enough to obscure the scientific flow;
- easier to test or review as a function;
- a shell pipeline or scheduler implementation whose details are easier to review separately, while its launch remains explicit in the notebook.

Use `tools/<tool-name>/` for a coherent analysis tool with a defined independent interface and its own internal structure; follow [project-tools.md](project-tools.md). Keep project-specific adapters in root `src/` when needed. The tool may expose a CLI, while notebook cells still launch its use in this research workflow.

Functions imported from `src/*.py` or tool packages must not perform work at import time. After a local edit, the user must run the VS Code sync task before rerunning the import/call cell. `%autoreload 2` normally reloads changed modules; use explicit `importlib.reload()` only when autoreload is unsuitable for the package.

### External tools and scheduler launch cells

Use notebook cells as the default entry point for every analysis step, including external tools, file-changing operations, and long-running computation. `subprocess.run` is allowed in cells or source functions. Prefer a clear argument list with `check=True` and visible stdout/stderr or a named log; a simple shell magic is also acceptable when it communicates the operation clearly. Long/reused shell or scheduler implementations can live in `src/` or the relevant `tools/<tool-name>/`, with the notebook explicitly calling them and setting their key parameters. Do not require users to edit/run scripts outside the notebook solely because an operation is external or expensive.

Before a launch cell, briefly explain its scientific purpose and necessary method definitions in Markdown. Put execution context, inputs/output paths, resource settings, and invocation details in code. Show progress or log location through code, propagate failures, and only reuse complete relevant outputs at the layer owning that step. Keep automatic import side effects prohibited; launching happens when the reader deliberately runs the cell, not when a module is imported.

For scheduler work, use commands/resources from the machine profile. The notebook should expose submission, recorded job identity, status/log inspection, and a completion check before downstream results are loaded. Submission is not completion. Prefer a simple profile-specific implementation; do not build a universal scheduler platform. Existing pending jobs must not be silently resubmitted after a kernel restart. Direct compute cells must run within an allowed allocation; notebook convenience does not permit scientific work on a forbidden login node.

If the notebook's Run All is intended to complete the workflow, a job-backed step must wait/check completion before continuing. If the actual scheduler/session behavior requires separate submit/check/continue cells, explain that order prominently so the reader can still complete it within the notebook. Outside-notebook analysis actions are exceptions only for explicit user choices or concrete machine/tool limitations, and must have a reason and an exact notebook continuation point. Infrastructure setup (Jupyter, SSH tunnel, manual source synchronization) retains the existing project-guide workflow.

For example, a short external sample-extraction step can be launched directly from a cell. Adapt the inputs and threads to the confirmed project and allocation; `bcftools` must already be available. A longer implementation may move into a documented source function without moving its launch out of the notebook:

```python
import subprocess
from datetime import datetime

input_vcf = f'{source_dir}/variants.vcf.gz'
sample_file = f'{source_dir}/analysis_samples.txt'  # One selected sample ID per line.
output_vcf = f'{results_dir}/analysis_samples.vcf.gz'
threads = 4  # Within the confirmed allocation.

if not os.path.exists(output_vcf):
    print(f'[{datetime.now():%H:%M:%S}] Extracting samples: {output_vcf}', flush=True)
    temporary_vcf = f'{output_vcf}.tmp'
    subprocess.run([
        'bcftools', 'view', '--samples-file', sample_file,
        '--threads', str(threads), '-Oz', '-o', temporary_vcf, input_vcf,
    ], check=True)
    os.replace(temporary_vcf, output_vcf)
if not os.path.exists(f'{output_vcf}.tbi'):
    subprocess.run(['bcftools', 'index', '--tbi', output_vcf], check=True)
```

Show only the scientific sample-selection rationale in paired narrative before this cell; keep output reuse assumptions in code comments or the interface docstring. This is an invocation pattern, not a mandatory step or a function to copy into every project.

## Python Source Style and Interfaces

See [style_examples.py](../assets/project-template/src/style_examples.py) for complete examples of the conventions below. The module is reference material for the agent, not a required project dependency or generated analysis file.

### Paths, tables, and progress

Prefer string paths built with `os` and f-strings, matching `project_dir = os.getcwd()` and `data_dir = f'{project_dir}/data'`. In remote notebooks, first change to the confirmed configured project root rather than trusting the initial kernel directory. Use `os.makedirs(..., exist_ok=True)` and `os.path.exists()` at the layer owning output creation/reuse; do not add `pathlib` abstractions by default.

Use pandas for tabular processing and persistence. Prefer `.csv.gz` for small tables; use one `.h5` file per large table, with key `'df'`. Read and write with `pd.read_csv`/`to_csv(..., compression='gzip')` and `pd.read_hdf(..., key='df')`/`to_hdf(..., key='df', mode='w')`. Set `index=False` for CSV unless the index carries scientific meaning. Choose formats based on actual size/access needs rather than a universal size cutoff. Non-tabular data can retain their appropriate native format. HDF requires the configured kernel's PyTables dependency; do not install it implicitly.

For multi-stage source tasks and notebook loops, show the current stage, reuse/save path, and elapsed time. Use `datetime.now()` for timestamps and `perf_counter()` for durations. For substantial loops, prefer `tqdm.auto.tqdm` with a meaningful `desc`, `unit`, and total where known, providing elapsed time, rate, and estimated remaining time. Parallel progress should count completed work. Avoid per-row print floods, duplicate nested bars, or building a logging framework; trivial helpers need no progress output.

When interrupted output could be mistaken for a completed stage, write to a temporary sibling path and use `os.replace()` only after the table is fully written. This is a small persistence safeguard, not an invitation to add elaborate cache validation. Document reuse assumptions in code comments or interface docstrings and retain targeted compatibility checks as needed, without narrating them in Notebook Markdown.

### Direct implementation and input assumptions

Target the current project's known inputs. Document expected fields and formats, then use them directly. Let ordinary library exceptions expose missing files, missing columns, and malformed inputs instead of adding a custom error layer. Avoid speculative format detection, legacy compatibility, automatic column guessing, broad exception handling, and returning empty results after failure.

Keep checks that prevent plausible silent scientific errors: mismatched sample order, ambiguous identifiers used for alignment, incompatible coordinate systems or units, and unintended output replacement. Place each check where the relevant assumption is established, without repeating it in downstream helpers. A documented requirement does not automatically need a runtime assertion. These conventions do not weaken remote execution or resource-policy checks.

Prefer a sequential flow of input selection, transformation, calculation, and output. Extract helpers for a meaningful independent step, real reuse, or a substantial improvement in readability. Avoid one-use wrappers around a few obvious statements and classes or factories without a concrete state-management need. Core computations can accept data and return results; large-file operations can accept paths when loading everything first would be impractical.

### Compact formatting

Keep short calls and expressions on one line. Wrap longer calls at a readable width, grouping related arguments rather than placing every argument on its own line by default. Use blank lines between logical stages, not between consecutive assignments or each statement. Do not change project formatter settings merely to enforce this preference.

Keep intermediate variables that explain scientific objects or transformations. Avoid semicolon-packed statements, nested one-line pipelines, and clever comprehensions that conceal the analysis. Function length is a review signal, not a hard limit; unnecessary whitespace and mechanical helper extraction do not improve it.

For a simple internal helper, this is sufficient:

```python
def summarize_contexts(context_df, context_names):
    """Count variants and their fraction in boolean context columns."""
    counts = context_df[context_names].sum()
    summary = counts.rename("count").to_frame()
    summary["fraction"] = summary["count"] / len(context_df)
    return summary
```

A short call can remain on one line; a longer call can group related parameters:

```python
df = pd.read_csv(input_file, sep="\t", usecols=["CHROM", "POS", "MAF"])
stats = calculate_statistics(
    df, window_size=500, min_sites=3,
    min_maf=0.05, max_het=0.05, n_jobs=8,
)
```

### Document according to interface role

- Simple internal helper: a one-sentence docstring, or none when the purpose is self-evident.
- Notebook-facing or shared function: an English NumPy-style docstring describing purpose, `Parameters`, `Returns`, and relevant assumptions or side effects.
- Multi-stage analysis/pipeline function: also include `Workflow` to explain the major stages and their order. Documenting a workflow does not authorize executing it or justify adding a workflow framework.

For important interfaces, explain what callers cannot reliably infer from the signature: required fields and ordering, scientific units and parameter meaning, output structure, external tools, files written, result reuse, overwrite scope, and concurrency behavior. Include only sections relevant to the actual function. Document actual behavior; do not promise checks, caching, or outputs the implementation does not provide. Use type hints when they clarify the interface without building an elaborate type system.

For example, a result-loading interface could use:

```python
def load_variant_sets(context_df, prefix):
    """
    Load positional variant sets and map them to variant IDs.

    Workflow
    --------
    1. Read the saved foreground and permutation positional indices.
    2. Map indices to IDs using the original context dataframe order.

    Parameters
    ----------
    context_df : pandas.DataFrame
        The same rows and order used when building the variant sets.
        Must contain unique variant identifiers in column "ID".
    prefix : str
        Prefix of <prefix>.foreground.npy and <prefix>.permutations.npy.
        Foreground indices are a one-dimensional integer array;
        permutation indices are a two-dimensional rectangular array.

    Returns
    -------
    tuple of numpy.ndarray
        Foreground IDs (1D) and permutation IDs (2D).
        Reads existing files; does not modify them or create missing sets.
    """
    ids = context_df["ID"].to_numpy()
    foreground = np.load(f"{prefix}.foreground.npy")
    permutations = np.load(f"{prefix}.permutations.npy")
    return ids[foreground], ids[permutations]
```

Use comments for scientific reasons, stage boundaries in longer functions, and non-obvious implementation choices. Do not narrate every assignment. Keep new comments, docstrings, and code labels in English unless the user requests another convention; the bilingual pairing rule applies to narrative documents and notebook Markdown, not to duplicating Python docstrings.

When editing existing source, apply these conventions to the requested work and necessary surrounding changes. Preserve unrelated working code instead of performing a project-wide style migration.

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
3. Keep edits scoped to the marked cell and the smallest necessary nearby cells, `src/` files, or tool files. A bilingual Markdown partner is required scope, not an unrelated expansion. Disclose every additional edit in the handoff.
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
- files written to `data/results/`, an existing project's `results/`, or other remote paths remain remote unless the user explicitly requests a download.

Do not assume a remote result exists locally or that a local file exists remotely.

## Whole-Notebook Execution

Do not run individual cells or the notebook by default. Only enter execution mode when the user explicitly asks to run the entire named notebook.

Separately authorized focused regression checks for style unification follow [project-style-unification.md](project-style-unification.md). Their authorization covers the specified checks only, not arbitrary notebook cells or unrelated computation.

Before execution:

1. confirm the exact notebook path;
2. confirm the intended remote kernelspec and environment;
3. confirm the configured remote project root;
4. verify the execution node and resource policy through `remote-hpc-operator`;
5. ensure required `src/`, `tools/`, and `config/` changes were synchronized;
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

If `src/`, `tools/`, or remote-consumed `config/` also changed, replace the sync line with the exact VS Code task and tell the user to sync before rerunning the marked cell. Omit irrelevant lines only when the remaining handoff is still unambiguous. Explicitly state when no sync or run is needed.
