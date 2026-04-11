# services/agri_service.py

from models.crop import Crop
from models.soil import Soil
from models.environment import Environment
from models.farm_log import FarmLog

farm_logs = []

# -----------------------------
# ADD RECORD
# -----------------------------
def add_log():
    date = input("Enter Date: ")

    # Crop
    name = input("Enter Crop Name: ")
    stage = input("Enter Growth Stage: ")
    height = float(input("Enter Crop Height: "))
    crop = Crop(name, stage, height)

    # Soil
    moisture = float(input("Enter Soil Moisture: "))

    if moisture < 70:
        m_status = "LOW ⚠️"
    elif moisture >= 70:
        m_status = "HIGH ✅"
    else:
        m_status = "NO MOISTURE ⚠️"

    print("Moisture Status:", m_status)

    ph = float(input("Enter Soil pH: "))

    if ph < 7:
        p_status = "LOW (ACIDIC) ⚠️"
    elif ph == 7:
        p_status = "NEUTRAL ✅"
    else:
        p_status = "HIGH (BASIC) ⚠️"

    print("pH Status:", p_status)

    soil = Soil(moisture, ph)

    # Environment
    temp = float(input("Enter Temperature: "))
    humidity = float(input("Enter Humidity: "))
    rainfall = float(input("Enter Rainfall: "))
    env = Environment(temp, humidity, rainfall)

    # Create Log
    log = FarmLog(date, crop, soil, env)
    farm_logs.append(log)

    print("✅ Record added successfully!")

# -----------------------------
# VIEW RECORDS (WITH INDEX)
# -----------------------------
def view_logs():
    if not farm_logs:
        print("No records found")
        return

    i = 0
    while i < len(farm_logs):
        log = farm_logs[i]

        # Moisture status
        m = log.soil.moisture
        if m < 30:
            m_status = "LOW"
        elif m <= 70:
            m_status = "OPTIMAL"
        else:
            m_status = "HIGH"

        # pH status
        p = log.soil.ph
        if p < 7:
            p_status = "LOW (ACIDIC)"
        elif p == 7:
            p_status = "NEUTRAL"
        else:
            p_status = "HIGH (BASIC)"

        print("\nIndex:", i)
        print("Date:", log.date)
        print("Crop:", log.crop.name, "| Stage:", log.crop.stage, "| Height:", log.crop.height)
        print("Soil Moisture:", m, "| Status:", m_status)
        print("Soil pH:", p, "| Status:", p_status)
        print("Temperature:", log.environment.temperature,
              "| Humidity:", log.environment.humidity,
              "| Rainfall:", log.environment.rainfall)

        i += 1

# -----------------------------
# UPDATE FULL RECORD
# -----------------------------
def update_log():
    if not farm_logs:
        print("No records to update")
        return

    view_logs()

    idx = int(input("\nEnter record index: "))

    if idx < 0 or idx >= len(farm_logs):
        print("Invalid index")
        return

    log = farm_logs[idx]

    print("\n--- Enter New Values ---")

    # Crop update
    log.crop.name = input("New Crop Name: ")
    log.crop.stage = input("New Growth Stage: ")
    log.crop.height = float(input("New Height: "))

    # Soil update
    log.soil.moisture = float(input("New Moisture: "))

    if log.soil.moisture < 30:
        m_status = "LOW"
    elif log.soil.moisture <= 70:
        m_status = "OPTIMAL"
    else:
        m_status = "HIGH"

    print("Updated Moisture Status:", m_status)

    log.soil.ph = float(input("New pH: "))

    if log.soil.ph < 7:
        p_status = "LOW (ACIDIC)"
    elif log.soil.ph == 7:
        p_status = "NEUTRAL"
    else:
        p_status = "HIGH (BASIC)"

    print("Updated pH Status:", p_status)

    # Environment update
    log.environment.temperature = float(input("New Temperature: "))
    log.environment.humidity = float(input("New Humidity: "))
    log.environment.rainfall = float(input("New Rainfall: "))

    print("✅ Record updated successfully!")

# -----------------------------
# ALERT CHECKS
# -----------------------------
def check_alerts():
    if not farm_logs:
        print("No data")
        return

    i = 0
    while i < len(farm_logs):
        log = farm_logs[i]

        if log.soil.moisture < 30:
            print("⚠️ ALERT: Low Moisture on", log.date)
        if log.soil.moisture > 70:
            print("⚠️ ALERT: High Moisture on", log.date)

        if log.soil.ph < 7:
            print("⚠️ ALERT: Low pH (Acidic) on", log.date)
        if log.soil.ph > 7:
            print("⚠️ ALERT: High pH (Basic) on", log.date)
        if log.soil.moisture < 30:
                print("⚠️ ALERT: Low Moisture on", log.date)

        if log.environment.temperature > 35:
                print("⚠️ ALERT: High Temperature on", log.date)

        i += 1