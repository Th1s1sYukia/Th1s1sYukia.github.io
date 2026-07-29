# Research Brief：GSC 与 GA4 数据差异

```yaml
title: "为什么 GSC 点击和 GA4 自然搜索会话对不上：先统一口径再排查"
slug: gsc-ga4-data-mismatch
search_intent: "信息型/诊断型；读者需要理解并排查 Search Console 点击与 GA4 会话差异"
audience: "负责 SEO 报表、GA4 配置与数据沟通的运营和分析协作者"
thesis: "GSC 点击与 GA4 会话不是同一事件的两个显示器；先把搜索结果点击、页面成功加载、Analytics 采集和会话归因拆成一条链，差异才会变成可诊断的信号"
experience_basis:
  - fact_id: lead-dashboard-project
    use: "仅作为作者理解跨系统数据口径的内部背景，不在正文披露内部流程或结果"
claims:
  - statement: "GSC clicks 统计用户从 Google Search 结果点击站点，GA4 session 则从可采集的页面或屏幕互动开始"
    type: external_fact
    evidence: "Search Console Performance report 与 GA4 sessions 文档"
  - statement: "Search Console 与 GA4 的连接报告会并列两套指标，且 Search Console 数据可用时间与兼容维度有限"
    type: external_fact
    evidence: "Google Analytics Search Console integration 文档"
  - statement: "Search Analytics API 受内部限制影响，不保证返回所有数据行"
    type: external_fact
    evidence: "Search Console API query 文档"
  - statement: "点击到会话的漏斗和排查数字为假设示例"
    type: hypothetical_example
    evidence: "明确标注为假设示例"
sources:
  - publisher: Google Search Console
    title: "Performance report (Search results): Overview and basic setup"
    url: "https://support.google.com/webmasters/answer/7576553?hl=en"
    published_or_updated: "页面未标注发布日期"
    accessed: "2026-07-29"
    tier: official
  - publisher: Google Analytics
    title: "About Analytics sessions"
    url: "https://support.google.com/analytics/answer/9191807?hl=en"
    published_or_updated: "页面未标注发布日期"
    accessed: "2026-07-29"
    tier: official
  - publisher: Google Analytics
    title: "Connect Search Console to Google Analytics"
    url: "https://support.google.com/analytics/answer/10737381?hl=en"
    published_or_updated: "页面未标注发布日期"
    accessed: "2026-07-29"
    tier: official
  - publisher: Google Search Console API
    title: "Search Analytics: query"
    url: "https://developers.google.com/webmaster-tools/v1/searchanalytics/query"
    published_or_updated: "页面未标注发布日期；页面包含 2026-05-07 起的 API 变更说明"
    accessed: "2026-07-29"
    tier: official
disclosure_notes:
  - "文章发布日期晚于 API 页面所述 2026-05-07 变更"
  - "不使用真实后台数字；不把差异率设为通用健康阈值"
internal_links:
  - "/insights/gsc-high-impression-low-ctr/"
  - "/insights/seo-ads-lead-attribution/"
  - "/insights/b2b-seo-lead-quality-loop/"
artifact:
  type: diagnostic_tree
  purpose: "从日期、维度、落地页加载、同意与采集逐层排查"
failure_modes:
  - "把 clicks 与 sessions 当作必须相等的同一指标"
  - "比较不同日期、时区、国家、设备或 Search type"
  - "只调整报表，不验证标签、同意状态、重定向和页面加载"
```
