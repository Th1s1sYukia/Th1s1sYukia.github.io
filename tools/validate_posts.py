#!/usr/bin/env python3
"""Validate Yukia Hexo posts without changing them."""

from __future__ import annotations

import re
import sys
from pathlib import Path

REQUIRED = {
    "title",
    "date",
    "updated",
    "description",
    "categories",
    "tags",
    "permalink",
    "draft",
}
REFERENCE_RE = re.compile(
    r"^- .+：《\[[^]]+\]\(https?://[^)]+\)》"
    r"（(?:官方|第一方)，(?:页面未标注发布日期|发布/更新：\d{4}-\d{2}-\d{2})）$",
    re.M,
)
OFFICIAL_RE = re.compile(
    r"（(?:官方|第一方)，(?:页面未标注发布日期|发布/更新：\d{4}-\d{2}-\d{2})）"
)
SOURCE_DATE_RE = re.compile(r"发布/更新：(\d{4}-\d{2}-\d{2})")
METRIC_RE = re.compile(r"\b(?:29K|1\.9M|9\.22K|1\.42M|3,000\+|310K)\b", re.I)
DISCLAIMER = "以上为任职期间网站整体表现，不作个人单一归因。"


def split_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        raise ValueError("missing opening frontmatter delimiter")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("missing closing frontmatter delimiter")
    raw = text[4:end]
    body = text[end + 5 :]
    fields: dict[str, str] = {}
    for line in raw.splitlines():
        if line and not line[0].isspace() and ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip()
    return fields, body


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    try:
        frontmatter, body = split_frontmatter(text)
    except ValueError as exc:
        return [str(exc)]

    missing = sorted(REQUIRED - frontmatter.keys())
    if missing:
        errors.append(f"missing frontmatter: {', '.join(missing)}")
    legacy = "历史归档" in text
    permalink = frontmatter.get("permalink", "").strip("\"'")
    if not legacy and permalink and not re.fullmatch(
        r"/[a-z0-9][a-z0-9/-]*/", permalink
    ):
        errors.append("permalink must be a stable lowercase ASCII path ending in /")
    if frontmatter.get("draft") not in {"true", "false"}:
        errors.append("draft must be true or false")
    if len(frontmatter.get("description", "").strip("\"'")) < 40:
        errors.append("description must be at least 40 characters")

    if not legacy:
        references = REFERENCE_RE.findall(body)
        if not 3 <= len(references) <= 6:
            errors.append(f"expected 3-6 formatted references, found {len(references)}")
        official = sum(1 for line in body.splitlines() if OFFICIAL_RE.search(line))
        if official < 2:
            errors.append(f"expected at least 2 official/primary references, found {official}")
        if not re.search(r"^## .*(边界|失败|不适用|局限)", body, re.M):
            errors.append("missing boundaries/failure-modes section")
        if not re.search(r"^## .*(清单|决策表|诊断树|示例)", body, re.M):
            errors.append("missing checklist/table/tree/example section")
        internal_links = re.findall(r"\[[^]]+\]\((/[^)]+)\)", body)
        if not internal_links:
            errors.append("missing internal link")
        post_updated = frontmatter.get("updated", "").strip("\"'")[:10]
        for source_date in SOURCE_DATE_RE.findall(body):
            if post_updated and source_date > post_updated:
                errors.append(
                    f"source date {source_date} is later than post updated date {post_updated}"
                )

    if METRIC_RE.search(body) and DISCLAIMER not in body:
        errors.append("resume metrics require the site-wide, non-sole-attribution disclaimer")
    if re.search(r"(我带来|由我实现|我使).{0,20}(点击|展示|流量|线索|排名)", body):
        errors.append("possible sole-attribution performance claim")
    if re.search(r"(公开履历|公开简历|简历允许|履历中|任职期间)", body):
        errors.append("reader-facing resume/disclosure language should not appear in articles")
    if re.search(r"访问：\d{4}-\d{2}-\d{2}", body):
        errors.append("reader-facing references must not use a verification date after a backdated publication")
    if re.search(r"\b1[3-9]\d{9}\b", text):
        errors.append("possible phone number")
    return errors


def iter_posts(target: Path):
    if target.is_file():
        yield target
    else:
        yield from sorted(target.rglob("*.md"))


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_posts.py <post-or-directory>", file=sys.stderr)
        return 2
    target = Path(sys.argv[1])
    failures = 0
    for path in iter_posts(target):
        errors = validate(path)
        if errors:
            failures += 1
            for error in errors:
                print(f"ERROR {path}: {error}")
        else:
            print(f"OK {path}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
