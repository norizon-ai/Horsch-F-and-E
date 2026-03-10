---
title: SPS startet nicht - Checkliste
space: SRV
parent: Störungsdatenbank
level: 2
---

# SPS startet nicht - Checkliste

## Einleitung
Diese Checkliste dient zur systematischen Fehlersuche, wenn eine speicherprogrammierbare Steuerung (SPS) nicht startet. Die nachfolgenden Schritte sollen helfen, die häufigsten Ursachen zu identifizieren und zu beheben.

## 1. Stromversorgung prüfen
- **Überprüfen Sie die Netzspannung**: 
  - Erwartete Spannung: 24 V DC (oder gemäß Datenblatt)
  - Messen Sie die Spannung an den Versorgungsklemmen der SPS.
- **Sicherungen**: 
  - Überprüfen Sie die Sicherungen im Schaltschrank.
  - Sicherungstyp: T5A oder spezifisch laut Schaltplan.

## 2. Anschlussverbindungen kontrollieren
- **Kabelverbindungen**: 
  - Stellen Sie sicher, dass alle Kabel korrekt angeschlossen sind.
  - Überprüfen Sie insbesondere die Verbindungen zu den Ein- und Ausgängen.
- **Stecker**: 
  - Prüfen Sie, ob Stecker fest sitzen und keine Beschädigungen aufweisen.

## 3. Statusanzeigen auswerten
- **LED-Anzeigen**:
  - Prüfen Sie die Status-LEDs auf der SPS.
  - Beispiel: 
    - **Grün**: Betriebsbereit
    - **Rot**: Fehlerzustand
    - **Orange**: Wartemodus
- **Displayausgaben**: 
  - Bei SPS mit Display: Prüfen Sie auf Fehlermeldungen oder Statusanzeigen.

## 4. Konfiguration überprüfen
- **Software-Konfiguration**: 
  - Stellen Sie sicher, dass die SPS korrekt programmiert und konfiguriert ist.
  - Beispiel-Konfiguration:
    - Projektname: Automatisierungslinie_01
    - Firmware-Version: V2.3.1
- **Netzwerkkonfiguration**: 
  - Überprüfen Sie die IP-Adressen und Subnetze für eine korrekte Kommunikation.
  
## 5. Fehlerprotokolle einsehen
- **Protokolle**: 
  - Prüfen Sie die Fehlerprotokolle im SPS-Programm.
  - Typische Fehlercodes und deren Bedeutungen:
    - **F001**: Kommunikationsfehler
    - **F002**: Eingangsfehler
    - **F003**: Übertemperatur

## 6. Umgebungsbedingungen prüfen
- **Temperatur**: 
  - Messen Sie die Umgebungstemperatur: Idealbereich 0°C bis 50°C.
- **Feuchtigkeit**: 
  - Überprüfen Sie die relative Luftfeuchtigkeit: Idealbereich unter 85%.

## 7. Fachpersonal hinzuziehen
Sollten die oben genannten Schritte keine Lösung bringen, ziehen Sie bitte das Fachpersonal oder den technischen Support hinzu. Halten Sie relevante Informationen bereit, wie z.B. Fehlermeldungen, bisherige Maßnahmen und die verwendete Hardware.

## Fazit
Durch systematische Überprüfung der genannten Punkte sollte es möglich sein, das Problem der nicht startenden SPS zu identifizieren. Dokumentieren Sie alle Schritte und Ergebnisse zur weiteren Analyse oder zur Unterstützung des technischen Supports.