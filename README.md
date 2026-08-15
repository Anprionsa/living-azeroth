# A Living Azeroth

Systems design for a WoW Classic+ that reads as inhabited rather than as a static diorama. Four documents on one page: world systems across 74 proposals and 14 sections, all 27 vanilla talent trees rebuilt, ten post-vanilla classes absorbed as talent trees, and the simulation work that tuned them. The site is a single self-contained page; every talent, proposal, and tree renders from the data files it ships with.

This is a design proposal, not a prediction. Blizzard has announced no product called Classic+, and nothing here assumes otherwise.

## Viewing

The page is `index.html`, served by GitHub Pages. To view locally, serve the folder over HTTP; the page loads its data with fetch and does not work from `file://`.

```bash
python -m http.server 8000
```

## Layout

| Path | What it is |
|---|---|
| `index.html` | the site, a copy of `DocumentPage.dc.html` |
| `DocumentPage.dc.html` | the working page; after editing it, re-copy to `index.html` |
| `data/` | canonical data. `talent-data.json` is canonical for what a talent does |
| `files/` | the design record: documents, simulators, validators, working notes |
| `tools/` | runnable copies of the validators and renderers, with repo-relative paths |
| `assets/`, `icons/`, `_ds/`, `vendor/` | images, talent icons, the design system, vendored React |
| `.image-slots.state.json` | image payloads for the page's six map and reference slots |

`files/MANIFEST.md` is the reading order for the record. `files/SCHEMA.md` explains the data shape. The documents are canonical for why; the data is canonical for what.

## Provenance

Original design writing and data. Talent icons, map plates, and screenshots derive from World of Warcraft, which belongs to Blizzard Entertainment; they appear here as reference in an unaffiliated fan design document.
