# https://dodona.ugent.be/nl/courses/359/series/3493/activities/82601015
def coordinates(filename):
    file = open(filename, 'r')
    crd = set()
    for row, line in enumerate(file):
        for col, star in enumerate(line):
            if star == '*':
                crd.add((row, col))
    return crd

def divergence(file1, file2):
    set1, set2 = coordinates(file1), coordinates(file2)
    return (set1 - set2, set2 - set1)

def planets(file1, file2):
    def distance(coor1, coor2):
        x1, y1 = coor1
        x2, y2 = coor2
        return (x1 - x2) ** 2 + (y1 - y2) **2

    values, keys = divergence(file1, file2)
    candidate1 = {}
    for coor1 in keys:
        nearest, stars = None, set()
        for coor2 in values:
            d = distance(coor1, coor2)
            if nearest is None or d < nearest:
                nearest = d
                stars = {coor2}
            elif d == nearest:
                stars.add(coor2)
        candidate1[coor1] = stars
    return candidate1

def comparator(file1, file2):
    # read old image
    starmap = [list(line.rstrip('\n')) for line in open(file1, 'r')]
    file1 , file2 = divergence(file1, file2)
    for x, y in file1:
        starmap[x][y] = 'o'
    for x, y in file2:
        starmap[x][y] = 'n'

    return '\n'.join(''.join(row) for row in starmap)

if __name__ == '__main__':
    import doctest
    doctest.testmod()