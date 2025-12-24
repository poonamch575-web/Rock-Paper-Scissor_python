import random

print("Welcome to Rock Paper Scissors Game")
print("Choices: rock, paper, scissors")

while True:
    user_choice = input("Enter your choice: ").lower()

    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please try again.")
        continue

    computer_choice = random.choice(["rock", "paper", "scissors"])

    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It's a Tie!")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("You Win!")
    elif user_choice == "paper" and computer_choice == "rock":
        print("You Win!")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("You Win!")
    else:
        print("Computer Wins!")

    play_again = input("Do you want to play again? (y/n): ").lower()
    if play_again != "y":
        print("Thanks for playing!")
        break
