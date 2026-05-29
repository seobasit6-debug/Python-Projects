questions = [
    ("The HTML5 standard was published in 2014.", True),
    ("The first computer bug was formed by faulty wires.", False),
    ("FLAC stands for 'Free Lossless Audio Condenser'.", False),
    ("All program codes have to be compiled into an executable file in order to be run. This file can then be executed on any machine.", False),
    ("Linus Torvalds created Linux and Git.", True),
    ("Python was created by Guido van Rossum.", True),
    ("HTTP stands for HyperText Transfer Protocol.", True),
    ("A byte consists of 16 bits.", False),
    ("RAM stands for Random Access Memory.", True),
    ("The first version of Windows was released in 1995.", False),
    ("CSS stands for Cascading Style Sheets.", True),
    ("Java and JavaScript are the same language.", False),
    ("The binary number system uses digits 0 and 1.", True),
    ("An IP address can be used to identify a device on the internet.", True),
    ("SQL is used to manage NoSQL databases.", False),
    ("The internet and the World Wide Web are the same thing.", False),
    ("USB stands for Universal Serial Bus.", True),
    ("A compiler translates source code into machine code.", True),
    ("Python is a statically typed language.", False),
    ("The GPU is primarily used for processing graphics.", True),
    ("Wi-Fi stands for Wireless Fidelity.", False),
    ("An algorithm must always be written in a programming language.", False),
    ("The cloud refers to servers accessed over the internet.", True),
    ("JPEG is a lossless image format.", False),
    ("Open source software can be freely modified and distributed.", True),
]

import random

def play_quiz():
    print("\n" + "="*55)
    print("   🎮  TRUE / FALSE QUIZ — You have 4 lives!")
    print("="*55)
    print("  Type  'true' or 'false'  to answer each question.")
    print("  You lose a life for every wrong answer.")
    print("  The quiz ends when you lose all 4 lives.\n")

    lives = 4
    score = 0
    question_number = 0

    pool = questions.copy()
    random.shuffle(pool)

    while lives > 0:
        if not pool:
            pool = questions.copy()
            random.shuffle(pool)

        question, correct_answer = pool.pop()
        question_number += 1

        print(f"  ❤️  Lives: {lives}   |   ✅  Score: {score}")
        print(f"\nQ.{question_number}: {question} (True/False): ", end="")

        while True:
            user_input = input().strip().lower()
            if user_input in ("true", "false", "t", "f"):
                break
            print("  ⚠️  Please enter 'true' or 'false': ", end="")

        if user_input in ("true", "t"):
            user_answer = True
        else:
            user_answer = False

        if user_answer == correct_answer:
            score += 1
            print("  ✅  You got it right!")
        else:
            lives -= 1
            print("  ❌  That's wrong.")

        print(f"  The correct answer was: {correct_answer}.")
        print(f"  Your current score is: {score}/{question_number}")

        if lives > 0:
            print()
        else:
            print("\n" + "="*55)
            print("  💀  GAME OVER! You've used all 4 lives.")
            print(f"  🏆  Final Score: {score} correct out of {question_number} questions.")
            print("="*55 + "\n")

            again = input("  Play again? (yes/no): ").strip().lower()
            if again in ("yes", "y"):
                play_quiz()
            else:
                print("\n  Thanks for playing! Goodbye 👋\n")

if __name__ == "__main__":
    play_quiz()