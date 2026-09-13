# Kondo Research Institute

Kondo Research Institute is a private research institute in Tokyo, working on theoretical physics, information theory, cryptography and distributed computing. Its central work is Existence Theory — a framework that derives Standard Model parameters from three axioms with zero free parameters.

This repository holds the institute's public documentation. The website at <https://www.kondo-lab.com/> is the place to start reading about the research itself; these pages carry the reference material behind it, in a form that stays readable in plain text and is versioned with the work it describes.

## Contents

| Section | What it covers |
| --- | --- |
| [About](01-about/README.md) | The institute, its research areas and its director |
| [Research](02-research/README.md) | The three lines of work and where each is documented |
| [Papers](03-papers/README.md) | The Existence Theory series, its DOIs and where each paper lives |

## About this repository

The documentation is plain Markdown in the Lunascape Docs format: `lunascape-docs.json` marks the documentation root, each page carries its own title and order in front matter, and Japanese pages live under [`i18n/ja/`](i18n/ja/README.md). English is the canonical language. No build step is required — GitHub renders the pages as they are, and Lunascape Docs opens the same files with an index and a locale switcher.

Related repositories:

- [kondo-research/pfe](https://github.com/kondo-research/pfe) — the Existence Theory papers, their verification code and their own documentation
