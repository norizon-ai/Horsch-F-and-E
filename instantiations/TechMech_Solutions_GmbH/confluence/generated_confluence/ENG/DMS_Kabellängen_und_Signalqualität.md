---
title: DMS Kabellängen und Signalqualität
space: ENG
parent: Qualitätsprüfsysteme
level: 3
---

# DMS Kabellängen und Signalqualität

## Einleitung
In der Automatisierungstechnik ist die Signalqualität von entscheidender Bedeutung für die Zuverlässigkeit und Genauigkeit von Messsystemen. Diese Seite behandelt die optimalen Kabellängen für Dehnungsmessstreifen (DMS) sowie die Auswirkungen auf die Signalqualität. 

## Kabellängen

### Empfohlene Kabellängen
Die Kabellänge hat einen direkten Einfluss auf die Signalqualität und die Messgenauigkeit. Für DMS-Anwendungen gilt:

- **Maximale Kabellänge:** 10 Meter
- **Empfohlene Kabellänge:** 5 Meter

### Kabellängen und Signalverlust
Längere Kabel führen zu einem erhöhten Widerstand und können das Signal dämpfen. Hier sind die typischen Signalverluste pro Meter Kabel aufgeführt:

| Kabeltyp       | Signalverlust (dB/m) | Maximale Länge (m) |
|----------------|-----------------------|---------------------|
| Kupferkabel    | 0,2                   | 10                  |
| Silberkabel    | 0,1                   | 15                  |
| Litzendraht    | 0,3                   | 5                   |

## Signalqualität

### Einflussfaktoren
Die Signalqualität wird durch verschiedene Faktoren beeinflusst:

1. **Kabeltyp:** Der Materialtyp hat einen großen Einfluss auf die Leitfähigkeit und damit die Signalverluste.
2. **Umgebungsbedingungen:** Temperatur, Feuchtigkeit und elektromagnetische Störungen können die Signalqualität negativ beeinflussen.
3. **Verbindungen:** Schlechte Löt- oder Steckverbindungen können zu Signalrauschen führen.

### Messwerte
Bei der Installation von DMS-Systemen sollten die folgenden Messwerte beachtet werden, um eine optimale Signalqualität zu gewährleisten:

- **Widerstand:** Der Gesamtwiderstand des Kabels sollte unter 5 Ohm liegen.
- **Signal-Rausch-Verhältnis (SNR):** Ein SNR von mindestens 20 dB ist empfehlenswert, um zuverlässige Messwerte zu erhalten.

## Konfigurationsempfehlungen

### Schaltung
Um die Signalqualität zu maximieren, empfehlen wir folgende Schaltung:

- **Differenzmessung:** Reduziert die Auswirkungen von Rauschen und verbessert die Genauigkeit.
- **Verwendung von Abschirmung:** Schirmkabel können externe Störungen minimieren und die Signalqualität erhöhen.

### Beispielkonfiguration
Für eine typische DMS-Konfiguration könnte die folgende Spezifikation verwendet werden:

- **DMS-Typ:** Strain Gauge SG-100
- **Kabeltyp:** Silberkabel
- **Kabellänge:** 5 Meter
- **Widerstand:** 2 Ohm
- **SNR:** 25 dB

## Fazit
Die Auswahl der richtigen Kabellängen und Kabeltypen ist entscheidend für die Signalqualität in DMS-Anwendungen. Durch die Beachtung der oben genannten Empfehlungen können die Zuverlässigkeit und Genauigkeit von Qualitätsprüfsystemen in der Automatisierungstechnik signifikant verbessert werden.