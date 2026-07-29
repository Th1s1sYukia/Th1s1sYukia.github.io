# Research Brief：SEO 内容审计诊断

```yaml
title: "B2B SEO 内容审计：流量下滑、关键词内耗与意图错位怎么区分"
slug: seo-content-audit-diagnosis
search_intent: "信息型/诊断型；读者需要判断页面表现下降的原因并安排修复优先级"
audience: "维护已有内容库的独立站 SEO 与内容运营者"
thesis: "内容审计不是给文章打统一分数，而是先把站点级下滑、查询迁移、页面互抢和意图错位分成不同假设，再用最小证据决定动作"
experience_basis:
  - fact_id: jimi-scope
    use: "仅作为作者理解多站点与多页面诊断的内部背景，不在正文披露站点数据"
claims:
  - statement: "自然搜索流量下降可能来自算法变化、排名变化、技术问题、安全或垃圾内容问题、季节性与需求变化"
    type: external_fact
    evidence: "Google Search Central traffic drops 文档"
  - statement: "GSC Performance report 可按查询、页面、国家和设备等维度观察点击、展示、CTR 与平均排名"
    type: external_fact
    evidence: "Google Search Console Performance report"
  - statement: "两个页面同时获得同类查询并不自动等于有害的关键词内耗"
    type: author_analysis
    evidence: "需要结合页面任务、趋势和转化路径判断"
  - statement: "审计矩阵中的数据为假设示例"
    type: hypothetical_example
    evidence: "明确标注为假设示例"
sources:
  - publisher: Google Search Central
    title: "Debugging drops in Google Search traffic"
    url: "https://developers.google.com/search/docs/monitor-debug/debugging-search-traffic-drops"
    published_or_updated: "页面未标注发布日期"
    accessed: "2026-07-29"
    tier: official
  - publisher: Google Search Console
    title: "Performance report (Search results): Overview and basic setup"
    url: "https://support.google.com/webmasters/answer/7576553?hl=en"
    published_or_updated: "页面未标注发布日期"
    accessed: "2026-07-29"
    tier: official
  - publisher: Google Search Central
    title: "Creating helpful, reliable, people-first content"
    url: "https://developers.google.com/search/docs/fundamentals/creating-helpful-content"
    published_or_updated: "页面未标注发布日期"
    accessed: "2026-07-29"
    tier: official
  - publisher: Google Search Central
    title: "Search Engine Optimization (SEO) Starter Guide"
    url: "https://developers.google.com/search/docs/fundamentals/seo-starter-guide"
    published_or_updated: "页面未标注发布日期"
    accessed: "2026-07-29"
    tier: official
disclosure_notes:
  - "不使用真实站点流量或线索数字"
  - "自定义诊断矩阵不是 Google 官方评分"
internal_links:
  - "/insights/gsc-high-impression-low-ctr/"
  - "/insights/b2b-product-pages-vs-blog/"
  - "/insights/b2b-seo-lead-quality-loop/"
artifact:
  type: diagnostic_tree
  purpose: "用站点、查询和页面三个层级排除错误假设"
failure_modes:
  - "只看同比总流量，忽略品牌词、国家、设备或页面结构变化"
  - "发现两个 URL 后立即合并，没有确认页面任务"
  - "一次改动 title、正文、内链与模板，无法判断什么起作用"
```
