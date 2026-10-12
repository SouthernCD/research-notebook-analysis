# <项目标题>

[English](README.md)

## 研究目标

简要说明本项目要回答的科研问题。未知内容应明确保留为待解决事项，不提前编造研究假设或结论。

## 如何开始

先说明当前研究问题、已有输入的路径、格式及标识符，以及首先想查看的表、图或检查结果。不需要已有完整分析方案。文件说明和少量示例通常足以开始；不要仅为打开项目而把大型数据复制到本地。

在这里说明本项目的第一本 notebook 及其输入准备，明确首先运行哪些 cells、检查什么输出，以及仍待决定的事项。远端配置确认后，按照私有 `JUPYTER_START.zh-CN.md` 指南连接。运行源码的导入或调用 cells 前，先通过指定 VS Code 任务同步源码修改。Agent 准备代码，不自动运行分析。

## Notebook 顺序

1. `notebooks/01_<step>.ipynb` — 当前研究步骤和预期产出。

只列出当前研究计划已经明确需要的 notebook。

## 数据与复现边界

- `data/source/`：来自项目外部的只读输入，可以包括已记录来源、可直接分析的加工数据。
- `data/results/`：分析产物，包括中间表格、模型、外部程序输出、作图数据及最终输出。

说明实际使用的输入、来源和获取方式、复现起点，以及不属于本项目范围的上游处理。保留已有的数据布局，不要仅为匹配本示例而迁移目录。

科学参数通常在 notebook 中实际使用的位置说明和设置。跨分析共用的定义可以放在 `config/` 中，并明确其权威来源。

## 本地与远端文件

- 本地：`README.md`、`README.zh-CN.md`、`notebooks/`、`src/`、`config/` 和 `.vscode/tasks.json`。
- 私有本地指南：`JUPYTER_START.md` 和 `JUPYTER_START.zh-CN.md`；二者均为项目专用文件，并由 Git 忽略。
- 远端：同步后的 `src/` 和 `config/`，以及 `data/`（或项目已有布局）中的大型输入与分析产物。
- Notebook 保存在本地，其中的 Python 代码通过所选远端 Jupyter kernel 运行。
- 图、表和文字显示通过 Jupyter 返回；写入磁盘的文件默认仍保存在远端。

## 环境与执行

- Machine profile：`<machine-id>`
- 远端项目根目录：`<absolute-remote-project-root>`
- Jupyter server 环境：`<jupyter-server-environment-name>`
- Notebook kernel：`<kernel-display-name>`（`<notebook-kernel-environment-name>`）
- Scheduler：`<scheduler-type>`

远端机器、软件和 scheduler 规则来自 `remote-hpc-operator` 中对应的机器 profile。

## 笔记工作流

1. 在本地编辑 notebook、`src/` 或 `config/`。
2. 修改 `src/` 或远端需要读取的配置后，在 VS Code 中运行 `Sync <project> to <machine>`。
3. 按照 `JUPYTER_START.zh-CN.md` 在允许的远端节点启动 Jupyter，并打开本地 SSH tunnel。
4. 在 VS Code 中连接 Existing Jupyter Server URL，并选择已配置的 kernel。
5. 手动运行 Codex 交接中指定的单元格，并检查其输出。
6. 在明确的 notebook cells 中启动外部工具或调度器管理的大型分析；检查日志和 job 状态，确认完成后再运行下游 cells。

可复用的步骤应定义预期输出，并在已有结果完整且适用时读取。显示复用路径及相关 metadata；文件存在本身不能证明其与当前输入和参数一致。有意重跑某一步前，应明确受影响的输出。较大的计算 cell 保存可复用结果，使后续 notebook session 能跳过已完成步骤。cell 内循环默认只展示进度；确有需要时再采用更细的断点。使用 pandas：小表保存为 `.csv.gz`，大表一表一个 `.h5` 文件（key 为 `df`）。路径采用 `os` 和 f-string。计算与绘图分成独立 cells；绘图读取已保存统计，并始终将实际作图数据导出为 `.csv.gz`，便于发表检查。多步骤任务报告时间及耗时，较长循环使用 `tqdm` 显示进度和速度。Notebook 是既定分析范围的完整入口：源码文件承载实现，cells 展示并启动各步骤及其关键参数。笔记外的分析操作须有明确说明的例外理由。

共享仓库时，提供去除私有信息的项目配置和同步任务示例，将真实的机器专用设置保持为私有文件。

远端配置验证完成后生成项目专用启动指南。只有用户明确要求时，Codex 才代为启动或管理服务。

项目图件统一基于 `src/plot_style.py`；在 notebook 初始化时调用 `set_plot_style()`。单张图可调整尺寸与布局，同时保留共用字体及线宽。
