# https://dodona.ugent.be/nl/courses/359/series/3491/activities/775005366
def digit_count(string):
    """
    >>> digit_count('10 71 32 23 14 15 16 27 18 19')
    (1, 7, 3, 2, 1, 1, 1, 2, 1, 1)
    >>> digit_count('F1gur471v3ly 5p34k1ng?')
    (0, 3, 0, 2, 2, 1, 0, 1, 0, 0)
    """
    output = [0] * 10
    for i in range(10):
        output[i] = string.count(str(i))
    return tuple(output)

def description(tuple):
    """
    >>> description((1, 7, 3, 2, 1, 1, 1, 2, 1, 1))
    '10 71 32 23 14 15 16 27 18 19'
    >>> description((0, 3, 0, 2, 2, 1, 0, 1, 0, 0))
    '0 31 2 23 24 15 6 17 8 9'
    """
    list = []
    for index, item in enumerate(tuple):
        item = '' if item == 0 else str(item)
        list.append(item + str(index))
    return " ".join(list)

def isselfinventorying(list):
    """
    >>> isselfinventorying(['10 71 32 23 14 15 16 27 18 19'])
    True
    >>> isselfinventorying(['F1gur471v3ly 5p34k1ng?'])
    False
    >>> isselfinventorying([
    ...     '10 71 32 23 14 15 16 27 18 19',
    ...     '20 81 72 53 44 35 26 47 38 29'
    ... ])
    True
    >>> isselfinventorying((
    ...     '10 71 32 23 14 15 16 27 18 19',
    ...     '20 81 72 53 44 35 26 47 38 29',
    ...     '40 101 82 73 64 65 56 77 58 39',
    ...     '60 131 92 93 74 75 86 107 88 69',
    ...     '80 201 122 113 84 85 96 117 138 89',
    ... ))
    True
    """
    concatenated = ''
    for sequence in list:
        concatenated += sequence
        if sequence != description(digit_count(concatenated)):
            return False
    return True

def isselfinventorying_2(*input):
    return isselfinventorying(input)



if __name__ == '__main__':
    import doctest
    doctest.testmod()