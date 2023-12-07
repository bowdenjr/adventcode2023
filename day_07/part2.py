from pprint import pprint

def identify_hand_jacks_wild(hand):

    # cards = [card for card in hand]
    # counts = [cards.count(card) for card in cards]
    card_order = ["A","K","Q","T","9","8","7","6","5","4","3","2","J"]

    # Each wild J can be different, which allows for full houses
    best_rank = 8

    for wild_repalcement in card_order:

        cards = [card for card in hand]
        
        """
        A6AJ6 can come out as a full house, but in order to detect this
        I need to try KKK77 and KK777
        """

        cards = [card.replace("J", wild_repalcement) for card in cards] # change this to only replace the first J
        counts = [cards.count(card) for card in cards]

        if sum(counts) == 13:
            rank = 3 # full house
        elif sum(counts) == 9:
            rank = 5 # two pair
        elif max(counts) == 5:
            rank = 1 # 5kind
        elif max(counts) == 4:
            rank = 2 #4kind
        elif max(counts) == 3:
            rank = 4 #3kind
        elif max(counts) == 2:
            rank = 6 #pair
        else:
            rank = 7 # high card
        
        best_rank = min(rank, best_rank)
    
    return best_rank


def get_card_ranks_per_hand(hand):
    """
    Replace the card numbers with the rank they are in terms of value
    This will be used to help find the highest card.
    """

    card_order = ["A","K","Q","T","9","8","7","6","5","4","3","2","J"]
    cards = [card for card in hand]

    ranks = [card_order.index(card) for card in cards]   
    
    return ranks


def part2():

    # data = open("day_07/test_data_day_07.txt").read().split("\n")
    data = open("day_07/input_day_07.txt").read().split("\n")
    hands, bets = [row.split()[0] for row in data], [row.split()[1] for row in data]
    num_of_hands = len(hands)

    hands_and_bets = []

    for hand, bet in zip(hands, bets):
        hand_type = identify_hand_jacks_wild(hand)
        hand_card_ranks = get_card_ranks_per_hand(hand)
        hands_and_bets.append({"hand": hand, "type": hand_type, "hand_card_ranks": hand_card_ranks, "bet": bet})
        
    hands_and_bets = sorted(hands_and_bets, key=lambda x: (x["type"], x["hand_card_ranks"]))
    pprint(hands_and_bets[:100])

    with open("day_07/output_file.txt","w") as f:
        for line in hands_and_bets:
            f.write(str(line)+"\n")

    answer = sum([x * int(y["bet"]) for x,y in zip(reversed(range(1, num_of_hands+1)), hands_and_bets)])

    print(answer) # 245,497,758 too low, 248,083,749 too high, is it 248,316,311 no


if __name__ == "__main__":
    part2()