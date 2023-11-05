import random

# a rock paper, scissors game, with the computer

'''
rock beats scissors
scissors beats paper
paper beats rock
'''

'''
rock is 0
scissors is 1
paper is three 2
'''

print("Welcome to rock paper scissors pick 0 for Rock, 1 for scissors and 2 for paper\n")

# get input from the user convert it to Number.
print("Press (quit) to exit the game")
computer_score = 0
user_score = 0

# list to store the choices.
choices = ["rock", "paper", "scissors"]

# using conditional statement to determine the winner
while True:
    # get a random number first for the computer.
    user_input = input("rock (0), paper(0), scissors(0) ? ")

    if user_input == "quit":
        break
    if user_input == "":
        print("Enter a value in input stream")
        continue
    # convert user_Input back to int

    user_input = int(user_input)
    if user_input > 2 or user_input < 0 or user_input == -0:
        print("invalid input")  # error message
        continue

    computer_random = random.randint(0, 2)

    # associate the random number to Computer choice
    computer_choice = choices[computer_random]

    # associate the random number to User choice
    user_choice = choices[user_input]

    # Conditional statement to determine the winner
    if user_choice == computer_choice:
        print("tie")
        # check for when the computer wins  (rock== 0, paper == 1, scissors == 2)
    elif (user_input == 2 and computer_random == 0) or (user_input == 1 and computer_random == 2) or (
            user_input == 0 and computer_random == 1):
        print("Computer wins")
        computer_score += 1
    else:
        print("You win")
        user_score += 1

    print("computer picked", computer_choice)
    print("you  picked", user_choice)

print(f"Computer HighScore: {computer_score}")
print(f"Your_score: {user_score}")
