from database import add_employee as db_add_employee
from database import delete_employee as db_delete_employee

# Kept for compatibility with the old version of the project
employees = {}


# Adding employees
def add_employee(employees=None):
    employee_id = input("Enter employee ID to add: ").strip()
    employee_name = input("Enter employee name: ").strip()
    employee_department = input("Enter employee department: ").strip()
    employee_role = input("Enter employee role: ").strip()

    try:
        employee_id = int(employee_id)
        if employee_id <= 0:
            print("Employee ID must be a positive number.")
            return
    except ValueError:
        print("Employee ID must be a number.")
        return

    while True:
        try:
            employee_salary = float(input("Enter employee salary: "))
            if employee_salary < 0:
                print("Salary can't be negative")
                continue
            break
        except ValueError:
            print("Salary must be a number")

    success, message = db_add_employee(
        employee_id,
        employee_name,
        employee_department,
        employee_role,
        employee_salary
    )

    print(message)


# Removing employees
def remove_employee(employees=None):
    employee_id = input("Enter employee ID to remove: ").strip()

    try:
        employee_id = int(employee_id)
    except ValueError:
        print("Employee ID must be a number.")
        return

    success, message = db_delete_employee(employee_id)
    print(message)

        
