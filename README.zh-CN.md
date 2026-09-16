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

## 最新研究 · 2026-09-17

| 审阅论文 | 即时价值 | 趋势价值 | 长尾价值 | 暂时忽略 |
| ---: | ---: | ---: | ---: | ---: |
| 10 | 108 | 177 | 167 | 1318 |

**今日深挖：** [ZGCM-1: A Fully Open and Extremely Efficient Foundation Model for Math and Agentic Search](daily/2026/2026-09-17.md) · 趋势价值 · 重点学习

**核心判断：** 据摘要（arXiv 2609.13356），ZGCM-1 是完全开源的 7B 密集基础模型，主打 math + agentic search，256K 上下文，并把架构与系统协同设计（Architecture & System Co-design）作为训练配方的核心。其核心命题是'紧凑模型无法被动记忆开放网络，但能通过内部思考 + 主动外部工具调用突破参数容量上限'——这是 ai-agent × context-engineering 的直接路线。属于当日最高势能的'agent 工程 + 长上下文 + 开源 7B'趋势资产，与 aiutil 长期关注路线共振。

**建议动作：** 跟踪 ZGCM-1（[2609.13356](https://arxiv.org/abs/2609.13356)）完整 PDF 与 7B 权重 / 训练配方 / math / agentic 评测脚本是否开源；同步把 OrchSLM（[2609.13470](https://arxiv.org/abs/2609.13470)）、Root-Cause Attribution as Search（[2609.13463](https://arxiv.org/abs/2609.13463)）、Generalized Agent Iteration（[2609.13406](https://arxiv.org/abs/2609.13406)）纳入趋势观察；为 LabAgent / TimeThink / Vibe Patenting / Self-Adaptive Physical AI / MOBO / Governing at Machine Speed 建立长尾卡片。

![最近三十次研究活动](docs/images/research-activity.svg)

## 最近 7 期日报

| 日期 | 深挖论文 | 价值类型 | 判断 |
| --- | --- | --- | --- |
| [2026-09-17](daily/2026/2026-09-17.md) | ZGCM-1: A Fully Open and Extremely Efficient Foundation Model for Math and Agentic Search | 趋势价值 | 重点学习 |
| [2026-09-16](daily/2026/2026-09-16.md) | Corrupt Plans, Clean Traces: Evading Chain-of-Thought Monitoring with Plan Injection | 趋势价值 | 重点学习 |
| [2026-09-15](daily/2026/2026-09-15.md) | Embodied-BenchForge: A Closed-Loop Agentic Workflow for Embodied Benchmark Construction | 趋势价值 | 轻量试点 |
| [2026-09-14](daily/2026/2026-09-14.md) | [占位] 今日论文抓取失败或无新论文 | 暂时忽略 | 暂时忽略 |
| [2026-09-13](daily/2026/2026-09-13.md) | Data Scarcity and Model Sparsity: Mixtures-of-Experts Overfit More to Repeated Data | 趋势价值 | 轻量试点 |
| [2026-09-12](daily/2026/2026-09-12.md) | Data Scarcity and Model Sparsity: Mixtures-of-Experts Overfit More to Repeated Data | 趋势价值 | 轻量试点 |
| [2026-09-11](daily/2026/2026-09-11.md) | IBIB: A Protocol for Measuring Enterprise AI Systems by Serving Route, Not Model Identifier | 趋势价值 | 轻量试点 |

## 当前重点趋势

| 方向 | 阶段 | 关联论文 |
| --- | --- | ---: |
| [Agentic World Modeling](https://radar.aiutil.com/trend-detail.html?id=agentic-world-modeling) | 上升 | 566 |
| [Coding Agent](https://radar.aiutil.com/trend-detail.html?id=coding-agent) | 主流化 | 494 |
| [Context Engineering](https://radar.aiutil.com/trend-detail.html?id=context-engineering) | 上升 | 566 |

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
