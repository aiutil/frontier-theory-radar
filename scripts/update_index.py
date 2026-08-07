#!/usr/bin/env python3
"""论文价值发现系统 - 索引更新脚本"""
import glob
import json
import os
import re
import sys
from datetime import datetime, timedelta
from pathlib import Path

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DAILY_DIR = os.path.join(PROJECT_ROOT, 'daily')
PAPERS_DIR = os.path.join(PROJECT_ROOT, 'papers')
TRENDS_DIR = os.path.join(PROJECT_ROOT, 'trends')
INSIGHTS_DIR = os.path.join(PROJECT_ROOT, 'insights')
DOCS_DATA_DIR = os.path.join(PROJECT_ROOT, 'docs', 'data')

VALUE_LABELS = {'immediate':'即时价值','trend':'趋势价值','long_tail':'长尾价值','ignore':'暂时忽略'}
TREND_STAGE_LABELS = {'emerging':'萌芽','rising':'上升','mainstream':'主流化','overheated':'过热','noise':'噪声','long_tail_watch':'长尾观察'}
TOPIC_LABELS = {
    'ai-agent':'AI Agent', 'coding-agent':'Coding Agent', 'context-engineering':'Context Engineering',
    'rag-knowledge':'RAG / 知识系统', 'multimodal-agent':'Multimodal Agent', 'llm-evaluation':'LLM 评测',
    'inference-serving':'推理与服务', 'ai-k8s-platform':'AI 平台工程', 'data-engineering':'数据工程', 'security-governance':'安全与治理'
}


def save_json(filename, data):
    Path(DOCS_DATA_DIR).mkdir(parents=True, exist_ok=True)
    path = Path(DOCS_DATA_DIR) / filename
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'[index] 已更新: {path}')


def parse_front_matter(text):
    if not text.startswith('---\n'):
        return {}, text
    end = text.find('\n---\n', 4)
    if end == -1:
        return {}, text
    meta = {}
    for raw in text[4:end].splitlines():
        raw = raw.strip()
        if not raw or raw.startswith('#') or ':' not in raw:
            continue
        k, v = raw.split(':', 1)
        v = v.strip().strip('"').strip("'")
        if v.startswith('[') and v.endswith(']'):
            meta[k.strip()] = [x.strip().strip('"').strip("'") for x in v[1:-1].split(',') if x.strip()]
        else:
            meta[k.strip()] = v
    return meta, text[end+5:]


def slugify(text):
    text = text.lower().strip()
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return re.sub(r'-+', '-', text).strip('-') or 'paper'


def make_cn_brief(paper):
    topic = (paper.get('matched_topics') or ['未分类'])[0]
    topic_cn = TOPIC_LABELS.get(topic, '前沿论文')
    abstract = ' '.join((paper.get('abstract') or '').split())
    if abstract:
        return f"{topic_cn}：{abstract[:78]}{'…' if len(abstract) > 78 else ''}"
    return f"{topic_cn}：当前需要更多上下文来做价值判断。"


def one_line_judgement(paper):
    vt = paper.get('value_type', 'ignore')
    reason = paper.get('llm_reason') or make_cn_brief(paper)
    prefix = {'immediate':'今天值得试', 'trend':'值得继续观察', 'long_tail':'值得先保存', 'ignore':'当前可忽略'}.get(vt, '待判断')
    return f"{prefix}：{reason[:70]}{'…' if len(reason) > 70 else ''}"


def action_text(value_type):
    return {
        'immediate':'今天先做摘要精读 + 最小实验设计。',
        'trend':'纳入趋势雷达，连续观察 7-30 天。',
        'long_tail':'加入长尾库，标注触发条件，先不重投入。',
        'ignore':'仅保留最小索引，不继续深挖。'
    }.get(value_type, '待分析')


def future_trigger(paper):
    if paper.get('value_type') == 'long_tail':
        return '出现开源实现 / 被高质量论文引用 / 进入 benchmark / 与当前系统问题交集增强'
    if paper.get('value_type') == 'trend':
        return '出现多篇跟进论文、开源项目和工程博客共振'
    return '待更多证据'


