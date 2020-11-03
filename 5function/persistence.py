# https://dodona.ugent.be/nl/courses/359/series/3489/activities/582137927
def multiplication(integer):
    """
    >>> multiplication(327)
    42
    >>> multiplication(42)
    8
    >>> multiplication(277777788888899)
    4996238671872
    """
    product = 1
    for number in str(integer):
        product *= int(number)
    return product

def digital_root(integer):
    """
    >>> digital_root(327)
    8
    >>> digital_root(68889)
    0
    >>> digital_root(277777788888899)
    0
    """
    while len(str(integer)) != 1:
        integer = multiplication(integer)
    return integer

def persistence(integer):
    """
    >>> persistence(327)
    2
    >>> persistence(8)
    0
    >>> persistence(277777788888899)
    11
    """
    count = 0
    while len(str(integer)) != 1:
        integer = multiplication(integer)
        count += 1
    return count
def most_persistent(a, b):
    """
    >>> most_persistent(1, 100)
    77
    >>> most_persistent(100, 1000)
    679
    >>> most_persistent(1000, 10000)
    6788
    >>> most_persistent(277777788888000, 277777788889000)
    277777788888899
    """
    greatest_persis = 0
    i = 0
    for integer in range(a, b+1):
        if persistence(integer) > greatest_persis:
            greatest_persis = persistence(integer)
            i = integer
        elif persistence(integer) == greatest_persis:
            if integer <= i:
                i = integer
    return i




if __name__ == '__main__':
    import doctest
    doctest.testmod()