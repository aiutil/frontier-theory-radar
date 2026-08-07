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

## 最新研究 · 2026-08-08

| 审阅论文 | 即时价值 | 趋势价值 | 长尾价值 | 暂时忽略 |
| ---: | ---: | ---: | ---: | ---: |
| 10 | 83 | 111 | 102 | 924 |

**今日深挖：** [The Bitter Lesson of Tool Calling](daily/2026/2026-08-08.md) · 即时价值 · 轻量试点

**核心判断：** The Bitter Lesson of Tool Calling 系统性跨代际实证对比程序化工具调用（PTC，写脚本链式/并行调工具）与原生 JSON 工具调用，在真实世界任务条件下——它直接回答'该让 agent 写脚本调工具还是逐个 JSON 调工具'这个工程选型问题，标题致敬 Rich Sutton 的 Bitter Lesson 暗示可能有反直觉发现。AV-AIVAT 用 anytime-valid stopping 让 agent 对战评估在证据充足时立即停止，声称比基线便宜 74x 且置信水平有效——它解决'该打多少局才能可信判断 agent 强弱'这个 agent A/B 评估的高频痛点。

**建议动作：** 完成三件事：把 The Bitter Lesson of Tool Calling 的 PTC vs JSON 跨代际实证结论纳入团队 tool-use agent 选型参考文档；评估 AV-AIVAT 的 anytime-valid stopping 能否引入团队 agent A/B 评估流程降低评估推理成本（若开源则在一个内部 agent 对比任务上试跑）；为 MIST（选择性信任评测）、CalibForge（对抗性 solver 校准合成 agent 任务）、Resourced Authority（计算预算自执行 agent 治理）建立趋势观察卡片。

![最近三十次研究活动](docs/images/research-activity.svg)

## 最近 7 期日报

| 日期 | 深挖论文 | 价值类型 | 判断 |
| --- | --- | --- | --- |
| [2026-08-08](daily/2026/2026-08-08.md) | The Bitter Lesson of Tool Calling | 即时价值 | 轻量试点 |
| [2026-08-07](daily/2026/2026-08-07.md) | Argus: A General-Purpose Agentic Runtime for Long-Horizon Reasoning | 即时价值 | 重点学习 |
| [2026-08-06](daily/2026/2026-08-06.md) | When Attention Goes Blind: Numerical Failure in ALiBi Positional Encodings | 即时价值 | 重点学习 |
| [2026-08-05](daily/2026/2026-08-05.md) | UEmbed: Unified Sparse and Dense Multimodal Embeddings | 即时价值 | 重点学习 |
| [2026-08-04](daily/2026/2026-08-04.md) | TokTier: Exact Stateful Tokenization for Agentic LLM Serving | 即时价值 | 重点学习 |
| [2026-08-03](daily/2026/2026-08-03.md) | Change2Task: From Repository Changes to Executable Coding Agent Tasks and Environments | 即时价值 | 重点学习 |
| [2026-08-02](daily/2026/2026-08-02.md) | Change2Task: From Repository Changes to Executable Coding Agent Tasks and Environments | 即时价值 | 重点学习 |

## 当前重点趋势

| 方向 | 阶段 | 关联论文 |
| --- | --- | ---: |
| [Agentic World Modeling](https://radar.aiutil.com/trend-detail.html?id=agentic-world-modeling) | 上升 | 416 |
| [Coding Agent](https://radar.aiutil.com/trend-detail.html?id=coding-agent) | 主流化 | 343 |
| [Context Engineering](https://radar.aiutil.com/trend-detail.html?id=context-engineering) | 上升 | 416 |

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
