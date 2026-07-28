#!/usr/bin/env python3
"""Validate generated output and internal links for the Yukia blog."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

REQUIRED_PATHS = [
    "index.html",
    "about/index.html",
    "editorial-policy/index.html",
    "categories/index.html",
    "tags/index.html",
    "archives/index.html",
    "atom.xml",
    "sitemap.xml",
    "robots.txt",
    "404.html",
    "2023/07/12/初见·从零开始的AI宇宙构建/index.html",
    "2023/07/22/从零开始的AI宇宙·ChatGpt火爆后的行业观察/index.html",
    "2023/08/02/从零开始的AI宇宙·不要让ChatGpt牵着你走/index.html",
    "2023/08/17/Nodejs笔记01/index.html",
    "2023/08/18/Nodejs笔记02/index.html",
    "2023/08/27/2023-8生成式AI推荐汇总/index.html",
    "insights/b2b-seo-lead-quality-loop/index.html",
    "insights/new-site-keyword-mapping/index.html",
    "insights/gsc-high-impression-low-ctr/index.html",
    "insights/wix-discovered-not-indexed/index.html",
    "insights/seo-ads-lead-attribution/index.html",
]


def target_exists(public: Path, raw_url: str) -> bool:
    parsed = urlsplit(raw_url)
    if parsed.scheme or parsed.netloc or raw_url.startswith(("#", "mailto:", "tel:")):
        return True
    path = unquote(parsed.path)
    if not path.startswith("/"):
        return True
    candidate = public / path.lstrip("/")
    return (
        candidate.is_file()
        or (candidate / "index.html").is_file()
        or candidate.with_suffix(".html").is_file()
    )


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: check_site.py <public-directory>", file=sys.stderr)
        return 2
    public = Path(sys.argv[1]).resolve()
    errors: list[str] = []
    for relative in REQUIRED_PATHS:
        if not (public / relative).is_file():
            errors.append(f"missing required output: /{relative}")

    for html in sorted(public.rglob("*.html")):
        text = html.read_text(encoding="utf-8", errors="replace")
        if "draft: true" in text:
            errors.append(f"draft marker leaked into {html.relative_to(public)}")
        if "<link rel=\"canonical\"" not in text:
            errors.append(f"missing canonical in {html.relative_to(public)}")
        for url in re.findall(r"""(?:href|src)=["']([^"']+)["']""", text):
            if not target_exists(public, url):
                errors.append(
                    f"broken internal target in {html.relative_to(public)}: {url}"
                )

    if errors:
        for error in errors:
            print(f"ERROR {error}")
        return 1
    print(f"OK generated site: {len(list(public.rglob('*.html')))} HTML files checked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
