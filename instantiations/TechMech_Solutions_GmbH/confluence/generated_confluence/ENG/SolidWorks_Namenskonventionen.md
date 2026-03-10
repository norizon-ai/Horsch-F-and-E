---
title: SolidWorks Namenskonventionen
space: ENG
parent: CAD-Richtlinien
level: 1
---

# SolidWorks Namenskonventionen

## Einleitung
Die Einhaltung von Namenskonventionen in SolidWorks ist entscheidend für die Organisation und Nachvollziehbarkeit von CAD-Daten im Rahmen der Entwicklungsprozesse bei TechMech Solutions GmbH. Diese Richtlinien helfen dabei, Missverständnisse und Verwirrungen zu vermeiden und gewährleisten eine effiziente Zusammenarbeit zwischen den Teams.

## Grundsätze der Namensgebung

1. **Eindeutigkeit**: Jeder Dateiname muss einzigartig sein, um Verwechslungen zu vermeiden.
2. **Klarheit**: Dateinamen sollten den Inhalt und die Funktion des Modells klar widerspiegeln.
3. **Konsistenz**: Einheitliche Benennungsstrukturen sollten über alle Projekte hinweg angewendet werden.

## Namensstruktur

Die Namenskonventionen für SolidWorks-Dateien setzen sich aus mehreren Komponenten zusammen:

| Komponente       | Beschreibung                                        | Beispiel                |
|------------------|----------------------------------------------------|-------------------------|
| Projektkürzel    | Abkürzung des Projektnamens                        | PRJ-AUT                 |
| Bauteiltyp       | Typ des Bauteils (z.B. Baugruppe, Einzelteil)     | ASSY, PART              |
| Funktionsbezeichnung | Kurze Beschreibung der Funktion                  | Förderband, Roboterarm  |
| Versionsnummer    | Versionsangabe in Form von V1, V2, etc.           | V1                      |

**Beispiel eines vollständigen Dateinamens:**
`PRJ-AUT_ASSY_Foerderband_V1.SLDPRT`

## Dateitypen und deren Namenskonventionen

### Einzelteile (SLDPRT)

- **Format**: `Projektkürzel_PART_Funktionsbezeichnung_Versionsnummer`
- **Beispiel**: `PRJ-LFB_PART_Roboterarm_V2.SLDPRT`

### Baugruppen (SLDASM)

- **Format**: `Projektkürzel_ASSY_Funktionsbezeichnung_Versionsnummer`
- **Beispiel**: `PRJ-LFB_ASSY_Foerderband_V1.SLDASM`

### Zeichnungen (SLDDRW)

- **Format**: `Projektkürzel_DWG_Funktionsbezeichnung_Versionsnummer`
- **Beispiel**: `PRJ-LFB_DWG_Roboterarm_V1.SLDDRW`

## Zusätzliche Hinweise

- **Verwendung von Unterstrichen**: Unterstriche (_) sind als Trennzeichen zwischen den Komponenten zu verwenden, um die Lesbarkeit zu erhöhen.
- **Sonderzeichen**: Vermeiden Sie die Verwendung von Sonderzeichen (z.B. / \ : * ? " < > |), da diese Probleme beim Speichern und Verwalten von Dateien verursachen können.
- **Dokumentation**: Änderungen an Dateinamen müssen in den Versionskontrollsystemen dokumentiert werden, um die Rückverfolgbarkeit sicherzustellen.

## Fazit

Die Einhaltung dieser Namenskonventionen für SolidWorks-Dateien trägt entscheidend zur Effizienz und Klarheit im Konstruktionsprozess bei TechMech Solutions GmbH bei. Alle Mitarbeiter sind angehalten, diese Richtlinien strikt zu befolgen, um eine reibungslose Zusammenarbeit und einen effektiven Datenaustausch zu gewährleisten.