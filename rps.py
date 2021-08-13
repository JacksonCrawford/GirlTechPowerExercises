import random

# Function to generate the computer's choice
def generate_hand():
    rand_num = random.randint(0, 3)
    if rand_num == 0:
        return "rock"
    elif rand_num == 1:
        return "paper"
    else:
        return "scissors"

# Function to determine winner
def whoWins(user, computer):
    if user == "rock" and computer == "scissors":
        return "You won!"
    elif user == "rock" and computer == "paper":
        return "You lost :("
    elif user == "rock" and computer == "rock":
        return "We tied!"
    elif user == "paper" and computer == "rock":
        return "You win!"
    # Continue for all five other combinations

print("Let's play rock paper scissors!")

# Add input prompt
user_choice = input("")

# Call generate_hand() for this value
computer_choice = 

# Determine the winner
winner = whoWins(user_choice, computer_choice)

# Print out who won
print(winner)

# CHALLENGE: Make a loop that keeps the game going until you win!
