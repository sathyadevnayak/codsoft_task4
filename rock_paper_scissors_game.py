import random
import time

def display_title():
    print("\n")
    print("************************************************")
    print("* Welcome to Rock, Paper, Scissors!               *")
    print("************************************************")
    print("\n")

def display_rules():
    print("Rules:")
    print("- Rock beats Scissors")
    print("- Scissors beats Paper")
    print("- Paper beats Rock")
    print("\n")

def get_user_choice():
    while True:
        user_choice = input("Enter your choice {Rock(r), Paper(p), Scissors(s), Quit(q)}: ").lower()
        if user_choice=="r":
            user_choice="rock"
        if user_choice=="p":
            user_choice="paper"
        if user_choice=="s":
            user_choice="scissors"
        if user_choice=="q":
            user_choice="quit"
        if user_choice in ["rock" , "paper" , "scissors" , "quit"]:
            return user_choice
        else:
            print("Invalid choice. Please enter rock, paper, scissors, or quit.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors" ) or
        (user_choice == "paper" and computer_choice == "rock" ) or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def display_result(user_choice, computer_choice, result):
    print(f"\nYou choose: {user_choice.capitalize()}")
    print(f"Computer choose: {computer_choice.capitalize()}")
    print(result)

def main():
    user_score = 0
    computer_score = 0

    display_title()
    display_rules()

    while True:
        user_choice = get_user_choice()
        if user_choice == "quit":
            print("Thanks for playing!")
            break

        computer_choice = get_computer_choice()

        result = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, result)

        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1

        print(f"\nScore:\nYou: {user_score}\nComputer: {computer_score}")

        time.sleep(2)  # Pause for 2 seconds before next round

if __name__ == "__main__":
    main()
