# main.py

from services.agri_service import add_log, view_logs, update_log, check_alerts, farm_logs
from utils.file_handler import save_to_csv, load_from_csv
from utils.stats import average_moisture, max_temperature
from utils.charts import plot_moisture

def main():
    while True:
        print("\n--- SAMAS MENU ---")
        print("1. Add Record")
        print("2. View Records")
        print("3. Update Record")
        print("4. Check Alerts")
        print("5. Save to CSV")
        print("6. Load CSV")
        print("7. Analytics")
        print("8. Show Chart")
        print("9. Exit")

        ch = input("Enter choice: ")

        if ch == "1":
            add_log()

        elif ch == "2":
            view_logs()

        elif ch == "3":
            update_log()

        elif ch == "4":
            check_alerts()

        elif ch == "5":
            save_to_csv(farm_logs)

        elif ch == "6":
            load_from_csv()

        elif ch == "7":
            print("\n--- ANALYTICS ---")
            print("Average Moisture:", average_moisture(farm_logs))
            print("Max Temperature:", max_temperature(farm_logs))

        elif ch == "8":
            plot_moisture(farm_logs)

        elif ch == "9":
            print("Exiting SAMAS...")
            break

        else:
            print("Invalid choice, try again!")

if __name__ == "__main__":
    main()