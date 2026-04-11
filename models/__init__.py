# main.py

from models.crop import Crop
from models.soil import Soil
from models.environment import Environment
from models.farm_log import FarmLog

farm_logs = []

def add_record():
    date = input("Enter Date: ")

    # Crop
    name = input("Enter Crop Name: ")
    stage = input("Enter Growth Stage: ")
    height = float(input("Enter Crop Height: "))
    crop = Crop(name, stage, height)

    # Soil
    moisture = float(input("Enter Soil Moisture: "))

    # Moisture Status (AUTO OUTPUT)
    if moisture >= 70:
        moisture_status = "SOIL MOISTURE IS HIGH"
    elif moisture < 70:
        moisture_status = "SOIL MOISTURE IS LOW"
    else:
        moisture_status = "NO SOIL MOISTURE"

    print("Moisture Status:", moisture_status)

    ph = float(input("Enter Soil pH: "))

    # pH Status (AUTO OUTPUT)
    if ph < 7:
        ph_status = "ACIDIC"
    elif ph == 7:
        ph_status = "NEUTRAL"
    else:
        ph_status = "BASIC"

    print("pH Status:", ph_status)

    soil = Soil(moisture, ph)

    # Environment
    temp = float(input("Enter Temperature: "))
    humidity = float(input("Enter Humidity: "))
    rainfall = float(input("Enter Rainfall: "))
    env = Environment(temp, humidity, rainfall)

    log = FarmLog(date, crop, soil, env)
    farm_logs.append(log)

    print("Record added successfully!")

def view_records():
    if not farm_logs:
        print("No records found")
        return

    i = 0
    while i < len(farm_logs):
        log = farm_logs[i]

        # Moisture status again for display
        m = log.soil.moisture
        if m >= 70:
            m_status = "SOIL MOISTURES HIGH"
        elif m < 70:
            m_status = "SOIL MOISTURES LOW"
        else:
            m_status = "NO SOIL MOISTURES"

        # pH status again
        p = log.soil.ph
        if p < 7:
            p_status = "ACIDIC"
        elif p == 7:
            p_status = "NEUTRAL"
        else:
            p_status = "BASIC"

        print("\nDate:", log.date)
        print("Crop:", log.crop.name, "| Stage:", log.crop.stage, "| Height:", log.crop.height)
        print("Soil Moisture:", m, "| Status:", m_status)
        print("Soil pH:", p, "| Status:", p_status)
        print("Temp:", log.environment.temperature,
              "| Humidity:", log.environment.humidity,
              "| Rainfall:", log.environment.rainfall)

        i += 1

def main():
    while True:
        print("\n--- SAMAS MENU ---")
        print("1. Add Record")
        print("2. View Records")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_record()
        elif choice == "2":
            view_records()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()