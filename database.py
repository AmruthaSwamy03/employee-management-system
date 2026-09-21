import sqlite3
from employee import Employee

DATABASE_NAME = "employees.db"


def create_database():

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            department TEXT NOT NULL,
            designation TEXT NOT NULL,
            salary REAL NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def add_employee_to_db(employees):

    employee = employees[-1]

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO employees
        (name, age, department, designation, salary)
        VALUES (?, ?, ?, ?, ?)
    """, (
        employee.name,
        employee.age,
        employee.department,
        employee.designation,
        employee.salary
    ))

    connection.commit()
    connection.close()

def get_all_employees(employee_class):

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, age, department, designation, salary
        FROM employees
    """)

    rows = cursor.fetchall()

    connection.close()

    employees = []

    for row in rows:

        employee = employee_class(
            row[1],
            row[2],
            row[3],
            row[4],
            row[5]
        )

        employees.append(employee)

    return employees

def search_employee_in_db(employee_class, name):

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name, age, department, designation, salary
        FROM employees
        WHERE LOWER(name) = LOWER(?)
    """, (name,))

    row = cursor.fetchone()

    connection.close()

    if row is None:
        return None

    employee = employee_class(
        row[1],
        row[2],
        row[3],
        row[4],
        row[5]
    )

    return employee

def update_employee_in_db(name, age, department, designation, salary):

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        UPDATE employees
        SET age = ?,
            department = ?,
            designation = ?,
            salary = ?
        WHERE LOWER(name) = LOWER(?)
    """, (
        age,
        department,
        designation,
        salary,
        name
    ))

    connection.commit()

    rows_updated = cursor.rowcount

    connection.close()

    return rows_updated

def delete_employee_from_db(name):

    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        DELETE FROM employees
        WHERE LOWER(name) = LOWER(?)
    """, (name,))

    connection.commit()

    rows_deleted = cursor.rowcount

    connection.close()

    return rows_deleted

if __name__ == "__main__":

    create_database()

    search_name = input("Enter employee name to search: ")

    employee = search_employee_in_db(Employee, search_name)

    if employee:
        print("\nEmployee Found!")
        employee.display()
    else:
        print("\nEmployee not found.")