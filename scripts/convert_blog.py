#!/usr/bin/env python3
"""Convert mirrored Squarespace blog posts to Astro content-collection markdown.

Reads the wget mirror at ../squarespace-mirror, writes markdown to
src/content/blog/<slug>.md and copies referenced images to
public/images/blog/<slug>/.
"""
import os, re, shutil, sys
from pathlib import Path
from urllib.parse import unquote, urlparse
from bs4 import BeautifulSoup, NavigableString, Tag

SITE = Path(__file__).resolve().parent.parent
MIRROR = SITE.parent / "squarespace-mirror" / "www.wyldcard.io"
OUT_MD = SITE / "src" / "content" / "blog"
OUT_IMG = SITE / "public" / "images" / "blog"

NEWSLETTER_MARKERS = ("newsletter", "sqs-block-newsletter")


def in_newsletter(el: Tag) -> bool:
    for parent in el.parents:
        classes = " ".join(parent.get("class", []))
        if any(m in classes for m in NEWSLETTER_MARKERS):
            return True
    return False


def inline_md(el) -> str:
    if isinstance(el, NavigableString):
        return str(el)
    if not isinstance(el, Tag):
        return ""
    inner = "".join(inline_md(c) for c in el.children)
    if el.name in ("strong", "b"):
        return f"**{inner.strip()}**" if inner.strip() else ""
    if el.name in ("em", "i"):
        return f"*{inner.strip()}*" if inner.strip() else ""
    if el.name == "code":
        return f"`{inner}`"
    if el.name == "br":
        return "  \n"
    if el.name == "a":
        href = el.get("href", "")
        href = rewrite_link(href)
        return f"[{inner}]({href})" if href else inner
    return inner


def rewrite_link(href: str) -> str:
    if not href:
        return href
    # local mirror artifacts like ../design.html or blog/foo.html
    href = re.sub(r"^(\.\./)*", "", href)
    if href.startswith("http"):
        u = urlparse(href)
        if u.netloc.endswith("wyldcard.io"):
            return u.path or "/"
        return href
    if href.endswith(".html"):
        href = "/" + href[: -len(".html")]
    return href


def copy_image(src: str, post_file: Path, slug: str, counter: list) -> str | None:
    if not src or src.startswith("data:"):
        return None
    local = (post_file.parent / unquote(src)).resolve()
    # strip query-string suffix wget may have left in the filename
    if not local.exists():
        candidates = list(local.parent.glob(local.name + "*")) if local.parent.exists() else []
        if candidates:
            local = candidates[0]
        else:
            return None
# the CDN re-encodes regardless of filename — trust magic bytes, not extensions
    with open(local, "rb") as f:
        head = f.read(12)
    ext = ".png" if head.startswith(b"\x89PNG") else ".gif" if head[:3] == b"GIF" else ".webp" if head[8:12] == b"WEBP" else ".jpg"
    counter[0] += 1
    dest_dir = OUT_IMG / slug
    dest_dir.mkdir(parents=True, exist_ok=True)
    dest = dest_dir / f"{counter[0]:02d}{ext}"
    shutil.copyfile(local, dest)
    return f"/images/blog/{slug}/{dest.name}"


def block_md(el: Tag, post_file: Path, slug: str, counter: list, out: list):
    if in_newsletter(el):
        return
    if el.name in ("h1",):
        return  # title handled via frontmatter
    if el.name in ("h2", "h3", "h4"):
        text = inline_md(el).strip()
        if text and text.lower() != "subscribe for updates!":
            level = {"h2": "##", "h3": "###", "h4": "####"}[el.name]
            out.append(f"{level} {text}\n")
        return
    if el.name == "p":
        text = inline_md(el).strip()
        if text and text not in ("Sign up with your email address to receive news and updates.", "We respect your privacy."):
            out.append(text + "\n")
        return
    if el.name == "pre":
        out.append("```\n" + el.get_text().rstrip() + "\n```\n")
        return
    if el.name == "hr":
        out.append("---\n")
        return
    if el.name in ("ul", "ol"):
        for i, li in enumerate(el.find_all("li", recursive=False), 1):
            bullet = "-" if el.name == "ul" else f"{i}."
            out.append(f"{bullet} {inline_md(li).strip()}")
        out.append("")
        return
    if el.name == "blockquote":
        text = inline_md(el).strip()
        if text:
            out.append("> " + text.replace("\n", "\n> ") + "\n")
        return
    if el.name == "img":
        path = copy_image(el.get("src") or el.get("data-src", ""), post_file, slug, counter)
        if path:
            alt = el.get("alt", "").strip()
            # drop useless auto-alts like "95F7797E-...jpeg" or "IMG_1234.jpg"
            if re.fullmatch(r"[\w+-]+\.(jpe?g|png|gif|webp)", alt, re.I):
                alt = ""
            out.append(f"![{alt}]({path})\n")
        return
    # containers: recurse in document order over direct children
    for child in el.children:
        if isinstance(child, Tag):
            block_md(child, post_file, slug, counter, out)


def convert(post_file: Path):
    slug = post_file.stem
    soup = BeautifulSoup(post_file.read_text(encoding="utf-8"), "html.parser")
    article = soup.find("article")
    title = soup.find("h1").get_text(strip=True)
    meta_date = soup.find("meta", {"itemprop": "datePublished"})
    date = meta_date["content"][:10] if meta_date else "1970-01-01"
    desc_tag = soup.find("meta", property="og:description")
    description = desc_tag["content"].strip() if desc_tag else ""
    counter = [0]
    out: list[str] = []
    block_md(article, post_file, slug, counter, out)
    body = "\n".join(out)
    # collapse >2 consecutive blank lines
    body = re.sub(r"\n{3,}", "\n\n", body).strip() + "\n"
    fm = (
        "---\n"
        f'title: "{title}"\n'
        f'description: "{description.replace(chr(34), chr(39))}"\n'
        f"pubDate: {date}\n"
        "---\n\n"
    )
    OUT_MD.mkdir(parents=True, exist_ok=True)
    (OUT_MD / f"{slug}.md").write_text(fm + body, encoding="utf-8")
    print(f"{slug}: {counter[0]} images, {len(body)} chars, date {date}")


if __name__ == "__main__":
    posts = [p for p in MIRROR.glob("blog/*.html") if "tag" not in p.name]
    for p in sorted(posts):
        convert(p)
