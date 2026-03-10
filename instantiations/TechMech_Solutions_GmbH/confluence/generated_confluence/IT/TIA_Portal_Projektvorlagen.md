---
title: TIA Portal Projektvorlagen
space: IT
parent: SPS-Programmierung
level: 2
---

# TIA Portal Projektvorlagen

## Einleitung
Das TIA Portal (Totally Integrated Automation Portal) ist die integrierte Softwareumgebung von Siemens für die Automatisierungstechnik. Um die Effizienz bei der SPS-Programmierung zu steigern und Konsistenz über Projekte hinweg zu gewährleisten, stellen wir verschiedene Projektvorlagen zur Verfügung. Diese Vorlagen sind für unterschiedliche Anwendungen und Branchen optimiert.

## Projektvorlagen Übersicht

| Vorlage               | Beschreibung                                        | Branchen                      | Anwendungsbereich                     |
|----------------------|----------------------------------------------------|-------------------------------|---------------------------------------|
| **Roboterzelle**     | Vorlage zur Integration von Robotersystemen       | Automotive, Lebensmittel      | Montage, Verpackung                   |
| **Fördertechnik**    | Vorlage zur Steuerung von Förderanlagen            | Pharma, Automotive            | Materialtransport, Logistik           |
| **Qualitätsprüfung**  | Vorlage zur Implementierung von Prüfstandsystemen  | Pharma, Lebensmittel          | Qualitätssicherung, Testautomatisierung|

## Vorlagen Details

### 1. Roboterzelle
**Hardware:**  
- SPS: Siemens S7-1500  
- Steuerung: TIA Portal V15.1  
- Roboter: KUKA KR AGILUS

**Software-Konfiguration:**  
- Programmstruktur: OB1 (Hauptprogramm), FB1 (Robotersteuerung), FB2 (Sensorintegration)  
- Kommunikationsprotokoll: Profinet

**Beispieldaten:**  
- Roboterbewegung: Geschwindigkeit 1 m/s, Beschleunigung 2 m/s²  
- Sensoren: Lichtschranken, die bei Objekterkennung aktiv werden

### 2. Fördertechnik
**Hardware:**  
- SPS: Siemens S7-1200  
- Steuerung: TIA Portal V14.0  
- Antrieb: Siemens G120C Frequenzumrichter

**Software-Konfiguration:**  
- Programmstruktur: OB1 (Hauptprogramm), FB1 (Förderbandsteuerung)  
- Kommunikationsprotokoll: Profibus DP

**Beispieldaten:**  
- Förderbandgeschwindigkeit: 0,5 m/s  
- Not-Aus-Funktion: Integriert in das Hauptprogramm zur Sicherheitsüberwachung

### 3. Qualitätsprüfung
**Hardware:**  
- SPS: Siemens S7-1500  
- Steuerung: TIA Portal V15.0  
- Prüfstand: Vision-System von Basler

**Software-Konfiguration:**  
- Programmstruktur: OB1 (Hauptprogramm), FB1 (Bildverarbeitung), FB2 (Datenlogging)  
- Kommunikationsprotokoll: Profinet und MQTT für Cloud-Anbindung

**Beispieldaten:**  
- Prüfparameter: Bildauflösung 1920x1080, Prüfzeit pro Bild 0,5 s  
- Reporting: Automatisierte Erstellung von Prüfberichten im CSV-Format

## Nutzung der Vorlagen
Die bereitgestellten Vorlagen können durch Anpassung der spezifischen Parameter und Funktionen an die individuellen Anforderungen des Projektes angepasst werden. Bitte beachten Sie, dass jede Vorlage mit den neuesten Sicherheitsstandards und Normen konform ist.

## Fazit
Die Verwendung von TIA Portal Projektvorlagen ermöglicht eine schnellere Implementierung von Automatisierungslösungen und minimiert Fehlerquellen. Für weitere Informationen oder individuelle Anpassungen wenden Sie sich bitte an die IT-Abteilung oder die Fachabteilung Automatisierungstechnik.