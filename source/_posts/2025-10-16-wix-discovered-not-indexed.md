---
title: "“Discovered - currently not indexed” 怎么排查：Wix 新站诊断树"
date: "2025-10-16 10:00:00"
updated: 2026-07-28 09:40:00
description: "用发现、抓取、渲染、内容价值、内部链接和站点信号六层诊断树，排查 Wix 新站 Discovered - currently not indexed。"
categories:
  - "技术 SEO"
tags:
  - "Wix SEO"
  - "Google Search Console"
  - "索引诊断"
permalink: "/insights/wix-discovered-not-indexed/"
draft: false
tableOfContents: true
---

`Discovered - currently not indexed` 的意思可以先按字面理解：Google 知道这个 URL，但当下没有把它纳入索引。它不是一个能靠“再提交一次 sitemap”统一修好的错误码，也不自动等于内容差或 crawl budget 不足。

我的处理方式，是把问题拆成六层：**发现 → 抓取 → 渲染 → 内容价值 → 内部链接 → 站点信号**。每一层只在证据支持时继续，不从状态名称直接猜原因。

## 先确认状态和样本，不先批量请求收录

Search Console 的 Page Indexing 报告用于查看 Google 已知 URL 的索引状态及未收录原因。第一步应确认：

- 问题是单个 URL、某个模板，还是大量页面；
- 受影响 URL 是否确实应该被索引；
- 报告的“上次更新”与页面发布时间是否匹配；
- 是否存在重复、参数、分页或测试 URL；
- Google 选择的 canonical 是否是预期版本。

新站刚发布的 URL 和长期未抓取的核心商业页，紧急程度不同。先抽取代表样本：主页、核心商业页、一个场景页和一篇内容页，避免只盯一个偶然 URL。

## 六层诊断树

### 第一层：发现是否正确

检查 URL 是否出现在当前 sitemap，返回 200，且不是旧路径、预览地址或带参数版本。Wix 官方说明其 sitemap 会随网站变更自动更新；通过 Wix SEO Setup Checklist 连接 Search Console 时也可自动提交。

因此，重复提交同一个 sitemap 通常不是主要动作。更重要的是确认 sitemap 中只包含希望索引的规范 URL，页面没有仍处于未发布状态。

### 第二层：抓取是否受阻

使用 URL Inspection 查看已索引版本和 live test：

- robots 是否允许抓取；
- 页面是否返回正常状态码；
- 是否存在意外的 `noindex`；
- canonical 指向何处；
- Googlebot 能否加载关键资源。

Google 的说明特别指出，live test 显示“可索引”并不保证页面一定会被索引；它只证明实时检查没有发现某些技术阻碍。把这个结果写成“Google 已批准收录”会误导判断。

### 第三层：关键内容能否渲染

在 URL Inspection 的已抓取页面或实时测试中查看截图、HTML 与加载资源。对 Wix 页面，我会特别核对：

- 首屏主要标题和正文是否在渲染结果中出现；
- 关键模块是否依赖失败的资源；
- 移动端是否出现遮挡或空白；
- 页面语言、title、canonical 是否与发布版本一致。

如果 Googlebot 看不到核心内容，继续讨论内容深度没有意义；先解决渲染和发布状态。

### 第四层：页面是否提供独立价值

技术上可抓取不等于值得索引。把页面与同站相近页面并排检查：

- 是否只是替换地区名或产品名的模板；
- 标题承诺是否在正文中得到直接回答；
- 是否有独立规格、场景、限制、步骤或证据；
- 是否与另一个 URL 服务同一查询任务；
- 页面是否主要是占位文本、图片或重复模块。

若多个页面无法形成不同的用户任务，应考虑合并或重做 [Keyword Mapping](/insights/new-site-keyword-mapping/)，而不是继续请求收录。

### 第五层：内部链接是否表达优先级

一个只存在于 sitemap、没有任何正文链接的新页面，在站点结构中几乎没有角色。检查：

