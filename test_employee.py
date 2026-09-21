from employee import Employee
from storage import save_employees, load_employees


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

from storage import save_employees, load_employees


def test_save_and_load_employee(tmp_path, monkeypatch):

    test_file = tmp_path / "test_employees.json"

    monkeypatch.setattr("storage.FILE_NAME", str(test_file))

    employee = Employee(
        "Test User",
        25,
        "IT",
        "Developer",
        60000
    )

    save_employees([employee])

    loaded_employees = load_employees(Employee)

    assert len(loaded_employees) == 1

    loaded_employee = loaded_employees[0]

    assert loaded_employee.name == "Test User"
    assert loaded_employee.age == 25
    assert loaded_employee.department == "IT"
    assert loaded_employee.designation == "Developer"
    assert loaded_employee.salary == 60000

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