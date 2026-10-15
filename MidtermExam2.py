firstnum_int = int(input(f"What is your first number?" ))
secondnum_int = int(input(f"What is your second number? "))

if(firstnum_int > secondnum_int):
    print(f"The first number is greater than the second number.")
elif(firstnum_int < secondnum_int):
    print(f"The first number is less than the second number.")
elif(firstnum_int == secondnum_int):
    print(f"First number is equal to the second number.")
    if(firstnum_int % 2) == 0:
        print(f"Your first number is Even")
    else:
        print(f"Your first number is Odd")
    if(secondnum_int % 2) == 0:
        print(f"Your second number is Even")
    else: 
        print(f"Your second number is Odd") 