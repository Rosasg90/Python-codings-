# Josue Rosas 
# Student ID: 877784637 
# Section: 08
# Module 9 Assignment 1
population_dict = {}
while True: 
    city = input(f"What is the next city? (press q to quit) ")
    if city == 'q' or city == 'Q':
        break
    pop_city = int(input(f'What is the poplution of {city}?'))
    population_dict[city] = pop_city
    
small_cites = int(input(f"What is the largest population for a small town? "))
groups = {
    'Big Cities:':{}, 
    
    'Small Towns:': {}
}
for city , pop_city  in population_dict.items():
    if pop_city <= small_cites:
        groups['Small Towns:'][city] = pop_city
    else:
        groups['Big Cities:'][city] = pop_city 
with open("populationdata.txt" , "w") as f:
    for group_name, cities in groups.items():
        f.write(f"{group_name}\n")
        for city, pop in cities.items():
            f.write(f"{city},{pop}\n")



