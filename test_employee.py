from employee import Employee

from database import (
    create_database,
    add_employee_to_db,
    get_all_employees,
    search_employee_in_db,
    update_employee_in_db,
    delete_employee_from_db
)


def test_employee_creation():

    employee = Employee(
        "Amrutha",
        20,
        "IT",
        "Software Engineer",
        50000
    )

    assert employee.name == "Amrutha"
    assert employee.age == 20
    assert employee.department == "IT"
    assert employee.designation == "Software Engineer"
    assert employee.salary == 50000


def test_employee_to_dict():

    employee = Employee(
        "Amrutha",
        20,
        "IT",
        "Software Engineer",
        50000
    )

    data = employee.to_dict()

    assert data["name"] == "Amrutha"
    assert data["age"] == 20
    assert data["department"] == "IT"
    assert data["designation"] == "Software Engineer"
    assert data["salary"] == 50000


def test_employee_attributes_can_be_updated():

    employee = Employee(
        "Amrutha",
        20,
        "IT",
        "Software Engineer",
        50000
    )

    employee.age = 21
    employee.department = "Data Engineering"
    employee.salary = 60000

    assert employee.age == 21
    assert employee.department == "Data Engineering"
    assert employee.salary == 60000


def test_employee_json_data():

    employee = Employee(
        "Amrutha",
        20,
        "IT",
        "Software Engineer",
        50000
    )

    data = employee.to_dict()

    assert data == {
        "name": "Amrutha",
        "age": 20,
        "department": "IT",
        "designation": "Software Engineer",
        "salary": 50000
    }


def test_database_crud(tmp_path, monkeypatch):

    test_database = tmp_path / "test_employees.db"

    monkeypatch.setattr(
        "database.DATABASE_NAME",
        str(test_database)
    )

    create_database()

    employee = Employee(
        "Test User",
        25,
        "IT",
        "Developer",
        60000
    )

    # CREATE
    add_employee_to_db([employee])

    # READ
    employees = get_all_employees(Employee)

    assert len(employees) == 1
    assert employees[0].name == "Test User"

    # SEARCH
    found_employee = search_employee_in_db(
        Employee,
        "Test User"
    )

    assert found_employee is not None
    assert found_employee.name == "Test User"

    # UPDATE
    rows_updated = update_employee_in_db(
        "Test User",
        26,
        "Data Engineering",
        "Data Engineer",
        70000
    )

    assert rows_updated == 1

    # Verify update
    updated_employee = search_employee_in_db(
        Employee,
        "Test User"
    )

    assert updated_employee.age == 26
    assert updated_employee.department == "Data Engineering"
    assert updated_employee.designation == "Data Engineer"
    assert updated_employee.salary == 70000

    # DELETE
    rows_deleted = delete_employee_from_db(
        "Test User"
    )

    assert rows_deleted == 1

    # Verify deletion
    deleted_employee = search_employee_in_db(
        Employee,
        "Test User"
    )

    assert deleted_employee is None


def test_employee_display(capsys):

    employee = Employee(
        "Amrutha",
        20,
        "IT",
        "Software Engineer",
        50000
    )

    employee.display()

    captured = capsys.readouterr()

    assert "Amrutha" in captured.out
    assert "20" in captured.out
    assert "IT" in captured.out
    assert "Software Engineer" in captured.out
    assert "50000" in captured.out