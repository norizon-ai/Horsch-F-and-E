---
title: HMI Design Guidelines
space: IT
parent: SPS-Programmierung
level: 2
---

# HMI Design Guidelines

## Einleitung
Die Gestaltung von Human-Machine Interfaces (HMI) ist entscheidend für die Benutzerfreundlichkeit und Effizienz von Automatisierungssystemen. Diese Richtlinien bieten einen Rahmen für die Entwicklung intuitiver und effektiver HMIs bei TechMech Solutions GmbH, um sicherzustellen, dass alle Benutzer – vom Maschinenbediener bis hin zum Wartungspersonal – die Systeme optimal nutzen können.

## Design-Prinzipien

### 1. Benutzerzentrierter Ansatz
- **Zielgruppenanalyse**: Bestimmen Sie die spezifischen Anforderungen und Fähigkeiten der Endbenutzer.
- **Feedback einholen**: Regelmäßige Benutzerumfragen und Usability-Tests durchführen.

### 2. Konsistenz
- **Design-Standards**: Einheitliche Farbpaletten, Schriftarten und Layouts verwenden.
- **Interaktive Elemente**: Gleiche Symbole und Terminologien für ähnliche Funktionen verwenden.

### 3. Klarheit und Einfachheit
- **Minimierung von Informationen**: Nur relevante Informationen anzeigen, um Überfrachtung zu vermeiden.
- **Eindeutige Beschriftungen**: Alle Schaltflächen und Anzeigen klar und präzise beschriften.

## Technische Spezifikationen

### 1. Bildschirmauflösungen
| Anwendung         | Empfohlene Auflösung | Min. Auflösung   |
|-------------------|----------------------|-------------------|
| Roboterzellen     | 1920 x 1080 px       | 1280 x 720 px     |
| Fördertechnik      | 1280 x 800 px        | 1024 x 600 px     |
| Qualitätsprüfsystem| 1920 x 1080 px       | 1280 x 720 px     |

### 2. Farbcodierung
- **Hintergrundfarben**: Helle Farben für aktive Elemente, dunkle Farben für inaktive Elemente.
- **Warnhinweise**: Rot für kritische Fehler, Gelb für Warnungen, Grün für betriebsbereite Zustände.

## Interaktive Elemente

### 1. Schaltflächen
- **Größe**: Mindestgröße von 44 x 44 px für Touch-Bedienung.
- **Farben**: Klare Farbkontraste für bessere Sichtbarkeit.

### 2. Anzeigen
- **Datenanzeigen**: Echtzeitdaten sollten klar dargestellt werden, z.B. Produktionszahlen, Fehlercodes.
- **Messwerte**: Anzeigen von Messwerten in verständlichen Einheiten (z.B. Temperatur in °C oder Druck in bar).

## Layout-Empfehlungen
- **Rasterlayout**: Verwenden Sie ein flexibles Raster, um die Anordnung der Elemente zu optimieren.
- **Navigation**: Klare und intuitive Navigationselemente, die den Benutzer schnell zu den gewünschten Informationen führen.

## Beispiele für HMI-Elemente

### Beispiel: Roboterzelle
- **Statusanzeige**: 
  - Grün: Betriebsbereit
  - Gelb: Warten auf Material
  - Rot: Fehlerzustand (mit Fehlercode angezeigt)

### Beispiel: Fördertechnik
- **Produktionszähler**: 
  - Bereich: 0 bis 1000 Einheiten
  - Einheit: Stück
  - Aktualisierungsintervall: alle 5 Sekunden

## Fazit
Die Implementierung dieser HMI Design Guidelines wird dazu beitragen, die Benutzerfreundlichkeit und Effizienz unserer Automatisierungslösungen zu verbessern. Die kontinuierliche Überprüfung und Anpassung dieser Richtlinien ist notwendig, um den sich ändernden Anforderungen und Technologien gerecht zu werden.