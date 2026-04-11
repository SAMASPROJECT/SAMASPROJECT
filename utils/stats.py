# utils/stats.py

def average_moisture(logs):
    if not logs:
        return 0

    total = 0
    i = 0
    while i < len(logs):
        total += logs[i].soil.moisture
        i += 1

    return total / len(logs)

def max_temperature(logs):
    if not logs:
        return 0

    max_temp = logs[0].environment.temperature
    i = 1

    while i < len(logs):
        if logs[i].environment.temperature > max_temp:
            max_temp = logs[i].environment.temperature
        i += 1

    return max_temp