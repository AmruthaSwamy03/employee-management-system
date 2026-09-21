from database import (
    create_database,
    get_all_employees,
    add_employee_to_db,
    search_employee_in_db,
    update_employee_in_db,
    delete_employee_from_db
)

from employee import (
    Employee,
    add_employee,
    view_employees
)

create_database()

employees = get_all_employees(Employee)


print("===================================")
print("     EMPLOYEE MANAGEMENT SYSTEM")
print("===================================")


while True:

    print("\n1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Update Employee")
    print("5. Delete Employee")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        add_employee(employees,add_employee_to_db)

    elif choice == "2":
        view_employees(employees)

    elif choice == "3":
        search_name = input("Enter employee name to search: ").strip()

        employee = search_employee_in_db(Employee, search_name)

        if employee:
            print("\nEmployee Found!")
            employee.display()
        else:
            print("\nEmployee not found.")

    elif choice == "4":
        search_name = input("Enter employee name to update: ").strip()
        employee = search_employee_in_db(Employee, search_name)
        if employee is None:
            print("\nEmployee not found.")
            continue
        print("\nCurrent Employee Details:")
        employee.display()

        while True:
            try:
                age = int(input("\nEnter new age: "))
                if age <= 0:
                    print("Age must be greater than 0.")
                    continue
                break

            except ValueError:
                print("Please enter a valid number for age.")

        while True:
            department = input("Enter new department: ").strip()
            if department:
                break
            print("Department cannot be empty.")

        while True:
            designation = input("Enter new designation: ").strip()
            if designation:
                break
            print("Designation cannot be empty.")

        while True:
            try:
                salary = float(input("Enter new salary: "))
                if salary < 0:
                    print("Salary cannot be negative.")
                    continue
                break
            except ValueError:
                print("Please enter a valid number for salary.")

        rows_updated = update_employee_in_db(
            search_name,
            age,
            department,
            designation,
            salary
        )

        if rows_updated:
            print("\nEmployee updated successfully!")
            employees = get_all_employees(Employee)
        else:
            print("\nEmployee update failed.")

    elif choice == "5":
        search_name = input("Enter employee name to delete: ").strip()
        employee = search_employee_in_db(Employee, search_name)
        if employee is None:
            print("\nEmployee not found.")
            continue
        print("\nEmployee Found:")
        employee.display()
        confirmation = input(
            "\nAre you sure you want to delete this employee? (yes/no): "
        )
        if confirmation.lower() == "yes":
            rows_deleted = delete_employee_from_db(search_name)
            if rows_deleted:
                print("\nEmployee deleted successfully!")
                employees = get_all_employees(Employee)
            else:
                print("\nEmployee could not be deleted.")
        else:
            print("\nDeletion cancelled.")

    elif choice == "6":
        print("\nGoodbye!")
        break

    else:
        print("\nInvalid choice!")