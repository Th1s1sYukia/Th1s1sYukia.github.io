# Research Brief：国际站语言与地区架构

```yaml
title: "国际站 SEO 架构怎么选：hreflang、canonical 与 URL 的分工"
slug: international-seo-site-architecture
search_intent: "信息型/决策型；读者需要判断多语言、多地区站点的 URL 结构与技术标记"
audience: "准备扩展语言或国家版本的独立站运营者、SEO 与开发协作者"
thesis: "先明确页面差异来自语言、地区还是业务，再让独立 URL、hreflang、canonical 各司其职；把三者当成一组地区定向标签，往往会制造冲突信号"
experience_basis:
  - fact_id: jimi-scope
    use: "仅作为作者理解多站点协作约束的内部背景，不在正文披露公司、任职或项目细节"
claims:
  - statement: "Google 建议不同语言版本使用不同 URL，并可通过 HTML、HTTP Header 或 Sitemap 声明 hreflang"
    type: external_fact
    evidence: "Google Search Central localized versions 与 multi-regional sites 文档"
  - statement: "重定向和 rel=canonical 是强 canonicalization 信号，Sitemap 是较弱信号；多个信号可叠加"
    type: external_fact
    evidence: "Google Search Central canonical 文档"
  - statement: "hreflang 解决版本匹配，canonical 解决重复或近重复页面的首选 URL，两者不能互相替代"
    type: author_analysis
    evidence: "基于三份官方文档的职责拆分"
  - statement: "示例中的 en-us、en-gb 与 zh-cn URL、产品差异和决策均为假设"
    type: hypothetical_example
    evidence: "明确标注为假设示例"
sources:
  - publisher: Google Search Central
    title: "Tell Google about localized versions of your page"
    url: "https://developers.google.com/search/docs/specialty/international/localized-versions"
    published_or_updated: "页面未标注发布日期"
    accessed: "2026-07-29"
    tier: official
  - publisher: Google Search Central
    title: "Managing multi-regional and multilingual sites"
    url: "https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites"
    published_or_updated: "页面未标注发布日期"
    accessed: "2026-07-29"
    tier: official
  - publisher: Google Search Central
    title: "How to specify a canonical URL with rel=\"canonical\" and other methods"
    url: "https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls"
    published_or_updated: "页面未标注发布日期"
    accessed: "2026-07-29"
    tier: official
disclosure_notes:
  - "不写具体公司的站点结构、后台信息或上线结果"
  - "不把 Google 的发现与索引信号写成排名保证"
internal_links:
  - "/insights/new-site-keyword-mapping/"
  - "/insights/wix-discovered-not-indexed/"
artifact:
  type: decision_table
  purpose: "按语言、地区和业务差异选择 URL、hreflang 与 canonical 组合"
failure_modes:
  - "将所有地区页 canonical 到全球页，导致地区版本信号被合并"
  - "hreflang 不互相返回、语言地区代码错误或自动跳转阻挡访问"
  - "站点尚无真实地区差异却提前复制大量近重复页面"
```
