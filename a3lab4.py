# Josue Rosas 
# Student ID: 877784637 
# Section: 08
# Module 3, Assignment 4

current_year = int(input(f"What year is it now? "))
user_year = int(input(f"What year were you born? "))
age_int = current_year - user_year
if  (age_int % 2) == 0 and age_int < 50:
    print(f"This will be a great year")
elif(age_int % 2) != 0 and age_int < 50:
    print(f"This year will be tough")
elif (age_int == 50):
    print (f"Your future is unclear") 
elif (age_int > 50 ):
    print(f"Death will come to you")