# Ask the user to choose one of two options:
# if they type 'p', our program should print "Hello" and then ask the user again. Keep repeating this until...
# if they type 'q', our program should terminate.


# Let's begin by asking the user to type either 'p' or 'q'. You know how to do this using input()
# user_input = ...

user_input = input("Do you wish to print Hello? (type p to yes/type q to no)")

while user_input != 'q':
    if user_input == 'p':
        print("Hello")
    user_input = input("Do you wish to print Hello? (type p to yes/type q to no)")





