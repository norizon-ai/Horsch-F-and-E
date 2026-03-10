---
title: Ventil schaltet nicht - Prüfablauf
space: SRV
parent: Störungsdatenbank
level: 2
---

# Ventil schaltet nicht - Prüfablauf

## Einleitung
Diese Seite beschreibt den Prüfablauf zur Identifizierung von Fehlern, die dazu führen können, dass ein Ventil in einer automatisierten Anlage nicht ordnungsgemäß schaltet. Der Prüfablauf ist für Techniker und Instandhaltungsmitarbeiter gedacht und soll eine systematische Fehlersuche ermöglichen.

## Voraussetzungen
- Zugang zu den Steuerungs- und Diagnosewerkzeugen
- Sicherheitsunterweisungen beachtet
- Notwendige persönliche Schutzausrüstung (PSA)

## Prüfablauf

### 1. Sichtprüfung
- Überprüfen Sie alle elektrischen Verbindungen zum Ventil auf Beschädigungen oder lose Kontakte.
- Stellen Sie sicher, dass keine mechanischen Blockaden das Ventil behindern.
- Prüfen Sie die pneumatischen/hydraulischen Anschlüsse auf Leckagen.

### 2. Elektrische Überprüfung
- **Multimeter verwenden:** Messen Sie die Spannung am Ventilantrieb.
    - Erwartete Messwerte: 24 V DC (bei Verwendung von 24 V Ventilen)
- Überprüfen Sie die Signalführung zum Steuergerät.
    - Prüfen Sie die Anschlussbelegung gemäß der Schaltpläne.

### 3. Steuerung und Software
- Überprüfen Sie die Programmierung der Steuerung auf fehlerhafte Logik.
- Führen Sie eine Diagnose über die Steuerungssoftware durch:
    - **Beispiel:** Wenn das Ventil bei „Betriebsart MANUELL“ nicht schaltet, überprüfen Sie die entsprechenden Eingabewerte.
- Notieren Sie Fehlermeldungen, die im System angezeigt werden.

### 4. Funktionstest
- Führen Sie einen manuellen Test des Ventils durch:
    - Aktivieren Sie das Ventil manuell über die Steuerung.
    - Beobachten Sie die Reaktion des Ventils und protokollieren Sie das Verhalten.
- **Protokollierung:**
    | Test       | Erwartetes Verhalten | Tatsächliches Verhalten | Anmerkungen         |
    |------------|---------------------|------------------------|---------------------|
    | Manuelle Aktivierung | Ventil öffnet/schließt | [Eintrag hier]   | [Eintrag hier]      |

### 5. Austausch und Wartung
- Falls das Ventil nach den oben genannten Prüfungen weiterhin nicht funktioniert, prüfen Sie die Möglichkeit eines Austauschs.
- Stellen Sie sicher, dass das Ersatzventil den folgenden Spezifikationen entspricht:
    - Typ: [z.B. pneumatisches Regelventil]
    - Nennweite: [z.B. DN 15]
    - Druckbereich: [z.B. 0-10 bar]

## Abschluss
Nach Abschluss der Prüfungen und gegebenenfalls durchgeführten Reparaturen sollte das Ventil erneut getestet werden, um die ordnungsgemäße Funktion sicherzustellen. Dokumentieren Sie alle durchgeführten Schritte und Ergebnisse in der Störungsdatenbank zur späteren Referenz. Bei weiteren Fragen oder Unsicherheiten wenden Sie sich bitte an den technischen Support.