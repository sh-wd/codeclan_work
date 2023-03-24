my_number = 6

user_value = int(input("Guess a number: "))

while user_value != my_number:
    if user_value > my_number:
        print("Too high")
    if user_value < my_number:
        print("Too low")
    user_value = int(input("Sorry, wrong! Try again "))

print("You got it!")