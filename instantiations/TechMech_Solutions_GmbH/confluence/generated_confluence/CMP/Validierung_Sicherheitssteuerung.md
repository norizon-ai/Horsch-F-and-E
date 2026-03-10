---
title: Validierung Sicherheitssteuerung
space: CMP
parent: Sicherheitsnormen
level: 2
---

# Validierung Sicherheitssteuerung

## Einleitung
Die Validierung von Sicherheitssteuerungen ist ein essenzieller Bestandteil der Entwicklung und Implementierung automatisierter Systeme. Sie gewährleistet, dass alle sicherheitsrelevanten Funktionen gemäß den geltenden Normen und Vorschriften ordnungsgemäß funktionieren. Diese Seite beschreibt den Validierungsprozess, die relevanten Normen sowie die erforderlichen Tests und Dokumentationen.

## Relevante Sicherheitsnormen
Die folgenden Normen sind für die Validierung von Sicherheitssteuerungen in der Automatisierungstechnik von Bedeutung:

- **ISO 13849-1**: Sicherheitsbezogene Teile von Steuerungen
- **IEC 62061**: Sicherheit von Maschinen – Sicherheitssteuerungen
- **EN 954-1**: Sicherheit von Maschinen – Sichere Steuerungssysteme

## Validierungsprozess
Der Validierungsprozess gliedert sich in mehrere Schritte:

1. **Anforderungsanalyse**
   - Identifizierung der sicherheitsrelevanten Funktionen
   - Festlegung der Sicherheitsanforderungen gemäß den Normen

2. **Designverifikation**
   - Überprüfung der Sicherheitsarchitektur
   - Sicherstellung der Einhaltung der Sicherheitskategorien gemäß ISO 13849-1

3. **Testplanung**
   - Definition der Testmethoden und -szenarien
   - Erstellung eines Testplans mit Zeitrahmen und zuständigen Personen

4. **Durchführung der Tests**
   - Funktionstest der sicherheitsrelevanten Steuerungen
   - Simulation von Fehlerszenarien zur Validierung der Reaktionen

5. **Dokumentation**
   - Vollständige Erfassung aller Testergebnisse
   - Erstellung eines Validierungsberichts als Nachweis der Konformität

## Beispielhafte Testkonfiguration
| Test-ID | Funktion              | Erwartetes Ergebnis                | Tatsächliches Ergebnis | Status       |
|---------|----------------------|-----------------------------------|-----------------------|--------------|
| T001    | Not-Aus-Funktion     | System stoppt innerhalb 0,5s     | 0,4s                  | Bestanden    |
| T002    | Sicherheits-Lichtschranke | Maschine stoppt bei Unterbrechung | Maschine läuft weiter   | Nicht bestanden |
| T003    | Überwachung der Sicherheitssteuerung | Fehlermeldung bei Fehler | Fehlermeldung angezeigt| Bestanden    |

## Fazit
Die Validierung der Sicherheitssteuerung ist entscheidend für die Sicherheit und Zuverlässigkeit automatisierter Systeme. Durch die systematische Durchführung der beschriebenen Schritte und die Einhaltung der Normen wird sichergestellt, dass alle sicherheitsrelevanten Funktionen korrekt implementiert sind. Eine umfassende Dokumentation unterstützt die Nachvollziehbarkeit und ist wichtig für zukünftige Audits und Zertifizierungen.