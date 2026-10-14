# 1 

l1 = [101,105,102,101, 108, 105, 110]
# l3 = {101,105,102,101, 108, 105, 110}
    

unique_roll_num = set(l1)
# print (unique_roll_num)  



#  2

employee_details = [{"Employee Id": 101, "Employee_Name": "Alice", "Salary": 50000},
                  {"Employee Id": 102, "Employee_Name": "Bob", "Salary": 65000},
                  {"Employee Id": 103, "Employee_Name": "Charlie", "Salary": 45000}]

user_id = int(input("Enter employee id: "))
found = False

for i in employee_details:
    if user_id == i["Employee Id"]:
        print(i)
        found = True
        break

if not found:
    print("Employee not found")

