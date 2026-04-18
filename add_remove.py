

employees = {}
#Adding employees
def add_employee(employees):
     
    employee_id = input("Enter employee ID to add: ")                  #Adding ID
    employee_name = input("Enter employee name: ")              #Adding name 
    employee_department = input("Enter employee department: ")  #Adding department     
    
    
    if employee_id in employees:
        print (f"Employee {employee_id} already exists")            #Preventing crash if ID already exists
        return
    
    
    while True:
        try:
            employee_salary = int(input("Enter employee salary: ")) #Adding salary 
            if employee_salary < 0:                                 #Preventing negative salary
                print("Salary can't be a negative")
                continue
            break
        except ValueError:                                          #Preventing crash if not given a number
            print("Salary must be a number")

    
#Adding employee dictionary
    employees[employee_id] = {
        "name": employee_name,
        "department": employee_department,
        "salary": employee_salary
    }

    print(f"Employee {employee_name} added successfully")

#Removing employees
def remove_employee(employees):
    employee_id = input("Enter employee ID to remove: ")
    
    if employee_id in employees:
        del employees[employee_id]
        print (f"Employee {employee_id} removed successfully")
    else:
        print(f"Employee not found")
        
