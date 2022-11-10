import numpy as np
import pandas as pd
import altair as alt
alt.data_transformers.enable('data_server')
from collections import defaultdict

deck = sorted(
    [ str( i) for i in range( 2, 10)] * 4 + ['10'] * (4*4) + ['A'] * 4
    )

basic_strategy_hard = pd.read_csv('data\\basic-strategy-hard.csv', index_col = 'Index')

basic_strategy_soft = pd.read_csv('data\\basic-strategy-soft.csv', index_col = 'Index')

basic_strategy_split = pd.read_csv('data\\basic-strategy-split.csv', index_col = 'Index')
basic_strategy_hard.index = list( map( str, basic_strategy_hard.index))

basic_strategy_soft.index = list( map( str, basic_strategy_soft.index))

def value_sum( cards):

    values = np.array( [], dtype = int)
    num_A = np.count_nonzero( cards == 'A')
    values = np.append( values, sum( list( map( value, cards))))
    for i in range( 1, num_A+1):
        values = np.append( values, sum( list( map( value, cards)))-10*i)
    return values

def HiLo( card):
    Hi = [ '10', 'A']
    Lo = [ '2', '3', '4', '5', '6']
    if card in Hi:
        return -1
    elif card in Lo:
        return 1
    else:
        return 0

def value( card):
    try:
        return int( card)
    except:
        return 11

def check( value):
    if value == 11:
        return 'A'
    else:
        return str( value)
            
def basic_strategy_action( player, dealer, total):
    if total == 'pair':
        return basic_strategy_split.loc[ str( min( player.cards)), check( dealer.value)]
    elif total == 'hard':
        return basic_strategy_hard.loc[ str( player.value), check( dealer.value)]
    elif total == 'soft':
        return basic_strategy_soft.loc[ str( player.value), check( dealer.value)]

record_game = {
    'run_num': 0,
    'player_cards': np.array([]),
    'dealer_cards': np.array([]),
    'change': 0,
    'running_count': 0,
    'true_count': 0,
    'betsize': 0
}

record_run = defaultdict( lambda: record_game)

def testf():
    global x
    return x + 1