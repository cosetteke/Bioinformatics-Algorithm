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
    return all(seq[i-1] <= seq[i] for i in range(1,len(seq))) # 注意specify循环从1开始，不然默认从0开始

def frequency_sequence(seq):
    """
    >>> frequency_sequence([2, 3, 5, 7, 11, 13])
    [0, 0, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6]
    >>> frequency_sequence((0, 0, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6))
    [2, 3, 5, 7, 11, 13, 14]
    >>> frequency_sequence([5, 3, 2, 7, 8, 1, 9])
    Traceback (most recent call last):
    AssertionError: given sequence is not increasing
    """
    assert increasing(seq), 'given sequence is not increasing'
    freq, value, count = [], 0, 0
    for number in seq:
        while value < number:
            freq.append(count)
            value += 1
        count += 1
    freq.append(count)
    return freq
def lift(seq):
    """
    >>> lift([2, 3, 5, 7, 11, 13])
    [3, 5, 8, 11, 16, 19]
    >>> lift((0, 0, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6))
    [1, 2, 4, 6, 7, 9, 10, 12, 13, 14, 15, 17, 18, 20]
    >>> lift([5, 3, 2, 7, 8, 1, 9])
    [6, 5, 5, 11, 13, 7, 16]
    """
    lift = []
    for index, item in enumerate(seq):
        lift.append(item+index+1)
    return lift

def complementary_sequences(seq):
    """
    >>> complementary_sequences([2, 3, 5, 7, 11, 13])
    ([3, 5, 8, 11, 16, 19], [1, 2, 4, 6, 7, 9, 10, 12, 13, 14, 15, 17, 18, 20])
    >>> complementary_sequences((1, 3, 3, 5, 5, 5, 7, 7, 7, 7))
    ([2, 5, 6, 9, 10, 11, 14, 15, 16, 17], [1, 3, 4, 7, 8, 12, 13, 18])
    >>> complementary_sequences([5, 3, 2, 7, 8, 1, 9])
    Traceback (most recent call last):
    AssertionError: given sequence is not increasing
    """
    assert increasing(seq), 'given sequence is not increasing'
    return lift(seq), lift(frequency_sequence(seq))

if __name__ == '__main__':
    import doctest
    doctest.testmod()