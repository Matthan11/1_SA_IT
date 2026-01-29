# Hier nur die Lichtsteurung


from logging_system import write_log

def toggle_light(self, user):
    self.light_on = not self.light_on
    action = f"{self.name}: Licht {'AN' if self.light_on else 'AUS'}"
    write_log(user, action)