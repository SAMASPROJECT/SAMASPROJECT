# models/crop.py

class Crop:
    def __init__(self, name, stage, height):
        self.name = name
        self.stage = stage
        self.height = height

    def display(self):
        print("Crop:", self.name, "| Stage:", self.stage, "| Height:", self.height)