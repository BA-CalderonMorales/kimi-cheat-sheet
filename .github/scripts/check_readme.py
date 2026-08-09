#!/usr/bin/env python3
"""
Conservative README checker:
- Finds HTTP/HTTPS links in README.md
- Fixes obvious issues (http://github.com -> https://github.com, http badges -> https)
- Validates links with a HEAD/GET request and records broken links
- Appends a small report to README.md when changes or broken links are found
- Exits 0 on success; non-zero only on unexpected errors

This script intentionally makes minimal edits and writes back to README.md so CI can commit them.
"""

from __future__ import annotations
import re
import sys
import time
from urllib.parse import urlparse
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

README = "README.md"

LINK_RE = re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+)\)")
URL_RE = re.compile(r"(?P<url>https?://[\w\-\.\/:?=&%#~+,]+)")

# conservative replacements: only for well-known hosts
REPLACEMENTS = [
    (r"http://github.com", r"https://github.com"),
    (r"http://www.github.com", r"https://www.github.com"),
    (r"http://img.shields.io", r"https://img.shields.io"),
    (r"http://shields.io", r"https://shields.io"),
    (r"http://badge.fury.io", r"https://badge.fury.io"),
]

TIMEOUT = 10


def smart_head(url: str) -> int | None:
    """Try HEAD, fall back to GET. Return HTTP status code or None on unreachable."""
    try:
        req = Request(url, method="HEAD")
    except TypeError:
        # older Python without method support on Request
        req = Request(url)
    try:
        with urlopen(req, timeout=TIMEOUT) as resp:
            return getattr(resp, "status", None) or getattr(resp, "getcode", lambda: None)()
    except HTTPError as e:
        return e.code
    except Exception:
        # try GET as fallback
        try:
            with urlopen(url, timeout=TIMEOUT) as resp:
                return getattr(resp, "status", None) or getattr(resp, "getcode", lambda: None)()
        except Exception:
            return None


def main() -> int:
    try:
        with open(README, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print("README.md not found; nothing to do.")
        return 0

    original = content
    changed = False

    # Apply conservative replacements
    for old, new in REPLACEMENTS:
        if old in content:
            content = content.replace(old, new)
            changed = True

    # Collect links to validate (from markdown link syntax and bare URLs)
    links = set()
    for m in LINK_RE.finditer(content):
        links.add(m.group(2))
    for m in URL_RE.finditer(content):
        links.add(m.group("url"))

    # Limit number of checks to avoid long runs
    MAX_CHECKS = 100
    checked = 0
    broken = []

    for url in sorted(links):
        if checked >= MAX_CHECKS:
            break
        checked += 1
        # ignore mailto and local anchors
        if url.startswith("mailto:") or url.startswith("#"):
            continue
        parsed = urlparse(url)
        if parsed.scheme not in ("http", "https"):
            continue
        # Skip commonly flaky hosts (avoid heavy false positives)
        if parsed.netloc.endswith("localhost"):
            continue
        status = smart_head(url)
        if status is None:
            broken.append((url, "unreachable"))
        elif status >= 400:
            broken.append((url, f"HTTP {status}"))
        # be polite between requests
        time.sleep(0.1)

    report_lines = []
    if broken:
        report_lines.append("\n\n---\n## Automated README link check (generated)\nThe automated checker found potential broken links or unreachable URLs:\n")
        for u, reason in broken:
            report_lines.append(f"- {u} — {reason}\n")
        report_lines.append("\nPlease review the links above. This automated check only reports reachability, not content correctness.\n")
        changed = True

    if changed:
        # remove any previous generated section to avoid duplicates
        content = re.sub(r"\n\n---\n## Automated README link check \(generated\)[\s\S]*$", "", content)
        content = content.rstrip() + "\n" + "".join(report_lines)
        with open(README, "w", encoding="utf-8") as f:
            f.write(content)
        print("README.md updated with conservative fixes and/or a link report.")
    else:
        print("No changes required for README.md.")

    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as e:
        print("Unexpected error:", e)
        raise
