---
title: SPS-Programmierung Grundlagen für Kunden
space: SRV
parent: Schulungsunterlagen
level: 1
---

# SPS-Programmierung Grundlagen für Kunden

## Einleitung
Die SPS-Programmierung (Speicherprogrammierbare Steuerung) ist ein wesentlicher Bestandteil der Automatisierungstechnik. Diese Seite bietet einen Überblick über die Grundlagen der SPS-Programmierung, die für unsere Kunden von Bedeutung sind. Ziel ist es, ein Verständnis für die Funktionsweise und die Anwendungsmöglichkeiten von SPS-Systemen zu schaffen.

## Grundbegriffe der SPS-Programmierung
- **SPS**: Ein elektronisches Gerät, das zur Automatisierung von Maschinen und Prozessen verwendet wird.
- **Eingänge und Ausgänge**: Eingänge sind Signale von Sensoren, Ausgänge steuern Aktoren wie Motoren oder Ventile.
- **Programmiersprachen**: Die gängigsten Programmiersprachen sind:
  - **Ladder Diagram (LD)**: Grafische Programmierung, die Schaltplänen ähnelt.
  - **Funktionale Blockdiagramme (FBD)**: Visualisierung von Funktionen durch Blöcke.
  - **Structured Text (ST)**: Textbasierte Programmiersprache, ähnlich wie Pascal.

## SPS-Hardware
| Komponenten         | Beschreibung                                    |
|---------------------|------------------------------------------------|
| CPU                 | Zentrale Verarbeitungseinheit der SPS.        |
| I/O-Module          | Schnittstellen für digitale und analoge Ein-/Ausgänge. |
| Netzwerkkarten      | Ermöglichen die Kommunikation mit anderen SPS oder Systemen. |

## Programmierprozess
1. **Bedarfsanalyse**: Festlegung der Anforderungen und Zielsetzungen des Automatisierungsprojekts.
2. **Auswahl der SPS-Hardware**: Basierend auf den eingegebenen Signalen und der benötigten Reaktionszeit.
3. **Erstellung des Programms**: Implementierung der Logik in einer der oben genannten Programmiersprachen.
4. **Simulation und Test**: Vorabtests am PC oder an der SPS zur Fehlersuche und Validierung der Logik.
5. **Inbetriebnahme**: Implementierung des Programms in die SPS und Testlauf mit der realen Anlage.

## Beispielhafte Konfiguration
Für eine einfache Förderbandsteuerung könnte eine Konfiguration wie folgt aussehen:

- **Eingänge**: 
  - I0.0: Starttaste (Taster)
  - I0.1: Not-Aus (Schalter)
  
- **Ausgänge**: 
  - Q0.0: Förderband-Motor

### Ladder-Diagramm (LD) Beispiel
```plaintext
|---[I0.0]---(Q0.0)---|
|---[I0.1]---(RESET)---|
```
- **Erläuterung**: Das Förderband startet, wenn die Starttaste betätigt wird und stoppt, wenn der Not-Aus-Schalter aktiviert wird.

## Fazit
Die SPS-Programmierung ist ein zentraler Bestandteil der Automatisierungstechnik und ermöglicht eine flexible und effiziente Steuerung von Prozessen. Ein grundlegendes Verständnis dieser Technologie ist entscheidend für die erfolgreiche Implementierung von Automatisierungslösungen. Für weiterführende Informationen und spezifische Schulungsunterlagen wenden Sie sich bitte an unser Schulungsteam.