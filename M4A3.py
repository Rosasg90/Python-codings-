# Josue Rosas 
# Student ID: 877784637 
# Section: 08
# Module 4 Assignment 3
games_dict = {}
for i in range(3):
    games = input(f" What is a great game?")
    system = input(f" What system can I play that on? ")
    games_dict[games] = system 

print(f"That's too many, let get rid of one")
user_input = input(f"What game whould we remove?")

if user_input in games_dict:
    del games_dict[user_input]
print(f"This new dictionary is:")

for games, system in games_dict.items():
    print(f"You can play {games} on {system}")