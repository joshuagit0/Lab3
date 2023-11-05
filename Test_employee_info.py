import employee_info as info

employee_data = [
    {"name": "John", "age": 30, "department": "Sales", "salary": 50000},
    {"name": "Jane", "age": 25, "department": "Marketing", "salary": 60000},
    {"name": "Mary", "age": 23, "department": "Marketing", "salary": 56000},
    {"name": "Chloe",  "age": 35, "department": "Engineering", "salary": 70000},
    {"name": "Mike", "age": 32, "department": "Engineering", "salary": 65000},
    {"name": "Peter", "age": 40, "department": "Sales", "salary": 60000}
]

def test_get_employees_by_age_range():
    result = []
    input_age_lower_limit = 26
    input_age_upper_limit = 39
    test_arr = [{'name': 'John', 'age': 30, 'department': 'Sales', 'salary': 50000}, {'name': 'Chloe', 'age': 35, 'department': 'Engineering', 'salary': 70000}, {'name': 'Mike', 'age': 32, 'department': 'Engineering', 'salary': 65000}]

    result = info.get_employees_by_age_range(input_age_lower_limit, input_age_upper_limit)

    assert (result == test_arr)


def test_calculate_average_salary():
    result = []
    test_arr = 60166.67

    result = info.calculate_average_salary()

    assert (result == test_arr)


def test_get_employees_by_dept():
    result = []
    test_arr = [{'name': 'Jane', 'age': 25, 'department': 'Marketing', 'salary': 60000}, {'name': 'Mary', 'age': 23, 'department': 'Marketing', 'salary': 56000}]
    department = "Marketing"

    result = info.get_employees_by_dept(department)

    assert (result == test_arr)