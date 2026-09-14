#!/usr/bin/env python3
"""Build the paper-1 documentation root from the sealed Paper I manuscripts.

The sealed Markdown manuscripts are single files written for conversion to
LaTeX. Lunascape Docs reads a paper best as a title page, one page per chapter
and a references page. This script produces exactly that from the sealed
sources, and changes no wording, number, table or equation:

  * the title block and abstract become README.md, with a chapter list;
  * each chapter, the acknowledgements and the references become their own page;
  * `[Figure N] *caption*` placeholders become the image followed by its caption;
  * adjacent footnote definitions get a blank line, so Markdown keeps them apart;
  * the `[N] text` reference entries become a numbered list, and the script
    checks that the numbers run 1, 2, 3, ... so every in-text citation still
    points at the right entry.

Japanese is the canonical language of this documentation, so the Japanese
manuscript is written in place and the English one to i18n/en/ beside it.

    python3 tools/build-paper.py \\
        --ja <sealed Japanese manuscript>.md \\
        --en <sealed English manuscript>.md \\
        --img <directory holding fig_potential.png and fig_pg23_v2.png> \\
        --version v4.1.1 --date 2026-09-01 --doi 10.5281/zenodo.22217837

--check builds everything in memory and reports whether paper-1/ is up to date.
Rebuilding from the same sources always produces the same files.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from pathlib import Path

CHAPTERS = {
    1: "01-introduction",
    2: "02-from-existence-to-the-equation",
    3: "03-schrodinger-equation",
    4: "04-gauge-structure",
    5: "05-gauge-couplings",
    6: "06-higgs-sector",
    7: "07-fermion-masses",
    8: "08-mixing-angles",
    9: "09-spacetime",
    10: "10-results",
    11: "11-conclusion",
}
FIGURES = {"1": "fig_potential.png", "2": "fig_pg23_v2.png"}
BACK_MATTER = {"acknowledgements": {"Acknowledgements", "謝辞"}, "references": {"References", "参考文献"}}

TEXT = {
    "ja": {
        "author": "著者", "version": "版", "abstract": "概要", "contents": "目次", "figure": "図",
        "about": "この文書について", "open": "（", "close": "）", "sep": "・",
        "about_body": "Zenodo で公開している論文 {version}（{date}）の全文を、章ごとに分けて掲載しています。"
                      "組版の正本は PDF、引用先は Zenodo のレコードです。PDF・検証コード・版の履歴は "
                      "[kondo-research/pfe](https://github.com/kondo-research/pfe) にあります。",
    },
    "en": {
        "author": "Author", "version": "Version", "abstract": "Abstract", "contents": "Contents", "figure": "Figure",
        "about": "About this document", "open": " (", "close": ")", "sep": "·",
        "about_body": "The full text of the paper as published on Zenodo, version {version} ({date}), split by chapter. "
                      "The PDF is the typeset version of record, and the Zenodo record is what to cite. The PDF, "
                      "the verification code and the version history are in "
                      "[kondo-research/pfe](https://github.com/kondo-research/pfe).",
    },
}

FIGURE_LINE = re.compile(r"^\[Figure (\d+)\]\s*\*(.+)\*\s*$")
FOOTNOTE_LINE = re.compile(r"^\[\^[^\]]+\]: ")
REFERENCE_LINE = re.compile(r"^\[(\d+)\]\s+(.*)$")
AUTHOR_LINE = re.compile(r"^\*\*(.+?)\*\*\s+—\s+(.+?)\s+\((.+)\)\s*$")


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(2)


def trim(lines: list[str]) -> list[str]:
    start, end = 0, len(lines)
    while start < end and lines[start].strip() in ("", "---"):
        start += 1
    while end > start and lines[end - 1].strip() in ("", "---"):
        end -= 1
    return lines[start:end]


def alt_text(caption: str) -> str:
    for stop in ("。", ". "):
        head, sep, _ = caption.partition(stop)
        if sep:
            return head.strip()
    return caption.strip()


class Manuscript:
    def __init__(self, text: str, source: Path):
        lines = text.split("\n")
        if not lines or not lines[0].startswith("# "):
            fail(f"{source}: the first line is not the title")
        title, _, subtitle = lines[0][2:].partition(" — ")
        self.title, self.subtitle = title.strip(), subtitle.strip()

        headings = [i for i, line in enumerate(lines) if line.startswith("# ")]
        self.chapters: dict[int, tuple[str, str, list[str]]] = {}
        self.back: dict[str, tuple[str, list[str]]] = {}
        first_chapter = None
        for k, i in enumerate(headings[1:], start=1):
            end = headings[k + 1] if k + 1 < len(headings) else len(lines)
            head, body = lines[i][2:].strip(), lines[i + 1:end]
            numbered = re.match(r"^(\d+)\.\s+(.*)$", head)
            if numbered:
                self.chapters[int(numbered.group(1))] = (head, numbered.group(2), body)
                first_chapter = i if first_chapter is None else first_chapter
                continue
            key = next((key for key, names in BACK_MATTER.items() if head in names), None)
            if key is None:
                fail(f"{source}: unexpected top-level heading {head!r}")
            self.back[key] = (head, body)

        if set(self.chapters) != set(CHAPTERS):
            fail(f"{source}: chapters {sorted(self.chapters)} do not match {sorted(CHAPTERS)}")
        if set(self.back) != set(BACK_MATTER):
            fail(f"{source}: back matter {sorted(self.back)} is incomplete")

        front = lines[1:first_chapter]
        author = next((AUTHOR_LINE.match(line) for line in front if AUTHOR_LINE.match(line)), None)
        if author is None:
            fail(f"{source}: no author line")
        self.author, self.affiliation = author.group(1), author.group(2)
        abstract_at = next((i for i, line in enumerate(front) if line.startswith("## ")), None)
        if abstract_at is None:
            fail(f"{source}: no abstract heading")
        self.abstract = trim(front[abstract_at + 1:])


def body(lines: list[str], lang: str, counts: dict[str, int]) -> list[str]:
    out: list[str] = []
    for i, line in enumerate(lines):
        figure = FIGURE_LINE.match(line)
        if figure and figure.group(1) in FIGURES:
            number, caption = figure.groups()
            out += [f"![{alt_text(caption)}](img/{FIGURES[number]})", "",
                    f"*{TEXT[lang]['figure']} {number}. {caption}*"]
            counts["figures"] += 1
            continue
        out.append(line)
        following = lines[i + 1] if i + 1 < len(lines) else ""
        if FOOTNOTE_LINE.match(line) and FOOTNOTE_LINE.match(following):
            out.append("")
            counts["footnotes"] += 1
    return trim(out)


def references(lines: list[str], source: Path) -> list[str]:
    entries = []
    for line in lines:
        if not line.strip():
            continue
        match = REFERENCE_LINE.match(line)
        if not match:
            fail(f"{source}: unexpected line in the references: {line[:70]!r}")
        entries.append((int(match.group(1)), match.group(2)))
    numbers = [n for n, _ in entries]
    if numbers != list(range(1, len(numbers) + 1)):
        fail(f"{source}: reference numbers do not run 1..{len(numbers)}: {numbers}")
    return [f"{n}. {text}" for n, text in entries]


def page(heading: str, lines: list[str], order: int | None) -> str:
    front = f"---\nnavigation:\n  order: {order}\n---\n\n" if order is not None else ""
    return front + f"# {heading}\n\n" + "\n".join(lines).rstrip() + "\n"


def title_page(m: Manuscript, lang: str, version: str, date: str, doi: str) -> str:
    t = TEXT[lang]
    lines = [f"# {m.title}", ""]
    if m.subtitle:
        lines += [f"*{m.subtitle}*", ""]
    lines += [
        f"**{t['author']}**: {m.author}{t['open']}{m.affiliation}{t['close']}", "",
        f"**{t['version']}**: {version}{t['open']}{date}{t['close']} {t['sep']} **DOI**: [{doi}](https://doi.org/{doi})", "",
        f"## {t['abstract']}", "", *m.abstract, "",
        f"## {t['contents']}", "",
    ]
    lines += [f"{n}. [{m.chapters[n][1]}]({slug}.md)" for n, slug in CHAPTERS.items()]
    lines += [""] + [f"- [{m.back[key][0]}]({key}.md)" for key in BACK_MATTER]
    lines += ["", f"> **{t['about']}**", "> " + t["about_body"].format(version=version, date=date)]
    return "\n".join(lines) + "\n"


def build(args: argparse.Namespace) -> tuple[dict[str, bytes], dict[str, dict[str, int]], dict[str, str]]:
    files: dict[str, bytes] = {}
    stats: dict[str, dict[str, int]] = {}
    hashes: dict[str, str] = {}
    for lang, source in (("ja", args.ja), ("en", args.en)):
        raw = source.read_text(encoding="utf-8")
        hashes[lang] = hashlib.sha256(raw.encode("utf-8")).hexdigest()
        m = Manuscript(raw, source)
        base = "" if lang == "ja" else "i18n/en/"
        canonical = lang == "ja"
        counts = {"figures": 0, "footnotes": 0, "references": 0}

        files[base + "README.md"] = title_page(m, lang, args.version, args.date, args.doi).encode()
        for number, slug in CHAPTERS.items():
            heading, _, lines = m.chapters[number]
            files[f"{base}{slug}.md"] = page(heading, body(lines, lang, counts), number * 10 if canonical else None).encode()
        heading, lines = m.back["acknowledgements"]
        files[base + "acknowledgements.md"] = page(heading, body(lines, lang, counts), 120 if canonical else None).encode()
        heading, lines = m.back["references"]
        entries = references(lines, source)
        counts["references"] = len(entries)
        files[base + "references.md"] = page(heading, entries, 130 if canonical else None).encode()
        for name in FIGURES.values():
            image = args.img / name
            if not image.exists():
                fail(f"missing figure {image}")
            files[f"{base}img/{name}"] = image.read_bytes()
        stats[lang] = counts
    return files, stats, hashes


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--ja", type=Path, required=True, help="sealed Japanese manuscript")
    parser.add_argument("--en", type=Path, required=True, help="sealed English manuscript")
    parser.add_argument("--img", type=Path, required=True, help="directory holding the figure PNGs")
    parser.add_argument("--version", required=True)
    parser.add_argument("--date", required=True)
    parser.add_argument("--doi", required=True)
    parser.add_argument("--out", type=Path, default=Path(__file__).resolve().parent.parent / "paper-1")
    parser.add_argument("--check", action="store_true", help="do not write; fail if --out is not up to date")
    args = parser.parse_args()

    files, stats, hashes = build(args)
    for lang in ("ja", "en"):
        s = stats[lang]
        print(f"{lang}: source sha256 {hashes[lang]}")
        print(f"    pages {sum(1 for p in files if p.endswith('.md') and (p.startswith('i18n/en/') == (lang == 'en')))}, "
              f"figures {s['figures']}, footnote gaps {s['footnotes']}, references {s['references']}")

    stale = [path for path, data in files.items()
             if not (args.out / path).exists() or (args.out / path).read_bytes() != data]
    if args.check:
        if stale:
            print("check: OUT OF DATE — " + ", ".join(stale), file=sys.stderr)
            return 1
        print(f"check: {len(files)} files up to date")
        return 0
    for path in stale:
        target = args.out / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(files[path])
    print(f"wrote {len(stale)} of {len(files)} files to {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
