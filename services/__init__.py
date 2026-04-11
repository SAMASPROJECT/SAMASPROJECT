from agri_service import add_log, view_logs, update_log, check_alerts

def main():
    while True:
        print("\n--- SAMAS MENU ---")
        print("1. Add Record")
        print("2. View Records")
        print("3. Update Record")
        print("4. Check Alerts")
        print("5. Exit")

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
            print("Exiting...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()