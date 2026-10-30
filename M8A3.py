# Josue Rosas 
# Student ID: 877784637 
# Section: 08
# Module 8 Assignment 3

while True:
    first_num = input(f" What is your first number? ( or type q to quit)")
    if first_num == 'q' or first_num == 'Q':
        print(f"The program is over")
        break
    second_num = input (f" What is the second number?") 
    try:
         answer = int(first_num) /int( second_num) 
    except ZeroDivisionError:
        print(f"You can't divide by zero")
    else:
        print(f"{first_num} / {second_num} is {answer}")
