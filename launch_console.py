print('Welcome to the Launch Console')
name = input('What is your name? ')
print(f'Hello, {name}')
menu = ["About me", "My goals", "My grade", "Exit"]
print(f'You have 4 options, {menu} what would you like')
option = input('What option would you like to pick')

def about_me():
    return "My name is Kabinsoul and my hobby is soccer"

def my_goals():
    return "My goal is to just have a peaceful life and become successful"

def my_grade():
    return "I am currently in 9th grade and doing pretty good right now"

question_loop = True
while question_loop == True:
    if option == "1":
        print(about_me())
        option = input('What option would you like to pick')
    elif option == "2":
        print(my_goals())
        option = input('What option would you like to pick')
    elif option == "3":
        print(my_grade())
        option = input('What option would you like to pick')
    else:
        print('Goodbye')
        question_loop = False