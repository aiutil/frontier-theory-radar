# 前沿理论驱动技术雷达

<h3 align="center">用可追溯证据判断：哪些前沿 AI 论文现在值得行动、哪些值得观察、哪些应当暂缓。</h3>

<p align="center">
  每日完成论文采集、价值路由、深度判断与趋势沉淀，区分即时价值、趋势价值、长尾价值与噪声。
</p>

<p align="center">
  <a href="README.md">English</a> ·
  <a href="https://radar.aiutil.com">在线雷达</a> ·
  <a href="https://radar.aiutil.com/daily.html">日报</a> ·
  <a href="https://radar.aiutil.com/about.html">研究方法</a>
</p>

<p align="center">
  <a href="https://github.com/aiutil/frontier-theory-radar/actions/workflows/ci.yml"><img alt="研究流水线" src="https://img.shields.io/github/actions/workflow/status/aiutil/frontier-theory-radar/ci.yml?branch=main&style=flat-square&label=research%20pipeline"></a>
  <a href="LICENSE"><img alt="Apache-2.0 许可证" src="https://img.shields.io/badge/license-Apache--2.0-2563eb?style=flat-square"></a>
  <img alt="每日研究" src="https://img.shields.io/badge/cadence-daily-0f766e?style=flat-square">
</p>

![前沿理论雷达真实研究工作台](docs/images/readme-overview.png)

## 最新研究 · 2026-08-25

| 审阅论文 | 即时价值 | 趋势价值 | 长尾价值 | 暂时忽略 |
| ---: | ---: | ---: | ---: | ---: |
| 10 | 92 | 128 | 115 | 1275 |

**今日深挖：** [Natural-Language Workflows Are Not Software Yet: Artifact-Driven Compilation for Reliable Agent Execution](daily/2026/2026-08-25.md) · 即时价值 · 轻量试点

**核心判断：** Artic 把自然语言工作流转成 artifact 形式，强迫把隐式数据依赖外化为可被求解的输入——这是当前 agent 工作流易碎（长程/分支下 context 压力失效）的关键工程缺口，可直接对接到 LangGraph/DSPy/Temporal 这类编排器的'workflow-as-input'思路。AI with Authority 论证机器验证是规模化调度自主机器工作的前提——'不可腐化裁判'作为一项基础设施命题，足以催生一整个工程方向：verification-first agent runtimes、evaluator harness 与 runtime rollback。Asymmetric Capacity Allocation 则用 self-refinement 三阶段容量异构的实验探索，支撑'mixed-size pipeline 是 LLM 工程的成本金矿'这一更普遍趋势。三者共同折射：agent 价值密度正在从模型能力转向'基础设施（编译、验证、容量编排）'。

**建议动作：** 完成三件事：(1) Artic 落地：选一条高频长程工作流，把自然语言步骤描述 schema-化为 typed intermediate representation，跑样本验证对'隐式数据依赖漏判'的修复比例。(2) Verification-first 盘点：写出团队当前 agent runtime 已有/可补的 verifier 锚点清单（spec check / output schema validation / tool-call replay audit / deterministic replay 各一项）。(3) Asymmetric capacity 实验：固定生成侧强模型，在 critique 与 revision 阶段试 30%/10% 成本模型替代，绘制 cost-quality Pareto 曲线。

![最近三十次研究活动](docs/images/research-activity.svg)

## 最近 7 期日报

| 日期 | 深挖论文 | 价值类型 | 判断 |
| --- | --- | --- | --- |
| [2026-08-25](daily/2026/2026-08-25.md) | Natural-Language Workflows Are Not Software Yet: Artifact-Driven Compilation for Reliable Agent Execution | 即时价值 | 轻量试点 |
| [2026-08-24](daily/2026/2026-08-24.md) | AI4AI-Bench: Benchmarking LLM Agents in Algorithmic Design for Recursive Self-Improvement | 即时价值 | 轻量试点 |
| [2026-08-23](daily/2026/2026-08-23.md) | AI4AI-Bench: Benchmarking LLM Agents in Algorithmic Design for Recursive Self-Improvement | 即时价值 | 轻量试点 |
| [2026-08-21](daily/2026/2026-08-21.md) | AI4AI-Bench: Benchmarking LLM Agents in Algorithmic Design for Recursive Self-Improvement | 即时价值 | 轻量试点 |
| [2026-08-20](daily/2026/2026-08-20.md) | Projecting BrowseComp-Plus onto ClimbMix: Toward More Realistic Corpora for Agentic Search | 暂时忽略 | 暂时忽略 |
| [2026-08-19](daily/2026/2026-08-19.md) | Accelerated Genetic Programming Hyper-Heuristics for Simulation-Based Scheduling via Agentic AI | 长尾价值 | 持续观察 |
| [2026-08-18](daily/2026/2026-08-18.md) | ComponentBench: Diagnosing Component-Level Failures in Computer-Use Agents | 暂时忽略 | 暂时忽略 |

## 当前重点趋势

| 方向 | 阶段 | 关联论文 |
| --- | --- | ---: |
| [Agentic World Modeling](https://radar.aiutil.com/trend-detail.html?id=agentic-world-modeling) | 上升 | 534 |
| [Coding Agent](https://radar.aiutil.com/trend-detail.html?id=coding-agent) | 主流化 | 433 |
| [Context Engineering](https://radar.aiutil.com/trend-detail.html?id=context-engineering) | 上升 | 534 |

## 为什么做这个项目

论文聚合站通常优化“新”和“热”，本项目优化“判断”：哪些值得今天试验，哪些需要连续观察，哪些虽然不热但应该保留，哪些证据不足应明确暂缓。每个结论都保留来源，并写清当前最大不确定性。

## 研究工作流

```mermaid
flowchart LR
  A["采集论文"] --> B["评估相关性与证据"]
  B --> C["价值路由"]
  C --> D["今日深挖"]
  C --> E["趋势观察"]
  C --> F["长尾保存"]
  D --> G["行动与可复用资产"]
```

- `papers/`：按日期保存来源快照和评分候选。
- `daily/`：保存每次研究运行的人类可读判断记录。
- `trends/`、`insights/`：沉淀跨日趋势与可复用发现。
- `docs/data/`：在线站点使用的结构化公开投影。
- `scripts/generate_readme.py`：从已提交证据生成双语 README 和活动图表。

## 证据边界

评分与结论属于研究判断，不等于独立复现。论文摘要、作者自述 Benchmark、开源实现与第三方复现是不同证据等级。代码缺失、摘要截断或 Benchmark 未核验时，会明确标注，不把推断包装成事实。

## 本地运行与验证

```bash
./run_daily.sh 2026-08-07
python3 -m pytest tests
python3 scripts/generate_readme.py
```

生产定时任务运行在 AIUtil 私有自动化环境中，凭据和私有运行记忆不进入本仓库。生成后的 Markdown、SVG、JSON 和来源链接均可通过 Git 历史审阅。

## 安全

请勿提交数据源凭据、API Token、私有论文集合或运营记忆。安全问题请通过 [GitHub Security Advisories](https://github.com/aiutil/frontier-theory-radar/security/advisories/new) 私下报告。

## 开源协议

Apache License 2.0，详见 [NOTICE](NOTICE)。
