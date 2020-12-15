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

    assert (isinstance(action, str) and
            len(rate) == len(action) and
            set(action) in {'B','S','-'} and
            
    ), 'invalid actions'