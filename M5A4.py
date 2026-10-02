# Josue Rosas 
# Student ID: 877784637 
# Section: 08
# Module 5 Assignment 4
orders_list = ['pastrami', 'turkey', 'pastrami', 'ham', 'turkey']
finished_list = []
food_going = True
while food_going:
    finished_list.append(orders_list.pop())
    if len(orders_list) == 0:
        food_going = False
for food in finished_list:
    print(f"I made your {food}")
print(f"Here are all the sandwitches I made:")
for food in finished_list: 
    print(food)



        