import json
import os


FILE_NAME = "employees.json"


def load_employees(employee_class):

    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        data = json.load(file)

    employees = []

    for item in data:
        employee = employee_class(
            item["name"],
            item["age"],
            item["department"],
            item["designation"],
            item["salary"]
        )

        employees.append(employee)

    return employees


def save_employees(employees):

    employee_data = []

    for employee in employees:
        employee_data.append(employee.to_dict())

    with open(FILE_NAME, "w") as file:
        json.dump(employee_data, file, indent=4)