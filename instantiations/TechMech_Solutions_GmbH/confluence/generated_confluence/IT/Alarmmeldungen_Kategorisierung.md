---
title: Alarmmeldungen Kategorisierung
space: IT
parent: Visualisierung (HMI)
level: 1
---

# Alarmmeldungen Kategorisierung

## Einleitung
Die Kategorisierung von Alarmmeldungen ist ein wesentlicher Bestandteil der Überwachung und Steuerung von Automatisierungssystemen. Eine präzise Klassifizierung ermöglicht eine schnellere Reaktion auf kritische Ereignisse und verbessert die Effizienz der Wartungsmaßnahmen. In diesem Dokument werden die verschiedenen Kategorien von Alarmmeldungen sowie deren spezifische Eigenschaften und Handhabung beschrieben.

## Kategorisierungen

Die Alarmmeldungen werden in drei Hauptkategorien unterteilt:

1. **Kritische Alarme**
   - **Beschreibung**: Alarmmeldungen, die sofortige Maßnahmen erfordern, um einen Ausfall oder eine Gefährdung zu verhindern.
   - **Beispiele**:
     - Not-Aus aktiviert
     - Sicherheitsrelevante Systemfehler
   - **Reaktionszeit**: Sofortige Intervention erforderlich

2. **Wichtige Alarme**
   - **Beschreibung**: Alarme, die eine signifikante Störung anzeigen, jedoch nicht sofortige Maßnahmen erfordern.
   - **Beispiele**:
     - Übertemperatur in einem Prozess
     - Abweichungen von Sollwerten in der Produktionslinie
   - **Reaktionszeit**: Innerhalb von 1 Stunde

3. **Informative Alarme**
   - **Beschreibung**: Alarme, die zur Information des Bedienpersonals dienen und keine unmittelbaren Maßnahmen erfordern.
   - **Beispiele**:
     - Wartungserinnerungen
     - Statusänderungen (z. B. Wechsel des Betriebsmodus)
   - **Reaktionszeit**: Innerhalb von 24 Stunden

## Alarmmeldeprozess

Die Alarmmeldungen werden in der Visualisierung (HMI) wie folgt dargestellt:

| Alarmkategorie      | Farbe          | Symbol      | Priorität  |
|---------------------|----------------|-------------|------------|
| Kritische Alarme    | Rot            | ![Notaus](link)      | Hoch       |
| Wichtige Alarme     | Orange         | ![Warnung](link)     | Mittel     |
| Informative Alarme   | Blau           | ![Info](link)        | Niedrig    |

## Technische Spezifikationen

Die Alarmmeldungen werden über das zentrale Steuerungssystem (SPS) generiert und über das HMI visualisiert. Die Konfiguration der Alarmmeldungen erfolgt in der Softwareumgebung gemäß den folgenden Spezifikationen:

- **SPS-Typ**: Siemens S7-1500
- **HMI-Typ**: Siemens WinCC
- **Kommunikationsprotokoll**: PROFINET
- **Ereignisprotokollierung**: Alle Alarme werden in einer Datenbank protokolliert, einschließlich Zeitstempel und Schweregrad.

## Beispiel für Alarmkonfiguration

Hier ein Beispiel zur Konfiguration eines wichtigen Alarms:

- **Alarmname**: Übertemperatur Zylinder
- **Schwellwert**: 85°C
- **Aktion bei Alarm**: 
  - Akustisches Signal
  - Visuelle Alarmmeldung im HMI
  - Benachrichtigung an Wartungsteam per E-Mail

## Fazit

Die ordnungsgemäße Kategorisierung und Handhabung von Alarmmeldungen ist entscheidend für die Sicherheit und Effizienz unserer Automatisierungssysteme. Durch die klare Strukturierung und Dokumentation der Alarmprozesse stellen wir sicher, dass alle Mitarbeiter die notwendigen Informationen zur Verfügung haben, um effektiv auf potenzielle Störungen zu reagieren.