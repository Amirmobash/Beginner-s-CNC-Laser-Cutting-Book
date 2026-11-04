# Software comparison

Reviewed2026-11-04. This compares functional roles first. A screenshot-capable design program is not a CNC controller. A tool's zero license price is not a zero-cost safe machine workflow.

| Candidate | Role / formats evidenced | License and commercial-use evidence | Windows / German support | Practical limits |
|---|---|---|---|---|
| Inkscape1.4 | Vector design; native SVG (S26); local binary available | FOSS, source mostly GPL2+, binaries GPL3+ (S31); original artwork not automatically GPL | Windows advertised S26; installed Linux version1.4; German Windows dialogs not tested | No released machine control or CNC CAM assumed |
| FreeCAD1.0.0 | Parametric CAD; CAM job, engraving and GRBL post in project sources S06/S08–10/S19 | LGPL root notice S07; mixed components require review; no subscription for standard application | Windows advertised S06; Linux installed; German Windows CAM not tested | More concepts than a 2D-only tool; postprocessor must match actual controller |
| OpenBuilds CAM | DXF/SVG/bitmap/Gerber→G-code (S21) | Repository public; exact current hosted-service/commercial terms not reviewed | Browser-based description; Windows browser plausibility is not launch validation; German support unknown | Hosted service unavailable for live test; laser/enclosed machine support not established |
| OpenBuilds CONTROL | GRBL sender/host S22; not a full parametric CAD | Exact current license terms not inspected | Windows/Linux/Mac build evidence S22; German tutorial coverage unknown | Valid GRBL connection is not enclosure or laser-system approval |
| LaserGRBL | Windows laser sender/preparer S11 | Free/open-source project description; exact release license audit pending | Windows expressly documented; German localization not tested | SVG import marked experimental; minimal Z control; not main CNC CAM |
| LightBurn | Laser preparation/control; archived SVG/DXF import and Line/Fill docs S24/S27/S28 | Commercial application; current German/euro prices, tax and package terms unverified. Archived $40/$80 pricing S30 deliberately excluded | Current supported OS/version and German interface require official current docs | Not installed; exact laser-controller support and license selection unresolved |
| Autodesk Fusion | CAD/CAM candidate | Current personal-use eligibility, commercial-use restrictions and euro subscription prices unverified | Current Windows support/version and German tutorials not inspected | Personal use must not be assumed suitable for commercial projects; not selected |
| Universal Gcode Sender | Cross-platform Java sender; GRBL/TinyG/g2core/Smoothieware S23 | Public open-source project; exact license notice not independently audited | Windows64 stable download listed S23; German beginner coverage unknown | A sender does not replace CAD, CAM, a machine-specific postprocessor or safety review |

## Weighted comparison

Required weights: learning25%, tutorials20%, cost20%, hardware15%, screenshot reproducibility10%, maintenance10%. Scores1–5 are editorial estimates constrained by the evidence. **U means unknown and contributes a range1–5, never a fabricated midpoint.** Hardware means the exact intended system, which has not been selected and verified; all hardware scores are therefore U. Tutorial availability remains U because no comprehensive or German-language tutorial audit was possible. Installed screenshots are potential reproducibility, not a claim screenshots already exist.

| Candidate | Learn25% | Tutorials20% | Cost20% | Hardware15% | Capture10% | Maintain10% | Weighted possible range /5 |
|---|---:|---:|---:|---:|---:|---:|---:|
| Inkscape | 4 | U | 5 | U | 5 | 4 | 3.25–4.65 |
| FreeCAD | 2 | U | 5 | U | 5 | 4 | 2.75–4.15 |
| OpenBuilds CAM | 3 | U | U | U | U | U | 1.50–4.50 |
| OpenBuilds CONTROL | 3 | U | U | U | U | U | 1.50–4.50 |
| LaserGRBL | 3 | U | 5 | U | U | 3 | 2.50–4.30 |
| LightBurn | 4 | U | U | U | U | U | 1.75–4.75 |
| Fusion | 2 | U | U | U | U | U | 1.25–4.25 |
| UGS | 3 | U | 5 | U | U | 4 | 2.60–4.40 |

Calculation: sum(weight×score), e.g. Inkscape fixed contribution2.90 plus unknown0.35–1.75 =3.25–4.65. Learning scores express project-specific judgment (2D panel drawing versus parametric CAM), not measured user-study results. Maintenance scores express available open project/source access, not guarantees of future service. The broad overlapping ranges prohibit a definitive market-wide winner.

**Result:** retain the locally reproducible Inkscape+FreeCAD authoring core. Use one provisional laser handoff to LightBurn for its separately documented vector/operation concepts, conditional on exact hardware/current-version verification. Do not replace it with an untested OpenBuilds combination solely to reduce application count. An approved manufacturer sender remains a hardware-dependent prerequisite rather than a third speculative universal tool.
