---
title: Firewall-Regeln für Anlagenvernetzung
space: IT
parent: Cyber Security
level: 1
---

# Firewall-Regeln für Anlagenvernetzung

## Einleitung
Im Rahmen der Cyber Security ist die Absicherung der Anlagenvernetzung von zentraler Bedeutung, um unbefugte Zugriffe und potenzielle Sicherheitsvorfälle zu verhindern. Diese Seite beschreibt die erforderlichen Firewall-Regeln zur Sicherstellung einer sicheren Kommunikation zwischen den verschiedenen Systemen innerhalb der TechMech Solutions GmbH.

## Grundlegende Sicherheitsrichtlinien
Die folgenden Grundsätze sollten bei der Implementierung der Firewall-Regeln beachtet werden:

- **Minimalprinzip**: Nur die notwendigsten Ports und Protokolle freigeben.
- **Standardmäßig blockieren**: Alle nicht explizit genehmigten Verbindungen sollten standardmäßig blockiert werden.
- **Überwachung und Protokollierung**: Alle Zugriffe und Verbindungsversuche sind zu protokollieren und regelmäßig zu überprüfen.

## Firewall-Regeln

| Regel-Nr. | Quelle (IP/Netzwerk) | Ziel (IP/Netzwerk) | Port/Protokoll | Aktion      | Beschreibung                          |
|-----------|----------------------|--------------------|----------------|-------------|---------------------------------------|
| 1         | 192.168.1.0/24       | 192.168.2.0/24     | TCP 80         | Erlauben    | Zugriff auf HTTP-Dienste der Steuerung |
| 2         | 192.168.2.0/24       | 192.168.1.0/24     | TCP 443        | Erlauben    | Zugriff auf HTTPS-Dienste der Datenbank |
| 3         | 192.168.1.10         | 192.168.1.11       | UDP 123        | Erlauben    | NTP-Zugriff für Zeitabgleich         |
| 4         | 192.168.1.0/24       | 0.0.0.0/0          | TCP 22         | Blockieren  | SSH-Zugriff von extern blockieren    |
| 5         | 192.168.2.0/24       | 192.168.3.0/24     | TCP 8080       | Erlauben    | Zugriff auf interne Webanwendungen    |
| 6         | 192.168.3.0/24       | 192.168.1.0/24     | ICMP            | Erlauben    | Ping-Zugriffe für Netzwerkdiagnose    |

## Beispielkonfiguration
### Beispiel für eine Cisco ASA Firewall
Die folgende Konfiguration zeigt, wie die oben genannten Regeln in einer Cisco ASA Firewall implementiert werden können:

```plaintext
object network obj-192.168.1.0
  subnet 192.168.1.0 255.255.255.0

object network obj-192.168.2.0
  subnet 192.168.2.0 255.255.255.0

access-list outside_access_in extended permit tcp object obj-192.168.1.0 object obj-192.168.2.0 eq 80
access-list outside_access_in extended permit tcp object obj-192.168.2.0 object obj-192.168.1.0 eq 443
access-list outside_access_in extended permit udp host 192.168.1.10 host 192.168.1.11 eq 123
access-list outside_access_in extended deny tcp object obj-192.168.1.0 any eq 22
access-list outside_access_in extended permit tcp object obj-192.168.2.0 object obj-192.168.3.0 eq 8080
access-list outside_access_in extended permit icmp object obj-192.168.3.0 object obj-192.168.1.0
```

## Monitoring und Wartung
Die Firewall-Regeln sollten regelmäßig überprüft und an die sich ändernden Anforderungen der Anlagenvernetzung angepasst werden. Eine monatliche Überprüfung der Protokolle und der Regelkonfiguration ist empfehlenswert, um potenzielle Sicherheitsrisiken frühzeitig zu erkennen. 

## Fazit
Die Implementierung und Pflege von Firewall-Regeln ist ein essenzieller Bestandteil der Cyber-Security-Strategie der TechMech Solutions GmbH. Durch die Einhaltung der hier beschriebenen Richtlinien und Regeln kann die Sicherheit der Anlagenvernetzung signifikant erhöht werden.