"""The Game of Hog."""

from dice import four_sided, six_sided, make_test_dice
from ucb import main, trace, log_current_line, interact

GOAL_SCORE = 100 # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################

def roll_dice(num_rolls, dice=six_sided):
    """Roll DICE for NUM_ROLLS times. Return either the sum of the outcomes,
    or 1 if a 1 is rolled (Pig out). This calls DICE exactly NUM_ROLLS times.

    num_rolls:  The number of dice rolls that will be made; at least 1.
    dice:       A zero-argument function that returns an integer outcome.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    if_one = False 
    current_turn_points = 0
    for x in range(num_rolls):
        one_roll = dice()
        if one_roll == 1:
            if_one = True
        else:
            current_turn_points = current_turn_points + one_roll
    if if_one:
        return 1
    else:
        return current_turn_points



def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free bacon).

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function of no args that returns an integer outcome.
    """
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    first_digit = opponent_score//10
    second_digit = opponent_score%10
    if num_rolls == 0:
        return 1 + max(first_digit,second_digit)
    else:
        return roll_dice(num_rolls,dice)

def select_dice(score, opponent_score):
    """Select six-sided dice unless the sum of SCORE and OPPONENT_SCORE is a
    multiple of 7, in which case select four-sided dice (Hog wild).
    """
    if (score + opponent_score)%7 == 0:
        return four_sided
    else:
        return six_sided

def is_prime(n):
    """Return True if a non-negative number N is prime, otherwise return
    False. 1 is not a prime number!
    """
    assert type(n) == int, 'n must be an integer.'
    assert n >= 0, 'n must be non-negative.'
    if n == 1 or n == 0:
        return False
    for x in range(2,n):
        if n % x == 0:
            return False
    return True


def other(who):
    """Return the other player, for a player WHO numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - who

def play(strategy0, strategy1, score0=0, score1=0, goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first
    strategy1:  The strategy function for Player 1, who plays second
    score0   :  The starting score for Player 0
    score1   :  The starting score for Player 1
    """
    home_score, opponent_score = 0, 0
    who = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
    def num_rolls(who):
        if who == 0:
            return strategy0(score0, score1)
        else:    
            return strategy1(score1, score0)

    while score0 < goal and score1 < goal:
        if who == 0:
            home_score, opponent_score = score0, score1
        else:
            home_score, opponent_score = score1, score0
        dice_sides = select_dice(home_score, opponent_score)
        current_turn_points = take_turn(num_rolls(who), opponent_score, dice_sides)

        if who == 0:
            score0 = score0 + current_turn_points
        else:
            score1 = score1 + current_turn_points

        if is_prime(score0 + score1):
            if score1>score0:
                score1 = score1 + current_turn_points
            elif score0>score1:
                score0 = score0 + current_turn_points
        who = other(who)
    return score0, score1  # You may want to change this line.

#######################
# Phase 2: Strategies #
#######################

def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    return strategy

# Experiments

def make_averaged(fn, num_samples=10000):
    """Return a function that returns the average_value of FN when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(3, 1, 5, 6)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()                                    
    3.75
    >>> make_averaged(roll_dice, 1000)(2, dice)
    6.0

    In this last example, two different turn scenarios are averaged.
    - In the first, the player rolls a 3 then a 1, receiving a score of 1.
    - In the other, the player rolls a 5 and 6, scoring 11.
    Thus, the average value is 6.0.
    """
    
    def average(*args):
        total = 0
        for x in range(num_samples):
            total = fn(*args) + total
        return total/num_samples
    return average