- 核心页面能否从导航或重要聚合页到达；
- 相关页面是否用描述性锚文本链接它；
- 是否存在孤立页；
- 面包屑、上下文链接和分页是否形成可理解路径；
- 链接是否是真实可抓取的 `<a href>`。

内部链接的目标不是“每页加三个链接”，而是说明页面之间的从属、比较与下一步关系。

### 第六层：站点层信号和抓取需求

Google 的 crawl budget 文档明确说，这是一份面向超大型、快速变化或大量 URL 处于该状态的网站的高级指南；普通站点通常保持 sitemap 更新并检查 Page Indexing 报告即可。

对页面数量有限的 Wix 新站，我不会一开始就把问题归为 crawl budget。先检查站点是否持续提供可发现、非重复、有真实内部链接的页面；再看服务器稳定性、错误 URL 增长和整个模板的状态。如果大量 URL 长期受影响，才提升到站点层处理。

## 假设示例与诊断表

以下为匿名化的**假设诊断**，不代表真实站点结果：

| 证据 | 所在层 | 下一步 | 暂不做 |
| --- | --- | --- | --- |
| sitemap 有 URL，live test 200 且可索引 | 发现/抓取通过 | 检查渲染、内容差异和内链 | 重复提交 sitemap |
| Google-selected canonical 指向相近页 | 规范化/内容 | 比较两页任务，合并或增强差异 | 强行增加关键词 |
| 关键正文未出现在渲染 HTML | 渲染 | 检查发布与资源加载 | 扩写不可见模块 |
| 页面无正文内链，仅存在于 sitemap | 内链 | 从真实相关页面建立路径 | 批量建更多类似页 |
| 同模板大量页长期未抓取 | 站点层 | 检查 URL 规模、质量与服务器信号 | 逐个手动请求收录 |

## 复查清单与停止条件

- [ ] 从 Page Indexing 报告确认范围、状态和更新时间
- [ ] 用代表样本做 URL Inspection，而不是逐个点所有 URL
- [ ] 检查 200、robots、noindex、canonical 与渲染资源
- [ ] 比较相近页面的任务和独立价值
- [ ] 确保重要页面获得真实、相关的内部链接
- [ ] 记录修改日期，在报告刷新后按同一批样本复查
- [ ] 若 URL 本就不应索引，停止“修复”，改为正确规范化或移除

停止条件很重要：当 live test 通过、页面价值与内链已改善、sitemap 正常时，不应每天重复请求索引。等待抓取与报告更新，并继续建设站点中真正重要的页面。

## 方法的边界与失败模式

Search Console 展示的是 Google 侧的状态和样本，不是完整抓取日志；Wix 也限制了部分服务器层控制。若涉及大规模异常、持续 5xx、复杂国际化或迁移，可能需要平台支持、开发资源与日志证据。

另一种失败模式是把“索引率”当成越高越好。过滤页、重复页、参数 URL 或低价值归档本就不一定需要索引。目标应是让每个重要 canonical 页面可发现、可抓取、可渲染且值得被检索，而不是让所有 URL 变绿。

最后，Google 明确不保证某个网站或页面一定进入索引。本文是诊断顺序，不是收录承诺。

## 延伸阅读

- 新站如何避免页面重复：[先做 Keyword Mapping](/insights/new-site-keyword-mapping/)
- 页面收录后如何安排迭代：[高曝光低点击页面优先级](/insights/gsc-high-impression-low-ctr/)

## 参考资料

- Google Search Console：《[Page indexing report](https://support.google.com/webmasters/answer/7440203?hl=en)》（官方，页面未标注发布日期）
- Google Search Console：《[URL Inspection tool](https://support.google.com/webmasters/answer/9012289?hl=en)》（官方，页面未标注发布日期）
- Google Crawling Infrastructure：《[Optimize your crawl budget](https://developers.google.com/crawling/docs/crawl-budget)》（官方，页面未标注发布日期）
- Wix：《[Submitting Your Sitemap and URLs Directly to Search Engines](https://support.wix.com/en/article/submitting-your-sitemap-and-urls-directly-to-search-engines)》（第一方，页面未标注发布日期）
