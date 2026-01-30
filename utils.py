def clamp_shutter(value):   # Maximal und Minimal wert des Rollos 
    return max(0, min(50, value))

def clamp_light(value):   # Maximal und Minimal wert des Rollos 
    return max(0, min(100, value))