---
title: Sicherheitsrelais Schaltungen
space: ENG
parent: Konstruktionsstandards
level: 2
---

# Sicherheitsrelais Schaltungen

## Einleitung

Sicherheitsrelais sind essentielle Komponenten in der Automatisierungstechnik, insbesondere im Kontext der Maschinen- und Anlagensicherheit. Sie dienen der Überwachung von Sicherheitsfunktionen und gewährleisten, dass im Fehlerfall die entsprechenden sicherheitsrelevanten Maßnahmen ergriffen werden. Diese Seite beschreibt die grundlegenden Aspekte und Konstruktionsstandards für Sicherheitsrelais Schaltungen bei TechMech Solutions GmbH.

## Funktionsweise

Sicherheitsrelais überwachen sicherheitskritische Eingangsparameter und steuern Ausgänge, um eine sichere Maschine oder Anlage zu gewährleisten. Bei einem Fehler oder einer Störung wird der Ausgang in den sicheren Zustand versetzt. Die typischen Funktionen umfassen:

- **Not-Halt Schaltung:** Unterbricht die Stromversorgung bei Betätigung des Not-Halt-Schalters.
- **Überwachung von Schutztüren:** Gewährleistet, dass Maschinen stillstehen, solange Schutztüren geöffnet sind.
- **Überwachung von Sicherheitssteuerungen:** Steuert den Betrieb von Maschinen in Abhängigkeit von sicherheitsrelevanten Sensoren.

## Typische Schaltungsbeispiele

### Beispiel 1: Not-Halt Schaltung

| Komponente          | Typ             | Anzahl  |
|---------------------|-----------------|---------|
| Not-Halt Taster     | NC              | 1       |
| Sicherheitsrelais   | SR-1234         | 1       |
| Motor               | 3-Phasen, 400V  | 1       |
| Schütz              | 3-Polig         | 1       |

**Funktionsbeschreibung:** Bei Betätigung des Not-Halt Tasters wird das Sicherheitsrelais aktiviert, welches das Schütz öffnet und somit den Motor stilllegt.

### Beispiel 2: Sicherheitsüberwachung einer Schutztür

| Komponente                   | Typ             | Anzahl  |
|------------------------------|-----------------|---------|
| Schutztür-Sensor             | Magnetkontakt    | 1       |
| Sicherheitsrelais            | SR-5678         | 1       |
| Schütz                       | 3-Polig         | 1       |

**Funktionsbeschreibung:** Wird die Schutztür geöffnet, schaltet der Sensor und das Sicherheitsrelais unterbricht die Stromzufuhr zum Schütz, wodurch die Maschine stoppt.

## Normen und Vorschriften

Die Konstruktion und der Einsatz von Sicherheitsrelais müssen den geltenden Normen und Vorschriften entsprechen. Dazu zählen insbesondere:

- **EN ISO 13849-1:** Sicherheitsbezogene Teile von Steuerungen
- **EN 60204-1:** Sicherheit von Maschinen - Elektrische Ausrüstung von Maschinen
- **DGUV Vorschrift 1:** Grundsätze der Prävention

## Umsetzung und Dokumentation

Für die Implementierung von Sicherheitsrelais Schaltungen sind folgende Schritte erforderlich:

1. **Bedarfsanalyse:** Identifikation der sicherheitsrelevanten Funktionen.
2. **Schaltungsdesign:** Erstellung eines Schaltplans unter Berücksichtigung der Normen.
3. **Test und Validierung:** Durchführung von Funktionstests und Sicherheitsprüfungen.
4. **Dokumentation:** Festhalten aller Schritte und Ergebnisse in der technischen Dokumentation.

## Fazit

Die ordnungsgemäße Planung und Ausführung von Sicherheitsrelais Schaltungen ist entscheidend für die Sicherheit von Maschinen und Anlagen. Bei TechMech Solutions GmbH wird großer Wert auf die Einhaltung der Konstruktionsstandards und Normen gelegt, um maximale Sicherheit für Bediener und Anlagen zu gewährleisten.