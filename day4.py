import random as rand

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
user_choice = int(input())
computer_choice = rand.randint(0, 2)
choices = ["Rock", "Paper", "Scissors"]
print(f"You chose: {choices[user_choice]}")
print(f"Computer chose: {choices[computer_choice]}")
if user_choice == computer_choice:
    print("It's a draw.")
elif (user_choice == 0 and computer_choice == 2) or \
     (user_choice == 1 and computer_choice == 0) or \
     (user_choice == 2 and computer_choice == 1):   
    print("You win!")
else:
    print("You lose.")