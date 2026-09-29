# Josue Rosas 
# Student ID: 877784637 
# Section: 08
# Module 4 Assignment 1
g_list = []
questions = [ 
    "What is your 1 favorite PlayStation game? ",
    "What is your 2 favorite PlayStation game? ",
    "What is your 3 favorite PlayStation game? "
]
for question in questions:
    response = input(question)
    g_list.append(response.title())

for index, game in enumerate(g_list, start=1):
    print(f"Your number {index} favorite game was {game}")
