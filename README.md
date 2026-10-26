# Research Notebook Analysis

[中文说明](README.zh-CN.md)

## The way we want to work

We want a collaborative research workflow built around VS Code and an AI agent, where researchers can follow the reasoning and analysis step by step, moving forward through observation, discussion, and exploration.

The researcher stays in the driver's seat: choosing the questions, deciding which evidence matters, interpreting results, and setting the next direction. The AI agent is a copilot. It helps frame questions, prepare code, explain methods, diagnose errors, and carry out the specific work the researcher points to. You can ask questions, change direction, or request an explanation before any edits.

As exploration proceeds, the project develops a collection of notebooks that reflects the progress of the research. The notebooks connect the analysis stages, show key technical choices and actual results, and explain what those results mean. They record or explicitly reference the data provenance, environments, parameters, code, and steps needed for reproduction. A future reader should be able to understand why the work was done this way, what the evidence supports, and how to obtain the results again.

## How notebooks carry the research

Each notebook covers a meaningful scientific stage, and the notebooks connect in analysis dependency order. Important parameters and calls remain visible where they are used. Complex methods receive the definitions they need; simple operations need only a brief cue. Figure captions explain how to read the results. Longer implementations can live in `src/`, and complete independent tools can live in `tools/`, with their entry points retained in the research notebooks.

The research record should develop with the work: actual observations, the judgments they support, limitations that affect interpretation, and unresolved questions belong near the relevant analysis. Proposed ideas should be distinguishable from existing evidence. Calculation and plotting are separate, and substantial steps save results so the next round of exploration can continue from completed work.

During development and debugging, adjacent English and Chinese Markdown cells share one set of code cells in each notebook. This makes comparison and revision easier. At final publication preparation, separate language directories can be generated if useful for readers.

## Start with a concrete question

You do not need a complete research plan. You can name `research-notebook-analysis` in your request, describe the current question and available materials, and identify the next step you want help with. For example:

> Use research-notebook-analysis. I have genotype data and sample environmental metadata, and I want to study environmental adaptation. I do not have a full plan yet. Help me understand the available materials and choose a useful first step.

You can also ask for specific work in an existing project:

> Read this notebook and explain its research logic, key assumptions, and what evidence is still missing. Discuss it first without editing code.

> Add a comparison to this section. Keep the existing samples and filtering criteria, make the method and parameters clear, and tell me how to run it when the code is ready.

> Adjust this figure's layout and caption using the statistics already saved.

> This step failed. Here are the notebook path and error output. Diagnose the cause in context.

File locations, data formats, relevant sections, existing outputs, and what you want changed or preserved are often more useful than a long specification. Data descriptions or small examples are enough to begin; large datasets usually stay remote.

## Working with the agent

Advance one meaningful step at a time. The agent inspects existing materials, explains its understanding and unresolved choices, and prepares notebooks and code. You run the work, inspect the results, and continue the discussion from what you observe. If a method is unclear, ask about its assumptions and scope. If a result is uncertain, ask for a diagnosis or a comparison before expanding the analysis.

You own the research goals, scientific choices, and interpretation. The agent helps express those choices as readable, operable, reproducible analyses. By default, the agent prepares edits and you run and inspect them. If you want the agent to execute an entire notebook, name it and state the execution request explicitly. Actions such as starting Jupyter or installing software also need an explicit request. The companion `remote-hpc-operator` skill governs machine, environment, and resource choices.

After an edit, the agent should explain what changed, whether synchronization is needed, which cells to run next, and what output to inspect. Bring actual results, errors, or specific questions back into the conversation. For example: “This distribution differs from what I expected; first check sample alignment and the denominator.” That feedback becomes the starting point for the next step.

## Local editing, remote computation

This workflow primarily serves projects whose notebooks remain in local VS Code while a remote HPC kernel performs the calculations. Source and configuration are synchronized through manual VS Code tasks. Jupyter returns figures and text for display, while large inputs and results usually remain remote. Once the project is configured, its private Jupyter startup guides help you connect and continue independently.

Notebooks record the analysis and reference supporting environment documentation, data inventories, and source code. The project README explains notebook order and where reproduction begins. Git preserves the evolution of code and research documentation; data and results need to be retained in their actual storage locations. Together, these records keep the research context with the project so later collaboration can continue from the work already done.

## Further reading

- [SKILL.md](SKILL.md): the detailed working conventions followed by the agent.
- [Example reading index](references/authoring-examples.md): how to organize explanations, code cells, and captions at different levels of complexity.
- [Example notebook](assets/project-template/notebooks/style_example.ipynb): an unexecuted reference for bilingual narrative, parameters, calculation, and plotting.
- [remote-hpc-operator](../remote-hpc-operator/SKILL.md): companion conventions for machines, environments, and remote operations.
