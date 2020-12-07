def has_won(player1, player2, L):
    """
    :param player1: the outcome (int) of a roll of the die by player 1
    :param player2: the outcome (int) of a roll of the die by player 2
    :param L: the upper limit L(int)
    :return: Boolean value (bool) that indicates whether player 1 has won the game.
    >>> has_won(3, 2, 4)
    True
    >>> has_won(1, 5, 4)
    False
    """
    return max(player1, player2) <= L

def winning_outcomes(n, L):
    """
    :param n: the number of sides (int) of the die
    :param L: the upper limit  (int)
    :return: a tuple with two numbers (int): possible outcomes player 1 wins an player 2 wins.
    >>> winning_outcomes(6, 4)
    (16, 20)
    """
    pl1_win = 0
    pl2_win = 0
    for player1 in range(1, n+1):
        for player2 in range(1, n+1):
            if has_won(player1, player2, L): # if pl1 wins
                pl1_win += 1
            else: # if pl2 wins
                pl2_win += 1
    return (pl1_win, pl2_win)

def odds(n, L):
    """
    :param n: the number of sides  (int) of the fair die
    :param L: the upper limit  (int)
    :return: a tuple with two numbers (float) pl1, pl2 wins then game
    >>> odds(6, 4)
    (44.44444444444444, 55.55555555555556)
    """
    # the times of winning for each player
    wintime1, wintime2 = winning_outcomes(n, L)[0], winning_outcomes(n, L)[1]
    pl1_chance = float(wintime1 / (wintime1 + wintime2)) * 100 # expressed as percentage
    return (pl1_chance, 100 - pl1_chance)

def winner(n, L):
    """
    :param n: the number of sides  (int) of the fair die
    :param L: the upper limit  (int).
    :return: 0 if both players have equal chance of winning, 1 if pl1 has better chance of winning, 2 if pl2 has better chance
    >>> winner(6, 4)
    2
    """
    pl1_chance, pl2_chance = odds(n, L)[0], odds(n, L)[1]
    if pl1_chance == pl2_chance:
        output = 0
    elif pl1_chance > pl2_chance:
        output = 1
    else:
        output = 2
    return output # 正确答案在dodona上



if __name__ == '__main__':
    import doctest
    doctest.testmod()
