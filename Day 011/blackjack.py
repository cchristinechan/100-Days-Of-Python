import random
import art
def calculate_score(hand):
    """Takes a list of cards and returns the score calculated from the cards"""
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    if sum(hand) > 21 and 11 in hand:
        hand[hand.index(11)] = 1
        # alternative:
        # hand.remove(11)
        # hand.append(1)
    return sum(hand)

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def compare(p_score, d_score):
    if p_score > 21 and d_score > 21:
        return"You both went over. You both lose. 😔"
    elif d_score == 0:
        return "Dealer has a Blackjack. You lose. 😭"
    elif p_score == 0:
        return"You have a Blackjack. You win! 🎊"
    elif p_score > 21:
        return"You went over. You lose. 😢"
    elif d_score > 21:
        return"Dealer went over. You win! 😮"
    elif p_score > d_score:
        return"You win! 😊"
    elif p_score == d_score:
        return"Draw! 😐"
    else:
        return"You lose. 😞"

play = True
while play:
    keep_playing = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if keep_playing == 'n':
        play = False
        break

    print("\n" * 20)
    print(art.logo)

    player_hand = []
    dealer_hand = []
    dealer_score = -1
    player_score = -1
    deal_another = True

    # Deal initial cards
    for _ in range(2):
        player_hand.append(deal_card())
        dealer_hand.append(deal_card())

    while deal_another:
        # calculate initial scores
        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)
        print(f"Your cards: {player_hand}, current score: {player_score}")
        print(f"Dealer's first card: {dealer_hand[0]}")

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            deal_another = False
        else:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if another_card == 'n':
                deal_another = False
            else:
                player_hand.append(deal_card())
                player_score = calculate_score(player_hand)

            # dealer's turn
    while dealer_score != 0 and dealer_score < 17:
        dealer_hand.append(deal_card())
        dealer_score = calculate_score(dealer_hand)

        # final results
    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer_hand}, final score: {dealer_score}")
    print(compare(player_score, dealer_score) + "\n")
