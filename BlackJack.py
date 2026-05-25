import random

LOGO = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      '------'                           |__/

SUITS = ["♠", "♥", "♦", "♣"]
RANKS = ["A", "2", "3", "4", "5", "6", "7",
         "8", "9", "10", "J", "Q", "K"]

def build_deck() -> list[str]:
    deck = [f"{rank}{suit}" for suit in SUITS for rank in RANKS]
    random.shuffle(deck)
    return deck

def card_value(card: str) -> int:
    rank = card[:-1]
    if rank in ("J", "Q", "K"):
        return 10
    if rank == "A":
        return 11
    return int(rank)

def hand_score(hand: list[str]) -> int:
    score = sum(card_value(c) for c in hand)
    aces  = sum(1 for c in hand if c[:-1] == "A")
    while score > 21 and aces:
        score -= 10
        aces  -= 1
    return score

def deal(deck: list[str]) -> str:
    return deck.pop()

def show_state(player_hand, dealer_hand, reveal_dealer=False):
    print(f"\n    Your cards:          {player_hand}, current score: {hand_score(player_hand)}")
    if reveal_dealer:
        print(f"    Computer's final hand: {dealer_hand}, final score: {hand_score(dealer_hand)}")
    else:
        print(f"    Computer's first card: {card_value(dealer_hand[0])}")

def play_round():
    deck        = build_deck()
    player_hand = [deal(deck), deal(deck)]
    dealer_hand = [deal(deck), deal(deck)]

    while True:
        show_state(player_hand, dealer_hand)
        score = hand_score(player_hand)

        if score == 21:
            print("    🃏  Blackjack!")
            break

        if score > 21:
            print(f"\n    Your final hand: {player_hand}, final score: {score}")
            print(f"    Computer's final hand: {dealer_hand}, final score: {hand_score(dealer_hand)}")
            print("\nYou went over 21. You lose 😤\n")
            return

        choice = input("\nType 'y' to get another card, type 'n' to pass: ").strip().lower()
        if choice == "y":
            player_hand.append(deal(deck))
        elif choice == "n":
            break
        else:
            print("    Invalid input – please type 'y' or 'n'.")

    while hand_score(dealer_hand) < 17:
        dealer_hand.append(deal(deck))

    p_score = hand_score(player_hand)
    d_score = hand_score(dealer_hand)

    print(f"\n    Your final hand:       {player_hand}, final score: {p_score}")
    print(f"    Computer's final hand: {dealer_hand}, final score: {d_score}")

    if d_score > 21:
        print("\nComputer went over 21. You win! 😄\n")
    elif p_score > d_score:
        print("\nYou win! 😄\n")
    elif p_score == d_score:
        print("\nDraw 🤝\n")
    else:
        print("\nYou lose 😤\n")

def main():
    print(LOGO)
    while True:
        ans = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").strip().lower()
        if ans == "y":
            play_round()
        elif ans == "n":
            print("\nThanks for playing. Goodbye! 👋\n")
            break
        else:
            print("    Please type 'y' or 'n'.")

if __name__ == "__main__":
    main()