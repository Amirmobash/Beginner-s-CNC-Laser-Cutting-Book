# CNC & Laser für Einsteiger: Deine erste Geschenkbox aus Holz

Author: **Amir Mobasheraghdam**. Reader language: German (de-DE), informal “du”. This digital-first technical working manuscript follows one personalized plywood gift box from design and laser cutting to assembly and CNC name engraving on the separate lid.

**Not approved for commercial publication or unattended manufacturing.** No physical prototype has been manufactured in this environment. Current publisher terms, exact hardware suitability, practical machining, rights and genuine human authorship remain review gates.

## Public repository boundary

This repository is public. The latest author instruction withholds the complete commercial manuscript, engineering product files, illustrations, cover and publication outputs until explicit public-distribution approval or a private repository is available. `.gitignore` enforces this boundary. The public repository contains build/validation infrastructure, research metadata and status documentation. A public clone alone intentionally cannot reconstruct the withheld book. No deployment or publisher submission has occurred.

## Local production environment

Prepared tools: Python 3.12, Pandoc 3.1.11.1, Inkscape 1.4, FreeCAD 1.0.0 and Java. Python packages are pinned in `requirements.txt`. The Linux operation checks do not establish that Windows tutorials have been tested.

```sh
python -m venv /workspace/book-venv
/workspace/book-venv/bin/pip install -r requirements.txt
# These commands require the locally retained manuscript and product assets:
/workspace/book-venv/bin/python scripts/build_book.py
/workspace/book-venv/bin/python scripts/validate_assets.py
/workspace/book-venv/bin/python scripts/validate_references.py
/workspace/book-venv/bin/python scripts/validate_epub.py
/workspace/book-venv/bin/python scripts/check_project.py
```

Local source directories: `manuscript/`, `engineering/`, `figures/`, `cover/`. Editions: `output/CNC_Laser_Geschenkbox_Amir_Mobasheraghdam.docx`, `output/CNC_Laser_Geschenkbox_Digital.pdf`, `output/CNC_Laser_Geschenkbox.epub`, `output/web/index.html`. Reader downloads: `output/reader_project_files.zip`.

## Evidence and limitations

`research/` records accessed original sources, claim mapping, software comparisons, hardware questions and blocked requests. URLs alone are not verification. Current prices and inaccessible official publisher policies are not fabricated. `publishing/` distinguishes a generated manuscript from genuine author approval and channel eligibility. `quality/` and `PROJECT_STATE.md` record executed checks and remaining work.

Diagrams are original explanations, not fabricated application screenshots or workshop photographs. Machine-independent learning examples are not production programs; no universal laser power, spindle speed, feed or engraving depth is prescribed. A manufacturer-compatible machine configuration, supervised first run, material test and suitable workholding are necessary.

Public availability of project metadata grants no blanket permission to use trademarks, third-party material or unreviewed content commercially. Full-source excerpts used as local evidence are excluded from Git and book editions. The project has no invented ISBN, endorsements, hardware test results or publisher approval.

Additional verification: `python scripts/verify_reproducibility.py` repeats the six-output build; `node scripts/check_browser.cjs` runs local HTTP browser/EPUB.js/axe checks with tools restored by `bash scripts/setup_tools.sh`. `python scripts/package_private_delivery.py` creates a **local-only** full production ZIP; it does not upload or stage content.