def read_daily_reports(max_count=30):
    reports = []
    for filepath in sorted(glob.glob(os.path.join(DAILY_DIR, '*', '*.md')), reverse=True)[:max_count]:
        date_str = Path(filepath).stem
        raw = Path(filepath).read_text(encoding='utf-8')
        meta, body = parse_front_matter(raw)
        reports.append({
            'date': date_str,
            'title': meta.get('title') or f'论文价值发现日报 - {date_str}',
            'deep_dive_title': meta.get('deep_dive_title', '待分析'),
            'deep_dive_url': meta.get('deep_dive_url', ''),
            'decision': meta.get('decision', '待定'),
            'value_type': meta.get('value_type', 'ignore'),
            'value_type_label': VALUE_LABELS.get(meta.get('value_type', 'ignore'), '待定'),
            'daily_action': meta.get('daily_action', action_text(meta.get('value_type', 'ignore'))),
            'max_uncertainty': meta.get('max_uncertainty', '待分析'),
            'one_line_judgement': next((ln.split('**为什么值得看：**',1)[1].strip() for ln in body.splitlines() if '**为什么值得看：**' in ln), '待补充价值判断'),
            'path': f'daily-detail.html?date={date_str}'
        })
    return reports


def map_related_trends(topics):
    mapping = {
        'ai-agent': 'agentic-world-modeling',
        'multimodal-agent': 'agentic-world-modeling',
        'context-engineering': 'context-engineering',
        'rag-knowledge': 'context-engineering',
        'coding-agent': 'coding-agent',
        'llm-evaluation': 'coding-agent'
    }
    ordered = []
    for topic in topics or []:
        slug = mapping.get(topic)
        if slug and slug not in ordered:
            ordered.append(slug)
    return ordered


def load_all_papers():
    papers = []
    seen = set()
    for filepath in sorted(glob.glob(os.path.join(PAPERS_DIR, '*', '*-papers.json')), reverse=True):
        data = json.loads(Path(filepath).read_text(encoding='utf-8'))
        date_str = data.get('date') or Path(filepath).name.split('-papers.json')[0]
        top_score = data.get('papers', [{}])[0].get('score', -1)
        for p in data.get('papers', []):
            pid = p.get('id') or slugify(p.get('title',''))
            if pid in seen:
                continue
            seen.add(pid)
            enriched = dict(p)
            enriched['id'] = pid
            enriched['brief_cn'] = make_cn_brief(enriched)
            enriched['one_line_judgement'] = one_line_judgement(enriched)
            enriched['first_seen_date'] = date_str
            enriched['first_deep_dive_daily'] = date_str if p.get('score', 0) == top_score else date_str
            enriched['value_type_label'] = VALUE_LABELS.get(enriched.get('value_type','ignore'),'待定')
            enriched['trend_stage_label'] = TREND_STAGE_LABELS.get(enriched.get('trend_status','noise'), '待定')
            enriched['future_trigger'] = future_trigger(enriched)
            enriched['long_tail_summary'] = (p.get('llm_reason') or enriched['brief_cn'])[:96]
            enriched['related_trends'] = map_related_trends(enriched.get('matched_topics', []))
            enriched['detail_path'] = f"paper-detail.html?id={pid}"
            papers.append(enriched)
    if 'agentic-world-modeling' not in seen:
        papers.append({
            'id': 'agentic-world-modeling',
            'title': 'Agentic World Modeling: Foundations, Capabilities, Laws, and Beyond',
            'authors': ['待核验'],
            'source': 'arXiv',
            'published': '2026-04-28',
            'url': 'https://arxiv.org/abs/2604.22748',
            'pdf_url': 'https://arxiv.org/pdf/2604.22748',
            'openreview_url': '',
            'paperswithcode_url': '',
            'code_url': '',
            'benchmark_url': '',
            'project_url': '',
            'abstract': '从世界状态建模、执行前预测、失败修正和行动规划视角梳理 Agentic World Modeling 的基础、能力边界与未来方向。',
            'categories': ['cs.AI'],
            'keywords': ['agentic world modeling', 'world model', 'ai agent'],
            'score': 86,
            'decision': '重点学习',
            'value_type': 'trend',
            'matched_topics': ['ai-agent', 'multimodal-agent'],
            'score_breakdown': {'novelty': 8.2, 'relevance': 8.5, 'evidence_strength': 6.4, 'engineering_testability': 5.8, 'trend_signal': 8.7, 'long_tail_potential': 8.0, 'actionability': 6.6, 'noise_risk': 2.5},
            'trend_status': 'rising',
            'brief_cn': 'AI Agent：把执行前预测、状态模拟与失败修正纳入 Agent 世界模型框架，适合纳入趋势观察。',
            'one_line_judgement': '值得继续观察：它可能把 Agent 从“会调用工具”推进到“会预测后果与修正执行”。',
            'first_seen_date': '2026-04-28',
            'first_deep_dive_daily': '2026-04-28',
            'value_type_label': '趋势价值',
            'trend_stage_label': '上升',
            'future_trigger': '出现开源实现 / benchmark / 多篇跟进论文 / 工程博客共振',
            'long_tail_summary': '值得作为趋势锚点长期保存，尤其适用于 Agent 规划、状态建模与执行修正研究。',
            'related_trends': ['agentic-world-modeling'],
            'detail_path': 'paper-detail.html?id=agentic-world-modeling',
            'links': [{'label': 'arXiv', 'url': 'https://arxiv.org/abs/2604.22748'}, {'label': 'PDF', 'url': 'https://arxiv.org/pdf/2604.22748'}]
        })
    return papers


