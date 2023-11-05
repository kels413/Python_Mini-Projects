import random
print("Welcome To The Guess The Secret Number 🎉")
#
# # Generate Random Number 0-20
# # Ask The User To Input A Random Number
# # it should be a for loop that continues to pop up until the user gets it, or decides to quit the game.
# # Check If the Number is Greate than the secret Number
# # if Number Greater than the secret Number suggest it's greater
# # if Number Lesser than the secret Number suggest it's lesser
#
secret_number = random.randint(1, 21)
# print(secret_number)
attempt = 0
while True:
    user_guess = int(input("Guess the secret Number: "))
    attempt += 1

    if user_guess > secret_number:
        print("Guess Too High Try Again!: ")
    elif user_guess < secret_number:
        print("Guess Too Low Try Again!: ")
    else:
        print("\nLucky this time you got it 🎉")
        print("your highScore is {}".format(attempt))
        break

    if attempt >= 5:
        continue_game = input("Seems Guessing too Hard 🤦 do you want to continue (y/n) ")
        if continue_game.lower() != 'y':
            print("Not Lucky this time 😭!")
            break





