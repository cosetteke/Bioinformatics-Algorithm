# https://dodona.ugent.be/nl/courses/359/series/3492/activities/1942875591
def ispolygon(arguement):
    """
    >>> ispolygon(['DISEASES', 'RENUMBER', 'SOCIABLE'])
    True
    >>> ispolygon('FREELOADS, TIMEPIECE, NORMALIZE')
    False
    >>> ispolygon({'CONSULTANT', 'CAPITALIZE', 'KETTLEDRUM', 'SUBSECTION', 'LOOKALIKES'})
    False
    >>> ispolygon(('JAWBREAKERS', 2.833, 'CONSEQUENCE', 'FRIGHTFULLY', 'UNWILLINGLY'))
    False
    """
    return isinstance(arguement, (list, tuple)) and len(arguement) >= 3 \
            and all(isinstance(item, str) and item.isupper() and item.isalpha() for item in arguement) \
            and len(set(len(item) for item in arguement)) == 1

def solution(p, start = 0, clockwise = True):
    """
    >>> solution(['DISEASES', 'RENUMBER', 'SOCIABLE'])
    'DECEMBER'
    >>> solution(('FREELOADS', 'TIMEPIECE', 'NORMALIZE'))
    'FIREPLACE'
    >>> solution(['PERFORMER', 'ANTIVIRAL', 'CROSSBOWS', 'PHENOTYPE'], start=2)
    'CHRISTMAS'
    >>> solution(('KETTLEDRUM', 'CONSULTANT', 'CAPITALIZE', 'SUBSECTION', 'LOOKALIKES'), clockwise=False, start=3)
    'SANTACLAUS'
    """
    assert ispolygon(p), 'invalid polygon'
    vertices = len(p)
    length = len(p[0])
    list = []
    for index in range(length):
        list.append(p[(start+index if clockwise else start - index) % vertices][index])
    return ''.join(list)

def solutions(p, clockwise = None):
    """
    >>> solutions(['DISEASES', 'RENUMBER', 'SOCIABLE'])
    {'DECEMBER', 'DONEABEE', 'RICUABES', 'ROSUASEE', 'SESIMSLR', 'SINIABLS'}
    >>> solutions(['FREELOADS', 'TIMEPIECE', 'NORMALIZE'], clockwise=True)
    {'FIREPLACE', 'NRMMLIIDE', 'TOEEAOEZS'}
    >>> solutions(['PERFORMER', 'ANTIVIRAL', 'CROSSBOWS', 'PHENOTYPE'], clockwise=True)
    {'AREFVBYEL', 'CHRISTMAS', 'PETSORRWE', 'PNONOIOPR'}
    >>> solutions(['KETTLEDRUM', 'CONSULTANT', 'CAPITALIZE', 'SUBSECTION', 'LOOKALIKES'], clockwise=False)
    {'CEOSTLDKOE', 'COTKEATREN', 'KOBIUEIIZT', 'LUPSLLTINM', 'SANTACLAUS'}
    """
    assert ispolygon(p), 'invalid polygon'

    vertices = len(p)

    if clockwise is None:
        directions = (True, False)
    else:
        directions = (clockwise, )

    return (solution(p, start, direction) for start in range(vertices) for direction in directions)




if __name__ == '__main__':
    import doctest

    doctest.testmod()
