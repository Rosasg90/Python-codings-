# Josue Rosas 
# Student ID: 877784637 
# Section: 08
# Module 8 Assignment 4

file_name = input(f"What is he file with the data? ")
def dictionary_maker(path):
    ret_dict = {}
    try: 
        with open (path) as file_object:
            for data in file_object:
                data = data.strip()
                data = data.split(':')
                ret_dict[data[0]] = data[1].strip()
    except FileNotFoundError: 
        print(f"The file {file_name} does not exist on this system ")
    
    return ret_dict

responde = dictionary_maker(file_name)
print(responde)