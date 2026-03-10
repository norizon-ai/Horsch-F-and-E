---
title: Antriebsauslegung für RBS-2400
space: ENG
parent: Fördertechnik
level: 3
---

# Antriebsauslegung für RBS-2400

## Einleitung
Die RBS-2400 ist eine hochmoderne Roboterzelle, die speziell für den Einsatz in der Fördertechnik konzipiert wurde. Diese Seite beschreibt die Antriebsauslegung der RBS-2400, einschließlich der erforderlichen Spezifikationen, der Auswahl der Antriebskomponenten und der Berechnung der notwendigen Leistung.

## Anforderungsanalyse
Bevor mit der Antriebsauslegung begonnen wird, sind die spezifischen Anforderungen zu ermitteln:

- **Maximale Traglast:** 2400 kg
- **Betriebsdauer:** 24/7
- **Umgebungstemperatur:** 0°C bis 40°C
- **Anwendungsbereich:** Automobilindustrie, Lebensmittelverarbeitung, Pharmazeutik

## Antriebskomponenten

### 1. Motor
Für die RBS-2400 wird ein Drehstrom-Asynchronmotor empfohlen. Die folgenden Spezifikationen sind zu berücksichtigen:

| Parameter                | Wert                 |
|--------------------------|----------------------|
| Nennleistung             | 15 kW                |
| Drehmoment                | 95 Nm                |
| Nennspannung             | 400 V                |
| Drehzahl                 | 1500 U/min           |
| Schutzart                | IP55                 |

### 2. Getriebe
Ein Planetengetriebe wird zur Anpassung der Drehzahl und zur Erhöhung des Drehmoments eingesetzt. Die Auswahl des Getriebes erfolgt basierend auf den folgenden Kriterien:

- **Übersetzungsverhältnis:**  i = 5:1
- **Max. Eingangsdrehmoment:** 500 Nm
- **Wirkungsgrad:** 95%

### 3. Antriebstechnik
Für die Ansteuerung des Motors wird ein Frequenzumrichter benötigt. Der Frequenzumrichter sollte folgende Spezifikationen erfüllen:

| Parameter                | Wert                 |
|--------------------------|----------------------|
| Nennstrom                | 30 A                 |
| Eingangsfrequenz         | 50 Hz                |
| Ausgangsfrequenz         | 0 - 100 Hz           |
| Kommunikationsschnittstelle | Profibus, Ethernet  |

## Berechnung der Antriebsleistung
Die erforderliche Antriebsleistung \( P \) kann mit der Formel berechnet werden:

\[
P = \frac{T \cdot \omega}{1000}
\]

wobei:
- \( T \) = Drehmoment in Nm
- \( \omega \) = Winkelgeschwindigkeit in rad/s

Für die RBS-2400 ergibt sich bei einem Drehmoment von 95 Nm und einer Drehzahl von 1500 U/min (25.13 rad/s):

\[
P = \frac{95 \cdot 25.13}{1000} \approx 2.39 \text{ kW}
\]

### Sicherheitsfaktor
Um eine zuverlässige Betriebsweise zu gewährleisten, sollte ein Sicherheitsfaktor von 1,5 angewendet werden. Daher ist eine Nennleistung des Motors von mindestens 15 kW gerechtfertigt.

## Zusammenfassung
Die Antriebsauslegung der RBS-2400 erfordert die sorgfältige Auswahl von Motor, Getriebe und Frequenzumrichter, um die spezifischen Anforderungen der jeweiligen Branche zu erfüllen. Mit den genannten Komponenten und den durchgeführten Berechnungen ist die Roboterzelle in der Lage, eine maximale Traglast von 2400 kg effizient zu bewegen und die geforderten Betriebsbedingungen zu erfüllen.