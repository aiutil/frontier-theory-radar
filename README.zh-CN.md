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

## 最新研究 · 2026-10-19

| 审阅论文 | 即时价值 | 趋势价值 | 长尾价值 | 暂时忽略 |
| ---: | ---: | ---: | ---: | ---: |
| 10 | 142 | 233 | 239 | 1356 |

**今日深挖：** [MLExpert: Towards a Generalist Agentic Model for Autonomous Machine Learning Engineering](daily/2026/2026-10-19.md) · 即时价值 · 重点学习

**核心判断：** 据摘要（arXiv 2610.22344），这篇把 MLE 从 'workflow 编排' 推到 'model-directed interaction, allowing models to autonomously organize and evolve their own ML engineering process'——即让单个 LLM 自主决定 dataset / feature / pipeline / training config / 训练超参与迭代路径。这是 ai-agent × coding-agent × llm-evaluation 的 'agent4AI / recursive self-improvement' 直接路线资产；与 9 月-10 月 KARO / AIDE / MLAgentBench 主线同源但定位更激进（'generalist agentic'），意味着团队日后做 AutoML / AutoMLOps 不再是写 workflow，而是构造 agent harness + rubric。

**建议动作：** 把 MLExpert（[2610.22344](http://arxiv.org/abs/2610.22344)）继续列为即时试点方向；为 FDE-Gym（[2610.22350](http://arxiv.org/abs/2610.22350)）建立即时试点卡片（与 MLExpert 一起构成 'MLE / delivery' 即时双线）；为 T2-Z（[2610.22364](http://arxiv.org/abs/2610.22364)）、CoDA（[2610.22362](http://arxiv.org/abs/2610.22362)）、OmniVerifier-C1（[2610.22355](http://arxiv.org/abs/2610.22355)）建立/更新趋势卡片（world-model / data-policy co-evolution / graded verifier 主线加固）；为 LIBERO-PeRM（[2610.22372](http://arxiv.org/abs/2610.22372)）、PathFM（[2610.22358](http://arxiv.org/abs/2610.22358)）、GeoState（[2610.22343](http://arxiv.org/abs/2610.22343)）、Rethinking Routing in MoE（[2610.22353](http://arxiv.org/abs/2610.22353)）、量子电路 LLM（[2610.22367](http://arxiv.org/abs/2610.22367)）保持/新增长尾卡片。

![最近三十次研究活动](docs/images/research-activity.svg)

## 最近 7 期日报

| 日期 | 深挖论文 | 价值类型 | 判断 |
| --- | --- | --- | --- |
| [2026-10-19](daily/2026/2026-10-19.md) | MLExpert: Towards a Generalist Agentic Model for Autonomous Machine Learning Engineering | 即时价值 | 重点学习 |
| [2026-10-18](daily/2026/2026-10-18.md) | MLExpert: Towards a Generalist Agentic Model for Autonomous Machine Learning Engineering | 即时价值 | 轻量试点 |
| [2026-10-17](daily/2026/2026-10-17.md) | The World Won't Wait: Evaluating and Teaching Agents Under a Live Clock | 即时价值 | 轻量试点 |
| [2026-10-16](daily/2026/2026-10-16.md) | Co-Evolving Acting and Forecasting for Language Agents | 即时价值 | 轻量试点 |
| [2026-10-15](daily/2026/2026-10-15.md) | Hybrid Reasoning Agents | 即时价值 | 轻量试点 |
| [2026-10-14](daily/2026/2026-10-14.md) | RSI-Anything: Unlocking Recursive Self-Improvement with World Models | 即时价值 | 轻量试点 |
| [2026-10-13](daily/2026/2026-10-13.md) | RSI-Anything: Unlocking Recursive Self-Improvement with World Models | 即时价值 | 轻量试点 |

## 当前重点趋势

| 方向 | 阶段 | 关联论文 |
| --- | --- | ---: |
| [Agentic World Modeling](https://radar.aiutil.com/trend-detail.html?id=agentic-world-modeling) | 上升 | 608 |
| [Coding Agent](https://radar.aiutil.com/trend-detail.html?id=coding-agent) | 主流化 | 609 |
| [Context Engineering](https://radar.aiutil.com/trend-detail.html?id=context-engineering) | 上升 | 608 |

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
