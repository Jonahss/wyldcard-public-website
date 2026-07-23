# wyldcard.io

Public website for [Wyldcard](https://www.wyldcard.io) — plastic cards with
e-paper screens that meld the physical and the digital.

Static site built with [Astro](https://astro.build). Rebuilt from the original
Squarespace site in July 2026; same URL structure, a fraction of the payload,
zero client-side JavaScript.

## Pages

- `/` — home: what Wyldcard is, DevKit on [Crowd Supply](https://www.crowdsupply.com/wyldcard/wyldcard-devkit), demo video
- `/design` — call for artists
- `/blog` — blog index; posts live in `src/content/blog/*.md`
- `/rss.xml`, `/sitemap-index.xml`, `/robots.txt` — generated at build time

## Writing a blog post

Add a markdown file to `src/content/blog/` with frontmatter:

```markdown
---
title: "Post Title"
description: "One-sentence summary, used for meta tags and the blog index."
pubDate: 2026-08-01
---

Post body. Images go in `public/images/blog/<slug>/` and are referenced
as `/images/blog/<slug>/whatever.webp`.
```

The filename (minus `.md`) becomes the URL slug: `my-post.md` → `/blog/my-post`.

## Development

Requires Node 22+ and [pnpm](https://pnpm.io).

| Command        | Action                                       |
| :------------- | :------------------------------------------- |
| `pnpm install` | Install dependencies                         |
| `pnpm dev`     | Dev server at `localhost:4321`               |
| `pnpm build`   | Build the production site to `./dist/`       |
| `pnpm preview` | Serve the built site locally                 |

## Deployment

Hosted on Cloudflare Pages: pushes to `main` build with `pnpm build` and
deploy `dist/` automatically.

## Repo layout

- `src/layouts/Base.astro` — shared shell: nav, footer, SEO/OG meta, global styles
- `src/pages/` — one file per route
- `src/content/blog/` — blog posts (markdown)
- `public/` — images and other static assets, served as-is
- `scripts/convert_blog.py` — one-shot converter used to port posts from the
  Squarespace mirror; kept for reference
