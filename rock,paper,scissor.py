import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_user_choice():
    choice = input("Enter rock, paper, or scissors: ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Try again.")
        choice = input("Enter rock, paper, or scissors: ").lower()
    return choice

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "You win! 🎉"
    else:
        return "Computer wins! 🤖"

def play_game():
    print("🎮 Welcome to Rock, Paper, Scissors!")
    
    while True:
        user = get_user_choice()
        computer = get_computer_choice()
        
        print(f"You chose: {user}")
        print(f"Computer chose: {computer}")
        
        result = determine_winner(user, computer)
        print(result)
        
        play_again = input("Play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! 👋")
            break

# Start the game
play_game()