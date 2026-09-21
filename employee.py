class Employee:

    def __init__(self, name, age, department, designation, salary):
        self.name = name
        self.age = age
        self.department = department
        self.designation = designation
        self.salary = salary

    def display(self):
        print("\nName:", self.name)
        print("Age:", self.age)
        print("Department:", self.department)
        print("Designation:", self.designation)
        print("Salary:", self.salary)

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "department": self.department,
            "designation": self.designation,
            "salary": self.salary
        }

def add_employee(employees, save_function):

    while True:
        name = input("Enter employee name: ").strip()

        if name:
            break

        print("Employee name cannot be empty.")

    for employee in employees:
        if employee.name.lower() == name.lower():
            print("\nEmployee already exists!")
            return

    while True:
        try:
            age = int(input("Enter employee age: "))

            if age <= 0:
                print("Age must be greater than 0.")
                continue

            break

        except ValueError:
            print("Please enter a valid number for age.")

    while True:
        department = input("Enter department: ").strip()

        if department:
            break

        print("Department cannot be empty.")

    while True:
        designation = input("Enter designation: ").strip()

        if designation:
            break

        print("Designation cannot be empty.")

    while True:
        try:
            salary = float(input("Enter salary: "))

        except ValueError:
            print("Please enter a valid number for salary.")
            continue

        if salary < 0:
            print("Salary cannot be negative.")
            continue

        break

    employee = Employee(
        name,
        age,
        department,
        designation,
        salary
    )

    employees.append(employee)

    save_function(employees)

    print("\nEmployee added successfully!")

def view_employees(employees):

    if not employees:
        print("\nNo employees found.")
        return

    print("\n========== EMPLOYEE LIST ==========")

    for employee in employees:
        employee.display()

        
def search_employee(employees):

    search_name = input("Enter employee name to search: ").strip()

    for employee in employees:

        if employee.name.lower() == search_name.lower():

            print("\nEmployee Found!")
            print("Name:", employee.name)
            print("Age:", employee.age)
            print("Department:", employee.department)
            print("Designation:", employee.designation)
            print("Salary:", employee.salary)

            return

    print("\nEmployee not found.")


def update_employee(employees, save_function):

    search_name = input("Enter employee name to update: ").strip()

    for employee in employees:

        if employee.name.lower() == search_name.lower():

            print("\nCurrent Employee Details:")
            print("Name:", employee.name)
            print("Age:", employee.age)
            print("Department:", employee.department)
            print("Designation:", employee.designation)
            print("Salary:", employee.salary)

            # Update age
            while True:
                try:
                    age = int(input("\nEnter new age: "))

                    if age <= 0:
                        print("Age must be greater than 0.")
                        continue

                    break

                except ValueError:
                    print("Please enter a valid number for age.")

            # Update department
            while True:
                department = input("Enter new department: ").strip()

                if department:
                    break

                print("Department cannot be empty.")

            # Update designation
            while True:
                designation = input("Enter new designation: ").strip()

                if designation:
                    break

                print("Designation cannot be empty.")

            # Update salary
            while True:
                try:
                    salary = float(input("Enter new salary: "))

                    if salary < 0:
                        print("Salary cannot be negative.")
                        continue

                    break

                except ValueError:
                    print("Please enter a valid number for salary.")

            # Update object attributes
            employee.age = age
            employee.department = department
            employee.designation = designation
            employee.salary = salary

            save_function(employees)

            print("\nEmployee updated successfully!")

            return

    print("\nEmployee not found.")

def delete_employee(employees, save_function):

    search_name = input("Enter employee name to delete: ").strip()

    for employee in employees:

        if employee.name.lower() == search_name.lower():

            print("\nEmployee Found:")
            print("Name:", employee.name)
            print("Department:", employee.department)
            print("Designation:", employee.designation)

            confirmation = input(
                "\nAre you sure you want to delete this employee? (yes/no): "
            )

            if confirmation.lower() == "yes":

                employees.remove(employee)

                save_function(employees)

                print("\nEmployee deleted successfully!")

            else:
                print("\nDeletion cancelled.")

            return

    print("\nEmployee not found.")