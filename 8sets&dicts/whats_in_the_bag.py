# https://dodona.ugent.be/nl/courses/359/series/3492/activities/680840770
def fill(collection):
    bag = {}
    for letter in collection:
        bag[letter] = bag.get(letter, 0) + 1
    return bag


def description(bag):
    ## 对调
    result = {}
    for letter, count in bag.items():
        if count in result:
            result[count].add(letter)
        else:
            result[count] = {letter}
    return result

def remove(collection, bag):
    needed = fill(collection)
    assert all(letter in bag and needed[letter] <= bag[letter] for letter in needed ), 'not all letters are in the bag'
    for letter in collection:
        if bag[letter] == 1:
            del bag[letter]
        else:
            bag[letter] -= 1


if __name__ == '__main__':
    import doctest
    doctest.testmod()