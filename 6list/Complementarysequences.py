# https://dodona.ugent.be/nl/courses/359/series/3490/activities/1096544639
def increasing(seq):
    """
    >>> increasing([2, 3, 5, 7, 11, 13])
    True
    >>> increasing((0, 0, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6))
    True
    >>> increasing([5, 3, 2, 7, 8, 1, 9])
    False
    """
    if isinstance(seq, tuple):

    for i in range(len(seq)):
        if seq[i+1] - seq_[i] < 0:
            return False

    return True