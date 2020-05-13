import os

import yahtzee_hand as hand
import yahtzee_scorecard as sc
import yahtzee_graphics as g

"""rows = ('Ones', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes', \
    '3 of a Kind', '4 of a Kind', \
    'Full House', 'Small Straight', 'Large Straight', \
    'Yahtzee', 'Chance', 'Yahtzee Bonus')
"""
num_players = 0

#booleans to track game status and keep while: loops running
game_running = True

def main():
    """This is the main loop for the game
    The loop has the following sections:
    1 - Check how many players are required and make scorecard objects
        1a - get int input
        1b - LOOP For each player ask for a name
            1b1 - create a ScoreCard('name') for each and add to the score_cards list
        draw the gameboard using the score_cards[] information
    2 - Play the game
        2a - LOOP For each row (1-14)
            2a1 - LOOP Give each player a turn
                2a1a - LOOP max of 3 times to give 3 dice "rolls" with 2 discard opportunities
                2a1b - LOOP Until hand is scored and written to score_cards['player']... keep loop going
                        some additional logic requred to figure out score

    See top level comments for Object methods used below
    """
    #main game loop
    while game_running:

        #startup steps. clear screen, get number of players
        #start by clearing terminal screen
        score_cards = []
        os.system('clear')
        #input message
        print('Welcome to Yahtzee!')
        #Get number of players
        #if the number is larger than 4 then restart the game
        num_players = ''
        num_players = input('How many players do you want (1-4)?')
        if not num_players.isdigit():
            continue
        num_players = int(num_players)
        if num_players <= 0 or num_players > 4:
            continue

        #create the score card objects and add them to an iterable list
        for x in range(0,num_players):
            name = input('Please input name for player {}:'.format(x+1))
            score_cards.append(sc.ScoreCard(name))

        #int to track how many rounds have been played
        match_length = 0
        #15 is the number of rows in a yahtzee board. A game is max 15 rounds
        while match_length < 14:
            #Each round to be played. Iterate through the players in the score_cards object list
            for player in score_cards:
                current_hand = hand.Hand()
                roll_finished = False
                discard_count = 0
                option = ''
                hand_discard_list = [False,False,False,False,False]
                while not roll_finished:
                    redraw(score_cards, current_hand, hand_discard_list, player.name)
                    if discard_count < 2:
                        #discard dice
                        #TODO need to make a loop that keeps marking until 'D' is detected
                        print('Hello {}'.format(player.name))
                        print('Type dice position to mark 1 or many dice (eg 2 or 135) and (D) to discard marked')
                        print('or (S) to sort')
                        option = input('or (X) to score with current hand:')
                    else:
                        option = 'X'

                    #first if option contaits only numbers then it is a filter input and needs to be handled
                    if option.isdigit() == True:
                        #Reset discard options each time a discard is tried. Do not discard yet just give player the visual feedback of what was chosen
                        hand_discard_list = [False,False,False,False,False]
                        for die in option:
                            die = int(die)
                            if die > 0 and die <=5:
                                hand_discard_list[die-1] = True
                        print(hand_discard_list)
                    #if option is a D then discard as per above genrated list
                    elif option.upper() == 'D' and sum(hand_discard_list):
                        #discard dice
                        current_hand.discard(hand_discard_list)
                        #count so there are only 2 discards maximum as per rules
                        discard_count += 1
                        hand_discard_list = [False,False,False,False,False]
                    elif option.upper() == 'S':
                        #sort
                        current_hand.sortHand()
                        #reset disard filter as it no longer relates to the sorted hand
                        hand_discard_list = [False,False,False,False,False]
                    elif option.upper() == 'X':
                        #keep track of whether the score loop is completed. May need totry a few different times so need to give visual feedback then get confirmation
                        scored = False
                        while not scored:
                            choice = input('Which row would you like to score?')
                            #has to be an int. also next line will throw a typeerror if not
                            if choice.isdigit():
                                choice = int(choice)
                                #out of the range of the score card
                                if choice < 1 or choice > 14:
                                    choice = ''
                                    #Just loop back to the top and start again
                                    continue
                                else:
                                    #In here the player has asked for a valid row
                                    #need to test the hand for accuracy for those rows that require it
                                    #Otherwise just calculate and visually feedback before getting confirmation to lock in the score
                                    #if player.rows[choice-1]
                                    if player.allRows()[choice-1]['disabled']:
                                        print('Row is disabled')
                                        continue
                                    elif player.allRows()[choice-1]['filled']:
                                        print('You have already used this row')
                                        continue
                                    else:
                                        scored = True
                        current_score = player.addScore(player.rows[choice - 1], current_hand)
                        redraw(score_cards, current_hand, hand_discard_list, player.name)
                        if current_score:
                            print('Score!')
                        else:
                            print('Better Luck Next Time.')
                        input()
                        roll_finished = True
                del(current_hand)
            #increment match_length after all players have gone
            match_length += 1
        print('Game Finished! Stay and play again.')
        input()

def redraw(score_cards, hand, discard_list, player_name):
    #draw scorecardfor all players
    g.drawGameBoard(score_cards, hand, discard_list, player_name)

if __name__ == '__main__':
    main()
    #drawGameBoard()