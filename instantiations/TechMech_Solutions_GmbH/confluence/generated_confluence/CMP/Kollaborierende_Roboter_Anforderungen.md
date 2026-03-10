---
title: Kollaborierende Roboter Anforderungen
space: CMP
parent: Sicherheitsnormen
level: 2
---

# Kollaborierende Roboter Anforderungen

## Einleitung
Kollaborierende Roboter (Cobots) sind eine zentrale Komponente in modernen Automatisierungslösungen. Diese Roboter sind so konzipiert, dass sie sicher und effizient mit Menschen in gemeinsamen Arbeitsumgebungen interagieren können. Die Anforderungen an diese Systeme müssen sorgfältig definiert werden, um sowohl die Sicherheit der Mitarbeiter als auch die Effizienz der Produktionsprozesse zu gewährleisten.

## Sicherheitsnormen
Die Sicherheitsanforderungen für kollaborierende Roboter basieren auf verschiedenen Normen, insbesondere der ISO 10218 und der ISO/TS 15066. Diese Normen legen die Grundsätze für die Sicherheit von Robotern und deren Interaktion mit Menschen fest. 

### Wesentliche Sicherheitsanforderungen
1. **Kollisionsvermeidung**: Cobots müssen in der Lage sein, Kollisionen mit Menschen zu erkennen und zu vermeiden. Dies kann durch:
   - **Sensorik**: Verwendung von Lichtsensoren, Drucksensoren oder Kameras.
   - **Not-Aus-Funktion**: Roboter müssen sofort anhalten, wenn ein Not-Aus betätigt wird.
  
2. **Kraft- und Druckbegrenzung**: Die maximalen Kräfte, die ein Cobot auf einen menschlichen Bediener ausüben kann, müssen begrenzt sein. Typische Werte sind:
   - Maximale Kraft: ≤ 140 N
   - Maximale Druckkraft: ≤ 60 N

3. **Sichere Programmierung**: Die Programmierung der Roboter muss so gestaltet sein, dass sicherheitskritische Funktionen nicht umgangen werden können. Hierzu gehören:
   - **Zugriffsrechte**: Nur autorisierte Benutzer dürfen Änderungen an sicherheitsrelevanten Parametern vornehmen.
   - **Sicherheitsprotokolle**: Implementierung von Protokollen zur Überprüfung der Sicherheitseinstellungen.

## Technische Spezifikationen
| Spezifikation            | Wert             |
|-------------------------|------------------|
| Max. Traglast           | 5-20 kg          |
| Reichweite               | 500-1500 mm      |
| Genauigkeit              | ±0,1 mm          |
| Geschwindigkeit         | bis zu 2 m/s     |
| Programmierbarkeit       | grafisch und textbasiert |

## Anwendungsbeispiele
### Beispiel 1: Montagezelle in der Automobilindustrie
- **Cobot-Modell**: UR10e
- **Anwendung**: Montage von Fahrzeuginnenausstattungen
- **Sicherheitsmechanismen**: Integrierte Kraftbegrenzung, Sicherheitsumhausung, Not-Aus-Taster an mehreren Positionen

### Beispiel 2: Verpackungslinie in der Lebensmittelindustrie
- **Cobot-Modell**: KUKA LBR iiwa
- **Anwendung**: Verpacken von Lebensmitteln in Kartons
- **Sicherheitsmechanismen**: 3D-Kollisionsvermeidung, Sensoren zur Gewichtsüberprüfung, Sicherheitszertifizierungen nach ISO 22000

## Fazit
Die Anforderungen an kollaborierende Roboter sind entscheidend für die erfolgreiche Implementierung in verschiedenen Industrien. Durch die Einhaltung der Sicherheitsnormen und die Berücksichtigung technischer Spezifikationen können Unternehmen wie die TechMech Solutions GmbH effiziente und sichere Automatisierungslösungen anbieten.