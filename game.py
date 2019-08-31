def poker(hands):
    "Return the best hand: poker([hand,...]) => hand"
    return max(hands, key=hand_rank)

def flush(ranks):
    return (max(ranks) - min(ranks) == 4) and len(set(ranks)) == 5

def straight(hand):
    suits = [s for r,s in hand]
    return len(set(suits)) == 1


def hand_rank(hand):
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):            # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):                           # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):        # full house
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):                              # flush
        return (5, ranks)
    elif straight(ranks):                          # straight
        return (4, max(ranks))
    elif kind(3, ranks):                           # 3 of a kind
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):                          # 2 pair
        return (2, kind(2, ranks), ranks)
    elif kind(2, ranks):                           # kind
        return (1, kind(1, ranks), ranks)
    else:                                          # high card
        return (0, ranks)

def card_ranks(hand):
    ranks = ['--23456789TJQKA'.index(r) for r,s in hand]
    ranks.sort(reverse = True)
    return ranks
    
def test():
    "Test cases for the functions in poker program"
    sf = "6C 7C 8C 9C TC".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    assert straight([9,8,7,6,5]) == True
    assert straight([9,8,8,6,5]) == False
    assert flush(sf) == True
    assert flush(fk) == False
    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]
    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    assert poker([sf]) == sf
    assert poker([sf] + 99*[fh]) == sf
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)
    return 'tests pass'