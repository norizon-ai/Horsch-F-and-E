---
title: HMI Styleguide TechMech
space: IT
parent: Visualisierung (HMI)
level: 1
---

# HMI Styleguide TechMech

## Einleitung
Der HMI Styleguide von TechMech Solutions GmbH dient als umfassende Richtlinie für die Gestaltung und Entwicklung von Benutzeroberflächen (HMI) in unseren Automatisierungs- und Maschinenbauprojekten. Ziel ist es, eine konsistente, benutzerfreundliche und effizient funktionierende Bedienoberfläche zu schaffen, die den Anforderungen unserer Kunden gerecht wird.

## Grundprinzipien

### Benutzerzentrierter Ansatz
Die HMI-Entwicklung orientiert sich an den Bedürfnissen der Benutzer. Dazu gehören:
- **Intuitive Navigation**: Benutzer sollen alle Funktionen schnell und einfach erreichen können.
- **Klarheit und Übersichtlichkeit**: Informationen müssen strukturiert und verständlich dargestellt werden.

### Konsistenz
Alle HMI-Elemente müssen ein einheitliches Erscheinungsbild und Verhalten aufweisen:
- **Farbschema**: Primärfarben: Blau (#003366), Grau (#CCCCCC), Akzentfarbe: Orange (#FF6600).
- **Schriftarten**: Hauptschriftart: Arial, Schriftgröße: 12 pt für Fließtext, 14 pt für Überschriften.

## Komponenten und Layout

### Bildschirmaufbau
Jede HMI-Oberfläche sollte in folgende Bereiche unterteilt werden:

| Bereich        | Beschreibung                               |
|----------------|-------------------------------------------|
| Kopfzeile      | Logo, Titel der Anwendung, Benutzername   |
| Navigationsmenü| Links zu den Hauptfunktionen               |
| Hauptinhalt    | Dynamische Anzeige der relevanten Daten    |
| Fußzeile       | Impressum, Versionierung, Kontaktinformationen |

### Bedienelemente
Die Auswahl der Bedienelemente ist entscheidend für die Benutzerinteraktion. Folgende Elemente sind zu verwenden:

- **Buttons**: Standardgröße 80x30 px, abgerundete Ecken, Farbcode entsprechend dem Farbschema.
- **Slider**: Breite 300 px, mit klaren Markierungen für Werte.
- **Dropdown-Menüs**: Maximale Anzahl an Optionen: 10, um Überladung zu vermeiden.

## Technische Spezifikationen

### Bildschirmauflösungen
Die HMI-Oberflächen sollen für folgende Bildschirmauflösungen optimiert werden:
- **Full HD (1920x1080)**: Für Desktop-Anwendungen.
- **HD (1280x720)**: Für mobile Geräte und Tablets.

### Responsive Design
Die HMI muss responsive gestaltet sein, um eine optimale Darstellung auf verschiedenen Geräten zu gewährleisten. Dies beinhaltet:
- **Flexible Layouts**: Verwendung von CSS Media Queries zur Anpassung der Darstellung.
- **Touch-freundliche Elemente**: Mindestens 50 px Abstand zwischen interaktiven Elementen.

## Beispielkonfiguration

### Beispiel HMI-Layout
Das folgende Beispiel zeigt ein typisches HMI-Layout für eine Roboterzelle im Automobilbereich:

- **Kopfzeile**: "Roboterzelle A1" | Benutzer: Max Mustermann
- **Navigation**:
  - Startseite
  - Statusanzeige
  - Wartungsprotokoll
- **Hauptinhalt**:
  - Aktueller Status: "Betrieb"
  - Letzte Wartung: "01.10.2023"
  - Fehlerstatus: "Keine Fehler"
- **Fußzeile**: Version 1.2 | Kontakt: support@techmech.de

## Fazit
Der HMI Styleguide stellt sicher, dass alle HMI-Anwendungen von TechMech Solutions GmbH benutzerfreundlich, konsistent und technisch auf dem neuesten Stand sind. Die Einhaltung dieser Richtlinien verbessert die Benutzerzufriedenheit und trägt zur Effizienz unserer Automatisierungslösungen bei.