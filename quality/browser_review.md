# Browser, EPUB reader and HTML accessibility review

Date: 2026-11-04. Final tested files:

- EPUB SHA-256: `a22362d2fd5bb2dd21f002b8f0f34450b91f6801e287e6207bcae07890d3afb7`.
- Self-contained HTML SHA-256: `9b26f6d1e5006528a6663a3bc62e27b095afbe6d20c63dace5d82c74078c4a43`.

**Final automated result: PASS for the bounded checks below.** Machine-readable results: `quality/browser_review.json`. These are reading/layout and selected automated accessibility checks, not a legal compliance statement, publisher approval or hardware validation.

## Tooling and execution

Executed `scripts/check_browser.cjs` with Playwright1.62.1 and Chromium155.0.8059.79. Test-only dependencies outside the checkout: ePub.js0.3.93, JSZip3.10.1 and @axe-core/playwright4.10.2 in `/workspace/book-tools/browser`. The harness opens a temporary127.0.0.1-only HTTP server, renders the actual ZIP-packaged EPUB through ePub.js, and closes both browser and server at completion. No content was deployed or published. This was an actual EPUB-reader test, not merely opening extracted XHTML in a browser.

The first harness attempt required changing Playwright's convenience page creation to an explicit browser context for the Axe integration. That harness error was corrected before content results were assessed. A later diagnostic attempt to open a `file://` URL was blocked by the managed browser policy; the supported local reader/server workflow was used for validation.

## Responsive HTML

Tested viewport widths1280px and375px, each900px high:

| Check | Desktop1280 | Mobile375 |
|---|---|---|
| Images decoded |34/34|34/34|
| Navigation links resolved |12/12|12/12|
| Document horizontal overflow |none|none|
| Axe WCAG2A/AA and2.1A/AA rule violations |0|0|
| Axe rules recorded as passed |20|20|
| Axe incomplete rule entries |0|0|

A real defect was found on the earlier HTML build: the `.cover` rule allowed a400px image inside a375px viewport, extending the document to416px. The build owner added `width:100%` while retaining the cover's maximum width. The final regenerated HTML measured exactly375px at the mobile viewport; the correction was verified against the final hash above.

All navigation targets were checked in the HTML DOM. The page includes105 headings. Automated checks did not certify keyboard workflow, screen-reader pronunciation, text quality, reading comprehension or image-description adequacy.

## EPUB reading

At both viewport widths, the harness opened chapters1,4,5,6,8 and9 through the EPUB reader. All12 render cases displayed the expected chapter heading. All22 instructional images across those selected chapters decoded at each viewport. There were no JavaScript page errors, broken selected-chapter images or document-width overflows. The reader parsed13 spine items and12 navigation entries; every navigation href resolved to a spine item.

The reader was set to a single-column scrolling flow without spreads. Screenshots were captured at chapter starts and after scrolling to the G-code example and figures in chapters5 and8. This proves the tested ePub.js/Chromium configuration; it does not establish Kindle, Tolino, Apple Books, Adobe Digital Editions or other device compatibility. Chapters2,3,7, front matter, appendix and bibliography were not individually opened in the reader by this representative-content test; package navigation and asset structure have their own separate validators.

## Visual inspection actually performed

Viewed final screenshots of:

- Mobile HTML cover/title: the cover fits the available width and its proportions are retained.
- Mobile EPUB chapter4 code: the educational warning and code remain visible without horizontal scrolling; the long warning wraps.
- Mobile EPUB chapter5 figure/table region: the panel illustration and caption fit the reading width; table text wraps instead of extending the document.
- Desktop EPUB chapter8 support/engraving-zone diagram: the image is visible, with clear annotation and no observed clipping in the captured view.

Also viewed an earlier representative mobile chapter5 opening and desktop chapter8 opening. The screenshots are local review evidence under ignored `quality/screenshots/`, not authentic CAD application screenshots or photographs. Small labels inside technical figures may require reader zoom on a phone; captions and nearby text supply the corresponding dimensions. Detailed drawing inspection remains better suited to the digital PDF or a larger viewport.

## Remaining manual work

Test with a real screen reader and keyboard, review alt descriptions against images, verify zoom and orientation changes on actual devices, and inspect publisher-specific conversions. No conclusion about BFSG applicability or legal conformity follows from zero automated violations. Re-run the harness after content, stylesheet or generated-artifact changes; hashes above bind these results to the reviewed build.
