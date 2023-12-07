def part_one():
    import re
    import numpy as np

    with open("./data/07_one.txt") as f:
        data = f.readlines()
    
    def type_strength(hand):
        if hand[0] == 5: return 6
        if hand[0] == 4: return 5
        if hand == [3, 2]: return 4
        if hand[0] == 3: return 3
        if hand == [2, 2, 1]: return 2
        if hand[0] == 2: return 1
        return 0

    def strength(card):
        if re.match("\d+", card):
            return int(card)
        match card:
            case "A": return 14
            case "K": return 13
            case "Q": return 12
            case "J": return 11
            case "T": return 10
    
    hands = []
    for line in data:
        hand, bid = line.strip().split(" ")

        hand = [strength(card) for card in hand]
        _, counts = np.unique(hand, return_counts=True)

        hand.insert(0, type_strength(sorted(counts, reverse=True)))
        bid = int(bid)
        
        hands.append([hand, bid])
    
    result = 0
    for i, hand in enumerate(sorted(hands, key=lambda hand: hand[0])):
        result += (i+1) * hand[1]

    print(result)

def part_two():
    import re
    import numpy as np

    with open("./data/07_one.txt") as f:
        data = f.readlines()
    
    def type_strength(hand):
        if hand[0] == 5: return 6
        if hand[0] == 4: return 5
        if hand == [3, 2]: return 4
        if hand[0] == 3: return 3
        if hand == [2, 2, 1]: return 2
        if hand[0] == 2: return 1
        return 0

    def strength(card):
        if re.match("\d+", card):
            return int(card)
        match card:
            case "A": return 14
            case "K": return 13
            case "Q": return 12
            case "J": return 1
            case "T": return 10
    
    hands = []
    for line in data:
        hand, bid = line.strip().split(" ")

        hand = np.array([strength(card) for card in hand])
        _, counts = np.unique(hand[hand != strength("J")], return_counts=True)
        
        if len(counts) > 0:
            counts = sorted(counts, reverse=True)
            counts[0] += (sum(hand == strength("J")))
        else:
            counts = [5]

        hand = list(hand)
        hand.insert(0, type_strength(sorted(counts, reverse=True)))
        bid = int(bid)
        
        hands.append([hand, bid])
    
    result = 0
    for i, hand in enumerate(sorted(hands, key=lambda hand: hand[0])):
        result += (i+1) * hand[1]
        
    print(result)

if __name__ == "__main__":
    part_one()
    part_two()