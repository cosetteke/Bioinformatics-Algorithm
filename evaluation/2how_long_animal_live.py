def read_properties(textname):
    reader = open(textname, 'r')
    table = {}
    for line in reader.readlines():
        line = line.rstrip('\n').split(',')
        key = line[0]
        value = map(lambda x: int(x), (line[1:])) # convert each value as integer in value list
        table[key] = tuple(value)
    reader.close()
    return table

def values(names, location, field = 0):
    """
    >>> properties['CHICKEN']
    (10, 7, 22, -1)
    >>> properties['KOI']
    (50, 3, 19, 7)
    >>> properties['COW']
    (20, 3, 9, 2)
    """
    table = read_properties(location)
    result = []
    for name in names:
        result.append(table[name][field])
    return result

from operator import itemgetter, attrgetter

def arrange(names, location, field=0, descending=False):
    table = read_properties(location)
    # create a new dictionary only contain names of given as key
    new_dic = dict((key,value) for key, value in table.items() if key in names)
    # sort by field
    word_dic = sorted(new_dic.items(), key=lambda item:item[field],reverse=descending)


if __name__ == '__main__':
    import doctest
    doctest.testmod()