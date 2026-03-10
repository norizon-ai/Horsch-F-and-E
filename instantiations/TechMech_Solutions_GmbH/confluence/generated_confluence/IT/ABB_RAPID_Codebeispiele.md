---
title: ABB RAPID Codebeispiele
space: IT
parent: Roboterprogrammierung
level: 1
---

# ABB RAPID Codebeispiele

## Einleitung
In dieser Seite finden Sie eine Sammlung von ABB RAPID Codebeispielen, die als Grundlage für die Programmierung von Robotern in verschiedenen Anwendungen dienen. Die Beispiele decken grundlegende Funktionen bis hin zu komplexeren Programmlogiken ab und sind darauf ausgelegt, Fachleuten im Bereich der Automatisierungstechnik als Referenz zu dienen.

## Grundlagen der RAPID Programmierung
RAPID ist die Programmiersprache von ABB, die speziell für die Programmierung von Industrierobotern entwickelt wurde. Sie ermöglicht eine einfache und effiziente Steuerung von Roboterbewegungen, Sensoren und Aktoren.

### Wichtige Aspekte:
- **Datentypen**: VAR, BOOL, STRING, NUM
- **Bewegungsarten**: MoveJ (Joint), MoveL (Linear), MoveC (Circular)
- **Programmstruktur**: MODULE, PROC, VAR

## Beispiel 1: Einfacher Bewegungsablauf

```rapid
MODULE MainModule
    PROC Start
        ! Initialisierung der Roboterposition
        MoveJ [[1000, 0, 500], [0, 0, 1, 0], 100%], v100, z50, tool0;
        
        ! Bewege den Roboter zu einer neuen Position
        MoveL [[500, 500, 300], [0, 0, 1, 0], 100%], v200, z10, tool0;
    ENDPROC
ENDMODULE
```

### Erläuterung:
- **MoveJ**: Bewegung zu einer Gelenkposition.
- **MoveL**: Lineare Bewegung zu einer Koordinate.
- **v100**, **v200**: Geschwindigkeitseinstellungen in mm/s.
- **z50**, **z10**: Zonenbreite für das Annähern an die Zielposition.

## Beispiel 2: Verwendung von Schleifen und Bedingungen

```rapid
MODULE MainModule
    VAR num i;
    VAR BOOL isActive := TRUE;

    PROC Start
        FOR i := 1 TO 10 DO
            IF isActive THEN
                MoveL [[i*100, 0, 300], [0, 0, 1, 0], 100%], v200, z10, tool0;
            ENDIF
        ENDFOR
    ENDPROC
ENDMODULE
```

### Erläuterung:
- **FOR-Schleife**: Wiederholt den Bewegungsbefehl 10 Mal.
- **IF-Bedingung**: Überprüft, ob die Variable `isActive` aktiv ist, bevor die Bewegung ausgeführt wird.

## Beispiel 3: Einfache Fehlerbehandlung

```rapid
MODULE MainModule
    PROC Start
        VAR num result;

        result := MoveL [[500, 500, 300], [0, 0, 1, 0], 100%], v200, z10, tool0;
        IF result <> 0 THEN
            Write "Fehler bei der Bewegung!";
        ENDIF
    ENDPROC
ENDMODULE
```

### Erläuterung:
- **Fehlerüberprüfung**: Das Ergebnis der Bewegungsfunktion wird überprüft, und bei einem Fehler wird eine Warnmeldung ausgegeben.

## Fazit
Die oben genannten Beispiele bieten einen grundlegenden Überblick über die Programmierung mit ABB RAPID und können als Ausgangspunkt für weiterführende Projekte im Bereich der Roboterautomatisierung dienen. Für komplexere Anwendungen empfiehlt es sich, die ABB RAPID-Dokumentation zu konsultieren und zusätzliche Funktionen wie Sensorintegration oder Kommunikationsprotokolle zu berücksichtigen.