---
title: Mehrsprachigkeit Setup
space: IT
parent: Visualisierung (HMI)
level: 1
---

# Mehrsprachigkeit Setup

## Einleitung
Die Implementierung einer mehrsprachigen Benutzeroberfläche (UI) in unseren HMI-Systemen ist entscheidend für die Benutzerfreundlichkeit und die Zugänglichkeit in internationalen Märkten. Diese Seite beschreibt die notwendigen Schritte, um die Mehrsprachigkeit in unseren Visualisierungen zu konfigurieren.

## Technische Anforderungen
Um die Mehrsprachigkeit in HMI-Systemen zu implementieren, sind folgende technische Voraussetzungen erforderlich:

- **Software-Version**: Mindestens Version 3.2.0 der HMI-Software
- **Datenbank**: Unterstützung für UTF-8-Kodierung
- **Sprachdateien**: Extern gelagerte Sprachdateien im JSON-Format
- **Locale-Einstellungen**: Unterstützung für verschiedene Locale-Formate (z.B. de-DE, en-US, fr-FR)

## Konfigurationsschritte

### 1. Sprachdateien erstellen
Erstellen Sie für jede gewünschte Sprache eine separate JSON-Datei. Jede Datei sollte Schlüssel-Wert-Paare enthalten, die die zu übersetzenden Texte abbilden. Beispiel:

**de-DE.json**
```json
{
    "greeting": "Hallo",
    "exit": "Beenden"
}
```

**en-US.json**
```json
{
    "greeting": "Hello",
    "exit": "Exit"
}
```

### 2. Integration der Sprachdateien
Fügen Sie die Sprachdateien in das HMI-Projekt ein. Dies geschieht in der Regel über den Projektordner `resources/lang/`. Vergewissern Sie sich, dass die Dateien korrekt benannt sind und im richtigen Format vorliegen.

### 3. Locale-Anpassung
Die Locale kann im HMI-System durch eine einfache Konfiguration in der `config.properties`-Datei festgelegt werden. Beispielkonfiguration:

```properties
app.locale=de-DE
```

### 4. UI-Elemente anpassen
Stellen Sie sicher, dass alle UI-Elemente die Texte dynamisch aus den Sprachdateien abrufen. Beispiel für eine Button-Integration in der UI:

```html
<button>{{ 'greeting' | translate }}</button>
```

## Test und Validierung
Nach der Implementierung ist es wichtig, die Mehrsprachigkeit zu testen. Führen Sie die folgenden Schritte durch:

1. **Sprachwechsel**: Testen Sie den Wechsel zwischen den Sprachen in der Betriebsumgebung.
2. **Textüberprüfung**: Überprüfen Sie, ob alle Texte korrekt aus den Sprachdateien geladen werden.
3. **Sichtbarkeit**: Stellen Sie sicher, dass die Texte in allen UI-Elementen richtig angezeigt werden.

## Beispielkonfiguration
| Sprache   | Dateiname       | Locale   |
|-----------|------------------|----------|
| Deutsch   | de-DE.json       | de-DE    |
| Englisch  | en-US.json       | en-US    |
| Französisch| fr-FR.json     | fr-FR    |

## Fazit
Die Implementierung der Mehrsprachigkeit in unseren HMI-Systemen ist ein wesentlicher Schritt zur Verbesserung der Benutzererfahrung. Durch die Befolgung dieser Anleitung stellen wir sicher, dass unsere Produkte den Anforderungen internationaler Märkte gerecht werden. Bei Fragen oder Problemen wenden Sie sich bitte an das IT-Support-Team.