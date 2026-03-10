---
title: Performance Level Berechnung
space: CMP
parent: Sicherheitsnormen
level: 2
---

# Performance Level Berechnung

## Einleitung
Die Berechnung des Performance Levels (PL) ist ein entscheidender Schritt in der Sicherheitsbewertung von Automatisierungssystemen. Der Performance Level gibt an, wie zuverlässig ein Sicherheitsmechanismus funktioniert und wird gemäß den Vorgaben der Norm EN ISO 13849-1 ermittelt. Diese Norm beschreibt die Sicherheitsanforderungen und den Nachweis für Maschinensteuerungen.

## Grundlagen der Performance Level Berechnung
Der Performance Level wird auf einer Skala von PL a bis PL e bewertet, wobei PL e die höchste Sicherheitsstufe darstellt. Die Berechnung erfolgt auf Basis von drei Hauptfaktoren:

- **Sicherheitsanforderungsstufe (SRS)**: Definiert die erforderliche Sicherheitsfunktion.
- **Verfügbarkeit (MTTFd)**: Mean Time To Failure, beschreibt die durchschnittliche Betriebszeit bis zum ersten Ausfall.
- **Diagnosedeckungsgrad (DC)**: Prozentualer Anteil der Fehler, die durch Diagnosefunktionen erkannt werden.

## Berechnungsschritte
Die Berechnung des Performance Levels erfolgt in mehreren Schritten:

1. **Bestimmung der Sicherheitsanforderungsstufe (SRS)**
   - Identifikation der gefährlichen Situationen.
   - Bewertung der Risiken.

2. **Ermittlung der Verfügbarkeit (MTTFd)**
   - Ermittlung der MTTFd-Werte für alle sicherheitsrelevanten Komponenten.
   - Beispielwerte:
     | Komponente        | MTTFd (Jahre) |
     |-------------------|---------------|
     | Sicherheitsschalter| 20            |
     | Not-Aus-Taster     | 30            |
     | Sensor             | 15            |

3. **Berechnung des Diagnosedeckungsgrades (DC)**
   - Ermittlung der Diagnosefähigkeiten der verwendeten Komponenten.
   - Beispielwerte:
     | Komponente        | DC (%) |
     |-------------------|--------|
     | Sicherheitsschalter| 60     |
     | Not-Aus-Taster     | 90     |
     | Sensor             | 30     |

## Performance Level Bestimmung
Die endgültige Bestimmung des Performance Levels erfolgt durch die Kombination der ermittelten Werte:

- **PL a**: MTTFd < 1 Jahr
- **PL b**: 1 ≤ MTTFd < 10 Jahre
- **PL c**: 10 ≤ MTTFd < 100 Jahre und DC ≥ 60%
- **PL d**: 100 ≤ MTTFd < 1000 Jahre und DC ≥ 90%
- **PL e**: MTTFd ≥ 1000 Jahre und DC = 99%

### Beispielberechnung
Angenommen, wir haben die folgenden Werte für ein System:

- MTTFd (gesamt) = 15 Jahre
- DC (gesamt) = 70%

In diesem Fall würde das System als **PL c** eingestuft werden, da der MTTFd-Wert im Bereich von 10 bis 100 Jahren liegt und der DC über 60% liegt.

## Fazit
Die korrekte Berechnung des Performance Levels ist für die Sicherheit und Zuverlässigkeit von Automatisierungssystemen unerlässlich. Eine sorgfältige Analyse der sicherheitsrelevanten Komponenten und deren Eigenschaften ermöglicht es, die Anforderungen der EN ISO 13849-1 zu erfüllen und somit sichere Maschinen und Anlagen zu gewährleisten. Bei weiteren Fragen oder zur Unterstützung bei spezifischen Projekten steht das Team von TechMech Solutions GmbH jederzeit zur Verfügung.