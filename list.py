my_list = [ "1", 2, "ready"]
my_list[-1] = "late"
print (my_list)
print (f"my list is {len(my_list)} items")
my_list.append("for")
my_list.append("work")
my_list.insert(1,"will")
print(my_list)
print(f"my last item of my list was {my_list.pop()}")
print(my_list)

del(my_list[-1])
print(my_list)

new_list = ("I" , "am", "the", "very", "model", "of", "a","modern", "general" )
print(new_list)
print(sorted(new_list))
print(new_list)
new.list.sort()
print(new_list)
new_list.reverse()
print(new_list)