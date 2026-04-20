from database import get_all_employees
from database import search_by_department as db_search_by_department


def format_salary(value):
    try:
        value = float(value)
        if value.is_integer():
            return int(value)
        return value
    except (ValueError, TypeError):
        return value

#  VIEW & SEARCH EMPLOYEES

def view_employees(employees=None):
    """Prints all employees in a clean format."""
    success, result = get_all_employees()

    if not success:
        print(f"\n{result}\n")
        return

    if not result:
        print("\nNo employees in the list.\n")
        return

    print("\n----- EMPLOYEE LIST -----")
    for emp in result:
        print(f"ID: {emp['id']}")
        print(f"Name: {emp['name']}")
        print(f"Department: {emp['department']}")
        print(f"Role: {emp['role']}")
        print(f"Salary: {format_salary(emp['salary'])} €")
        print("---------------------------")
    print()


def search_by_department(employees=None):
    """Searches employees by department."""
    dept = input("Enter department: ").strip()

    success, result = db_search_by_department(dept)

    print()

    if not success:
        print(f"{result}\n")
        return

    if not result:
        print(f"No employees found in department '{dept}'.\n")
        return

    for emp in result:
        print(f"ID: {emp['id']}")
        print(f"Name: {emp['name']}")
        print(f"Role: {emp['role']}")
        print(f"Salary: {format_salary(emp['salary'])} €")
        print("---------------------------")
