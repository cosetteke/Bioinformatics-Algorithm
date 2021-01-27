# https://dodona.ugent.be/nl/courses/359/series/3492/activities/427941655

def diff_3(collection):
    return (len(collection) >= 3) and (len(set(collection)) == len(collection))

def group(collection):
    """
    >>> group(['4R', '4B', '4Y', '4K'])
    True
    >>> group({'6B', '7B', '8B', '9B', '10B'})
    False
    >>> group(('11R', '2B', '7Y', '2B', '9K'))
    False
    """
    if not diff_3(collection):
        return False
    # check if all tiles have a distinct color
    colors = {tile[-1] for tile in collection}
    if len(colors) != len(collection):
        return False

    # check if have the same value
    values = {tile[:-1] for tile in collection}
    if len(values) != 1:
        return False
    return True

def run(collections):
    """
    >>> run(['4R', '4B', '4Y', '4K'])
    False
    >>> run({'6B', '7B', '8B', '9B', '10B'})
    True
    >>> run(('11R', '2B', '7Y', '2B', '9K'))
    False
    """
    if not diff_3(collections):
        return False
    colors = {tile[-1] for tile in collections}
    if len(colors) != 1:
        return False
    values = sorted({int(tile[:-1]) for tile in collections})
    for i in range(len(values)-1):
        if values[i+1] - values[i] != 1:
            return False
    return True

if __name__ == '__main__':
    import doctest
    doctest.testmod()