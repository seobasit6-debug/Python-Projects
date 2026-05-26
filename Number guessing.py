import random

# ASCII art banner
BANNER = r"""
 _   _                 _               
| \ | |_   _ _ __ ___ | |__   ___ _ __ 
|  \| | | | | '_ ` _ \| '_ \ / _ \ '__|
| |\  | |_| | | | | | | |_) |  __/ |   
|_| \_|\__,_|_| |_| |_|_.__/ \___|_|   
  ____                     _             
 / ___|_   _  ___  ___ ___(_)_ __   __ _ 
| |  _| | | |/ _ \/ __/ __| | '_ \ / _` |
| |_| | |_| |  __/\__ \__ \ | | | | (_| |
 \____|\__,_|\___||___/___/_|_| |_|\__, |
  ____                              |___/ 
 / ___| __ _ _ __ ___   ___               
| |  _ / _` | '_ ` _ \ / _ \              
| |_| | (_| | | | | | |  __/              
 \____|\__,_|_| |_| |_|\___|              
"""

def print_banner():
    print(BANNER)

def get_difficulty():
    while True:
        choice = input("Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()
        if choice == 'easy':
            return 10
        elif choice == 'hard':
            return 5
        else:
            print("Invalid choice. Please type 'easy' or 'hard'.")

def play_game():
    print_banner()
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    secret_number = random.randint(1, 100)
    attempts = get_difficulty()

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        user_input = input("Make a guess: ").strip()

        # Validate input
        if not user_input.isdigit():
            print("Guess again.")
            attempts -= 1
            continue

        guess = int(user_input)

        if guess < 1 or guess > 100:
            print("Please guess a number between 1 and 100.")
            print("Guess again.")
            attempts -= 1
            continue

        if guess < secret_number:
            print("Too low.")
            if attempts > 1:
                print("Guess again.")
        elif guess > secret_number:
            print("Too high.")
            if attempts > 1:
                print("Guess again.")
        else:
            print(f"\n🎉 Congratulations! You guessed it! The number was {secret_number}!")
            return True

        attempts -= 1

    print(f"\n💀 You've run out of attempts! The number was {secret_number}. Better luck next time!")
    return False

def main():
    while True:
        play_game()
        again = input("\nWould you like to play again? (yes/no): ").strip().lower()
        if again not in ('yes', 'y'):
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()