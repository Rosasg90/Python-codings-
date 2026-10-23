# Josue Rosas 
# Student ID: 877784637 
# Section: 08
# Module 7 Assignment 3
import calendar 
class User: 
    def __init__(self,first_name, last_name, user_id, last_login, password):
        self.first_name = first_name 
        self.last_name = last_name 
        self.user_id = user_id
        self.last_login = last_login 
        self.password = password
        self.full_name = f"{self.first_name} {self.last_name} "
    
    def describe_user(self):
        print(f"Accessing user {self.user_id}: ") 
        print(f"{self.full_name} last logged in {self.last_login}")
    
    def greet_user(self):
        print(f"Welcome to the Jungle {self.full_name}, You gonna die ")
    
    def new_login( self, month, day, year):
        self.month = month 
        self.year = year 
        self.day = day
        if(self.month > 12 or self.month < 0):
            print(f"This is not a valid month.")
            return
        if(self.year > 2025 or self.year < 0):
            print(f"This is not a valid year.")
            return
        if(self.day > 31 or self.day < 0):
            print(f"This is not a vaild day.")
            return
        
        
        self.last_login = f"{calendar.month_name[month]} {day}, {year}"
        
class Admin(User):
   def __init__(self,first_name, last_name, user_id, login, password):
       super().__init__(first_name, last_name, user_id, login, password)
       self.privileges = []


   def add_privilege(self, privilages):
       self.privileges.append(privilages)


    
   def show_privileges(self):
       print(f"{self.full_name} has the following privilages:" )
       for privilege in self.privileges:
           print(f"{privilege}")      



jim = User(first_name='Jim',
           last_name='Bob',
           user_id=1000,
           last_login='June 12, 1998',
           password='password123')
jim.describe_user()
jim.greet_user()
joe = User('Joe',
           'Bob',
           1001,
           'July 4, 2001',
           'babygirl')
joe.greet_user()
joe.describe_user()
joe.new_login(2, 3, 2025)
joe.describe_user()
joe.new_login(15, 3, 2025)
joe.new_login(2, 35, 2025)
joe.new_login(2, 3, -55)
 
 
 
alice = Admin('Alice',
              'Wonder',
              1,
              'September 3, 2022',
              'P@ssw0rd')
alice.add_privilege('delete post')
alice.add_privilege('delete user')
alice.add_privilege('add user')
alice.add_privilege('give admin rights')
alice.show_privileges()
       
    
       



