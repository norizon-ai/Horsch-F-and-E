---
title: UR Script Vorlagen
space: IT
parent: Roboterprogrammierung
level: 1
---

# UR Script Vorlagen

## Einleitung
Diese Seite bietet eine Übersicht über die UR Script Vorlagen, die für die Programmierung von UR-Robotern innerhalb von TechMech Solutions GmbH verwendet werden. Die Vorlagen dienen als Basis für spezifische Anwendungen und erleichtern die schnelle Entwicklung von Roboterprogrammen in unterschiedlichen Branchen.

## Zielsetzung
Die UR Script Vorlagen sollen dazu beitragen, die Effizienz und Qualität der Roboterprogrammierung zu steigern. Sie bieten eine strukturierte Herangehensweise an häufige Aufgaben und ermöglichen eine einfache Anpassung an individuelle Anforderungen.

## Vorlagenübersicht

| Vorlage                  | Beschreibung                                      | Anwendungsbereich           |
|-------------------------|--------------------------------------------------|-----------------------------|
| **Basic_Movement.urs**  | Grundlegende Bewegungsbefehle für UR-Roboter     | Allgemeine Roboterbewegungen|
| **Pick_and_Place.urs**  | Vorlage für Pick-and-Place-Anwendungen           | Automobil-, Lebensmittelindustrie |
| **Quality_Check.urs**   | Programm zur Durchführung von Qualitätsprüfungen | Pharma- und Lebensmittelindustrie |
| **Conveyor_Control.urs** | Steuerung von Förderbändern in Automatisierungslösungen | Logistik und Fördertechnik  |

## 1. Basic_Movement.urs
Diese Vorlage enthält grundlegende Befehle zur Positionssteuerung des Roboters. Sie umfasst:

- **Bewegungsarten**: 
  - `movej` für Gelenkbewegungen
  - `movel` für lineare Bewegungen
- **Beispielkonfiguration**:
  ```plaintext
  movej([0, -1.57, 0, -1.57, 0, 0], a=1.0, v=0.5)
  movel([0.5, 0.5, 0.5, 0, 0, 0], a=0.5, v=0.1)
  ```

## 2. Pick_and_Place.urs
Diese Vorlage ist für Pick-and-Place-Prozesse optimiert und enthält:

- **Greifermodul**: Konfiguration für verschiedene Greifertypen
- **Beispielablauf**:
  ```plaintext
  set_tool(gripper)
  movej(pick_position, a=0.5, v=0.3)
  set_digital_out(0, True)  # Greifer schließen
  sleep(1)
  movej(place_position, a=0.5, v=0.3)
  set_digital_out(0, False)  # Greifer öffnen
  ```

## 3. Quality_Check.urs
Diese Vorlage ermöglicht die Durchführung von Qualitätsprüfungen und enthält:

- **Sensorintegration**: Anbindung an verschiedene Sensoren zur Datenerfassung
- **Beispielmessung**:
  ```plaintext
  set_tool(sensor_tool)
  movej(check_position, a=0.5, v=0.3)
  measurement = get_sensor_data()
  if measurement > threshold:
      set_digital_out(1, True)  # Alarm aktivieren
  ```

## 4. Conveyor_Control.urs
Diese Vorlage steuert die Fördertechnik und ermöglicht:

- **Synchronisation mit Robotern**: Koordinierung von Roboterbewegungen und Förderband
- **Beispielsteuerung**:
  ```plaintext
  set_digital_out(2, True)  # Förderband starten
  sleep(5)
  set_digital_out(2, False) # Förderband stoppen
  ```

## Fazit
Die UR Script Vorlagen bieten eine solide Grundlage für die Programmierung von UR-Robotern in verschiedenen industriellen Anwendungen. Durch die Verwendung dieser Vorlagen können Programmierer Zeit sparen und die Qualität der Roboteranwendungen erhöhen. Für detaillierte Anpassungen und spezifische Einsatzszenarien sind die Vorlagen leicht modifizierbar.