# Josue Rosas 
# Student ID: 877784637 
# Section: 08
# Module 3, Assignment 1

start_int = int(input(f"What is your first number? "))
end_int = int(input(f"What is your secound number? "))
num_list = list(range (start_int, end_int))
sum_int = 1
for num in num_list:
    sum_int += num
print(sum_int)