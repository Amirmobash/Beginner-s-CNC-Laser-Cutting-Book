#!/usr/bin/env bash
# Reproduce book-production tooling without uploading any commercial source.
set -eu
cd /workspace/Beginner-s-CNC-Laser-Cutting-Book
python -m venv /workspace/book-venv
/workspace/book-venv/bin/python -m pip install --no-input -r requirements.txt
/workspace/book-venv/bin/python -m pip check
pandoc --version
inkscape --version
command -v freecadcmd java chromium
mkdir -p /workspace/book-tools
book_archive=/workspace/book-tools/epubcheck-5.4.0.zip
book_digest=33350c61038e71dfb3d45a76aed04bf5481e6d5500cb780f6e98db8bbd15a28c
if ! test -f "$book_archive"; then
  curl --fail --location --retry 2 https://github.com/w3c/epubcheck/releases/download/v5.4.0/epubcheck-5.4.0.zip --output "$book_archive"
fi
printf '%s  %s\n' "$book_digest" "$book_archive" | sha256sum --check
if ! test -f /workspace/book-tools/epubcheck-5.4.0/epubcheck.jar; then
  unzip -q "$book_archive" -d /workspace/book-tools
fi
mkdir -p /workspace/book-tools/browser
PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1 npm --prefix /workspace/book-tools/browser install --save-exact --no-audit --no-fund epubjs@0.3.93 jszip@3.10.1 @axe-core/playwright@4.10.2
# Chromium is supplied by the managed base. No service should persist between tasks.
