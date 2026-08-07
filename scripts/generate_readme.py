#!/usr/bin/env python3
"""Generate bilingual, data-backed project READMEs and the activity chart."""

from __future__ import annotations

import html
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "docs" / "data"
CHART = ROOT / "docs" / "images" / "research-activity.svg"
VALUE_LABELS_EN = {
    "immediate": "Immediate",
    "trend": "Trend",
    "long_tail": "Long tail",
    "ignore": "Ignore",
}
VALUE_LABELS_ZH = {
    "immediate": "即时价值",
    "trend": "趋势价值",
    "long_tail": "长尾价值",
    "ignore": "暂时忽略",
}
COLORS = {
    "immediate": "#2563eb",
    "trend": "#7c3aed",
    "long_tail": "#d97706",
    "ignore": "#94a3b8",
}


def load_json(path: Path, default):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def load_history(limit: int = 30) -> list[dict]:
    rows = []
    for path in sorted((ROOT / "papers").glob("*/*-papers.json")):
        payload = load_json(path, {})
        papers = payload.get("papers", [])
        date = payload.get("date") or path.stem.removesuffix("-papers")
        counts = Counter(p.get("value_type", "ignore") for p in papers)
        rows.append({"date": date, "total": len(papers), **counts})
    return rows[-limit:]


def build_svg(history: list[dict]) -> str:
    width, height = 1200, 420
    left, top, chart_width, chart_height = 72, 76, 1060, 242
    max_total = max((row["total"] for row in history), default=1)
    step = chart_width / max(len(history), 1)
    bar_width = max(8, min(26, step * 0.62))
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
        '<title id="title">Frontier Theory Radar research activity</title>',
        '<desc id="desc">Daily papers reviewed and their value classification over the latest thirty runs.</desc>',
        '<rect width="1200" height="420" rx="20" fill="#f8fafc"/>',
        '<text x="56" y="42" font-family="Inter,system-ui,sans-serif" font-size="22" font-weight="700" fill="#0f172a">30-day research activity</text>',
        '<text x="1144" y="42" text-anchor="end" font-family="Inter,system-ui,sans-serif" font-size="14" fill="#64748b">papers reviewed per daily run</text>',
    ]
    for tick in range(5):
        value = round(max_total * tick / 4)
        y = top + chart_height - chart_height * tick / 4
        parts.append(f'<line x1="{left}" y1="{y:.1f}" x2="{left + chart_width}" y2="{y:.1f}" stroke="#e2e8f0"/>')
        parts.append(f'<text x="{left - 12}" y="{y + 5:.1f}" text-anchor="end" font-family="Inter,system-ui,sans-serif" font-size="12" fill="#64748b">{value}</text>')
    for index, row in enumerate(history):
        x = left + step * index + (step - bar_width) / 2
        bottom = top + chart_height
        for key in ("ignore", "long_tail", "trend", "immediate"):
            value = row.get(key, 0)
            segment = chart_height * value / max_total
            bottom -= segment
            parts.append(f'<rect x="{x:.1f}" y="{bottom:.1f}" width="{bar_width:.1f}" height="{segment:.1f}" rx="2" fill="{COLORS[key]}"><title>{html.escape(row["date"])} · {VALUE_LABELS_EN[key]}: {value}</title></rect>')
        if index in {0, len(history) - 1} or index % 5 == 0:
            label = html.escape(row["date"][5:])
            parts.append(f'<text x="{x + bar_width / 2:.1f}" y="{top + chart_height + 24}" text-anchor="middle" font-family="Inter,system-ui,sans-serif" font-size="11" fill="#64748b">{label}</text>')
    legend_x = 72
    for key in ("immediate", "trend", "long_tail", "ignore"):
        parts.append(f'<rect x="{legend_x}" y="367" width="12" height="12" rx="3" fill="{COLORS[key]}"/>')
        parts.append(f'<text x="{legend_x + 20}" y="378" font-family="Inter,system-ui,sans-serif" font-size="13" fill="#334155">{VALUE_LABELS_EN[key]}</text>')
        legend_x += 190
    latest = history[-1] if history else {"date": "n/a", "total": 0}
    parts.append(f'<text x="1144" y="378" text-anchor="end" font-family="Inter,system-ui,sans-serif" font-size="13" font-weight="600" fill="#0f172a">Latest: {html.escape(latest["date"])} · {latest["total"]} papers</text>')
    parts.append("</svg>")
    return "\n".join(parts) + "\n"


