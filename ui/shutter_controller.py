# Hier nur Rollosteuerung

from logging_system import write_log


def rollo_up(self, user):
        self.rollo_height = max(0, self.rollo_height - 5)
        write_log(user, f"{self.name}: Rollo hoch")

def rollo_down(self, user):
        self.rollo_height = min(self.window.height, self.rollo_height + 5)
        write_log(user, f"{self.name}: Rollo runter")