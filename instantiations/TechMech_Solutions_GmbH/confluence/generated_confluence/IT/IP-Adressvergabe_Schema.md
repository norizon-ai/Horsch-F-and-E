---
title: IP-Adressvergabe Schema
space: IT
parent: Netzwerkkonfiguration
level: 1
---

# IP-Adressvergabe Schema

**Einleitung**  
Die IP-Adressvergabe ist ein zentraler Bestandteil der Netzwerkinfrastruktur bei TechMech Solutions GmbH. Diese Seite beschreibt das Schema zur Vergabe von IP-Adressen in unseren Unternehmensnetzen, um eine effiziente und fehlerfreie Kommunikation zwischen den Geräten zu gewährleisten.

## IP-Adressbereich

| Netzwerkanwendung       | IP-Adressbereich         | Subnetzmaske      |
|-------------------------|--------------------------|--------------------|
| Büroverwaltung           | 192.168.1.0 – 192.168.1.255 | 255.255.255.0      |
| Entwicklungsumgebung    | 192.168.2.0 – 192.168.2.255 | 255.255.255.0      |
| Produktionsnetz         | 192.168.3.0 – 192.168.3.255 | 255.255.255.0      |
| Gastnetz                | 192.168.4.0 – 192.168.4.255 | 255.255.255.0      |

## Vergabeverfahren

Die Vergabe der IP-Adressen erfolgt nach dem DHCP (Dynamic Host Configuration Protocol)-Verfahren. Folgende Schritte sind notwendig:

1. **DHCP-Server Konfiguration**: Der DHCP-Server wird mit den oben genannten IP-Adressbereichen konfiguriert.
2. **Lease-Dauer**: Die Standard-Lease-Dauer für dynamisch vergebene IP-Adressen beträgt 24 Stunden. Diese kann je nach Bedarf angepasst werden.
3. **Reservierungen**: Für bestimmte Geräte (z.B. Drucker, Server) sollten statische IP-Adressen reserviert werden, um eine konsistente Erreichbarkeit zu gewährleisten.

## Statische IP-Adressen

Für kritische Systeme, die keine dynamische IP-Adresse erhalten sollten, werden statische IP-Adressen vergeben. Die folgenden Geräte sind davon betroffen:

- **Server**: 
  - Anwendungsserver: 192.168.1.10
  - Datenbankserver: 192.168.1.11
- **Drucker**:
  - Netzwerkdrucker Büros: 192.168.1.20
  - Produktionsdrucker: 192.168.3.20

## Dokumentation und Änderung

Änderungen an der IP-Adressvergabe sollten dokumentiert und in der zentralen IT-Dokumentation festgehalten werden. Dies umfasst:

- Datum der Änderung
- Verantwortliche Person
- Beschreibung der Änderung
- Grund für die Änderung

## Sicherheitsrichtlinien

Um die Sicherheit des Netzwerks zu gewährleisten, sind folgende Richtlinien zu beachten:

- **Zugriffssteuerung**: Nur autorisierte Mitarbeiter dürfen Änderungen an der DHCP-Serverkonfiguration vornehmen.
- **Netzwerküberwachung**: Alle IP-Adressen und deren Nutzung müssen regelmäßig überwacht werden, um unautorisierte Zugriffe zu identifizieren.

## Fazit

Die Einhaltung des IP-Adressvergabe-Schemas ist entscheidend für eine stabile und sichere Netzwerkumgebung bei TechMech Solutions GmbH. Bei Fragen oder Unsicherheiten bezüglich der Vergabe von IP-Adressen wenden Sie sich bitte an die IT-Abteilung.