# https://dodona.ugent.be/nl/courses/359/series/3491/activities/112444173
def hit(base, occupied = None):
    """
    >>> hit(2)
    (0, [2])
    >>> hit(0, [1, 3])
    (0, [1, 3])
    >>> hit(1, (1, 3))
    (1, [1, 2])
    >>> hit(2, occupied=[1, 3])
    (1, [2, 3])
    >>> hit(3, occupied=(1, 3))
    (2, [3])
    >>> hit(4, occupied=[1, 3])
    (3, [])
    """
    # default
    if occupied == None:
        occupied = []
    # move position
    occupied = [position + base for position in occupied]
    # add batter to the field
    if base:
        occupied.append(base)
    # calculate score:
    score = len([position for position in occupied if position >= 4])

    # new occupation
    occupied = sorted([position for position in occupied if position < 4])

    return score, occupied

def inning(nbases):
    """
    >>> inning([0, 1, 2, 3, 4])
    (4, [])
    >>> inning((4, 3, 2, 1, 0))
    (2, [1, 3])
    >>> inning([1, 1, 2, 1, 0, 0, 1, 3, 0])
    (5, [3])
    """
    score, occupied = 0, []
    for base in nbases:
        score_each, occupied = hit(base, occupied)
        score += score_each
    return score, occupied


if __name__ == '__main__':
    import doctest
    doctest.testmod()