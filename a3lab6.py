# Josue Rosas 
# Student ID: 877784637 
# Section: 08
# Module 3, Assignment 6

name = input(f"What is the student name? ")
grade = int(input(f"What is their score? "))
if grade <= 100 and grade >= 90:
    print(f"{name} earned an A") 
elif grade <= 89 and grade >= 80:
    print(f"{name} earned an B")
elif grade <= 79 and grade >= 70:
    print(f"{name} earned an C")
elif grade <= 69 and grade >= 60:
    print(f"{name} earned an D") 
elif grade <= 59: 
    print(f"{name} earned an F")