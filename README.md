# ✋ Gesture Control Smart Home – Schulprojekt IT

## 📌 Projektbeschreibung
Dieses Projekt simuliert eine Smart-Home-Steuerung mittels Handgesten.
Über eine Webcam werden Gesten erkannt, mit denen Benutzer, Räume,
Licht und Rollos gesteuert werden können.

## 🛠 Verwendete Technologien
- Python 3
- Pygame (UI)
- OpenCV (Kamera)
- MediaPipe (Handtracking)

## 🧠 Programmstruktur
- main.py → Hauptprogramm
- config.py → Einstellungen & Konstanten
- utils.py → Hilfsfunktionen
- logging_system.py → CSV-Logging
- vision/ → Handtracking & State-Machine
- ui/ → Grafische Darstellung & Steuerung

## 🧩 Zustandsmaschine (States)
- USER_SELECT
- ROOM_SELECT
- CONTROL_SELECT
- LIGHT_CONTROL
- SHUTTER_CONTROL

## ✋ Gesten
| Geste | Funktion |
|------|---------|
| ☝ | Auswahl |
| ✌ | Alternative Auswahl |
| 👍 | Erhöhen |
| 👎 | Verringern |
| ✊ | Aus / Öffnen |
| 🤙 | An / Schließen |
| 🖕 | Zurück |

## ⚠ Bekannte Probleme
- Kamera darf nur einmal geöffnet werden
- Controller müssen mit Objekt-Attributen arbeiten
- Cooldown muss zentral gesteuert werden

## ✅ Lernziele
- Modularisierung
- Zustandsautomaten
- Computer Vision Grundlagen
- UI & Logik Trennung