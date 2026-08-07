# Frontier Theory Radar

<h3 align="center">Evidence-first decisions on which frontier AI papers matter now, later, or not yet.</h3>

<p align="center">
  A daily research system that separates immediate engineering value, emerging trends, durable long-tail ideas, and noise.
</p>

<p align="center">
  <a href="README.zh-CN.md">简体中文</a> ·
  <a href="https://radar.aiutil.com">Live radar</a> ·
  <a href="https://radar.aiutil.com/daily.html">Daily reports</a> ·
  <a href="https://radar.aiutil.com/about.html">Methodology</a>
</p>

<p align="center">
  <a href="https://github.com/aiutil/frontier-theory-radar/actions/workflows/ci.yml"><img alt="CI" src="https://img.shields.io/github/actions/workflow/status/aiutil/frontier-theory-radar/ci.yml?branch=main&style=flat-square&label=research%20pipeline"></a>
  <a href="LICENSE"><img alt="Apache-2.0 license" src="https://img.shields.io/badge/license-Apache--2.0-2563eb?style=flat-square"></a>
  <img alt="Daily research" src="https://img.shields.io/badge/cadence-daily-0f766e?style=flat-square">
</p>

![Frontier Theory Radar live research workspace](docs/images/readme-overview.png)

## Latest research run · 2026-08-07

| Papers reviewed | Immediate | Trend | Long tail | Deferred |
| ---: | ---: | ---: | ---: | ---: |
| 10 | 81 | 108 | 99 | 922 |

**Deep dive:** [Argus: A General-Purpose Agentic Runtime for Long-Horizon Reasoning](daily/2026/2026-08-07.md) · Immediate · 重点学习

![Thirty-day research activity](docs/images/research-activity.svg)

## Recent reports

| Date | Deep dive | Value | Decision |
| --- | --- | --- | --- |
| [2026-08-07](daily/2026/2026-08-07.md) | Argus: A General-Purpose Agentic Runtime for Long-Horizon Reasoning | Immediate | 重点学习 |
| [2026-08-06](daily/2026/2026-08-06.md) | When Attention Goes Blind: Numerical Failure in ALiBi Positional Encodings | Immediate | 重点学习 |
| [2026-08-05](daily/2026/2026-08-05.md) | UEmbed: Unified Sparse and Dense Multimodal Embeddings | Immediate | 重点学习 |
| [2026-08-04](daily/2026/2026-08-04.md) | TokTier: Exact Stateful Tokenization for Agentic LLM Serving | Immediate | 重点学习 |
| [2026-08-03](daily/2026/2026-08-03.md) | Change2Task: From Repository Changes to Executable Coding Agent Tasks and Environments | Immediate | 重点学习 |
| [2026-08-02](daily/2026/2026-08-02.md) | Change2Task: From Repository Changes to Executable Coding Agent Tasks and Environments | Immediate | 重点学习 |
| [2026-08-01](daily/2026/2026-08-01.md) | Change2Task: From Repository Changes to Executable Coding Agent Tasks and Environments | Immediate | 重点学习 |

## Directions under active observation

| Direction | Stage | Related papers |
| --- | --- | ---: |
| [Agentic World Modeling](https://radar.aiutil.com/trend-detail.html?id=agentic-world-modeling) | 上升 | 413 |
| [Coding Agent](https://radar.aiutil.com/trend-detail.html?id=coding-agent) | 主流化 | 337 |
| [Context Engineering](https://radar.aiutil.com/trend-detail.html?id=context-engineering) | 上升 | 413 |

## Why this repository exists

Paper feeds optimize for recency and popularity. Frontier Theory Radar optimizes for decisions: what deserves an experiment today, what needs repeated observation, what should be preserved for later, and what does not yet justify attention. Each conclusion keeps its source link and states the largest remaining uncertainty.

## Research workflow

```mermaid
flowchart LR
  A["Collect papers"] --> B["Score relevance and evidence"]
  B --> C["Route by value"]
  C --> D["Deep dive"]
  C --> E["Trend watch"]
  C --> F["Long-tail archive"]
  D --> G["Action and reusable asset"]
```

- `papers/` stores dated source snapshots and scored candidates.
- `daily/` stores the human-readable decision record for each run.
- `trends/` and `insights/` retain multi-day directions and reusable findings.
- `docs/data/` is the structured public projection used by the live site.
- `scripts/generate_readme.py` rebuilds both READMEs and the activity chart from committed evidence.

## Evidence boundaries

Scores and decisions are research judgments, not claims of independent reproduction. A paper abstract, author-reported benchmark, open-source implementation, and independently reproduced result are treated as different evidence levels. Missing code, truncated abstracts, or unverified benchmarks are called out rather than silently upgraded into facts.

## Run and verify

```bash
./run_daily.sh 2026-08-07
python3 -m pytest tests
python3 scripts/generate_readme.py
```

The scheduled production job runs in the private AIUtil automation environment. Credentials and private runtime memory are not stored here. The generated Markdown, SVG, JSON, and source-linked reports remain reviewable in Git history.

## Security

Do not commit feed credentials, API tokens, private paper collections, or operator memory. Report a vulnerability privately through [GitHub Security Advisories](https://github.com/aiutil/frontier-theory-radar/security/advisories/new).

## License

Apache License 2.0. See [NOTICE](NOTICE).
