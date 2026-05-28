import random

TITLE = r"""
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ '/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/  
"""

# (name, category, country, followers_in_millions)
entities = [
    ("Virat Kohli", "Cricketer", "India", 269),
    ("Instagram", "Social media platform", "United States", 672),
    ("Kim Kardashian", "Reality TV personality and businesswoman", "United States", 364),
    ("Selena Gomez", "Musician and actress", "United States", 429),
    ("Cristiano Ronaldo", "Footballer", "Portugal", 638),
    ("Lionel Messi", "Footballer", "Argentina", 503),
    ("Kylie Jenner", "Media personality and businesswoman", "United States", 399),
    ("Dwayne Johnson", "Actor and wrestler", "United States", 396),
    ("Ariana Grande", "Singer", "United States", 380),
    ("Taylor Swift", "Singer", "United States", 283),
    ("Beyonce", "Singer", "United States", 318),
    ("Justin Bieber", "Singer", "Canada", 292),
    ("NASA", "Space agency", "United States", 97),
    ("National Geographic", "Media brand", "United States", 283),
    ("Nike", "Sports brand", "United States", 302),
]

def play_game():
    print(TITLE)
    print("Welcome to Higher or Lower Followers!\n")

    random.shuffle(entities)
    score = 0
    i = 0

    while i < len(entities) - 1:
        a = entities[i]
        b = entities[i + 1]

        print(f"Compare A: {a[0]}, a {a[1]}, from {a[2]}.")
        print()
        # ASCII art for "Ig" (vs logo style) — simple separator
        print(" _     __")
        print("| |   / /____")
        print("| |  / / ___/")
        print("| |_/ (__  )")
        print("|____/____/")
        print()
        print(f"Against B: {b[0]}, a {b[1]}, from {b[2]}.")

        answer = input("Who has more followers? Type 'A' or 'B': ").strip().upper()

        if answer not in ('A', 'B'):
            print("Invalid input. Please type 'A' or 'B'.")
            continue

        a_wins = a[3] >= b[3]
        correct = (answer == 'A' and a_wins) or (answer == 'B' and not a_wins)

        if correct:
            score += 1
            print(f"You're right! Current score: {score}.")
            i += 1
        else:
            print(TITLE)
            print(f"Sorry, that's wrong. Final score: {score}")
            return

    print(TITLE)
    print(f"You completed the game! Final score: {score}")

if __name__ == "__main__":
    play_game()