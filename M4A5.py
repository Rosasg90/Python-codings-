# Josue Rosas 
# Student ID: 877784637 
# Section: 08
# Module 4 Assignment 5
food_dict ={'Jim': 'Tacos',
             'Bob': 'Burgers',
             'Janelle': '',
             'Lisa': 'Pizza',
             'Thomas': '',
             'Yolanda': '',
             'Finn': 'Bread',
}
for key in food_dict.keys():
    if food_dict.get(key)== '':
       food_dict[key] = input(f"What is {key}'s favorite food?")

print(f"Here are the Favortie Food:")
for key, value in food_dict.items():
    print(f"{key}'s favorite food is {value}")
