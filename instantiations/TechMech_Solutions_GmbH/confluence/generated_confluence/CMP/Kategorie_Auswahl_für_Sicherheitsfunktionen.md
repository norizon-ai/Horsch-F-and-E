---
title: Kategorie Auswahl für Sicherheitsfunktionen
space: CMP
parent: Sicherheitsnormen
level: 2
---

# Kategorie Auswahl für Sicherheitsfunktionen

Die Auswahl geeigneter Sicherheitsfunktionen ist entscheidend für die Planung und Implementierung von Automatisierungssystemen. Im Folgenden sind die verschiedenen Kategorien von Sicherheitsfunktionen aufgeführt, die in unseren Projekten berücksichtigt werden sollten. Diese Funktionen sind gemäß den relevanten Sicherheitsnormen, insbesondere der ISO 13849-1 und der IEC 62061, klassifiziert.

## 1. Sicherheitsfunktionen

### 1.1 Not-Halt-Funktion
Die Not-Halt-Funktion dient dazu, Maschinen und Anlagen in einem Notfall schnell und sicher abzuschalten. Die Implementierung muss folgenden Anforderungen genügen:

- **Sicherheitskategorie**: PL e (Performance Level e) gemäß ISO 13849-1
- **Reaktionszeit**: < 0,5 Sekunden
- **Hardware-Anforderungen**: Verwendung von redundanten Schaltkreisen

### 1.2 Sicherheitsverriegelung
Diese Funktion verhindert den Zugang zu gefährlichen Bereichen, solange die Maschine in Betrieb ist.

- **Sicherheitskategorie**: PL c
- **Typen**: Mechanische und elektrische Verriegelungen
- **Sensorik**: Verwendung von sicherheitsgerichteten Türschaltern

### 1.3 Überwachungsfunktionen
Überwachungsfunktionen dienen der kontinuierlichen Überprüfung von sicherheitsrelevanten Parametern.

| Funktion             | Beschreibung                                 | Messbereich     | Toleranz       |
|---------------------|---------------------------------------------|------------------|----------------|
| Temperaturüberwachung | Überwachung der Temperatur von Komponenten  | 0 - 100 °C      | ± 2 °C         |
| Drucküberwachung     | Kontrolle des Betriebsdrucks                 | 0 - 10 bar      | ± 0,5 bar      |
| Positionsüberwachung | Sicherstellung der korrekten Positionierung  | 0 - 100 mm      | ± 1 mm         |

### 1.4 Sicherheits-Stop-Funktion
Diese Funktion stellt sicher, dass Maschinen im Falle eines Fehlers kontrolliert gestoppt werden.

- **Sicherheitskategorie**: PL d
- **Implementierung**: Nutzung von sicherheitsgerichteten Steuerungen
- **Testintervalle**: Mindestens alle 3 Monate

## 2. Auswahlkriterien

Bei der Auswahl der Sicherheitsfunktionen sind folgende Kriterien zu beachten:

- **Risikobewertung**: Analyse der Gefahrenpotenziale und Risikoeinstufung gemäß ISO 12100
- **Anwendungsspezifikationen**: Berücksichtigung der spezifischen Anforderungen der jeweiligen Branche (z. B. Automotive, Lebensmittel, Pharma)
- **Normenkonformität**: Sicherstellen, dass alle Funktionen den geltenden Sicherheitsnormen entsprechen
- **Wartbarkeit**: Berücksichtigung der einfachen Zugänglichkeit für Wartungs- und Prüfungsarbeiten

## 3. Fazit

Die korrekte Auswahl und Implementierung von Sicherheitsfunktionen ist fundamental für die Sicherheit von Automatisierungssystemen. Es ist unerlässlich, dass alle Funktionen regelmäßig überprüft und getestet werden, um die Einhaltung der Sicherheitsstandards zu gewährleisten. In der Planungsphase sollten alle relevanten Informationen und Daten dokumentiert werden, um eine transparente Nachverfolgbarkeit zu ermöglichen.