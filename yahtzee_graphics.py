import os
import yahtzee_hand

def drawGameBoard(score_cards, hand = [], discard_list = [], current_player = ''):
    #os.system('clear')
    #print(score_cards[0].allRows())
    #input()
    os.system('clear')
    player_count = len(score_cards)
    print('   ----------------------------------' + gameboardLines('-----------------',player_count))
    print('   | UPPER SECTION |  How to Score  |' + columnString(score_cards, 'name', hand, current_player))
    print('   |---------------|----------------|' + gameboardLines('----------------|',player_count))
    print(' 1 |  Ones         | Total of Ones  |' + columnString(score_cards, 'Ones', hand, current_player))
    print('   |---------------|----------------|' + gameboardLines('----------------|',player_count))
    print(' 2 |  Twos         | Total of Twos  |' + columnString(score_cards, 'Twos', hand, current_player))
    print('   |---------------|----------------|' + gameboardLines('----------------|',player_count))
    print(' 3 |  Threes       | Total of Threes|' + columnString(score_cards, 'Threes', hand, current_player))
    print('   |---------------|----------------|' + gameboardLines('----------------|',player_count))
    print(' 4 |  Fours        | Total of Fours |' + columnString(score_cards, 'Fours', hand, current_player))
    print('   |---------------|----------------|' + gameboardLines('----------------|',player_count))
    print(' 5 |  Fives        | Total of Fives |' + columnString(score_cards, 'Fives', hand, current_player))
    print('   |---------------|----------------|' + gameboardLines('----------------|',player_count))
    print(' 6 |  Sixes        | Total of Sixes |' + columnString(score_cards, 'Sixes', hand, current_player))
    print('   |---------------|----------------|' + gameboardLines('----------------|',player_count))
    print('   |  SubTotal     |   ---->>       |' + columnString(score_cards, 'Upper SubTotal', hand, current_player))
    print('   |---------------|----------------|' + gameboardLines('----------------|',player_count))
    print('   | Bonus if > 63 | Score 35       |' + columnString(score_cards, 'Upper Bonus', hand, current_player))
    print('   |---------------|----------------|' + gameboardLines('----------------|',player_count))
    print('   |  Total        |   ---->>       |' + columnString(score_cards, 'Upper Score', hand, current_player))
    print('   |---------------|----------------|' + gameboardLines('----------------|',player_count))
    print('   | LOWER SECTION |                |' + gameboardLines('----------------|',player_count))
    print('   |---------------|----------------|' + gameboardLines('----------------|',player_count))
    print(' 7 |  3 of a Kind  | Total all dice |' + columnString(score_cards, '3 of a Kind', hand, current_player))
    print('   |---------------|----------------|' + gameboardLines('----------------|',player_count))
    print(' 8 |  4 of a Kind  | Total all dice |' + columnString(score_cards, '4 of a Kind', hand, current_player))
    print('   |---------------|----------------|' + gameboardLines('----------------|',player_count))
    print(' 9 |  Full House   | Score 25       |' + columnString(score_cards, 'Full House', hand, current_player))
    print('   |---------------|----------------|' + gameboardLines('----------------|',player_count))
    print('10 |  Sm. Straight | Score 30       |' + columnString(score_cards, 'Small Straight', hand, current_player))
    print('   |---------------|----------------|' + gameboardLines('----------------|',player_count))
    print('11 |  Lg. Straight | Score 40       |' + columnString(score_cards, 'Large Straight', hand, current_player))
    print('   |---------------|----------------|' + gameboardLines('----------------|',player_count))
    print('12 |  Yahtzee!     | Score 50       |' + columnString(score_cards, 'Yahtzee', hand, current_player))
    print('   |---------------|----------------|' + gameboardLines('----------------|',player_count))
    print('13 |  Chance       | Total all dice |' + columnString(score_cards, 'Chance', hand, current_player))
    print('   |---------------|----------------|' + gameboardLines('----------------|',player_count))
    print('14 | YAHTZEE BONUS | Score 100 per  |' + columnString(score_cards, 'Yahtzee Bonus', hand, current_player))
    print('   |---------------|----------------|' + gameboardLines('----------------|',player_count))
    print('   | LOWER TOTAL   |   ---->>       |' + columnString(score_cards, 'Lower Score', hand, current_player))
    print('   |---------------|----------------|' + gameboardLines('----------------|',player_count))
    print('   | UPPER TOTAL   |   ---->>       |' + columnString(score_cards, 'Upper Score', hand, current_player))
    print('   |---------------|----------------|' + gameboardLines('----------------|',player_count))
    print('   | GRAND TOTAL   |   ---->>       |' + columnString(score_cards, 'Total Score', hand, current_player))
    print('   ----------------------------------' + gameboardLines('-----------------',player_count))
    print()
    #print('       (1)       (2)       (3)       (4)       (5)    ')
    print(diefaces(discard_list, 0))
    print('   /`````````/`````````/`````````/`````````/`````````\\')
    print(diefaces(hand.showHand(), 1))
    print(diefaces(hand.showHand(), 2))
    print(diefaces(hand.showHand(), 3))
    print('   \\_________\\_________\\_________\\_________\\_________/')
    print()
    """
    '     1      **(2)**      3     '
    '/`````````/`````````/`````````\'
    '|  O   O  |  O   O  |  O      |'
    '|    O    |         |    O    |'
    '|  O   O  |  O   O  |      O  |'
    '\_________\_________\_________/'
    """

