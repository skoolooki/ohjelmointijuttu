# -------------------------------
#  VIEW & SEARCH EMPLOYEES
# -------------------------------

def view_employees(employees):
    """Prints all employees in a clean format."""
    if not employees:
        print("\nNo employees in the list.\n")
        return

    print("\n----- EMPLOYEE LIST -----")
    for emp in employees:
        print(f"ID: {emp['id']}")
        print(f"Name: {emp['name']}")
        print(f"Department: {emp['department']}")
        print(f"Salary: {emp['salary']} €")
        print("---------------------------")
    print()


def search_by_department(employees):
    """Searches employees by department."""
    dept = input("Enter department: ").strip()

    print()
    found = False

    for emp in employees:
        if emp["department"].lower() == dept.lower():
            print(f"ID: {emp['id']}")
            print(f"Name: {emp['name']}")
            print(f"Salary: {emp['salary']} €")
            print("---------------------------")
            found = True

    if not found:
        print(f"No employees found in department '{dept}'.\n")
