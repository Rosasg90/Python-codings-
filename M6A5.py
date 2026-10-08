# Josue Rosas 
# Student ID: 877784637 
# Section: 08
# Module 6 Assignment 5
def comp_avg(*args):
    total = 0
    for num in args: 
        total += num
    return total /len(args)
def comp_max(*args): 
    max_number = max(args)
    return max_number
def comp_min(*args):
    min_number = min(args)
    return min_number 
