# Josue Rosas 
# Student ID: 877784637 
# Section: 08
# Module 2, Assignment 2

g_list = ['Mortal Kombat', 'Contra', 'Streets Of Rage', 'Shinobi', 'Sonic', 'Phantasy Star']
print(f"Here are the top Sega games: ")
for word in g_list:
    print(word)

user_input = input(f"Which you think should be removed? ")
g_list.remove(user_input)

print(f"Here are the top Sega games: ")
for word in g_list:
    print(word)
