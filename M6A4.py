# Josue Rosas 
# Student ID: 877784637 
# Section: 08
# Module 6 Assignment 4
def show_message(messages_list):
    copy_list = messages_list[:]
    while copy_list:
        current_message = copy_list.pop()
        print(current_message)
my_messages = []
while True: 
    message = input(f"What is your next message? (type 'quit' to exit)")
    if message == 'q':
        break
    my_messages.append(message)
print(f"First time calling function")
show_message(my_messages)
print(f"Second time calling function") 
show_message(my_messages) 