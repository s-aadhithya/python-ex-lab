import csv

def read_employee_data(file_path):
    employee_data = []
    with open(file_path, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            employee_data.append(row)
    return employee_data

def highest_paid_employee(employee_data):
    highest_salary = max(employee_data, key=lambda x: float(x['salary']))
    return highest_salary

def sort_employees_by_department(employee_data):
    sorted_employees = sorted(employee_data, key=lambda x: x['department'])
    return sorted_employees

def average_salary_per_department(employee_data):
    department_salaries = {}
    department_counts = {}
    for employee in employee_data:
        department = employee['department']
        salary = float(employee['salary'])
        if department not in department_salaries:
            department_salaries[department] = 0
            department_counts[department] = 0
        department_salaries[department] += salary
        department_counts[department] += 1
    average_salaries = {dept: department_salaries[dept] / department_counts[dept] for dept in department_salaries}
    return average_salaries

if __name__ == "__main__":
    file_path = 'employee_data.csv'  # Update with your CSV file path
    employee_data = read_employee_data(file_path)

    highest_paid = highest_paid_employee(employee_data)
    print(f"Highest paid employee: {highest_paid['name']} (Department: {highest_paid['department']}, Salary: {highest_paid['salary']})")

    sorted_employees = sort_employees_by_department(employee_data)
    print("\nEmployees sorted by department:")
    for employee in sorted_employees:
        print(f"{employee['name']} - Department: {employee['department']}")

    average_salaries = average_salary_per_department(employee_data)
    print("\nAverage salary per department:")
    for department, avg_salary in average_salaries.items():
        print(f"{department}: {avg_salary}")
