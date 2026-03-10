---
title: Abschlussbericht
space: PRJ
parent: PRJ-2024-067 - ElectroWerk Prüfstation
level: 2
---

# Abschlussbericht

## Projektübersicht

Im Rahmen des Projekts PRJ-2024-067 wurde eine Prüfstation für die ElektroWerk-Anlage entwickelt und implementiert. Ziel des Projektes war die Automatisierung des Prüfprozesses von elektrischen Komponenten zur Verbesserung der Qualitätssicherung und Effizienz in der Produktion.

## Projektziele

- Automatisierung der Prüfprozesse für elektrische Bauteile
- Reduzierung der Prüfzeiten um mindestens 30 %
- Sicherstellung der Einhaltung relevanter Normen und Standards (z. B. ISO 9001, IEC 61000)

## Technische Spezifikationen

| Spezifikation               | Wert                        |
|-----------------------------|-----------------------------|
| Prüfelemente                 | Widerstände, Kondensatoren, Transistoren |
| Max. Prüfspannung            | 500 V DC                    |
| Prüffrequenz                 | 1 Hz - 10 kHz               |
| Prüfdauer                    | 1-5 Sekunden pro Bauteil    |
| Automatisierungssystem       | Siemens S7-1500            |
| Sensorik                     | High-Precision Multimeter   |
| Datenschnittstelle           | OPC UA, Ethernet            |

## Prozessbeschreibung

Die Prüfstation ist in folgende Schritte unterteilt:

1. **Zufuhr der Prüfkandidaten**: Die Bauteile werden über eine integrierte Fördertechnik zur Prüfstation transportiert.
2. **Vorbereitung**: Vor der Prüfung erfolgt eine automatische Identifikation der Bauteile mittels RFID-Technologie.
3. **Durchführung der Prüfungen**:
   - **Widerstandsmessung**: Bauteile werden mit einer Prüfspeisung versehen, die Widerstandswerte werden erfasst und mit den Sollwerten verglichen.
   - **Kapazitätsmessung**: Messung der Kapazität für Kondensatoren unter definierten Bedingungen.
   - **Transistorprüfung**: Überprüfung der Funktionalität von Transistoren durch Spannungs- und Strommessungen.
4. **Auswertung**: Die Ergebnisse werden in einer Datenbank erfasst. Bei Abweichungen erfolgt eine automatische Alarmierung.
5. **Entsorgung**: Nicht konforme Bauteile werden automatisch in eine Ausschussbox geleitet.

## Messergebnisse

Im Rahmen der Erprobung der Prüfstation wurden folgende Messergebnisse erfasst:

| Bauteil         | gemessener Wert | Sollwert     | Status    |
|------------------|----------------|--------------|-----------|
| Widerstand R1    | 100 Ohm        | 100 Ohm      | Konform   |
| Kondensator C1   | 10 µF          | 10 µF        | Konform   |
| Transistor Q1    | 0.7 V          | 0.6-0.7 V    | Konform   |
| Widerstand R2    | 150 Ohm        | 100 Ohm      | Nicht konform |

## Fazit

Die Implementierung der ElektroWerk Prüfstation war durchweg erfolgreich. Die automatisierten Prüfprozesse führen zu einer signifikanten Reduzierung der Prüfzeiten und einer erhöhten Qualitätssicherung. Zukünftige Erweiterungen könnten die Integration weiterer Prüfzellen sowie die Implementierung einer umfassenden Datenanalyse zur Optimierung der Produktionsprozesse umfassen.