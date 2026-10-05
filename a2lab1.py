# Josue Rosas 
# Student ID: 877784637 
# Section: 08
# Module 2, Assignment 1

g_list= []
g_list.append (input(f"What is your favorite game? ").title())
g_list.append (input(f"What is your second favorite game? ").title())
g_list.append (input(f"What is your third favorite game? ").title())


print(f"One of your favorite games is {g_list.pop(2)}")
print(f"One of your favorite games is {g_list.pop(1)}")
print(f"One of your favorite games is {g_list.pop(0)}")


