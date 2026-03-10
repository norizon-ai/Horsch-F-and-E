---
title: Strukturierter Text Best Practices
space: IT
parent: SPS-Programmierung
level: 2
---

# Strukturierter Text Best Practices

## Einleitung
Strukturierter Text (ST) ist eine Hochsprache, die in der Programmierung von speicherprogrammierbaren Steuerungen (SPS) weit verbreitet ist. Um die Lesbarkeit, Wartbarkeit und Effizienz von ST-Code zu maximieren, sind einige Best Practices zu beachten.

## 1. Allgemeine Codierungsrichtlinien

### 1.1. Einrückungen und Formatierung
- Halten Sie eine konsistente Einrückung von 4 Leerzeichen für Codeblöcke ein.
- Verwenden Sie Leerzeilen, um logische Abschnitte zu trennen.
- Kommentare sollten stets in der Nähe des relevanten Codes platziert werden.

### 1.2. Benennungskonventionen
- Variablen: `v_Name` (z.B. `v_TempSensor`)
- Funktionen: `f_Name` (z.B. `f_BerechneDruck`)
- Konstanten: `c_Name` (z.B. `c_MaxDruck`)

## 2. Strukturierung des Codes

### 2.1. Modularer Aufbau
- Nutzen Sie Funktionen und Funktionsbausteine, um Code zu kapseln und Wiederholungen zu vermeiden.
- Beispiel:
    ```structured-text
    FUNCTION f_BerechneDruck : REAL
    VAR_INPUT
        v_Temp : REAL;
        v_Volumen : REAL;
    END_VAR
    
    f_BerechneDruck := v_Temp * v_Volumen; 
    ```

### 2.2. Verwendung von Datenstrukturen
- Definieren Sie benutzerdefinierte Datentypen zur besseren Organisation von Daten. 
- Beispiel:
    ```structured-text
    TYPE t_Fahrzeug
    STRUCT
        v_Geschwindigkeit : REAL;
        v_Richtung : INT;
    END_STRUCT
    END_TYPE
    ```

## 3. Fehlerbehandlung 

### 3.1. Verwendung von Statusvariablen
- Implementieren Sie Statusvariablen zur Überwachung des Programmstatus.
- Beispiel:
    ```structured-text
    IF v_Status = 0 THEN
        v_Status := 1; // Fehlerfall
    END_IF
    ```

### 3.2. Logging
- Führen Sie ein Protokoll über kritische Ereignisse, um die Fehlersuche zu erleichtern.
- Beispiel:
    ```structured-text
    IF v_ErrorFlag THEN
        LogError('Fehler im System', v_ErrorCode);
    END_IF
    ```

## 4. Testen und Validierung

### 4.1. Unit-Tests
- Erstellen Sie Unit-Tests für jede Funktion, um deren Korrektheit sicherzustellen.
- Beispiel:
    ```structured-text
    TEST f_BerechneDruck
    INPUT: v_Temp := 25.0, v_Volumen := 10.0;
    EXPECT: f_BerechneDruck = 250.0;
    ```

### 4.2. Simulation
- Nutzen Sie Simulationswerkzeuge, um das Verhalten des Codes unter verschiedenen Bedingungen zu testen.

## Fazit
Die Anwendung dieser Best Practices für strukturierten Text in der SPS-Programmierung trägt maßgeblich zur Verbesserung der Qualität und Wartbarkeit des Codes bei. Durch klare Strukturierung, modulare Programmierung und sorgfältige Fehlerbehandlung können langfristig Zeit und Ressourcen gespart werden.