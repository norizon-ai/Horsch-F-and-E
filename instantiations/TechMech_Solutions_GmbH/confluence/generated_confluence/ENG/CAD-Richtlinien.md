---
title: CAD-Richtlinien
space: ENG
parent: ENGINEERING - Home
level: 1
---

# CAD-Richtlinien

## Einleitung
Die vorliegenden CAD-Richtlinien dienen als Leitfaden für die Erstellung, Bearbeitung und Verwaltung von CAD-Daten in der TechMech Solutions GmbH. Diese Richtlinien sollen sicherstellen, dass alle technischen Zeichnungen und Modelle konsistent, genau und für alle Abteilungen verständlich sind.

## Allgemeine Anforderungen
- **Software**: Alle CAD-Modelle sind mit der aktuellen Version von AutoCAD und SolidWorks zu erstellen.
- **Dateiformat**: Die bevorzugten Dateiformate sind .dwg für 2D-Zeichnungen und .sldprt für 3D-Modelle.
- **Einheitensystem**: In allen Zeichnungen sind die Maße in Millimetern (mm) anzugeben.

## Zeichnungselemente
### Layerstruktur
Die Layerstruktur ist wie folgt zu organisieren:

| Layername         | Beschreibung                          |
|-------------------|---------------------------------------|
| 0_Geometrie       | Grundlegende Geometrie                |
| 1_Bemaßung        | Maße und Toleranzen                   |
| 2_Beschriftung    | Anmerkungen und Beschriftungen        |
| 3_Elektro         | Elektroinstallation und Verdrahtung   |
| 4_Hydraulik       | Hydraulische Komponenten               |

### Bemaßung
- Alle Maße müssen in Millimeter angegeben und mit einem klaren Bezugspunkt versehen sein.
- Toleranzen sind nach ISO 2768-1 (Allgemeintoleranzen) anzugeben.

### Beschriftungen
- Schriftart: Arial
- Schriftgröße: 2,5 mm für Hauptbeschriftungen, 1,5 mm für Nebenschrift
- Farbe: Schwarz für alle Beschriftungen

## Modellierung
### 3D-Modellierung
- Alle 3D-Modelle sind nach den Prinzipien des parametrischen Modellierens zu erstellen.
- Vermeiden Sie unnötige Details, die die Performance negativ beeinflussen könnten.
- Stellen Sie sicher, dass alle Teile mit einem eindeutigen Identifikationscode (z.B. TM-XXXX) benannt sind.

### Baugruppen
- Baugruppen müssen in einem separaten Dateiordner gespeichert werden, benannt nach dem Hauptkomponenten-ID.
- Verwenden Sie Standard-Vorlagen für die Montagezeichnungen, um Konsistenz zu gewährleisten.

## Dokumentation
Jede CAD-Zeichnung muss die folgenden Dokumentationsanforderungen erfüllen:
- **Titelblock**: Enthält Projektnamen, Erstellungsdatum, Ersteller und Revision.
- **Änderungshistorie**: Eine Tabelle zur Nachverfolgung aller Änderungen am Dokument.

### Beispiel für eine Änderungshistorie

| Änderungsnummer | Datum       | Beschreibung                  | Verantwortlicher |
|------------------|-------------|-------------------------------|------------------|
| 1                | 2023-01-15  | Erstellt                      | Max Mustermann    |
| 2                | 2023-03-10  | Maßänderung an Bauteil A     | Anna Beispiel     |

## Schlussfolgerung
Die Einhaltung dieser CAD-Richtlinien ist entscheidend für die Qualität und Effizienz unserer Projekte. Bei Fragen oder Unsicherheiten wenden Sie sich bitte an den zuständigen CAD-Administrator.