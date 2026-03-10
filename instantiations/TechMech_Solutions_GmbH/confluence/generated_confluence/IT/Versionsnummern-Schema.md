---
title: Versionsnummern-Schema
space: IT
parent: Backup und Versionierung
level: 1
---

# Versionsnummern-Schema

Das Versionsnummern-Schema von TechMech Solutions GmbH dient der einheitlichen und nachvollziehbaren Kennzeichnung aller Softwareversionen, Dokumentationen und Produkte. Die klare Strukturierung der Versionsnummern ermöglicht eine einfache Identifizierung des Status und der Änderungen an den jeweiligen Komponenten. 

## Grundstruktur der Versionsnummer

Die Versionsnummer setzt sich aus vier Hauptkomponenten zusammen:

```
Hauptversion.Nebenversionsnummer.Revision.Baubeschreibung
```

### Komponenten im Detail

1. **Hauptversion (X)**  
   - Diese Zahl wird erhöht, wenn signifikante Änderungen oder neue Funktionen implementiert werden, die die Kompatibilität mit vorherigen Versionen brechen.
   - Beispiel: 1.0.0.0 → 2.0.0.0

2. **Nebenversionsnummer (Y)**  
   - Die Nebenversionsnummer wird erhöht, wenn neue Funktionen hinzugefügt werden, die jedoch abwärtskompatibel sind.
   - Beispiel: 1.0.0.0 → 1.1.0.0

3. **Revision (Z)**  
   - Die Revision wird erhöht, wenn Fehlerbehebungen oder kleinere Verbesserungen vorgenommen werden, ohne die Funktionalität zu verändern.
   - Beispiel: 1.0.0.0 → 1.0.1.0

4. **Baubeschreibung (W)**  
   - Diese Zahl wird verwendet, um spezifische Änderungen oder Anpassungen zu kennzeichnen, z. B. bei speziellen Kundenanforderungen oder Anpassungen.
   - Beispiel: 1.0.0.0 → 1.0.0.1

## Versionsmanagement-Prozess

### Schritte zur Versionsvergabe

1. **Planung**  
   - Bei der Planung neuer Funktionen wird die Haupt- oder Nebenversionsnummer in Abhängigkeit von den Änderungen festgelegt.

2. **Entwicklung**  
   - Während der Entwicklung werden alle Änderungen in einem changelog dokumentiert. Die Revision wird nach Fertigstellung der Tests erhöht.

3. **Testphase**  
   - Nach der Testphase wird die Versionsnummer finalisiert. Bei schwerwiegenden Fehlern kann die Revision vor der Veröffentlichung nochmals erhöht werden.

4. **Veröffentlichung**  
   - Die finale Version wird dann in der entsprechenden Dokumentation und im System veröffentlicht. 

### Beispielversionen

| Versionsnummer | Beschreibung                                               | Status          |
|----------------|-----------------------------------------------------------|-----------------|
| 1.0.0.0        | Erstveröffentlichung                                      | Veröffentlicht   |
| 1.1.0.0        | Hinzufügung neuer Funktionen für die Fördertechnik        | Veröffentlicht   |
| 1.0.1.0        | Fehlerbehebung in der Qualitätsprüfsoftware               | Veröffentlicht   |
| 1.0.0.1        | Anpassung an Kundenanforderungen für Projekt X           | In Bearbeitung   |

## Fazit

Das Versionsnummern-Schema von TechMech Solutions GmbH stellt sicher, dass alle Änderungen und Entwicklungen transparent dokumentiert sind. Durch die klare Struktur können alle Beteiligten den Fortschritt und die Kompatibilität der Software und Systeme nachvollziehen. Bei Fragen oder weiteren Informationen wenden Sie sich bitte an die IT-Abteilung.