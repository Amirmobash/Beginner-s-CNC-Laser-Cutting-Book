# CNC-Fräsen und Laserschneiden für absolute Anfänger

Deutscher praktischer Buchentwurf für Erwachsene ohne CAD-/CAM-Erfahrung. Zwei getrennte Lernwege führen zum 120 × 80 mm CNC-Namensschild und zum 100 × 60 mm Laserschild. **Arbeitsmanuskript: NICHT ZUR VERÖFFENTLICHUNG FREIGEGEBEN.**

## Bauen und prüfen

Voraussetzungen: Python 3.12, Pandoc 3.1.11.1, Inkscape 1.4, FreeCAD 1.0.0 für das native CAD-Modell, Java für EPUBCheck. Linux-Buildumgebung; die Windows-Anleitungen benötigen einen gesonderten Praxistest.

```sh
python -m venv /workspace/book-venv
/workspace/book-venv/bin/pip install -r requirements.txt
/workspace/book-venv/bin/python scripts/build_book.py
/workspace/book-venv/bin/python scripts/validate_assets.py
/workspace/book-venv/bin/python scripts/validate_epub.py
```

Die EPUB-, DOCX- und PDF-Dateien stehen unter `output/`. `manuscript/` enthält die editierbaren Kapitel, `figures/` SVG und PNG, `projects/` die separaten Übungsdateien. `research/` dokumentiert Quellen, Aussagen und Abrufbelege; `publishing/` enthält die Autoren- und Verlagsprüfpunkte. Status und tatsächlich ausgeführte Prüfungen: `PROJECT_STATE.md` und `quality/`.

Alle Maschinenprogramme sind ausschließlich Lehrbeispiele. Es gibt keine universell freigegebenen Fertigungsparameter. Keine Maschine wurde in dieser Cloud betrieben. Keine praktische Freigabe durch Fachpersonal ist erfolgt.

## Recherche und Rechte

Primärquellen werden mit Abrufdatum, Aussage, Kapitelzuordnung und Beleg-Hash erfasst. Ein erfolgreicher Abruf bedeutet noch keine fachliche Freigabe. Nicht erreichbare Quellen werden als solche geführt. Quellcode aus Entwicklungszweigen beweist keine identischen Menüs in installierten Versionen.

Die Texte und Diagramme wurden KI-gestützt erstellt. Menschliche technische Prüfung, eigenständige schöpferische Autorenarbeit, echte Werkstattfotos, Rechteprüfung und Klärung der aktuellen BoD-Bedingungen bleiben Voraussetzung einer kommerziellen Ausgabe. Eine Korrekturlesung allein begründet keine BoD-Eignung. Keine ISBN, Identität oder Genehmigung wird erfunden. Öffentliche GitHub-Dateien sind herunterladbar; öffentliche Verfügbarkeit ist keine pauschale Lizenz für Marken oder eingebundene Fremdquellen. Fremde Belege behalten ihre jeweiligen Lizenzen.