def diefaces(hand_list, row):
    """Function returns a full row (rowstring) to show a graphical
        representation of the die faces
        There are 3 rows to return and each row is constructed of 5 dice
        Args:
            Hand is an array that holds the die values
            Row is an integer <= 3 that represents the row
        Returns:
            rowstring (string) - the entire row for all 5 dice

    """
    rowstring = ''
    #Added later ;)
    #Row 0 is the number line above the dice
    if row == 0:
        if hand_list == []:
            rowstring = '        1         2         3         4         5     '
        else:
            y = 1
            rowstring = '    '
            for x in hand_list:
                if x:
                    rowstring += ' **(' + str(y) + ')**  '
                else:
                    rowstring += '    ' + str(y) + '     '
                y += 1
        return rowstring
    #row must be an integer > 0 and <= 3
    if row > 3 or row < 1:
        return
    #if hand is empty then all 3 rows are the same blank face
    if hand_list == []:
        rowstring = '   |  X X X  |  X X X  |  X X X  |  X X X  |  X X X  |'
        return rowstring
    #All rowstrings start with "   | "
    rowstring = '   |'
    if row == 1:
        for die in hand_list:
            if die == 1:
                rowstring = rowstring + '         |'
            elif (die == 2) or (die == 3):
                rowstring = rowstring + '  *      |'
            elif (die == 4) or (die == 5) or (die == 6):
                rowstring = rowstring + '  *   *  |'
        return rowstring
    if row == 2:
        for die in hand_list:
            if (die == 1) or (die == 3) or (die == 5):
                rowstring = rowstring + '    *    |'
            elif (die == 2) or (die == 4):
                rowstring = rowstring + '         |'
            elif (die == 6):
                rowstring = rowstring + '  *   *  |'
        return rowstring
    if row == 3:
        for die in hand_list:
            if (die == 1):
                rowstring = rowstring + '         |'
            elif (die == 2) or (die == 3):
                rowstring = rowstring + '      *  |'
            elif (die == 4) or (die == 5) or (die == 6):
                rowstring = rowstring + '  *   *  |'
        return rowstring

def gameboardLines(column_string, count):
    columns = column_string * count
    return columns

def columnString(score_cards,row, hand = [], current_player = ''):
    columns = ''

    for x in score_cards:
        text = ''
        length = 0
        whitespace_length = 0

        if row == 'name':
            if len(x.name) > 14:
                text = 'Too Long'
            else:
                if current_player == x.name:
                    text = ">" + x.name + "<"
                else:
                    text = x.name

        elif row == 'Upper Score':
            text = str(x.upperScore())
        elif row == 'Lower Score':
            text = str(x.lowerScore())
        elif row == 'Total Score':
            text = str(x.totalScore())
        elif row == 'Upper Bonus':
            if x.isUpperBonus():
                text = '35'
            else:
                text = ''
        elif row == 'Upper SubTotal':
            if x.isUpperBonus():
                text = str(x.upperScore()-35)
            else:
                text = str(x.upperScore())
        else:
            current_row = dict(list(filter(lambda this_row: this_row['name'] == row,x.allRows()))[0])
            if current_row['disabled']:
                text = 'XXXXXX'
            elif current_row['filled']:
                text = str(current_row['score'])
            else:
                if current_player == x.name:
                    strscore = str(score_cards[0].addScore(row, hand, False))
                    if strscore == '0':
                        text = ''
                    else:
                        text = '       (' + strscore + ')'
                else:
                    text = ''
                #text = ''
                #text = '      ' + str(score_cards[0].addScore(row, hand, False))

        if len(text)%2 == 1:
            text = ' ' + text
        length = len(text)
        whitespace_length = (14 - length)//2
        columns += ' '+(' '*whitespace_length)+text+(' '*whitespace_length)+' |'

    return columns