def load_trends(papers):
    trend_counts = {}
    for p in papers:
        for t in p.get('related_trends', []):
            trend_counts[t] = trend_counts.get(t, 0) + 1
    trends = []
    for filepath in sorted(glob.glob(os.path.join(TRENDS_DIR, '*.md'))):
        if Path(filepath).name == 'index.md':
            continue
        raw = Path(filepath).read_text(encoding='utf-8')
        meta, body = parse_front_matter(raw)
        slug = Path(filepath).stem
        title = meta.get('title') or next((ln[2:].strip() for ln in body.splitlines() if ln.startswith('# ')), slug)
        stage = meta.get('stage', '上升')
        linked_topics = meta.get('priority_topics', []) if isinstance(meta.get('priority_topics'), list) else []
        count = sum(trend_counts.get(t, 0) for t in linked_topics) or trend_counts.get(slug, 0)
        trends.append({
            'title': title,
            'slug': slug,
            'stage': stage,
            'path': f'trend-detail.html?id={slug}',
            'markdown_path': f'trends/{slug}.md',
            'paper_count': count,
            'practice_count': 0,
            'updated_at': meta.get('updated_at') or datetime.now().date().isoformat(),
            'key_insight': next((ln[2:].strip() for ln in body.splitlines() if ln.startswith('- ')), '从多篇论文中寻找持续信号。')
        })
    return trends


def load_insights():
    items = []
    for filepath in sorted(glob.glob(os.path.join(INSIGHTS_DIR, '*.md'))):
        if Path(filepath).name == 'index.md':
            continue
        text = Path(filepath).read_text(encoding='utf-8')
        title = next((ln[2:].strip() for ln in text.splitlines() if ln.startswith('# ')), Path(filepath).stem)
        items.append({'title': title, 'slug': Path(filepath).stem, 'path': f'insights/{Path(filepath).name}', 'source_paper_ids': [], 'source_daily_dates': []})
    return items


def source_index():
    return {
        'updated_at': datetime.now().isoformat(),
        'theory_sources': [
            {'name':'arXiv','purpose':'理论源头主源','is_primary':True,'is_engineering_source':False,'frequency':'daily','status':'已接入','url':'https://arxiv.org'},
            {'name':'OpenReview','purpose':'会议论文与审稿信号','is_primary':True,'is_engineering_source':False,'frequency':'daily','status':'待接入','url':'https://openreview.net'},
            {'name':'Hugging Face Daily Papers','purpose':'社区关注度辅助排序','is_primary':False,'is_engineering_source':False,'frequency':'daily','status':'待接入','url':'https://huggingface.co/papers'},
            {'name':'Papers with Code','purpose':'代码 / Benchmark 证据','is_primary':False,'is_engineering_source':True,'frequency':'daily','status':'待接入','url':'https://paperswithcode.com'}
        ],
        'engineering_sources': [
            {'name':'GitHub Search','purpose':'工程实践验证','is_primary':False,'is_engineering_source':True,'frequency':'daily','status':'待接入','url':'https://github.com/search'},
            {'name':'GitHub Trending','purpose':'热度辅助与工程线索','is_primary':False,'is_engineering_source':True,'frequency':'daily','status':'待接入','url':'https://github.com/trending'},
            {'name':'大厂 Engineering Blog','purpose':'生产实践验证','is_primary':False,'is_engineering_source':True,'frequency':'weekly','status':'待接入','url':'暂无'},
            {'name':'CNCF / InfoQ / Thoughtworks Radar','purpose':'趋势与落地参考','is_primary':False,'is_engineering_source':True,'frequency':'weekly','status':'待接入','url':'https://www.thoughtworks.com/radar'}
        ],
        'community_sources': [
            {'name':'Hacker News','purpose':'弱信号与反证','is_primary':False,'is_engineering_source':False,'frequency':'daily','status':'待接入','url':'https://news.ycombinator.com'},
            {'name':'Reddit','purpose':'社区反馈','is_primary':False,'is_engineering_source':False,'frequency':'daily','status':'待接入','url':'https://reddit.com/r/MachineLearning'},
            {'name':'X','purpose':'早期讨论线索','is_primary':False,'is_engineering_source':False,'frequency':'daily','status':'待接入','url':'https://x.com'}
        ]
    }


