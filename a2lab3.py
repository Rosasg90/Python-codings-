# Josue Rosas 
# Student ID: 877784637 
# Section: 08
# Module 2, Assignment 3

uber_list = list(range(100,201,2))

start = int (input (f"what is the start of your slice? "))
end = int( input (f"what is the end of your slice? "))
data_list = uber_list[start:end]
total_int = 0
for num in data_list:
    total_int += num/ len(data_list)
print(f"Your slice contain {len(data_list)} values and has a average of {total_int}")



