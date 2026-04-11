# models/environment.py

class Environment:
    def __init__(self, temperature, humidity, rainfall):
        self.temperature = temperature
        self.humidity = humidity
        self.rainfall = rainfall

    def display(self):
        print("Temp:", self.temperature, "| Humidity:", self.humidity, "| Rainfall:", self.rainfall)