# utils/validators.py

def validate_moisture(m):
    if m < 0:
        print("Invalid moisture")
        return False
    return True

def validate_ph(ph):
    if ph < 0 or ph > 14:
        print("Invalid pH")
        return False
    return True

def validate_temp(t):
    if t < -10 or t > 60:
        print("Invalid temperature")
        return False
    return True