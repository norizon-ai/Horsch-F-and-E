---
title: Sichere SPS-Programmierung
space: CMP
parent: Sicherheitsnormen
level: 2
---

# Sichere SPS-Programmierung

## Einleitung

Die sichere SPS-Programmierung (Speicherprogrammierbare Steuerung) ist ein wesentlicher Bestandteil der Automatisierungstechnik, insbesondere im Hinblick auf die Sicherheit von Maschinen und Anlagen. Diese Seite beschreibt die grundlegenden Prinzipien und Normen, die bei der Programmierung von SPS-Systemen zu beachten sind, um eine hohe Betriebssicherheit und den Schutz von Mensch und Maschine zu gewährleisten.

## Sicherheitsnormen

Die wichtigsten Sicherheitsnormen, die bei der SPS-Programmierung berücksichtigt werden müssen, sind:

- **EN ISO 13849-1**: Sicherheit von Maschinen – Teile der Steuerungstechnik
- **IEC 61508**: Funktionale Sicherheit von elektrischen/elektronischen/programmierbaren elektronischen Sicherheitssystemen
- **EN 62061**: Sicherheit von Maschinen – Funktionale Sicherheit von sicherheitsbezogenen elektrischen Steuerungssystemen

## Prinzipien der sicheren Programmierung

### 1. Risikobewertung

Vor Beginn der SPS-Programmierung sollte eine umfassende Risikobewertung durchgeführt werden. Diese umfasst die Identifikation möglicher Gefahren und die Bewertung der Risiken, die mit der Steuerung von Maschinen verbunden sind.

### 2. Redundante Systeme

Um die Ausfallsicherheit zu erhöhen, sollten redundante Systeme implementiert werden. Dies kann durch den Einsatz von dualen SPS-Systemen oder durch Sicherstellung der Verfügbarkeit von Backup-Komponenten geschehen.

### 3. Sicherheitsfunktionen

Sicherheitsfunktionen sind spezielle Funktionen, die dazu dienen, gefährliche Zustände zu vermeiden oder zu kontrollieren. Typische Sicherheitsfunktionen sind:

- Not-Halt
- Überwachungen von Positionen und Geschwindigkeiten
- Sicherheitszäune und Lichtvorhänge

### 4. Programmierstandards

Die Programmierung sollte den festgelegten Standards und Richtlinien folgen:

- **Structured Text (ST)** oder **Ladder Diagram (LD)** für die Implementierung sicherheitsrelevanter Funktionen
- Verwendung von Kommentaren und Dokumentation, um die Nachvollziehbarkeit zu gewährleisten

## Beispielkonfiguration

| Funktion             | Beschreibung                              | Implementierung       |
|----------------------|------------------------------------------|------------------------|
| Not-Halt             | Sofortige Abschaltung bei Gefahr         | E-Stop Schalter        |
| Überwachung Geschwind. | Kontrolle der Motordrehzahl             | Sensoren mit SPS-Input |
| Sicherheitszäune     | Physische Trennung von Gefahrenbereiche  | Lichtvorhänge          |

### Beispielcode: Not-Halt-Funktion

```structured-text
IF NOT_HALT_BUTTON = TRUE THEN
    STOP_MACHINE();
    SET_SAFETY_STATUS('Not-Halt aktiv');
ELSE
    CONTINUE_OPERATION();
END_IF;
```

## Fazit

Die sichere SPS-Programmierung ist entscheidend für den reibungslosen Betrieb automatisierter Systeme und den Schutz von Bedienpersonal. Durch die Einhaltung von Sicherheitsnormen, die Implementierung redundanter Systeme und die Beachtung von Programmierstandards kann die Betriebssicherheit erheblich erhöht werden. Es liegt in der Verantwortung der Programmierer, diese Prinzipien konsequent anzuwenden und regelmäßig zu überprüfen.