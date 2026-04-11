# models/soil.py

class Soil:
    def __init__(self, moisture, ph):
        self.moisture = moisture
        self.ph = ph

    def display(self):
        print("Soil Moisture:", self.moisture, "| pH:", self.ph)