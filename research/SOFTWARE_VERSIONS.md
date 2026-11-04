# Software versions and verification

| Component | Version / evidence | Executed in this environment | Windows tutorial status |
|---|---|---|---|
| Inkscape | 1.4 (e7c3feb100,2024-10-09); Debian1.4-6 | Binary queried by root; project exports separately reported | Exact Windows installer and dialogs not tested |
| FreeCAD | Debian1.0.0+dfsg-8+deb13u3 | Installed package queried; geometry/native generation separately reported | Exact Windows installer and CAM dialogs not tested |
| Pandoc | 3.1.11.1 | Version queried; builds in quality reports | Build tool only |
| Python | 3.12.14 | Local build environment | Build tool only |
| LightBurn | Not installed; current version unverified | No | No exact-version screenshots or menu certification |
| GRBL | Reference1.1 source documented | No hardware/firmware execution | Teaching dialect only |
| OpenBuilds CAM/CONTROL | Current release not installed | Documentation reviewed S21/S22 | Candidate, not selected/validated |
| UGS | README offers stable2.1.27; not installed | Documentation reviewed S23 | Candidate, not selected/validated |
| LaserGRBL | Version not installed | Documentation reviewed S11 | Candidate, SVG import documented experimental |
| Fusion | No version installed | Official site blocked/not verified | Not selected |

Development-branch sources are not treated as proof of installed-version UI behavior. The committed requirements.txt pins actual build dependencies; version-specific launch tests are reported by the build owner.
