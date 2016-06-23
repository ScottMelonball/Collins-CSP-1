team_name = 'King of the world'
strategy_name = 'Copy and be king'
strategy_description = '''\
Collude first round. Copy Betray if they Betray'''
 
import random
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.'''

    # First move
    if len(my_history) == 0:
        return 'c'
    # React to the opponent's last move
    if my_history[-1]=='c' and their_history[-1]=='b':
            return 'b' # Betray if they were severely punished last time
    else:
        return 'c'
    if their_history[-1] == 'd':
        return 'd'
    else:
        return 'c'