def max_scoring_num_rolls(dice=six_sided):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE.  Assume that dice always
    return positive outcomes.

    >>> dice = make_test_dice(3)
    >>> max_scoring_num_rolls(dice)
    10
    """
    average = make_averaged(roll_dice, 1000)
    for x in range(1,10):
        initial_roll = average(x,dice)
        next_roll = average((x+1),dice)
        num_rolls = 1
        if next_roll > initial_roll:
            num_rolls = x+1
    return num_rolls


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1

def average_win_rate(strategy, baseline=always_roll(5)):
    """Return the average win rate (0 to 1) of STRATEGY against BASELINE."""
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)
    return (win_rate_as_player_0 + win_rate_as_player_1) / 2 # Average results

def run_experiments():
    """Run a series of strategy experiments and report results."""
    if False: # Change to False when done finding max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)
        four_sided_max = max_scoring_num_rolls(four_sided)
        print('Max scoring num rolls for four-sided dice:', four_sided_max)

    if False: # Change to True to test always_roll(8)
        print('always_roll(6) win rate:', average_win_rate(always_roll(6)))

    if False: # Change to True to test bacon_strategy
        print('bacon_strategy win rate:', average_win_rate(bacon_strategy))

    if False: # Change to True to test prime_strategy
        print('prime_strategy win rate:', average_win_rate(prime_strategy))

    if True: # Change to True to test final_strategy
        print('final_strategy win rate:', average_win_rate(final_strategy))

    "*** You may add additional experiments as you wish ***"

# Strategies

def bacon_strategy(score, opponent_score, margin=8, num_rolls=5):
    """This strategy rolls 0 dice if that gives at least MARGIN points,
    and rolls NUM_ROLLS otherwise.
    """
    first_digit = opponent_score//10
    second_digit = opponent_score%10
    if max(first_digit,second_digit) >= margin-1:
        return 0
    else:
        return num_rolls 

def prime_strategy(score, opponent_score, margin=8, num_rolls=5):
    """This strategy rolls 0 dice when it results in a beneficial boost and
    rolls NUM_ROLLS if rolling 0 dice gives the opponent a boost. It also
    rolls 0 dice if that gives at least MARGIN points and rolls NUM_ROLLS
    otherwise.
    """
    first_digit = opponent_score//10
    second_digit = opponent_score%10
    new_score = score + max(first_digit,second_digit) + 1
    if is_prime(new_score+opponent_score):
        if new_score > opponent_score:
            return 0
        else:
            return num_rolls
    else:
        return bacon_strategy(score, opponent_score, margin, num_rolls)


def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.
    - if rolling 0 dice will get you to the goal, do so.
    - if rolling 0 dice will lead to hog wild then lower the margin to do so
    - if you're losing by a lot take a bigger risk (eg. increase number of rolls)
    - if rolling 0 will enact the Hogtimus prime rule, and the increase in points is over the margin, then do so
    
    """
    def Hog_wild_strategy(score,opponent_score, margin=5, num_rolls=5):
        if (new_score+opponent_score)%7 == 0 and Hogtimus_prime and (max(first_digit,second_digit) + 1) > margin:
            return 0
        else:
            return num_rolls
    
    first_digit = opponent_score//10
    second_digit = opponent_score%10
    new_score = score + max(first_digit,second_digit) + 1
    Hogtimus_prime = prime_strategy(score, opponent_score, margin=8, num_rolls=5) == 0
    close_to_goal = new_score>=100
    Hog_wild = Hog_wild_strategy(score,opponent_score,margin=5,num_rolls=5) == 0
    score_dif = (opponent_score-score)

    default_num_rolls = 5
    if select_dice(score,opponent_score) == four_sided:
        default_num_rolls = 4
    if Hogtimus_prime or Hog_wild or close_to_goal:
        default_num_rolls = 0
    elif score_dif > 25:
        default_num_rolls = default_num_rolls + 3
    elif score_dif > 15:
        default_num_rolls = default_num_rolls + 2
    elif score_dif > 10:
        default_num_rolls = default_num_rolls + 1
    return default_num_rolls
    
    


##########################
# Command Line Interface #
##########################

# Note: Functions in this section do not need to be changed.  They use features
#       of Python not yet covered in the course.


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions.

    This function uses Python syntax/techniques not yet covered in this course.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')
    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()
