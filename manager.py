employee_name = "ROcky"
employee_id  = "empl@gmail.com"
employee_pass = "emp12345"
employee_salary = 45000

if __name__ == "__main__":
    # will not be accessible by other file 
    manager_name = "Suresh chandra"
    manager_id = "hello@gmail.com"
    manager_pass = "helo@12345"
    manager_salary = 80000



def average_finder(ls):
    total_sum = 0 
    count = 0 
    for item in ls:
        total_sum += item
        count += 1 
    average = total_sum / count
    print("Your average is : ",round(average,2)) 


print("MANAGER FILE EXECUTED!")
