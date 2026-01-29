# Hier kommen Konstanten und Einstellungen rein
# Modularisierung, Wartbarkeit, Saubere Struktur, Trennung von Logik & Konfiguration

import pygame
from ui.light_controller import toggle_light
from ui.shutter_controller import rollo_up, rollo_down

# Fenster
WIDTH = 800
HEIGHT = 600
FPS = 60
WINDOW_TITLE = "Schulaufgabe IT"

# Farben
WALL = (30, 30, 30)
FLOOR = (200, 190, 170)
WINDOW_COLOR = (180, 220, 255)
ROLLO = (120, 120, 120)
DARK = (0, 0, 0, 180)
BACKGROUND = (50, 50, 50)

# Schrift
FONT_SIZE = 36

# Benutzer
DEFAULT_USER = "user_a"

# -------------------------
# TASTENBELEGUNG
# -------------------------

KEYS = {
    # Raum 1 – Wohnküche
    pygame.K_1: ("room_1", toggle_light),
    pygame.K_q: ("room_1", rollo_up),
    pygame.K_a: ("room_1", rollo_down),

    # Raum 2 – Schlafzimmer
    pygame.K_2: ("room_2", toggle_light),
    pygame.K_w: ("room_2", rollo_up),
    pygame.K_s: ("room_2", rollo_down),

    # Benutzer wechseln
    pygame.K_p: ("user", "user_a"),
    pygame.K_o: ("user", "user_b"),
}