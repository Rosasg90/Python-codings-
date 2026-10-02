# Josue Rosas 
# Student ID: 877784637 
# Section: 08
# Module 5 Assignment 3
triviabank_dict = {}

triva_going = True
while triva_going: 
    question_str = input(f"Enter the next question: ")
    if question_str == 'done':
        print(f"We will stop entering question now") 
        break
    if question_str =='':
        print(f"You did not enter a question, let's try again.")
        continue       
    answer_str = input(f"Enter the correct answer: ")
    triviabank_dict[question_str] = answer_str

print(f"Here are the final trivia dictionary: ")
for question ,answer in triviabank_dict.items():
    print(f"The question is:{question}")
    print(f"And the answer is:{answer}")

