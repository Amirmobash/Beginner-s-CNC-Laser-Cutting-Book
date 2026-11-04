# Technical evidence and limits

The book uses one gift-box project. Laser-cut panels and spindle-engraved removable lid are separate manufacturing operations. Engrave the flat lid before final completion: clamping a complete thin box is a different, unsupported fixture problem.

GRBL1.1 reference source is a teaching dialect, not confirmation that a vendor controller uses unmodified GRBL. G20/G21, G90/G91, G94, G0/G1, M3/M4/M5 and the work coordinate systems are grounded in S01/S03. S values and M4 differ between spindle and laser contexts. Firmware support for a door input is not proof of a safety-rated interlock.

FreeCAD CAM source from main is newer than locally installed1.0.0. It demonstrates feature concepts only. Menu names, exact operation behavior and postprocessor output must be checked against installed files and real setup. No feeds, spindle speeds, laser power, passes or engrave depths are released for production.

S20 illustrates why simulation cannot establish real fixture clearance or machining quality. Digital box geometry checks demonstrate only the assertions named by engineering/validation. They do not measure plywood thickness, kerf, bond strength or warp.

Material purchase must specify laser suitability, adhesive/coating identity, batch and actual thickness. Unknown plastics, PVC and vinyl are excluded. Nominal3mm is a purchasing category; measured thickness determines joint design. No supplier quote or physical fit is verified in this run.

External safety guidance and manufacturer manuals were not retrievable under the current network policy; safety text is conservative draft guidance requiring qualified review, not certified operating instructions.
