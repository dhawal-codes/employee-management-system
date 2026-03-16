# List to store employee records
employees = []

# Function to add a new employee
def add_employees():
    name=get_valid_name()
    age=get_valid_age()
    department=get_valid_department()

    # Check if employee with same name and department already exists
    for emp in employees:
        if emp["name"].lower() == name.lower() and emp["department"].lower() == department.lower():
            print("Employee with the same name and department already exists. Please enter unique details.")
            return

    # Create employee dictionary
    employee={
        "id": generate_employee_id(),
        "name": name, "age": age, "department": department}

    employees.append(employee)
    save_employees()
    print("Employee added successfully!")


# Function to display all employees
def view_employees():
    if len(employees) == 0:
        print("\nNo employees to display.")
        return

    print("\nEMPLOYEE MANAGEMENT SYSTEM")
    print("-"*60)

    print(f"{'ID':<5} | {'Name':<20} | {'Age':<5} | {'Department':<15}")
    print("-"*60)

    # Loop through employees list and print details
    for emp in employees:
        print(f"{emp['id']:<5} | {emp['name']:<20} | {emp['age']:<5} | {emp['department']:<15}")
        print("-"*60)

    print(f"Total Employees: {len(employees)}")
    print("-"*60)


# Function to delete employee using name or ID
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

        # Find all employees with the same name
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

        # Confirm deletion
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


# Function to reassign employee IDs after deletion
def reassign_employee_ids():
    for index, emp in enumerate(employees, start=1):
        emp["id"] = index
    

# Function to generate unique employee ID
def generate_employee_id():
    max_id = 0
    for employee in employees:
        employee_id = employee.get("id", 0)
        if isinstance(employee_id, int) and employee_id > max_id:
            max_id = employee_id
    return max_id + 1


# Main menu function
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
