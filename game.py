import random
#imported random to shuffle the deck of cards before making a deal 
def poker(hands):
    "Return the list of best hand: poker([hand,...]) => hand"
    return max(hands, key=hand_rank)

def deal

def allmax(iterable, key = None):
    result, maxval = [], None
    key = key or (lambda x:x)
    for x in interable:
        xval = key(x)
        if (not result or xval > maxval):
            result, maxval = [x], xval
        elif (xval == maxval):
            result.append(x)
    return result

def flush(hand):
    suits = [s for r,s in hand]
    return len(set(suits)) == 1
    

def straight(ranks):
    return (max(ranks) - min(ranks) == 4) and len(set(ranks)) == 5
    

def kind(n, ranks):
    for rank in ranks:
        if (ranks.count(rank) == n):
            return rank
    return None

def two_pair(ranks):
    pair = kind(2, ranks)   
    lowpair = kind(2, list(reversed(ranks)))
    if(pair and lowpair != pair):
        return (pair, lowpair)
    else:
        return False
        
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
    return [5,4,3,2,1] if (ranks == [14,5,4,3,2]) else ranks
    
def test():
    "Test cases for the functions in poker program"
    sf = "6C 7C 8C 9C TC".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    tp = "5S 5H 9C 9H 6S".split() # Two Pairs
    s1 = "AS 2S 3S 4S 5C".split() # A-5 Straight
    s2 = "2C 3C 4C 5S 6S".split() # 2-6 Straight
    ah = "AS 2S 3S 4S 6C".split()
    sh = "2S 3S 4S 6C 7D".split() 
    assert poker([s1, s2, ah, sh]) == s2
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7
    assert two_pair(fkranks) == None
    assert two_pair(tpranks) == (9, 5)
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
