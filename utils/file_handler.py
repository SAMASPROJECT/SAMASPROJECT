# utils/file_handler.py

import pandas as pd
import os

FILE_PATH = "C:/Users/MOHANA KRISHNA REDDY/PycharmProjects/PythonProject/PROJECT SAMAS/utils/data/farm_logs.csv"

def save_to_csv(logs):
    data = []

    i = 0
    while i < len(logs):
        l = logs[i]
        data.append({
            "date": l.date,
            "crop": l.crop.name,
            "stage": l.crop.stage,
            "height": l.crop.height,
            "moisture": l.soil.moisture,
            "ph": l.soil.ph,
            "temp": l.environment.temperature,
            "humidity": l.environment.humidity,
            "rainfall": l.environment.rainfall
        })
        i += 1

    df = pd.DataFrame(data)
    df.to_csv(FILE_PATH, index=False)
    print("✅ Data saved to CSV")

def load_from_csv():
    if not os.path.exists(FILE_PATH):
        print("No CSV file found")
        return None

    df = pd.read_csv(FILE_PATH)
    print("✅ Data loaded from CSV")
    print(df)