---
title: VPN-Zugang für Fernwartung
space: IT
parent: Netzwerkkonfiguration
level: 1
---

# VPN-Zugang für Fernwartung

## Einleitung
Der VPN-Zugang (Virtual Private Network) ermöglicht es unseren Technikern, sicher und effizient auf die Systeme und Maschinen unserer Kunden zuzugreifen. Insbesondere bei der Fernwartung ist eine stabile und gesicherte Verbindung unerlässlich, um Ausfallzeiten zu minimieren und schnelle Lösungen zu bieten.

## Voraussetzungen
Um einen VPN-Zugang für die Fernwartung einrichten zu können, sind folgende Voraussetzungen erforderlich:

- **VPN-Client**: Installation des passenden VPN-Clients auf dem Endgerät (z.B. OpenVPN, Cisco AnyConnect)
- **Zugangsdaten**: Bereitstellung von Benutzername und Passwort durch die IT-Abteilung
- **Erlaubte IP-Adressen**: Die IP-Adresse des externen Geräts muss in der Firewall-Konfiguration freigegeben werden

## Einrichtung des VPN-Zugangs

### Schritt 1: Installation des VPN-Clients
1. Laden Sie den entsprechenden VPN-Client von der offiziellen Website herunter.
2. Folgen Sie den Installationsanweisungen und schließen Sie die Installation ab.

### Schritt 2: Konfiguration des VPN-Clients
- **Serveradresse**: `vpn.techmech-solutions.de`
- **Protokoll**: OpenVPN oder IKEv2 (je nach Client)
- **Port**: 1194 (Standardport für OpenVPN)

#### Beispielkonfiguration (OpenVPN):
```plaintext
client
dev tun
proto udp
remote vpn.techmech-solutions.de 1194
resolv-retry infinite
nobind
persist-key
persist-tun
remote-cert-tls server
auth SHA256
cipher AES-256-CBC
```

### Schritt 3: Verbindung herstellen
1. Starten Sie den VPN-Client.
2. Geben Sie Ihre Zugangsdaten ein.
3. Klicken Sie auf „Verbinden“ und warten Sie, bis die Verbindung hergestellt ist.

## Sicherheitshinweise
- Verwenden Sie stets starke Passwörter und ändern Sie diese regelmäßig.
- Stellen Sie sicher, dass Ihre Firewall aktiv ist und aktuelle Sicherheitsupdates installiert sind.
- Bei Verbindungsproblemen oder Sicherheitsvorfällen wenden Sie sich umgehend an die IT-Abteilung.

## Troubleshooting
| Problem                      | Mögliche Ursache                           | Lösung                                    |
|-----------------------------|-------------------------------------------|-------------------------------------------|
| Keine Verbindung möglich     | Falsche Zugangsdaten                      | Zugangsdaten überprüfen                   |
| Langsame Verbindung          | Hohe Netzwerklast                         | Verbindung außerhalb der Stoßzeiten testen |
| Verbindungsabbrüche         | Instabile Internetverbindung              | Internetverbindung überprüfen              |

## Fazit
Der VPN-Zugang für die Fernwartung ist ein sicheres und effektives Mittel, um unseren Kunden schnellstmöglich Unterstützung bieten zu können. Bei Fragen oder Problemen wenden Sie sich bitte an die IT-Abteilung unter it-support@techmech-solutions.de.