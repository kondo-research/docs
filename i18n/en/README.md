---
navigation:
  title: Kondo Research Institute
---

# Kondo Research Institute

Kondo Research Institute is a private research institute in Tokyo, working on theoretical physics, information theory, cryptography and distributed computing. At its centre is Existence Theory — a framework in which formalizing what it means "to exist" yields a single equation, and that equation gives the parameters of the Standard Model with no free parameters.

This repository holds the institute's public documentation. The [website](https://www.kondo-research.org/) is the place to start reading about the research itself; these pages carry the reference material behind it, in a form that stays readable in plain text and is versioned in the same repository as the work it describes.

## Contents

| Section | What it covers |
| --- | --- |
| [About](01-about/README.md) | The institute, its research areas and its director |
| [Research](02-research/README.md) | The three lines of work and where each is documented |
| [Papers](03-papers/README.md) | The Existence Theory series, its DOIs and where each paper lives |

## About this repository

The documentation is plain Markdown in the Lunascape Docs format. `lunascape-docs.json` at the repository root marks the documentation root, and each page carries its own title and order in front matter. **Japanese is the canonical language**; these English pages are its translations under `i18n/en/`. Order is owned by the [Japanese pages](../../README.md), and the English ones override only the title.

No build step is required. GitHub renders the pages as they are, and Lunascape Docs opens the same files with an index and a locale switcher.

Related repositories:

- [kondo-research/pfe](https://github.com/kondo-research/pfe) — the Existence Theory papers, their verification code and the papers' own documentation
