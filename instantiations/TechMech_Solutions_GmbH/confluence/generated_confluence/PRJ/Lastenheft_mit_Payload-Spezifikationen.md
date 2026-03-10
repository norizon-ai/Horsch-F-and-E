---
title: Lastenheft mit Payload-Spezifikationen
space: PRJ
parent: PRJ-2025-031 - FoodProc GmbH Palettierroboter
level: 2
---

# Lastenheft mit Payload-Spezifikationen

## 1. Einleitung
Im Rahmen des Projekts PRJ-2025-031 zur Entwicklung eines Palettierroboters für die FoodProc GmbH werden die spezifischen Anforderungen an die Payload und die damit verbundenen technischen Spezifikationen dokumentiert. Ziel ist es, eine robuste und effiziente Lösung zu entwickeln, die den Anforderungen der Lebensmittelindustrie gerecht wird.

## 2. Projektziele
- Entwicklung eines Palettierroboters, der eine flexible Handhabung von Produkten in unterschiedlichen Größen und Gewichten ermöglicht.
- Sicherstellung einer hohen Verfügbarkeit und Zuverlässigkeit im kontinuierlichen Betrieb.
- Integration in bestehende Produktionslinien der FoodProc GmbH.

## 3. Payload-Spezifikationen

### 3.1. Maximale Nutzlast
- **Maximale Nutzlast:** 150 kg
- **Verteilung der Last:** Gleichmäßige Verteilung auf die Greifvorrichtung

### 3.2. Produktvariabilität
Die folgenden Produkttypen müssen verarbeitet werden können:
| Produkttyp           | Gewicht (kg) | Abmessungen (mm)         |
|----------------------|--------------|--------------------------|
| Kartons (Standard)   | 10 - 15      | 400 x 300 x 200          |
| Plastikbehälter      | 5 - 8        | 300 x 200 x 150          |
| Glasflaschen         | 1 - 2        | 100 x 100 x 300          |
| Dosen                | 0.5 - 1      | 200 x 100 x 100          |

### 3.3. Greifmechanismus
- **Typ:** Vakuumgreifer mit anpassbaren Saugnäpfen
- **Saugnapfdurchmesser:** 100 mm (anpassbar)
- **Maximale Greifhöhe:** 2.500 mm
- **Minimale Greifhöhe:** 200 mm

## 4. Betriebsspezifikationen

### 4.1. Arbeitsbereich
- **Maximale Reichweite:** 2.000 mm
- **Drehbereich:** 360° (endlos drehbar)
- **Geschwindigkeit:** Maximal 1,5 m/s bei voller Nutzlast

### 4.2. Sicherheitsanforderungen
- Not-Aus Schalter an allen Zugangsstellen
- Sicherheitsumhausungen gemäß EN ISO 13857
- Einsatz von Lichtschranken zur Erkennung von Personen im Gefahrenbereich

## 5. Integration und Schnittstellen
Der Palettierroboter muss in bestehende Systeme integriert werden. Folgende Schnittstellen sind erforderlich:
- **IO-Link zur Ansteuerung**
- **Ethernet/IP für die Kommunikation mit der SPS**
- **RS-232 für externe Datenerfassung**

## 6. Schlussfolgerung
Das vorliegende Lastenheft beschreibt die wesentlichen Anforderungen an die Payload und die technischen Spezifikationen des Palettierroboters für die FoodProc GmbH. Die genannten Parameter sind entscheidend, um die Effizienz und Flexibilität der Produktionsprozesse zu gewährleisten. Weitere Details und Anpassungen werden in den folgenden Projektphasen erarbeitet.