def daily_path(date: str) -> str:
    return f"daily/{date[:4]}/{date}.md"


def build_recent_table(reports: list[dict], language: str) -> str:
    header = "| Date | Deep dive | Value | Decision |\n| --- | --- | --- | --- |" if language == "en" else "| 日期 | 深挖论文 | 价值类型 | 判断 |\n| --- | --- | --- | --- |"
    labels = VALUE_LABELS_EN if language == "en" else VALUE_LABELS_ZH
    rows = []
    for report in reports[:7]:
        value = labels.get(report.get("value_type", "ignore"), report.get("value_type_label", ""))
        rows.append(f'| [{report["date"]}]({daily_path(report["date"])}) | {report.get("deep_dive_title", "-")} | {value} | {report.get("decision", "-")} |')
    return header + "\n" + "\n".join(rows)


def build_trend_table(trends: list[dict], language: str) -> str:
    header = "| Direction | Stage | Related papers |\n| --- | --- | ---: |" if language == "en" else "| 方向 | 阶段 | 关联论文 |\n| --- | --- | ---: |"
    rows = []
    for trend in trends[:5]:
        url = f'https://radar.aiutil.com/{trend.get("path", "trends.html")}'
        rows.append(f'| [{trend.get("title", "-")}]({url}) | {trend.get("stage", "-")} | {trend.get("paper_count", 0)} |')
    return header + "\n" + "\n".join(rows)


def generate_readmes() -> None:
    daily_payload = load_json(DATA / "daily-index.json", {"reports": []})
    trend_payload = load_json(DATA / "trend-index.json", {"trends": []})
    latest_payload = load_json(DATA / "latest.json", {})
    reports = daily_payload.get("reports", [])
    trends = trend_payload.get("trends", [])
    history = load_history()
    latest = reports[0] if reports else {}
    current = history[-1] if history else {"date": "n/a", "total": 0}
    distribution = latest_payload.get("value_distribution", {})
    for key in VALUE_LABELS_EN:
        distribution.setdefault(key, current.get(key, 0))

    CHART.parent.mkdir(parents=True, exist_ok=True)
    CHART.write_text(build_svg(history), encoding="utf-8")

    en = f'''# Frontier Theory Radar

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

## Latest research run · {latest.get('date', current.get('date', 'n/a'))}

| Papers reviewed | Immediate | Trend | Long tail | Deferred |
| ---: | ---: | ---: | ---: | ---: |
| {current.get('total', 0)} | {distribution['immediate']} | {distribution['trend']} | {distribution['long_tail']} | {distribution['ignore']} |

**Deep dive:** [{latest.get('deep_dive_title', 'No report yet')}]({daily_path(latest.get('date', current.get('date', ''))) if latest else '#'}) · {VALUE_LABELS_EN.get(latest.get('value_type', 'ignore'), 'Unclassified')} · {latest.get('decision', '-')}

![Thirty-day research activity](docs/images/research-activity.svg)

## Recent reports

{build_recent_table(reports, 'en')}

## Directions under active observation

{build_trend_table(trends, 'en')}

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
'''

    zh = f'''# 前沿理论驱动技术雷达

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

## 最新研究 · {latest.get('date', current.get('date', '暂无'))}

| 审阅论文 | 即时价值 | 趋势价值 | 长尾价值 | 暂时忽略 |
| ---: | ---: | ---: | ---: | ---: |
| {current.get('total', 0)} | {distribution['immediate']} | {distribution['trend']} | {distribution['long_tail']} | {distribution['ignore']} |

**今日深挖：** [{latest.get('deep_dive_title', '暂无日报')}]({daily_path(latest.get('date', current.get('date', ''))) if latest else '#'}) · {VALUE_LABELS_ZH.get(latest.get('value_type', 'ignore'), '未分类')} · {latest.get('decision', '-')}

**核心判断：** {latest.get('one_line_judgement', '暂无。')}

**建议动作：** {latest.get('daily_action', '暂无。')}

![最近三十次研究活动](docs/images/research-activity.svg)

## 最近 7 期日报

{build_recent_table(reports, 'zh')}

## 当前重点趋势

{build_trend_table(trends, 'zh')}

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
'''

    (ROOT / "README.md").write_text(en, encoding="utf-8")
    (ROOT / "README.zh-CN.md").write_text(zh, encoding="utf-8")
    print(f"[readme] generated bilingual READMEs and {CHART.relative_to(ROOT)}")


if __name__ == "__main__":
    generate_readmes()
