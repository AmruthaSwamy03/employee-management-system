from storage import load_employees, save_employees

from employee import (
    Employee,
    add_employee,
    view_employees,
    search_employee,
    update_employee,
    delete_employee
)

employees = load_employees(Employee)


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
        add_employee(employees,save_employees)

    elif choice == "2":
        view_employees(employees)

    elif choice == "3":
        search_employee(employees)

    elif choice == "4":
        update_employee(employees, save_employees)

    elif choice == "5":
        delete_employee(employees, save_employees)

    elif choice == "6":
        print("\nGoodbye!")
        break

    else:
        print("\nInvalid choice!")