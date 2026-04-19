
def update_employee(employees):

    #syöttämällä ID valitaan minkä työntekijän tietoja päivitetään
    id = input("Enter employee ID to update details:")

    if id in employees:
        detail = input("Enter detail to be updated:")   #valitaan päivitettävä tieto

        if detail == "name":
            employees[id]["name"] = input("Enter updated name:")
            print("Employee name updated successfully.")
        
        elif detail == "department":
            employees[id]["department"] = input("Enter updated department:")
            print("Employee department updated successfully.")
        
        elif detail == "salary":    #palkan päivittämisessä huomioidaan mahdolliset syötetyt negatiiviset luvut + invalid input
            try:
                updated_salary = int(input("Enter updated salary:"))
                if updated_salary < 0:
                    print("Salary can't be negative.")
                else:
                    employees[id]["salary"] = updated_salary

            except ValueError:
                print("Salary must be a number.")

        else:
            print("Invalid detail.")
    
    else:
        print("Employee not found.")
        return