---
title: TwinCAT Projektstruktur
space: IT
parent: SPS-Programmierung
level: 2
---

# TwinCAT Projektstruktur

## Einleitung
Die TwinCAT Projektstruktur bildet das Fundament für die Entwicklung und Implementierung von Automatisierungslösungen in der SPS-Programmierung. Diese Seite beschreibt die grundlegenden Komponenten und die Organisation eines typischen TwinCAT-Projekts bei TechMech Solutions GmbH.

## Projektübersicht
Ein TwinCAT-Projekt wird in mehrere Hauptkomponenten unterteilt, die in der folgenden Tabelle dargestellt sind:

| Komponente            | Beschreibung                                                  |
|----------------------|--------------------------------------------------------------|
| **Projektdatei**     | Enthält die gesamte Projektkonfiguration und -einstellungen. |
| **PLC-Programme**    | Beinhaltet alle SPS-Programme, die in Structured Text (ST) oder Ladder Diagram (LD) implementiert sind. |
| **Visualisierungen**  | GUI-Elemente für die Benutzeroberfläche, die mit der TwinCAT HMI erstellt wurden. |
| **Bibliotheken**      | Externe und interne Bibliotheken, die Funktionen und Datentypen bereitstellen. |
| **Hardware-Konfiguration** | Definiert die verwendeten Hardwarekomponenten, wie I/O-Module und Steuerungen. |

## Projektstruktur im Detail
Die Struktur eines typischen TwinCAT-Projekts kann wie folgt aussehen:

1. **Projektdatei (.tsproj)**
   - Die zentrale Datei, die alle Projektinformationen speichert.
   - Beispiel: `Automatisierungslösung.tsproj`

2. **PLC-Programme**
   - Jedes Programm wird in einem eigenen Unterordner organisiert.
   - Beispiel: 
     - `MainProgram`
     - `SafetyControl`
     - `DataLogging`

3. **Visualisierungen**
   - Erstellen von Visualisierungselementen zur Überwachung und Steuerung.
   - Beispiel: 
     - `MainScreen`
     - `SettingsPage`

4. **Bibliotheken**
   - Verwendung von Bibliotheken zur Wiederverwendbarkeit von Code.
   - Beispiel: 
     - `TechMechLib`
     - `SafetyFunctions`

5. **Hardware-Konfiguration**
   - Konfiguration der verwendeten Hardware über TwinCAT System Manager.
   - Beispiel:
     - Steuerung: `Beckhoff CX5140`
     - I/O-Module: 
       - `EL1809` (8-Kanal Digitalausgang)
       - `EL1008` (8-Kanal Digitaleingang)

## Beispielkonfiguration
Hierbei handelt es sich um eine vereinfachte Konfiguration eines TwinCAT-Projekts für eine Roboterzelle:

| Komponente        | Detail                                  |
|-------------------|-----------------------------------------|
| Steuerung         | Beckhoff CX9020                         |
| I/O-Module        | EL3102 (2-Kanal Analog Input)          |
| Visualisierung     | `RobotControl.hmi`                     |
| PLC-Programm      | `RobotControl.pd`                      |
| Bibliothek        | `TechMechRobotLib`                     |

## Fazit
Die strukturierte Organisation der TwinCAT-Projekte bei TechMech Solutions GmbH ermöglicht eine effiziente Entwicklung und Wartung von Automatisierungslösungen. Eine klare Trennung zwischen Programmcode, Hardware-Konfiguration und Benutzeroberflächen trägt zur Verbesserung der Transparenz und Nachvollziehbarkeit bei. Bei weiteren Fragen zur Projektstruktur oder zur Nutzung von TwinCAT wenden Sie sich bitte an das technische Team.