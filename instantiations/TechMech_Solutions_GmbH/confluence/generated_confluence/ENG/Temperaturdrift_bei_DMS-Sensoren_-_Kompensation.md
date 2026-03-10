---
title: Temperaturdrift bei DMS-Sensoren - Kompensation
space: ENG
parent: Qualitätsprüfsysteme
level: 3
---

# Temperaturdrift bei DMS-Sensoren - Kompensation

## Einleitung
DMS-Sensoren (Dehnungsmessstreifen) sind in der Automatisierungstechnik weit verbreitet, insbesondere in Qualitätsprüfsystemen zur Überwachung von mechanischen Spannungen und Kräften. Eine Herausforderung bei der Nutzung dieser Sensoren stellt die Temperaturdrift dar, die zu fehlerhaften Messwerten führen kann. Diese Seite beschreibt die Ursachen der Temperaturdrift und die Methoden zur Kompensation.

## Ursachen der Temperaturdrift
Die Temperaturdrift von DMS-Sensoren wird durch verschiedene Faktoren beeinflusst:

1. **Materialausdehnung**: Die unterschiedlichen Ausdehnungskoeffizienten von DMS-Materialien und der Trägermaterialien führen zu Messabweichungen.
2. **Temperaturabhängigkeit des Widerstands**: Der Widerstand eines DMS ändert sich mit der Temperatur, was direkte Auswirkungen auf die Messgenauigkeit hat.
3. **Umgebungsbedingungen**: Schwankungen in der Umgebungstemperatur können ebenfalls zu Driftfehlern führen.

## Kompensationsmethoden

### 1. Hardwarebasierte Kompensation
Die hardwarebasierte Kompensation umfasst die Verwendung von temperaturabhängigen Widerständen, um die Drift in der Messschaltung auszugleichen. Ein Beispiel für eine solche Schaltung ist die Verwendung eines Thermistors, der in Reihe mit dem DMS geschaltet wird.

### 2. Softwarebasierte Kompensation
Die softwarebasierte Kompensation erfolgt durch Kalibrierung und Anpassung der Messwerte in der Auswertesoftware. Hierbei werden die Messwerte in Abhängigkeit von der Temperatur korrigiert. Ein typisches Vorgehen ist die Erstellung einer Kalibrierungstabelle, die wie folgt aussehen kann:

| Temperatur (°C) | Messwert (mV) | Korrekturwert (mV) |
|------------------|---------------|---------------------|
| 20               | 500           | 0                   |
| 25               | 520           | -5                  |
| 30               | 540           | -10                 |
| 35               | 560           | -15                 |

### 3. Temperaturüberwachung
Eine kontinuierliche Überwachung der Umgebungstemperatur ist entscheidend für die Kompensation. Hierzu können Temperatursensoren eingesetzt werden, die in die Messanordnung integriert sind. Die gemessene Temperatur wird dann in Echtzeit zur Anpassung der DMS-Messwerte herangezogen.

## Implementierung
Die Implementierung der Kompensationsmethoden erfolgt in mehreren Schritten:

1. **Kalibrierung**: Zu Beginn sollte eine umfassende Kalibrierung der DMS-Sensoren bei verschiedenen Temperaturen durchgeführt werden.
2. **Integration der Kompensation**: Sowohl hardware- als auch softwarebasierte Lösungen müssen in die bestehende Mess- und Auswertesoftware integriert werden.
3. **Testphase**: Nach der Implementierung sind umfangreiche Tests notwendig, um die Genauigkeit der kompensierten Messwerte zu validieren.

## Fazit
Die Temperaturdrift bei DMS-Sensoren kann die Genauigkeit von Messungen erheblich beeinträchtigen. Durch geeignete Kompensationsmethoden, sowohl hardware- als auch softwarebasiert, kann jedoch eine signifikante Verbesserung der Messgenauigkeit erzielt werden. Eine sorgfältige Kalibrierung und kontinuierliche Temperaturüberwachung sind entscheidend für den Erfolg dieser Maßnahmen.