def update_readme(daily_reports, trends):
    del daily_reports, trends
    from generate_readme import generate_readmes

    generate_readmes()


def update_markdown_indexes(trends, papers):
    trend_lines = ['# 趋势雷达索引', '', '> 只保留确有趋势价值、值得持续观察的方向。', '']
    for t in trends:
        trend_lines.append(f"- [{t['title']}]({t['path']}) · {t['stage']} · 关联论文 {t['paper_count']}")
    Path(TRENDS_DIR, 'index.md').write_text('\n'.join(trend_lines) + '\n', encoding='utf-8')
    insight_lines = ['# 启发索引', '', '> 从论文中提炼可复用研究资产。', '']
    focus = [p for p in papers if p.get('value_type') in ('immediate','long_tail')][:8]
    for p in focus:
        insight_lines.append(f"- [{p['title']}](../docs/{p['detail_path']}) · {p['value_type_label']} · {p['one_line_judgement']}")
    Path(INSIGHTS_DIR, 'index.md').write_text('\n'.join(insight_lines) + '\n', encoding='utf-8')
    print('[index] 已更新趋势 / 启发 Markdown 索引')


def main():
    papers = load_all_papers()
    daily_reports = read_daily_reports()
    trends = load_trends(papers)
    insights = load_insights()
    long_tail_items = [
        {
            'id': p['id'],
            'title': p['title'],
            'direction': ' / '.join(TOPIC_LABELS.get(t, t) for t in p.get('matched_topics', [])[:2]) or '未分类',
            'long_tail_type': '可迁移方法' if 'method' in (p.get('abstract') or '').lower() else '工程抽象',
            'why_save': p['long_tail_summary'],
            'future_trigger': p['future_trigger'],
            'reusable_assets': ['Prompt', 'Skill', 'Checklist'] if p.get('value_type') == 'long_tail' else ['Prompt'],
            'revisit_date': (datetime.fromisoformat(p['first_seen_date']) + timedelta(days=21)).date().isoformat() if p.get('first_seen_date') else '',
            'detail_path': p['detail_path']
        }
        for p in papers if p.get('value_type') == 'long_tail'
    ]
    latest_daily = daily_reports[0] if daily_reports else None
    top_paper = papers[0] if papers else None
    value_distribution = {k: len([p for p in papers if p.get('value_type') == k]) for k in ['immediate','trend','long_tail','ignore']}

    latest = {
        'updated_at': datetime.now().isoformat(),
        'site_title': '前沿理论驱动技术雷达日报',
        'site_subtitle': '从论文出发，快速判断即时价值、趋势价值和长尾价值，沉淀可复用研究资产。',
        'latest_daily': latest_daily,
        'top_paper': top_paper,
        'paper_count': len(papers),
        'daily_count': len(daily_reports),
        'trend_count': len(trends),
        'long_tail_count': len(long_tail_items),
        'value_distribution': value_distribution,
        'recent_dailies': daily_reports[:7],
        'top_papers': papers[:10],
        'long_tail_highlights': long_tail_items[:3],
        'common_research_path': ['论文', '理论', '工程实践', '趋势', '启发', '行动']
    }
    save_json('latest.json', latest)
    save_json('daily-index.json', {'updated_at': datetime.now().isoformat(), 'total': len(daily_reports), 'reports': daily_reports})
    save_json('paper-index.json', {'updated_at': datetime.now().isoformat(), 'total': len(papers), 'papers': papers})
    save_json('trend-index.json', {'updated_at': datetime.now().isoformat(), 'total': len(trends), 'trends': trends})
    save_json('insight-index.json', {'updated_at': datetime.now().isoformat(), 'total': len(insights), 'insights': insights})
    save_json('long-tail-index.json', {'updated_at': datetime.now().isoformat(), 'total': len(long_tail_items), 'items': long_tail_items})
    save_json('source-index.json', source_index())
    update_markdown_indexes(trends, papers)
    update_readme(daily_reports, trends)
    print('[index] 索引更新完成')
    return 0


if __name__ == '__main__':
    sys.exit(main())
