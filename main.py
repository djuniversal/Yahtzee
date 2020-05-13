import time

def main():
    x = True
    while x:
        start_time = time.time()
        for x in range(0,1000):
            hand = dieRoll(5)
            hand.sort()
            if isFullHouse(hand):
                print("Full House     {} - {}".format(x,hand))
            if isLargeStraight(hand):
                print("Large Straight {} - {}".format(x,hand))
            if isYahtzee(hand):
                print("Yahtzee!!      {} - {}".format(x,hand))
        print("time={}".format(time.time()-start_time))
        x = False


def dieRoll(dieCount):
     import random
     if type(dieCount) != int:
             raise TypeError('dieCount must be a positive integer =< 5')
     if dieCount < 1 or dieCount > 5:
             raise ValueError('dieCount must be a positive integer =< 5')
     roll = []
     i=0
     while i < dieCount:
             roll.append(random.randint(1,6))
             i += 1
     return roll

def isFullHouse(hand):
    if len(hand) != 5:
        return False
    count_unique = set()
    for x in hand:
        count_unique.add(x)
    if len(count_unique) == 2:
        y = next(iter(count_unique))
        if hand.count(y) == 2 or hand.count(y) == 3:
            return True
    return False

def isLargeStraight(hand):
    if len(hand) != 5:
        return False
    hand.sort()
    count_unique = set()
    for x in hand:
        count_unique.add(x)
    if len(count_unique) == 5:
        if hand[4] - hand[0] == 4:
            return True
    return False

def isYahtzee(hand):
    if len(hand) != 5:
        return False
    count_unique = set()
    for x in hand:
        count_unique.add(x)
    if len(count_unique) == 1:
        return True
    return False

def isSmallStraight(hand):
    if len(hand) != 5:
        return False
    count_unique = set()
    for x in hand:
        count_unique.add(x)
    if len(count_unique) < 4:
        return False


if __name__ == "__main__":
    main()