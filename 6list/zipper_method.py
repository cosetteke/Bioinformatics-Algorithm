# https://dodona.ugent.be/nl/courses/359/series/3490/activities/1325500143
def merge(l1, l2):
    """
    >>> merge(('A', 'B', 'C'),  [1, 2, 3])
    ['A', 1, 'B', 2, 'C', 3]
    >>> merge(['A'], [1, 2, 3, 4])
    ['A', 1]
    >>> merge(('A', 'B'),  (1, 2, 3, 4))
    ['A', 1, 'B', 2]
    >>> merge(('A', 'B', 'C'),  [1, 2])
    ['A', 1, 'B', 2]
    """
    newlist = []
    for i, j in zip(l1, l2):
        newlist.append(i)
        newlist.append(j)
    return newlist


from itertools import zip_longest


def weave(l1, l2):
    """
    >>> weave(('A', 'B', 'C'),  [1, 2, 3])
    ['A', 1, 'B', 2, 'C', 3]
    >>> weave(['A'], [1, 2, 3, 4])
    ['A', 1, 'A', 2, 'A', 3, 'A', 4]
    >>> weave(('A', 'B'),  (1, 2, 3, 4))
    ['A', 1, 'B', 2, 'A', 3, 'B', 4]
    >>> weave(('A', 'B', 'C'),  [1, 2])
    ['A', 1, 'B', 2, 'C', 1]
    """
    weave = []
    length = max(len(l1), len(l2))
    for i in range(length):
        weave.append(l1[i % len(l1)])
        weave.append(l2[i % len(l2)])
    return weave

def zipper(l1, l2):
    """
    >>> zipper(('A', 'B', 'C'),  [1, 2, 3])
    ['A', 1, 'B', 2, 'C', 3]
    >>> zipper(['A'], [1, 2, 3, 4])
    ['A', 1, 2, 3, 4]
    >>> zipper(('A', 'B'),  (1, 2, 3, 4))
    ['A', 1, 'B', 2, 3, 4]
    >>> zipper(('A', 'B', 'C'),  [1, 2])
    ['A', 1, 'B', 2, 'C']
    """
    short = l1 if len(l1) < len(l2) else l2
    long = l1 if len(l1) >= len(l2) else l2
    zipper = []

    for i in range(len(short)):
        zipper.extend((l1[i],l2[i])) # 注意这里是l1 l2 而不是 long short
    zipper.extend(long[len(short):])
    return zipper
if __name__ == '__main__':
    import doctest

    doctest.testmod()
