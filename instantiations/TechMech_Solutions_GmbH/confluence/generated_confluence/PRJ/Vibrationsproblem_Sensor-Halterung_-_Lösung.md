---
title: Vibrationsproblem Sensor-Halterung - Lösung
space: PRJ
parent: PRJ-2024-067 - ElectroWerk Prüfstation
level: 2
---

# Vibrationsproblem Sensor-Halterung - Lösung

## Einleitung

Im Rahmen des Projekts PRJ-2024-067 - ElectroWerk Prüfstation wurde ein spezifisches Vibrationsproblem bei der Sensor-Halterung identifiziert, das die Messgenauigkeit und Zuverlässigkeit der Prüfergebnisse beeinträchtigt hat. Diese Seite dokumentiert die durchgeführten Analysen sowie die implementierten Lösungen zur Behebung des Problems.

## Problemanalyse

### Ursachenidentifikation

Die ersten Tests zeigten, dass die Sensor-Halterung unter Betriebsbedingungen (Vibrationen durch benachbarte Maschinen) instabil war. Folgende Ursachen wurden identifiziert:

- **Unzureichende Dämpfung:** Die verwendeten Materialien und die Konstruktion der Halterung boten nicht ausreichend Vibrationseindämmung.
- **Falsche Montage:** Eine nicht optimale Ausrichtung der Sensoren führte zu zusätzlichen Belastungen.
- **Betriebsbedingungen:** Hohe Frequenzen und Amplituden der Vibrationen, die durch benachbarte Maschinen verursacht wurden (Messwerte: 5-20 Hz, Amplitude 0,5-1 mm).

### Messdaten

| Messpunkt       | Frequenz (Hz) | Amplitude (mm) | Vibrationstyp    |
|------------------|----------------|-----------------|-------------------|
| Sensor-Halterung  | 10             | 0,8             | Statische Vibration |
| Benachbarte Maschine | 15             | 0,6             | Dynamische Vibration |

## Lösungsansatz

### Konstruktive Änderungen

Um die Stabilität der Sensor-Halterung zu verbessern, wurden folgende Konstruktionsänderungen vorgenommen:

1. **Verwendung von Dämpfungsmaterialien:**
   - Implementierung von elastischen Gummipuffern (Material: EPDM) zur besseren Vibrationseindämmung.
   - Materialdicke: 10 mm.

2. **Optimierung der Halterungsgeometrie:**
   - Anpassung der Halterung auf eine breitere Basis zur Erhöhung der Stabilität.
   - Minimierung der Hebelarme, um die Kräfte gleichmäßiger zu verteilen.

3. **Verbesserte Montage:**
   - Einführung von präzisen Montagevorrichtungen zur Sicherstellung der optimalen Ausrichtung der Sensoren.

### Tests und Validierung

Nach der Implementierung der Änderungen wurden erneut Tests durchgeführt, um die Wirksamkeit der Maßnahmen zu überprüfen. Die neuen Messdaten ergaben:

| Messpunkt       | Frequenz (Hz) | Amplitude (mm) | Vibrationstyp   |
|------------------|----------------|-----------------|------------------|
| Sensor-Halterung  | 10             | 0,2             | Statische Vibration |
| Benachbarte Maschine | 15             | 0,3             | Dynamische Vibration |

Die Ergebnisse zeigen eine signifikante Reduzierung der Vibrationen an der Sensor-Halterung um bis zu 75 %.

## Fazit

Die durchgeführten Maßnahmen zur Verbesserung der Stabilität der Sensor-Halterung haben sich als erfolgreich erwiesen. Die Messgenauigkeit der ElectroWerk Prüfstation konnte wiederhergestellt werden, und die Zuverlässigkeit der Prüfergebnisse ist nun gewährleistet. Zukünftige Monitoring-Maßnahmen werden empfohlen, um die langfristige Stabilität zu überwachen.