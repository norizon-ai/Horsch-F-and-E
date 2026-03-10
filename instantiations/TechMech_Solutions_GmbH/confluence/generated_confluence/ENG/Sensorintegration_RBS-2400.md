---
title: Sensorintegration RBS-2400
space: ENG
parent: Fördertechnik
level: 3
---

# Sensorintegration RBS-2400

## Einleitung
Die Sensorintegration der RBS-2400 Roboterzelle stellt einen entscheidenden Schritt zur Optimierung der Fördertechnik dar. Diese Seite beschreibt die technischen Details, die Spezifikationen und die Implementierung der Sensoren in das System.

## Technische Spezifikationen

| Spezifikation              | Wert                     |
|---------------------------|-------------------------|
| Sensortyp                  | Infrarotsensor          |
| Erfassungsbereich          | 0,1 m - 5 m             |
| Reaktionszeit              | < 5 ms                  |
| Spannungsversorgung         | 24 V DC                 |
| Ausgangssignal             | PNP/NPN (wahlweise)     |
| IP-Schutzklasse            | IP65                    |

## Sensorarchitektur
Die Sensorintegration der RBS-2400 besteht aus mehreren Infrarotsensoren, die strategisch an den Förderstrecken positioniert sind. Diese Sensoren sind dafür verantwortlich, die Position und den Zustand der transportierten Objekte zu überwachen. Die wichtigsten Komponenten sind:

- **Einlasssensor**: Erfasst das Eintreffen eines Objekts an der Förderstrecke.
- **Auslasssensor**: Überwacht die Beendigung des Förderprozesses und sorgt für die korrekte Entladung.
- **Zwischenlagersensor**: Erfasst Objekte, die temporär auf der Förderstrecke gestoppt sind.

## Integration in das Steuersystem
Die Sensoren sind über eine zentrale Steuerungseinheit an die RBS-2400 angebunden. Die Integration erfolgt über einen CAN-Bus, wodurch eine hohe Datenübertragungsrate und Zuverlässigkeit gewährleistet sind. Folgende Schritte sind für die Integration erforderlich:

1. **Verkabelung**: Verbindung der Sensoren mit der Steuerungseinheit unter Berücksichtigung der elektrischen Standards.
2. **Konfiguration**: Anpassen der Sensoreinstellungen über die Software-Schnittstelle.
3. **Kalibrierung**: Durchführung von Tests zur Sicherstellung der korrekten Funktionalität.

## Beispielkonfiguration
Um eine präzise Erfassung zu gewährleisten, werden die Sensoren wie folgt konfiguriert:

- **Einlasssensor**: Erfassungsdistanz 0,5 m, Reaktionszeit 3 ms
- **Auslasssensor**: Erfassungsdistanz 0,3 m, Reaktionszeit 4 ms
- **Zwischenlagersensor**: Erfassungsdistanz 0,2 m, Reaktionszeit 2 ms

## Testprozeduren
Um die Funktionalität der Sensorintegration zu überprüfen, sind folgende Testprozeduren durchzuführen:

- **Funktionsprüfung**: Sicherstellen, dass jeder Sensor korrekt auf Objekte reagiert.
- **Störfallanalyse**: Simulation von Störungen (z. B. Blockierung) und Überprüfung der Reaktion des Systems.
- **Langzeittests**: Überwachung der Sensorleistung über einen Zeitraum von 72 Stunden unter Betriebsbedingungen.

## Fazit
Die Sensorintegration der RBS-2400 stellt eine essentielle Komponente dar, um die Effizienz und Zuverlässigkeit der Fördertechnik zu garantieren. Durch präzise Messwerte und eine robuste Architektur wird die Qualität der Prozesse in den unterschiedlichsten Branchen sichergestellt.