
from database import get_employee_by_id
from database import update_employee_detail


def update_employee(employees=None):
    # syöttämällä ID valitaan minkä työntekijän tietoja päivitetään
    employee_id = input("Enter employee ID to update details: ").strip()

    try:
        employee_id = int(employee_id)
    except ValueError:
        print("Employee ID must be a number.")
        return

    found, _ = get_employee_by_id(employee_id)

    if found:
        detail = input("Enter detail to be updated (name/department/role/salary): ").strip().lower()

        if detail == "name":
            new_name = input("Enter updated name: ").strip()
            success, message = update_employee_detail(employee_id, "name", new_name)
            print(message)

        elif detail == "department":
            new_department = input("Enter updated department: ").strip()
            success, message = update_employee_detail(employee_id, "department", new_department)
            print(message)

        elif detail == "role":
            new_role = input("Enter updated role: ").strip()
            success, message = update_employee_detail(employee_id, "role", new_role)
            print(message)

        elif detail == "salary":
            try:
                updated_salary = float(input("Enter updated salary: "))
                if updated_salary < 0:
                    print("Salary can't be negative.")
                else:
                    success, message = update_employee_detail(employee_id, "salary", updated_salary)
                    print(message)

            except ValueError:
                print("Salary must be a number.")

        else:
            print("Invalid detail.")

    else:
        print("Employee not found.")
        return
