import math

def identify_hand(hand):

    cards = [card for card in hand]
    counts = [cards.count(card) for card in cards]

    if sum(counts) == 13:
        return 3 # full house
    if sum(counts) == 9:
        return 5 # two pair
    elif max(counts) == 5:
        return 1 # 5kind
    elif max(counts) == 4:
        return 2 #4kind
    elif max(counts) == 3:
        return 4 #3kind
    elif max(counts) == 2:
        return 6 #pair
    else:
        return 7 # high card


def get_card_ranks_per_hand(hand):
    """
    Replace the card numbers with the rank they are in terms of value
    This will be used to help find the highest card.
    """

    card_order = ["A","K","Q","J","T","9","8","7","6","5","4","3","2"]
    cards = [card for card in hand]

    ranks = [card_order.index(card) for card in cards]   
    
    return ranks


def part1():        

    # data = open("day_07/test_data_day_07.txt").read().split("\n")
    data = open("day_07/input_day_07.txt").read().split("\n")
    hands, bets = [row.split()[0] for row in data], [row.split()[1] for row in data]
    num_of_hands = len(hands)

    hands_and_bets = []

    for hand, bet in zip(hands, bets):
        hand_type = identify_hand(hand)
        hand_card_ranks = get_card_ranks_per_hand(hand)
        print(f"{hand} is of type {hand_type}, with order {hand_card_ranks}")
        hands_and_bets.append({"hand": hand, "type": hand_type, "hand_card_ranks": hand_card_ranks, "bet": bet})
        

    # Sort by hand type
    hands_and_bets = sorted(hands_and_bets, key=lambda x: (x["type"], x["hand_card_ranks"]))
    # print(hands_and_bets)

    answer = sum([x * int(y["bet"]) for x,y in zip(reversed(range(1, num_of_hands+1)), hands_and_bets)])

    print(answer)


if __name__ == "__main__":
    part1()