class Hand:
    import time

    def __init__(self):
        self.hand = self.dieRoll(5)

    def main():
        x = True
        while x:
            start_time = time.time()
            for x in range(0,1000):
                hand = dieRoll(5)
                hand.sort()
                if is3ofaKind(hand):
                    print("3 of a Kind    {} - {}".format(x,hand))
                if is4ofaKind(hand):
                    print("4 of a Kind    {} - {}".format(x,hand))
                if isFullHouse(hand):
                    print("Full House     {} - {}".format(x,hand))
                if isLargeStraight(hand):
                    print("Large Straight {} - {}".format(x,hand))
                if isSmallStraight(hand):
                    print("Small Straight {} - {}".format(x,hand))
                if isYahtzee(hand):
                    print("Yahtzee!!      {} - {}".format(x,hand))
            print("time={}".format(time.time()-start_time))
            x = False

    def sortHand(self):
        self.hand.sort()

    def discard(self, discard_list):
        looper = list(range(0,5))
        looper.reverse()
        for x in looper:
            if discard_list[x]:
                del(self.hand[x])
        new_roll = self.dieRoll(5-len(self.hand))
        self.hand += new_roll

    def showHand(self):
        return list(self.hand)

    def sumHand(self, hand):
        """Sums all dice in hand for socring chance, 3 of a Kind, or 4 of a Kind

        Parameters:
            hand (list): List of integers that represent a hand of dice

        Returns:
            int: Sum of list of integers
        """
        handSum = 0
        for x in hand:
            handSum += x
        return handSum

    def dieRoll(self, dieCount):
        """Returns maximum of 5 random integers from 1-6 as a list.

        Parameters:
            dieCount (int): The number of dice required to be returned

        Returns:
            list(ints[]): List of dice
        """
        import random
        #2 checks to make sure the inpute is a positive integer
        if type(dieCount) != int:
                raise TypeError('dieCount must be a positive integer =< 5')
        if dieCount < 1 or dieCount > 5:
                raise ValueError('dieCount must be a positive integer =< 5')
        #empty return set
        roll = []
        i=0
        #For each 'Die' append a random int from 1-6 to the list
        while i < dieCount:
                roll.append(random.randint(1,6))
                i += 1
        #return list object with random numbers
        return roll

    def isFullHouse(self):
        """Checks if the current Hand object matches criteria for a Full House and returns a bool

        Returns:
            bool: The Hand is a Full House
        """
        hand = self.hand
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

    def isLargeStraight(self):
        """Checks if the current Hand object matches criteria for a Large Straight and returns a bool

        Returns:
            bool: The Hand is a Large Straight
        """
        hand = self.hand
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

    def isYahtzee(self):
        """Checks if the current Hand object matches criteria for a Yahtzee and returns a bool

        Returns:
            bool: The Hand is a Yahtzee
        """
        hand = self.hand
        if len(hand) != 5:
            return False
        count_unique = set()
        for x in hand:
            count_unique.add(x)
        if len(count_unique) == 1:
            return True
        return False

    def isSmallStraight(self):
        """Checks if the current Hand object matches criteria for a Small Straight and returns a bool

        Returns:
            bool: The Hand is a Small Straight
        """
        hand = self.hand
        if len(hand) != 5:
            return False
        count_unique = set()
        for x in hand:
            count_unique.add(x)
        if len(count_unique) < 4:
            return False
        if hand.count(3) and hand.count(4):
            if hand.count(5) and (hand.count(2) or hand.count(6)):
                return True
            if hand.count(2) and (hand.count(1) or hand.count(5)):
                return True
        return False

    def is3ofaKind(self):
        """Checks if the current Hand object matches criteria for a 3 of a Kind and returns a bool

        Returns:
            bool: The Hand is a 3 of a Kind
        """
        hand = self.hand
        if len(hand) != 5:
            return False
        if hand.count(hand[0]) >= 3 or hand.count(hand[1]) >= 3 or hand.count(hand[2]) >= 3:
            return True
        return False

    def is4ofaKind(self):
        """Checks if the current Hand object matches criteria for a 4 of a Kind and returns a bool

        Returns:
            bool: The Hand is a 4 of a Kind
        """
        hand = self.hand
        if len(hand) != 5:
            return False
        if hand.count(hand[0]) >= 4 or hand.count(hand[1]) >= 4:
            return True
        return False

    if __name__ == "__main__":
        main()