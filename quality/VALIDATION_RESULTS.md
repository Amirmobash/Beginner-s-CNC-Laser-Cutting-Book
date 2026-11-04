# Final validation results

2026-11-04. Evidence is in the named machine-readable reports; no unexecuted check is called passed.

|Check|Outcome|Scope|
|---|---|---|
|Dependency installation and pip check|PASS|Pinned packages installed; repeat setup successful|
|Source/image/caption/SVG/DOCX/PDF/HTML checks|PASS|assets_validation.json|
|References and retained evidence hashes|PASS|27 source files hash-verified; failed fetches separately warned|
|EPUBCheck5.4.0|PASS|0fatal/0error/0warning|
|Aggregate project checks|PASS|project_validation.json|
|Repeat build six artifacts|PASS|Byte-identical, unchanged inputs in this environment|
|Nominal engineering geometry|PASS|71 assertions; independent7solids and21 zero-volume overlaps|
|Exported SVG/DXF coordinates|PASS|Agreement within0.000001mm|
|Actual FreeCAD CAM virtual study|PASS|131 native commands plus native voxel material removal; hypothetical simulation inputs only|
|PDF rendering|PASS|All60 pages rendered; contact-sheet/representative inspection documented|
|HTML + EPUB.js browser previews|PASS|1280/375px;12EPUB chapter render cases|
|Axe automated rules|PASS|0violations under tested WCAG2A/AA+2.1 rules in HTML at both sizes|
|Ace CLI|UNCOMPLETED|Managed Chromium file:// policy blocks its document loading|
|Word/LibreOffice visual opening|UNRUN|Package/OOXML opened; office application renderer unavailable|
|Current publisher/manufacturer/price checks|BLOCKED|Official sites returned proxy403; pending network settings application|
|Physical prototype/machining/kerf/adhesive/fixture tests|UNRUN|Explicit human test plan; no hardware access|
|Commercial release/human authorship/legal approval|BLOCKED|No genuine author contributions or review signoff recorded|

Passing automated rules is not proof of legal accessibility, safe manufacture, human authorship or publisher acceptance.
