# https://dodona.ugent.be/nl/courses/359/series/3492/activities/1456155882
def reachable(coordinates, n):
    """
    >>> reachable((0, 0), 0)
    True
    >>> reachable((10, 20), 3)
    True
    >>> reachable((2, 3), 4)
    False
    """
    return sum(int(i) for i in (str(abs(coordinates[0])) + str(abs(coordinates[1])))) <= n


def neighbors(coordinates):
    """
    >>> neighbors((0, 0))
    {(0, 1), (0, -1), (1, 0), (-1, 0)}
    >>> neighbors((4, 3))
    {(4, 2), (4, 4), (3, 3), (5, 3)}
    """
    return {(coordinates[0] + dx, coordinates[1] + dy) for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0))}


def breadcrumbs(age):
    """
    >>> breadcrumbs(0)
    {(0, 0)}
    >>> breadcrumbs(2)
    {(0, 1), (-1, 1), (0, 0), (-1, 0), (0, -2), (0, 2), (2, 0), (-1, -1), (0, -1), (1, 0), (1, -1), (1, 1), (-2, 0)}
    """
    # initialize sets of visited points and points that need to be visited
    crumbs, border = set(), {(0, 0)}

    # investigate border points
    while border:
        point = border.pop()
        crumbs.add(point)
        for neighbor in neighbors(point):
            if neighbor not in crumbs and reachable(neighbor, age):
                border.add(neighbor)
    return crumbs



if __name__ == '__main__':
    import doctest

    doctest.testmod()
