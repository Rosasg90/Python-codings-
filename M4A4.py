# Josue Rosas 
# Student ID: 877784637 
# Section: 08
# Module 4 Assignment 4
guy_dict1 = {
    'name': 'Jimmer',
    'age': '23',
    'scout rank':'Eagles',
    'scout badge': []
}
print(f"I know Jimmer has three scout badges, what are they?") 
badge1 = input(f"The first badge is: ") 
badge2 = input(f"The second badge is: ") 
badge3 = input(f"The third badge is: ") 
guy_dict1['scout badge'] = badge1, badge2, badge3 
print(guy_dict1)