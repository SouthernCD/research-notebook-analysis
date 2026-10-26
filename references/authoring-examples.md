# Choosing Notebook Examples

Use this index before creating a notebook or substantially revising its narrative/cell organization. For a small edit, read only the matching example. The examples calibrate how much explanation and code to expose; do not impose all cases on every analysis.

The presentation draws on the real [sorghum local-adaptation project](https://github.com/SouthernCD/functional-genomic-local-adaptation-sorghum): scientific stages, concise routine prose, explicit definitions for derived metrics, local parameters, saved statistics, and figure-specific captions. The local examples are illustrative, unexecuted, and self-contained as references; they are not a reproduction of that project's methods or results. Follow this skill's adjacent English/Chinese cells during development, regardless of the reference repository's separate publication language directories. Read the local examples without fetching the repository each time.

## Read the matching pattern

Use headings and stable cell IDs in [style_example.ipynb](../assets/project-template/notebooks/style_example.ipynb), rather than positional cell numbers.

| Current task | Example to inspect | What to take from it |
| --- | --- | --- |
| Open a scientific stage | Notebook title; sections 1–5 | Short scope statement; headings follow research questions and dependencies. The section count is illustrative. |
| Initialize paths/kernel/style | `style-cell-04` | Explicit remote context, autoreload, one shared-style call; no research computation at import. |
| Explain a routine method briefly | Section 2.1 | One compact paragraph identifies filtering, windows, denominator, and omitted windows. |
| Introduce an obvious operation | `style-cell-13`, `composition-cue-en` and Chinese partners | A short bullet is sufficient; do not add a purpose/input/method/output block. |
| Show a small calculation/table | `composition-calculate` | A few direct pandas statements plus a table; no helper or repeated prose for obvious operations. |
| Set parameters shared by compute and plot | `style-cell-12`, `regional-setup` | Paths and scientific choices defined once near use; plotting can restart after setup. |
| Save and reuse substantial calculations | `style-cell-15`, `regional-calculate` | One owner of persistence/reuse, explicit assumptions and rerun choice, result preview, progress/time. |
| Define a nontrivial scientific metric | Section 5.1, `regional-definition-en/zh` | Formula, reference region, raw-versus-transformed quantile, coordinate conventions, low counts and undefined cases. |
| Explain interpretation without inventing results | `regional-interpretation-en/zh` | Explain what values mean and a specific limit; do not claim enrichment or significance without output. |
| Rerun a plot independently | `style-cell-18`, `regional-plot` | Load disk statistics, identify missing upstream calculation, style and export actual plotted values; no cache-miss analysis. |
| Write a minimal caption | Figure 2, `composition-caption-en/zh` | One sentence names the quantity and its scientific filter; visible axes need no redundant inventory. |
| Write an intermediate caption | Figure 1, `style-cell-19/20` | State panels, units, denominator, and the fact that lines connect across gaps. |
| Write a complex multi-panel caption | Figure 3, `regional-caption-en/zh` | Explain panel order, color/line meaning, baseline, coordinates, window scale, and meaningful edge cases. Refer to an earlier definition instead of reprinting its derivation. |
| Prepare external or scheduler work | [External launch cells](notebook-authoring.md#external-tools-and-scheduler-launch-cells) | Scientific purpose in paired prose; invocation/resources in code; status and completion before downstream reading. |
| Illustrate an optional independent tool | [English layout](../assets/project-template/README.md#optional-tool-layout) / [中文结构](../assets/project-template/README.zh-CN.md#可选工具结构); [tool rules](project-tools.md) | Minimal directory, explicit CLI call in a calculation cell, external output path, separate plotting, and source-only manual sync. This is illustrative; do not generate a tool merely to match it. |
| Move implementation into source | [style_examples.py](../assets/project-template/src/style_examples.py) | Meaningful interface docstrings, sample-alignment check, progress loop, and plotting helper; do not copy the module into projects. |

All numeric thresholds, sample identifiers, input contracts, and scientific methods in these examples are illustrative. Adapt them to actual project evidence. In particular, the regional-profile example requires association/anchor tables in its documented formats; do not create fictional data files, claim results, or substitute these definitions for an established project's algorithm.

## Calibrate narrative length

**Heading or cue only:** For an obvious count or display under an already defined stage, use the `Variant composition` example. The code and table identify the operation. No separate explanation of groupby, saving, or printing is needed.

**One compact methods paragraph:** Section 2.1 says which variants, which windows, what denominator, and what is omitted. Add one short rationale only when the choice needs scientific justification. Do not restate paths, process counts, or assignments in prose.

**Several paragraphs plus a formula:** Section 5.1 needs more space because the meaning depends on operation order, a regional reference, low counts, and undefined ratios. Keep the definition and edge cases together, then use a separate short interpretation cell. Formula length alone does not justify extra headings. A less complex metric needs less explanation.

**Specific limitation:** State the limitation that changes interpretation, as in “This descriptive ratio is not a significance test.” For a prediction evaluation with overlapping training samples, identify that overlap and its consequence using actual project facts. Do not add generic cautions, agent-editing history, or unsupported findings.

## Statistical comparisons and captions

Use more detail when readers need to distinguish the analysis background from the null distribution. The following are paired narrative examples for an analysis that actually uses this design; they are not findings or a required analysis step.

English cell:

```markdown
### 2.1 Matched control sets

Compare foreground variants with the complete eligible background, which includes the foreground. Draw 1,000 equal-size control sets without replacement within each set from non-foreground background variants, matching allele-frequency and recombination classes. Retain only strata with enough control variants; report the excluded foreground count.
```

Chinese cell:

```markdown
### 2.1 匹配对照集合

将前景变异与包含前景的完整合格背景比较。从背景的非前景变异中抽取 1,000 组等量对照，每组内部无放回抽样，并匹配等位基因频率和重组率类别。仅保留对照变异足够的分层，并报告被排除的前景变异数量。
```

The associated setup cell would visibly select foreground/background definitions, matching classes, repetitions, seed, and output paths. The calculation cell would save observed statistics, each control statistic, excluded counts, and the defined empirical test. The plot would read those results. Do not invent a callable API solely to make this prose example look runnable.

A caption for a hypothetical figure showing those saved statistics could read:

English cell:

```markdown
**Figure 1. Association signals in foreground and matched-control variants.** Columns show environmental variables. Blue and gray vertical lines mark mean −log10(P) for the retained foreground and complete eligible background, respectively; beige histograms show the means for 1,000 matched-control sets. Each control set contains the same number of variants as the retained foreground. The dashed line marks the median control mean. Background definitions and matching exclusions are described in section 2.1.
```

Chinese cell:

```markdown
**图 1. 前景与匹配对照变异中的关联信号。** 各列对应环境变量。蓝色和灰色竖线分别表示保留前景及完整合格背景的平均 −log10(P)；米色直方图表示 1,000 组匹配对照的均值。每组对照的变异数量与保留前景相同。虚线标记对照均值的中位数。背景定义与匹配排除规则见第 2.1 节。
```

If a real figure includes intervals or significance marks, define them precisely: a fifth–ninety-fifth percentile range across random sets is an empirical 90% interval, not automatically a confidence interval for the mean; identify the test, sidedness, threshold and correction when marks are shown. If the figure has none, do not add statistical claims to its caption. Do not call an SD or variance band a confidence interval. Figure numbers in this standalone illustration are local; number actual notebook figures consecutively.

## Apply, then review

Choose the smallest pattern that communicates the current science, adapt its content, and review the changed notebook against `SKILL.md`. Do not copy reference notebook stages, source imports, inputs or thresholds wholesale, and do not add these agent-facing explanations or this index to research notebooks. Preserve the user's established scientific meaning, working structure, and saved outputs where consistent. Reading or adapting an example never authorizes executing notebook cells.
