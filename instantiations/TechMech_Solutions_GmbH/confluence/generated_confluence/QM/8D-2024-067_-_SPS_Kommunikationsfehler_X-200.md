---
title: 8D-2024-067 - SPS Kommunikationsfehler X-200
space: QM
parent: 8D-Reports und Reklamationen
level: 1
---

# 8D-2024-067 - SPS Kommunikationsfehler X-200

## 1. Problemstellung
Am 15. März 2024 wurde ein Kommunikationsfehler zwischen der SPS (Speicherprogrammierbare Steuerung) und dem X-200 Roboter festgestellt. Der Fehler trat während des Produktionsprozesses in der Automobilindustrie auf und führte zu einem Produktionsstillstand von ca. 4 Stunden.

## 2. Fehlerbeschreibung
Der SPS Kommunikationsfehler äußerte sich durch folgende Symptome:
- Fehlermeldung auf dem HMI (Human-Machine Interface): „Kommunikationsfehler zu X-200“
- Unregelmäßige Robotervorfahrt und sporadische Stopps
- Datenübertragungsrate zwischen SPS und Roboter lag bei 50% der Norm

## 3. Ursachenanalyse
Nach einer ersten Analyse der Systemprotokolle und der Hardwarekonfiguration wurden folgende potenzielle Ursachen identifiziert:

| Ursache                          | Beschreibung                                            |
|----------------------------------|--------------------------------------------------------|
| Kabelverbindung                   | Überprüfung der Kabelverbindungen zwischen SPS und X-200 ergab lose Kontakte. |
| Softwarekonfiguration             | Unstimmigkeiten in der SPS-Softwareversion (V1.2.3) im Vergleich zur Roboterfirmware (V2.1.0). |
| Umgebungsfaktoren                | Hohe elektromagnetische Störungen durch benachbarte Maschinen. |

## 4. Sofortmaßnahmen
Um die Auswirkungen des Fehlers zu minimieren, wurden folgende Sofortmaßnahmen ergriffen:
- Überprüfung und Neuverbindung aller Kabelverbindungen zwischen SPS und X-200.
- Neustart der SPS und des Roboters zur Rücksetzung der Kommunikationsprotokolle.
- Durchführung einer Störungsmessung zur Analyse der elektromagnetischen Felder.

## 5. Langfristige Maßnahmen
Zur Vermeidung zukünftiger Kommunikationsprobleme sind folgende Maßnahmen geplant:
- Austausch von Kabeln durch geschirmte Varianten zur Reduzierung von Störungen.
- Upgrade der SPS-Software auf die neueste Version (V1.3.0) zur Verbesserung der Kommunikationsprotokolle.
- Installation eines zusätzlichen EMV-Filters an der SPS-Stromversorgung.

## 6. Verifizierung der Maßnahmen
Die Implementierung der oben genannten Maßnahmen wird durch folgende Schritte verifiziert:
- Durchführung von Funktionstests der SPS und des X-200 über einen Zeitraum von 72 Stunden.
- Dokumentation aller Fehlermeldungen und Systemprotokolle während der Testphase.
- Abschlussbericht zur Evaluierung der Effektivität der durchgeführten Maßnahmen.

## 7. Verantwortlichkeiten
- **Projektleiter:** Max Mustermann
- **Technische Überprüfung:** Anna Beispiel
- **Dokumentation:** Klaus Dokumentar

## 8. Nächste Schritte
- Termin für die Durchführung der Softwareupgrades und Kabeltests festlegen (bis 30. März 2024).
- Teammeeting zur Besprechung des Fortschritts und der Testergebnisse planen.

--- 

Für weitere Informationen oder Rückfragen stehen die verantwortlichen Mitarbeiter jederzeit zur Verfügung.