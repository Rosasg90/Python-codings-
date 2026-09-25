# Josue Rosas 
# Student ID: 877784637 
# Section: 08
# Module 4 Assignment 2
food_dict ={}
for i in range(3):
    food = input(f"What is good to eat? ")
    country = input(f"What country is that from? ")
    food_dict[food] = country
dish = input(f"What dish do you like? ")
if dish in food_dict:
    print(f"{food} is from {country}")