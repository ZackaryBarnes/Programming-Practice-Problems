import os
os.system("clear")

# Sort Employees problem from ProgrammingExpert.io

def sort_employees(employees, sort_by):
    key_list = ["name", "age", "salary"]
    key_idx = key_list.index(sort_by)

    sorted_employee_list = []
    temp_employees_list = employees[:]

    while len(temp_employees_list) > 0:
        smallest_employee_index = 0

        for i, employee in enumerate(temp_employees_list):
            current_smallest_value = temp_employees_list[smallest_employee_index][key_idx]
            if employee[key_idx] < current_smallest_value:
                smallest_employee_index = i

        sorted_employee_list.append(temp_employees_list[smallest_employee_index])
        temp_employees_list.pop(smallest_employee_index)

    return sorted_employee_list

# Test case    
employee_list_test = [
    ["Stan", 38, 100000],
    ["Steve", 17, 350],
    ["Roger", 2345, 1]
]

sort_by_key = "salary"

print(sort_employees(employee_list_test, sort_by_key))