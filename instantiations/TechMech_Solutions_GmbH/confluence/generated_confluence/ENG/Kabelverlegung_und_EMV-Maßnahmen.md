---
title: Kabelverlegung und EMV-Maßnahmen
space: ENG
parent: Konstruktionsstandards
level: 2
---

# Kabelverlegung und EMV-Maßnahmen

## Einleitung
Die korrekte Kabelverlegung und die Umsetzung von EMV-Maßnahmen (Elektromagnetische Verträglichkeit) sind entscheidend für die Funktionalität und Zuverlässigkeit unserer automatisierten Systeme. Diese Seite beschreibt die relevanten Standards, Methoden und Best Practices zur Kabelverlegung und zur Sicherstellung der EMV-Konformität in unseren Projekten.

## Kabelverlegung

### Grundsätze der Kabelverlegung
- **Kabelwege**: Kabel sollten in festgelegten Kabelkanälen oder -trassen verlegt werden. Eine klare Trennung zwischen Signal- und Energiekabeln ist zwingend erforderlich.
- **Biegeradien**: Mindestens 10-facher Durchmesser des Kabels für die Biegung einhalten.
- **Vermeidung von Kreuzungen**: Überlappungen zwischen Signal- und Energiekabeln sind zu vermeiden, um Störungen zu reduzieren.

### Verlegemuster
| Kabeltyp          | Verlegemuster              | Bemerkungen                       |
|-------------------|----------------------------|-----------------------------------|
| Energiekabel      | Parallelverlegung           | Abstand mindestens 30 cm zu Signal- und Datenkabeln |
| Signalkabel       | Stern-Topologie             | Zentraler Verteilungspunkt empfohlen |
| Datenkabel        | Ringverbindung              | Minimierung von Laufzeitverzögerungen |

### Kabeltypen
- **Energiekabel**: H05VV-F, NYM-J
- **Signalkabel**: LiYY, LiYCY
- **Datenkabel**: CAT6a, RS-485

## EMV-Maßnahmen

### Vorgaben zur EMV-Optimierung
- **Abschirmung**: Alle Signalkabel müssen geschirmt sein (z.B. mit einer Alu- oder Kupferabschirmung).
- **Erdung**: Eine durchgängige Erdung aller Gehäuse und Kabelschirme ist erforderlich. Die Erdung sollte an einem Punkt erfolgen, um Erdschleifen zu vermeiden.
- **Filter**: Einsatz von EMV-Filterkomponenten (z.B. Ferritkerne) an den Kabelanschlüssen zur Reduzierung hochfrequenter Störungen.

### Messung der EMV
- **Messgeräte**: Zur Überprüfung der EMV-Konformität sollen geeignete Messgeräte (z.B. Oszilloskope, Spektrumanalysatoren) verwendet werden.
- **Messprotokoll**: Alle EMV-Messungen sind zu dokumentieren. Ein Beispielprotokoll könnte folgende Parameter enthalten:
  - Frequenzbereich: 30 MHz - 1 GHz
  - Grenzwert: 30 dBμV/m
  - Messpunkt: 3 m Abstand zur Quelle

### Typische EMV-Probleme
1. **Störstrahlungen**: Können durch ungeeignete Kabelverlegung oder unzureichende Abschirmung entstehen.
2. **Erdschleifen**: Entstehen durch mehrere Erdungspunkte; sollten durch starre Erdungskonzepte vermieden werden.
3. **Induktive Kopplung**: Signalverluste durch nahegelegene Energiekabel; Lösung: Verlegemuster anpassen.

## Fazit
Die Einhaltung der beschriebenen Richtlinien zur Kabelverlegung und EMV-Maßnahmen ist unerlässlich für die Funktionsfähigkeit unserer Systeme und die Zufriedenheit unserer Kunden. Durch konsequente Anwendung dieser Standards können wir die Qualität unserer Lösungen nachhaltig sichern.