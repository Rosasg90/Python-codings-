# Josue Rosas 
# Student ID: 877784637 
# Section: 08
# Module 5 Assignment 2
start = int(input(f"Enter the start of the loop: "))
limit = int(input(f"Enter the limit of the loop: "))
current = start

print(f"The current value is {start}")
while (current * 2) <= limit:
    current *= 2
    if limit > current:
        print(f"The current value is {current}")
if limit > current: 
    print(f"The last value of current that was less than {limit} was {current}")

        



    

    

