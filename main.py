employees = []
def add_employees():
    name=get_valid_name()
    age=get_valid_age()
    department=get_valid_department()
    for emp in employees:
        if emp["name"].lower() == name.lower() and emp["department"].lower() == department.lower():
            print("Employee with the same name and department already exists. Please enter unique details.")
            return
    employee={
        "id": generate_employee_id(),
        "name": name, "age": age, "department": department}
    employees.append(employee)
    save_employees()
    print("Employee added successfully!")

def view_employees():
    if len(employees) == 0:
        print("\nNo employees to display.")
        return
    print("\nEMPLOYEE MANAGEMENT SYSTEM")
    print("-"*60)

    print(f"{'ID':<5} | {'Name':<20} | {'Age':<5} | {'Department':<15}")
    print("-"*60)

    for emp in employees:
        print(f"{emp['id']:<5} | {emp['name']:<20} | {emp['age']:<5} | {emp['department']:<15}")
        print("-"*60)
    print(f"Total Employees: {len(employees)}")
    print("-"*60)

def search_employee():
    search_name = input("Enter employes name to search ")
    for employee in employees:
        if employee["name"].lower() == search_name.lower():
            print(f"ID: {employee['id']}, Name: {employee['name']}, Age: {employee['age']}, Department: {employee['department']}")
            break
    else:
        print("Employee not found.")
def delete_employee():
    if len(employees) == 0:
        print("No employees to delete.")
        return
    print("\nDelete Employee Details")
    print("1.Delete by name")
    print("2.Delete by ID")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter employee name to delete: ").lower()
        matches = []
        for emp in employees:
            if emp["name"].lower() == name:
                matches.append(emp)

        if len(matches) == 0:
            print("Employee with this name not found.")
            return

        print("\nMatching Employees:")
        for emp in matches:
            print(f"ID: {emp['id']}, | Name: {emp['name']}, | Age: {emp['age']},| Department: {emp['department']}")

        emp_id = int(input("Enter employee ID to delete: "))
        for emp in matches:
            if emp["id"] == emp_id:
                confirm = input("Are you sure you want to delete this employee? (yes/no): ")
                if confirm.lower() == "yes":
                    employees.remove(emp)
                    reassign_employee_ids()
                    save_employees()
                    print("Employee detail deleted successfully!")
                else:
                    print("Deletion cancelled.")
                return

        print("Employee with this ID not found.")
    elif choice == 2:
        emp_id = int(input("Enter employee ID to delete: "))
        for emp in employees:
            if emp["id"] == emp_id:
                print("\nEmployee Found:")
                print(f"ID: {emp['id']}, | Name: {emp['name']}, | Age: {emp['age']},| Department: {emp['department']}")
                confirm = input("Are you sure you want to delete this employee? (yes/no): ")
                if confirm.lower() == "yes":
                    employees.remove(emp)
                    reassign_employee_ids()
                    save_employees()
                    print("Employee detail deleted successfully!")
                else:
                    print("Deletion cancelled.")
                return
        print("Employee with this ID not found.")
    else:
        print("Invalid choice. Please try again.")
def reassign_employee_ids():
    for index, emp in enumerate(employees, start=1):
        emp["id"] = index
    
def generate_employee_id():
    max_id = 0
    for employee in employees:
        employee_id = employee.get("id", 0)
        if isinstance(employee_id, int) and employee_id > max_id:
            max_id = employee_id
    return max_id + 1

def menu():
    while True:
        print("\n EMPLOYEE MANAGEMENT SYSTEM")
        print("1.ADD EMPLOYEE")
        print("2.VIEW EMPLOYEES")
        print("3.SEARCH EMPLOYEE")
        print("4.DELETE EMPLOYEE")
        print("5.UPDATE EMPLOYEE")
        print("6.SHOW STATISTICS")
        print("7.EXIT")
        
        wish = int(input("enter your choice:"))
        if wish ==1:
            add_employees()
        elif wish == 2:
            view_employees()
        elif wish == 3:
            search_employee()
        elif wish == 4:
            delete_employee()
        elif wish == 5:
            update_employee()
        elif wish == 6:
            show_statics()
        elif wish == 7:
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


