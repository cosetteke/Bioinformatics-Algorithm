# https://dodona.ugent.be/nl/courses/359/series/3490/activities/284336818
def profit(rate, action):
    """
    >>> profit([5, 11, 4, 2, 8, 10, 7, 4, 3, 6], 'BS-B-S--BS')
    17
    >>> profit((4, 2, 5, 11, 10, 4, 11, 7, 4, 11, 3, 11), '-B-S-BS-BSBS')
    31
    >>> profit([10, 9, 9, 10, 10, 9, 1, 4, 9, 3, 5, 6, 10], '-B-S--B-SB--S')
    16
    >>> profit((12, 4, 9, 5, 6, 7, 9, 9, 11, 7, 10), '-BSB----SBS')
    14
    >>> profit([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], '----------')
    0
    >>> profit((10, 4, 2, 4, 8, 12), 'B---SS')
    Traceback (most recent call last):
    AssertionError: invalid actions
    """
    error = 'invalid actions'
    assert (isinstance(action, str) and # a is a string
            len(rate) == len(action) and # same number of characters
            set(action).issubset({'B','S','-'}) # a only contains valid characters
    ), error

    profit, bitcoin = 0, False ## 注意
    for value, act in zip(rate, action):
        if act == 'B':
            assert not bitcoin, error
            bitcoin = True
            profit -= value
        elif act == 'S':
            assert bitcoin, error
            bitcoin = False
            profit += value
    # check if we don't have bitcoin at the end
    assert not bitcoin, error
    return profit

def maximal_profit(rate):
    """
    >>> maximal_profit([5, 11, 4, 2, 8, 10, 7, 4, 3, 6])
    17
    >>> maximal_profit((4, 2, 5, 11, 10, 4, 11, 7, 4, 11, 3, 11))
    31
    >>> maximal_profit([10, 9, 9, 10, 10, 9, 1, 4, 9, 3, 5, 6, 10])
    16
    >>> maximal_profit((12, 4, 9, 5, 6, 7, 9, 9, 11, 7, 10))
    14
    >>> maximal_profit([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    0
    >>> maximal_profit((10, 4, 2, 4, 8, 12))
    10
    """
    return profit(rate, optimal_actions(rate))
def optimal_actions(rate):
    """
    >>> optimal_actions([5, 11, 4, 2, 8, 10, 7, 4, 3, 6])
    'BS-B-S--BS'
    >>> optimal_actions((4, 2, 5, 11, 10, 4, 11, 7, 4, 11, 3, 11))
    '-B-S-BS-BSBS'
    >>> optimal_actions([10, 9, 9, 10, 10, 9, 1, 4, 9, 3, 5, 6, 10])
    '--B-S-B-SB--S'
    >>> optimal_actions((12, 4, 9, 5, 6, 7, 9, 9, 11, 7, 10))
    '-BSB----SBS'
    >>> optimal_actions([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    '----------'
    >>> optimal_actions((10, 4, 2, 4, 8, 12))
    '--B--S'
    """
    action = ''
    for i in range(len(rate) - 1):
        if rate[i+1] > rate[i] and action.rfind('B') <= action.rfind('S'): # b和s都不存在 为-1
            action += 'B'
        elif rate[i+1] < rate[i] and action.rfind('B') > action.rfind('S'):
            action += 'S'
        else:
            action += '-'
    return action + 'S' if action.rfind('B') > action.rfind('S') else action+'-'

if __name__ == '__main__':
    import doctest
    doctest.testmod()