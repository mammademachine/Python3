employee_file = open("28.txt", "r")
for employee in employee_file.readlines():
    print(employee)
employee_file.close()