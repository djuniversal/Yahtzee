class ScoreCard:
    def __init__(self, name):
        """Initialises the ScoreCard object. Attaches the name to the object and creates the self.upper and self.lower dicts that hold the scores.
            self.upper{name:(row name), die, score, disable, filled}
            self.lower{name, default_score(score if played. 0 if no default), score, disable, filled}
            self.lower{name:'Yahtzee Bonus' also has 'count' to track number of times)

        Parameters:
            name (str): First name of the player using that scorecard
        """
        self.name = name

        self.upper = [ \
            {'name':'Ones', 'die':1, 'score':0, 'disabled':False, 'filled':False}, \
            {'name':'Twos', 'die':2, 'score':0, 'disabled':False, 'filled':False}, \
            {'name':'Threes', 'die':3, 'score':0, 'disabled':False, 'filled':False}, \
            {'name':'Fours', 'die':4, 'score':0, 'disabled':False, 'filled':False}, \
            {'name':'Fives', 'die':5, 'score':0, 'disabled':False, 'filled':False}, \
            {'name':'Sixes', 'die':6, 'score':0, 'disabled':False, 'filled':False}]

        self.lower = [ \
            {'name':'3 of a Kind', 'default_score':0, 'score':0, 'disabled':False, 'filled':False}, \
            {'name':'4 of a Kind', 'default_score':0, 'score':0, 'disabled':False, 'filled':False}, \
            {'name':'Full House', 'default_score':25, 'score':0, 'disabled':False, 'filled':False}, \
            {'name':'Small Straight', 'default_score':30, 'score':0, 'disabled':False, 'filled':False}, \
            {'name':'Large Straight', 'default_score':40, 'score':0, 'disabled':False, 'filled':False}, \
            {'name':'Yahtzee', 'default_score':50, 'score':0, 'disabled':False, 'filled':False}, \
            {'name':'Chance', 'default_score':0, 'score':0, 'disabled':False, 'filled':False}, \
            {'name':'Yahtzee Bonus', 'default_score':100, 'count':0, 'score':0, 'disabled':False, 'filled':False}]

        self.rows = ('Ones', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes', \
            '3 of a Kind', '4 of a Kind', \
            'Full House', 'Small Straight', 'Large Straight', \
            'Yahtzee', 'Chance', 'Yahtzee Bonus')

    def allRows(self):
        """Returns self.upper and self.lower as concatenated list for easy iteration

        Returns:
            list: self.upper + self.lower
        """
        return self.upper + self.lower

    def addScore(self, row, hand, write_score = True):
        score = 'empty'
        for x in self.upper:
            if x['name'] == row:
                score = x['die'] * hand.showHand().count(x['die'])
                break
        if score == 'empty':
            for x in self.lower:
                if x['name'] == row:
                    if x['name'] == '3 of a Kind' and not hand.is3ofaKind():
                        score = 0
                        break
                    elif x['name'] == '4 of a Kind' and not hand.is4ofaKind():
                        score = 0
                        break
                    elif x['name'] == 'Small Straight' and not hand.isSmallStraight():
                        score = 0
                        break
                    elif x['name'] == 'Large Straight' and not hand.isLargeStraight():
                        score = 0
                        break
                    elif x['name'] == 'Full House' and not hand.isFullHouse():
                        score = 0
                        break
                    elif x['name'] == 'Yahtzee' and not hand.isYahtzee():
                        score = 0
                        break
                    elif x['name'] == 'Yahtzee Bonus' and not hand.isYahtzee():
                        score = 0
                        break
                    elif x['default_score']:
                        score = x['default_score']
                        break
                    else:
                        score = hand.sumHand(hand.showHand())
                        break

        if write_score:
            if not x['filled'] and not x['disabled']:
                x['score'] = score
                x['filled'] = True
            elif x['disabled']:
                score = 'disabled'
            elif x['filled']:
                score = 'filled'

        return score

    def removeScore(self, row):
        for x in self.upper:
            if x['name'] == row:
                x['score'] = 0
                x['filled'] = False
                return True

        for x in self.lower:
            if x['name'] == row:
                x['score'] = 0
                x['filled'] = False
                return True

    def upperScore(self):
        """Scores upper section by adding scores of self.upper

        Returns:
            int: Total score of upper section including bonus if one is applicable
        """
        upper_score = 0
        for x in self.upper:
            if x['filled']:
                upper_score += x['score']
        if upper_score >= 63:
            upper_score += 35
        return upper_score

    def lowerScore(self):
        """Scores lower section by adding scores of self.lower

        Returns:
            int: Total score of lower section
        """
        lower_score = 0
        for x in self.lower:
            if x['filled']:
                lower_score += x['score']
        return lower_score

    def totalScore(self):
        """Returns total score for entire scorecard

        Returns:
            int: Total summed score for entire scorecard including bonuses
        """
        return self.upperScore() + self.lowerScore()

    def isUpperBonus(self):
        """Indicated whether or not the self.upper section qualifies for a bonus.
            Would be used to see if upper has bonus applied as upperScore() does not preserve that information

        Returns:
            bool: A bonus is applied to upper score.
        """
        if self.upperScore() >= 98:
            return True
        return False