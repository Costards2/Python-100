import random as rd

def deal_card():
    """Return a random card from the deck (infinite deck)."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return rd.choice(cards)

def calculate_score(hand):
    """Return best blackjack score for a hand (aces 11 -> 1 if needed)."""
    score = sum(hand)
    while score > 21 and 11 in hand:
        ace_index = hand.index(11)
        hand[ace_index] = 1
        score = sum(hand)
    return score

def show_hands(user_cards, dealer_cards, reveal_dealer=False):
    print(f"Your cards: {user_cards}  (score: {calculate_score(user_cards)})")
    if reveal_dealer:
        print(f"Dealer cards: {dealer_cards}  (score: {calculate_score(dealer_cards)})")
    else:
        print(f"Dealer shows: [{dealer_cards[0]}]")

def compare_scores(user_score, dealer_score):
    if user_score > 21:
        return "Dealer Won!"
    if dealer_score > 21:
        return "You Won!"
    if user_score > dealer_score:
        return "You Won!"
    if user_score < dealer_score:
        return "Dealer Won!"
    return "Draw!"

def play_round():
    user_cards = [deal_card(), deal_card()]
    dealer_cards = [deal_card(), deal_card()]

    print("Welcome to BlackJack\n")
    show_hands(user_cards, dealer_cards, reveal_dealer=False)
    print()

    while True:
        user_score = calculate_score(user_cards)
        if user_score >= 21:
            break

        ans = input("Do you want another card? (y/n) ").strip().lower()
        print()
        if ans == "y":
            user_cards.append(deal_card())
            show_hands(user_cards, dealer_cards, reveal_dealer=False)
            print()
        else:
            break

    user_score = calculate_score(user_cards)
    dealer_score = calculate_score(dealer_cards)

    if user_score <= 21:
        while dealer_score < 17:
            dealer_cards.append(deal_card())
            dealer_score = calculate_score(dealer_cards)

    # Resultado
    show_hands(user_cards, dealer_cards, reveal_dealer=True)
    print()
    print(compare_scores(user_score, dealer_score))
    print()

def main():
    while True:
        start = input("Would you like to play? (y/n) ").strip().lower()
        print()
        if start == "n":
            break
        if start == "y":
            play_round()

if __name__ == "__main__":
    main()