import json
employees = []
def load_employees():
    global employees
    try:
        with open("employees.json", "r") as file:
            employees = json.load(file)
    except FileNotFoundError:
        employees = []

    updated = False
    next_id = 1
    for employee in employees:
        if not isinstance(employee.get("id"), int):
            employee["id"] = next_id
            updated = True
        next_id = max(next_id, employee["id"] + 1)

    if updated:
        save_employees()

def save_employees():
    with open("employees.json", "w") as file:
        json.dump(employees, file)
def update_employee():
    update_employee_name = input("Enter name of emplyoee name to update:")
    for emp in employees:
        if emp["name"].lower() == update_employee_name.lower():
            new_name = input("Enter new name:")
            new_age = int(input("Enter new age:"))
            new_department = input("Enter new department:")
            emp["name"] = new_name
            emp["age"] = new_age
            emp["department"] = new_department
            save_employees()
            print("Employee details updated successfully!")
            return
    print("Employee not found.")
def get_valid_name():
    while True:
        name = input("Enter employee name:").strip()
        if name.replace(" ", "").isalpha():
            return name 
        else:
            print("Invalid name. Please enter a valid name containing only letters and spaces.")
def get_valid_age():
    while True:
        try:
            age = int(input("Enter employee age:"))
            if 18 <= age <= 65:
                return age
            else:
                print("Invalid age. Please enter an age between 18 and 65.")
        except ValueError:
            print("Invalid input. Please enter a valid age.")

def get_valid_department():
    while True:
        department = input("Enter employee department:").strip()
        if department == "":
            print("Department cannot be empty. Please enter a valid department.")
        elif department.replace(" ", "").isalpha():
            return department
        else:
            print("Invalid department. Please enter letters and spaces only.")
def show_statics():
    if len(employees) == 0:
        print("No employees to show statistics.")
        return
    department_count = {}
    for emp in employees:
        dept = emp["department"]
        if dept in department_count:
            department_count[dept] += 1
        else:
            department_count[dept] = 1
    print("\nEmployee Statistics:")
    print("-"* 40)
    for dept, count in department_count.items():
        print(f'{dept:<15} : {count} employees')
    print("-"* 40)
    print(f'Total Employees: {len(employees)}')
    print("-"* 40)
def search_employee():
    if len(employees)==0:
        print("\nNo employees found.")
        return
    while True:
        print("\nSEARCH EMPLOYEE")
        print("1 Search by ID")
        print("2 Search by Name")
        print("3 Search by Department")
        print("4 Partial Name Search")
        print("5 Search by Age Range")
        print("6 Back")
        choice=input("Enter choice: ")
        if choice=="1":
            emp_id=int(input("Enter employee ID: "))
            for emp in employees:
                if emp["id"]==emp_id:
                    print(f'\nID:{emp["id"]} Name:{emp["name"]} Age:{emp["age"]} Dept:{emp["department"]}')
                    return
            print("Employee not found.")
        elif choice=="2":
            name=input("Enter name: ").lower()
            found=False
            for emp in employees:
                if emp["name"].lower()==name:
                    print(f'ID:{emp["id"]} Name:{emp["name"]} Age:{emp["age"]} Dept:{emp["department"]}')
                    found=True
            if not found:
                print("No employee found with this name.")
        elif choice=="3":
            dept=input("Enter department: ").lower()
            found=False
            for emp in employees:
                if emp["department"].lower()==dept:
                    print(f'ID:{emp["id"]} Name:{emp["name"]} Age:{emp["age"]} Dept:{emp["department"]}')
                    found=True
            if not found:
                print("No employees found in this department.")
        elif choice=="4":
            keyword=input("Enter name keyword: ").lower()
            found=False
            for emp in employees:
                if keyword in emp["name"].lower():
                    print(f'ID:{emp["id"]} Name:{emp["name"]} Age:{emp["age"]} Dept:{emp["department"]}')
                    found=True
            if not found:
                print("No matching employees found.")
        elif choice=="5":
            min_age=int(input("Enter minimum age: "))
            max_age=int(input("Enter maximum age: "))
            found=False
            for emp in employees:
                if min_age<=emp["age"]<=max_age:
                    print(f'ID:{emp["id"]} Name:{emp["name"]} Age:{emp["age"]} Dept:{emp["department"]}')
                    found=True
            if not found:
                print("No employees found in this age range.")
        elif choice=="6":
            return
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    load_employees()
    menu()
