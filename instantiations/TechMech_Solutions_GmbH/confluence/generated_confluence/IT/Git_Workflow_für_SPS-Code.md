---
title: Git Workflow für SPS-Code
space: IT
parent: Backup und Versionierung
level: 1
---

# Git Workflow für SPS-Code

## Einleitung
Der Einsatz von Git für die Versionierung von SPS-Code (Speicherprogrammierbare Steuerungen) ermöglicht eine effiziente Verwaltung von Codeänderungen und die Zusammenarbeit im Team. Dieser Dokumentationsabschnitt beschreibt den empfohlenen Git Workflow für den Umgang mit SPS-Projekten bei TechMech Solutions GmbH.

## Workflow-Übersicht
Der Git Workflow für SPS-Code besteht aus mehreren Phasen, die sicherstellen, dass Änderungen nachvollziehbar sind und die Integrität des Codes gewahrt bleibt. Der Workflow umfasst die folgenden Schritte:

1. **Branching**
   - Erstellen eines neuen Branches für jede neue Funktion oder Bugfix.
   - Namenskonvention: `feature/<Beschreibung>` für neue Funktionen, `bugfix/<Beschreibung>` für Fehlerbehebungen.

2. **Entwicklung**
   - Änderungen am SPS-Code im neuen Branch vornehmen.
   - Die Verwendung von klaren Commit-Nachrichten ist essenziell. Beispiel:
     ```
     git commit -m "Implementierung der neuen Förderbandsteuerung"
     ```

3. **Testing**
   - Vor dem Mergen in den Hauptbranch (main) sollten alle Änderungen lokal getestet werden.
   - Sicherstellen, dass der Code auf der SPS-Hardware oder im Simulator fehlerfrei läuft.

4. **Merge**
   - Pull-Request (PR) erstellen, um Änderungen in den Hauptbranch zu integrieren.
   - Code-Review durch mindestens einen anderen Entwickler anfordern.

5. **Deployment**
   - Nach genehmigten PRs wird der Code in den Hauptbranch gemerged.
   - Deployment auf die SPS-Hardware gemäß den Unternehmensrichtlinien.

## Branching-Strategie
| Branch-Typ         | Beschreibung                              |
|--------------------|------------------------------------------|
| `main`             | Stabiler Produktionscode                 |
| `develop`          | Entwicklungsbranch für laufende Arbeiten |
| `feature/*`        | Branches für neue Features               |
| `bugfix/*`         | Branches für Fehlerbehebungen            |

## Beispiel für einen Pull-Request
Ein Pull-Request sollte die folgenden Informationen enthalten:
- **Titel**: Kurze Zusammenfassung der Änderungen (z. B. "Neue Steuerung für Förderband")
- **Beschreibung**: Detaillierte Beschreibung der Änderungen, einschließlich:
  - Ziele der Implementierung
  - Verwendete Algorithmen oder Logik
  - Auswirkungen auf bestehende Funktionen
- **Testresultate**: Ergebnisse der durchgeführten Tests und mögliche bekannte Probleme.

## Best Practices
- **Regelmäßige Commits**: Häufiges Speichern von Änderungen fördert die Nachvollziehbarkeit.
- **Konsistente Namensgebung**: Einheitliche Benennung von Branches und Commits erleichtert die Orientierung.
- **Dokumentation der Änderungen**: Alle Änderungen sollten in den entsprechenden Dokumentationen festgehalten werden, um die Nachvollziehbarkeit zu gewährleisten.

## Fazit
Ein strukturierter Git Workflow ist entscheidend für die Effizienz und Qualität in der Entwicklung von SPS-Code. Durch die Einhaltung der beschriebenen Prozesse und Best Practices kann das Team von TechMech Solutions GmbH sicherstellen, dass der Code stets stabil und wartbar ist.