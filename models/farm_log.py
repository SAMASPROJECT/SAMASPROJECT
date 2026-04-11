# models/farm_log.py

class FarmLog:
    def __init__(self, date, crop, soil, environment):
        self.date = date
        self.crop = crop
        self.soil = soil
        self.environment = environment

    def display(self):
        print("\n--- Farm Log ---")
        print("Date:", self.date)
        self.crop.display()
        self.soil.display()
        self.environment.display()