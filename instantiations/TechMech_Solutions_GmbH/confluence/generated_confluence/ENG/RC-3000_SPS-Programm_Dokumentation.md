---
title: RC-3000 SPS-Programm Dokumentation
space: ENG
parent: Roboterzellen
level: 3
---

# RC-3000 SPS-Programm Dokumentation

## Einleitung

Die RC-3000 Roboterzelle ist eine hochmoderne Automatisierungslösung, die für die Verarbeitung und Handhabung von Bauteilen in verschiedenen Industrien konzipiert wurde. Diese Dokumentation beschreibt die Spezifikationen, das SPS-Programm sowie die Konfiguration der RC-3000 Roboterzelle.

## Technische Spezifikationen

| Spezifikation                | Wert                      |
|------------------------------|---------------------------|
| Roboter-Typ                  | 6-Achsen-Knickarmroboter  |
| Traglast                     | 15 kg                     |
| Reichweite                    | 1.200 mm                  |
| Wiederholgenauigkeit         | ± 0,05 mm                 |
| SPS-Typ                      | Siemens S7-1200           |
| Kommunikationsprotokoll      | Profinet                  |
| Netzspannung                  | 400 V AC                  |
| Umgebungstemperatur          | 0 °C bis 45 °C           |

## SPS-Programmübersicht

Das SPS-Programm der RC-3000 Roboterzelle ist in mehrere Module unterteilt, die jeweils spezifische Funktionen und Abläufe steuern. Die Hauptmodule sind:

1. **Initialisierung**
   - Überprüfung der Systemparameter
   - Kalibrierung des Roboters
   - Start der Kommunikationsschnittstellen

2. **Bauteil-Erkennung**
   - Verwendung von Sensoren zur Identifikation der Bauteile
   - Übermittlung von Bauteilparametern an das Hauptprogramm

3. **Greifprozess**
   - Ansteuerung des Greifmechanismus
   - Durchführung von Greiftests zur Sicherstellung der Bauteilsicherung

4. **Transport und Handhabung**
   - Steuerung der Fördertechnik
   - Koordination zwischen Roboter und Förderband

5. **Qualitätskontrolle**
   - Integrierte Kamerasysteme zur visuellen Inspektion
   - Erfassung und Protokollierung von Qualitätsdaten

## Beispielkonfiguration

### Initialisierung

```structured-text
PROGRAM Initialisierung
VAR
    Fehlercode : INT;
END_VAR

Fehlercode := SystemParameterÜberprüfung();
IF Fehlercode <> 0 THEN
    Fehlerbehandlung(Fehlercode);
END_IF;

KalibrierungRoboters();
```

### Greifprozess

```structured-text
PROGRAM Greifprozess
VAR
    BauteilErkannt : BOOL;
END_VAR

BauteilErkannt := SensorBauteilErkennung();
IF BauteilErkannt THEN
    AnsteuerungGreifer();
ELSE
    FehlerBauteilNichtGefunden();
END_IF;
```

## Sicherheitshinweise

- Alle Wartungsarbeiten an der Roboterzelle dürfen nur von qualifiziertem Personal durchgeführt werden.
- Die Sicherheitsvorkehrungen gemäß der Norm EN ISO 13849-1 sind einzuhalten.
- Vor der Inbetriebnahme ist eine umfassende Risikoanalyse durchzuführen.

## Fazit

Die RC-3000 Roboterzelle bietet durch ihre modulare SPS-Programmierung und hohe Flexibilität eine optimale Lösung für automatisierte Produktionsprozesse. Die detaillierte Dokumentation des SPS-Programms stellt sicher, dass alle Funktionen effizient und sicher implementiert werden können. Bei weiteren Fragen oder speziellen Anforderungen wenden Sie sich bitte an unser Technikteam.