from database import init_db
from add_remove import add_employee, remove_employee
from projekti import view_employees, search_by_department
from update import update_employee


def show_menu():
    print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
    print("1. Add employee")
    print("2. View employee list")
    print("3. Update employee details")
    print("4. Remove an employee")
    print("5. Search employees by department")
    print("6. Exit")


def main():
    success, message = init_db()
    print(message)

    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            update_employee()
        elif choice == "4":
            remove_employee()
        elif choice == "5":
            search_by_department()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 6.")


if __name__ == "__main__":
    main()