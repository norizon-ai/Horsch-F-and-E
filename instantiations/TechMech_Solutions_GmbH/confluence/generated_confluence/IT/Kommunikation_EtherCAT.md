---
title: Kommunikation EtherCAT
space: IT
parent: SPS-Programmierung
level: 2
---

# Kommunikation EtherCAT

## Einleitung

EtherCAT (Ethernet for Control Automation Technology) ist ein hochperformantes Ethernet-basiertes Feldbussystem, das insbesondere für die Automatisierungstechnik und den Maschinenbau genutzt wird. Diese Seite beschreibt die Grundlagen der EtherCAT-Kommunikation, deren Implementierung in SPS-Programmen und die relevanten Spezifikationen.

## Grundlagen der EtherCAT-Kommunikation

EtherCAT ermöglicht die Echtzeitkommunikation zwischen Steuerungen (SPS) und Peripheriegeräten. Die Hauptmerkmale sind:

- **Echtzeitfähigkeit**: Übertragungszeiten im Mikrosekundenbereich.
- **Flexibilität**: Unterstützung von verschiedenen Topologien (z.B. Linien-, Baum- und Ringtopologien).
- **Kosteneffizienz**: Verwendung von Standard-Ethernet-Hardware.

## EtherCAT-Topologien

Die gängigsten Topologien für EtherCAT-Netzwerke sind:

| Topologie   | Beschreibung                                         |
|-------------|-----------------------------------------------------|
| Linien      | Geräte sind in einer geraden Linie verbunden.       |
| Baum        | Geräte sind in einer baumartigen Struktur angeordnet.|
| Ring        | Geräte sind in einem geschlossenen Ring verbunden.  |

## Kommunikation und Protokolle

Die Kommunikation erfolgt über EtherCAT-Frames, die in einer speziellen Struktur vorliegen:

1. **SyncFrame**: Synchronisation der Teilnehmer.
2. **ProcessDataFrame**: Übertragung von Prozessdaten.
3. **ServiceFrame**: Verwendung für Diagnose- und Konfigurationsdaten.

### Beispiel eines EtherCAT-Frames

| Feld               | Größe (Byte) | Beschreibung                   |
|--------------------|--------------|---------------------------------|
| EtherCAT Header    | 14           | Standard Ethernet Header       |
| EtherCAT Command    | 2            | Befehlsart (z.B. lesen, schreiben) |
| Datenlängen        | 2            | Länge der Daten                 |
| Prozessdaten       | variable      | Nutzdaten, abhängig von der Anwendung |

## Implementierung in SPS-Programmen

Für die Implementierung von EtherCAT in SPS-Programmen sind folgende Schritte erforderlich:

1. **Netzwerkkonfiguration**: Einrichten der EtherCAT-Schnittstelle in der SPS-Programmiersoftware.
2. **Geräteanbindung**: Hinzufügen der EtherCAT-Geräte über die Software.
3. **Parameterkonfiguration**: Anpassen der Geräteparameter gemäß den spezifischen Anforderungen der Anwendung.

### Beispielhafte Konfiguration

| Parameter            | Wert          |
|----------------------|---------------|
| Zykluszeit           | 1 ms          |
| Max. Geräteanzahl    | 64            |
| PDOs pro Gerät       | 4             |

## Schlussfolgerung

Die EtherCAT-Technologie bietet eine leistungsstarke und flexible Lösung für die Automatisierungstechnik. Durch die Echtzeitkommunikation und die einfache Integration in bestehende Systeme kann die Effizienz in der Produktion erheblich gesteigert werden. Die Implementierung erfordert jedoch eine sorgfältige Planung und Konfiguration, um die vollen Vorteile der Technologie auszuschöpfen.