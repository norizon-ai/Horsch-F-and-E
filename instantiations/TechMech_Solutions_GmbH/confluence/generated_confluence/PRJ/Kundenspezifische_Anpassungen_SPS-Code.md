---
title: Kundenspezifische Anpassungen SPS-Code
space: PRJ
parent: PRJ-2024-052 - PlastTech Spritzguss Automation
level: 2
---

# Kundenspezifische Anpassungen SPS-Code

## Einleitung
Diese Seite dokumentiert die spezifischen Anpassungen des SPS-Codes für das Projekt PRJ-2024-052 – PlastTech Spritzguss Automation. Ziel dieser Anpassungen ist es, die Funktionalitäten der Roboterzellen und Fördertechnik optimal an die Anforderungen des Kunden anzupassen.

## Anforderungen
Die Anpassungen an dem SPS-Code wurden in Übereinstimmung mit den folgenden Anforderungen des Kunden durchgeführt:

- **Integration zusätzlicher Sensoren** zur Überwachung des Spritzgussprozesses
- **Erweiterung der Steuerungslogik** für unterschiedliche Kunststoffmaterialien
- **Optimierung der Fehlerdiagnose** zur schnellen Identifizierung von Störungen

## Technische Details

### 1. Erweiterte Sensorintegration
Für die Überwachung der Temperatur und des Drucks im Spritzgussprozess wurden die folgenden Sensoren integriert:

| Sensortyp         | Modell          | Messbereich       | Schnittstelle     |
|-------------------|----------------|-------------------|-------------------|
| Temperatursensor  | TMP-500        | 0°C bis 300°C     | Analog 4-20 mA     |
| Drucksensor       | PRT-200        | 0 bis 200 bar     | Digital RS485       |

Der SPS-Code wurde entsprechend angepasst, um die Eingangssignale dieser Sensoren zu verarbeiten und in den Produktionsprozess zu integrieren.

### 2. Steuerungslogik für Kunststoffmaterialien
Um die Steuerung an verschiedene Kunststoffmaterialien anzupassen, wurde eine Parameterisierung des SPS-Codes implementiert. Folgende Parameter wurden definiert:

- **Materialtyp:** Polypropylen (PP), Polyethylen (PE), Polyvinylchlorid (PVC)
- **Temperaturprofile:** Angepasste Heiz- und Kühlzeiten je nach Materialtyp
- **Druckprofile:** Dynamische Anpassungen der Einspritzdrücke

Die Programmierung wurde modular gestaltet, um zukünftige Erweiterungen zu erleichtern.

### 3. Fehlerdiagnose und Monitoring
Um die Effizienz der Fehlerdiagnose zu steigern, umfasst der SPS-Code die folgenden Funktionen:

- **Echtzeitüberwachung** aller relevanten Prozessparameter
- **Alarmierungssystem** für kritische Zustände (z.B. Übertemperatur, Überdruck)
- **Protokollierung von Fehlern** in einer Datenbank für spätere Analysen

Die Alarmgrenzen wurden wie folgt definiert:

| Parameter            | Grenzwert       | Maßnahme bei Überschreitung       |
|----------------------|----------------|-----------------------------------|
| Temperatur (°C)      | > 280°C        | Sofortige Abschaltung des Geräts   |
| Druck (bar)          | > 180 bar      | Alarmierung und Druckentlastung    |

## Fazit
Die kundenspezifischen Anpassungen des SPS-Codes für die Spritzgussautomation bieten eine robuste und flexible Lösung, die den spezifischen Anforderungen des Kunden gerecht wird. Durch die Integration erweiterter Sensoren, eine angepasste Steuerungslogik und ein effektives Fehlerdiagnosesystem wird die Effizienz und Sicherheit des Prozesses maßgeblich erhöht. 

Für weitere Informationen oder Unterstützung kontaktieren Sie bitte das Engineering-Team.