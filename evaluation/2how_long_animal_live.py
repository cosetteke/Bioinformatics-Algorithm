def read_properties(textname):
    reader = open(textname, 'r')
    table = {}
    for line in reader.readlines():
        line = line.rstrip('\n').split(',')
        key = line[0]
        value = map(int, (line[1:])) # convert each value as integer in value list
        table[key] = tuple(value)
    reader.close()
    return table

def values(names, location, field = 0):
    """
    >>> values(['CHICKEN', 'KOI', 'COW', 'DOG', 'CHEETAH', 'LOBSTER'], 'data.txt')
    [10, 50, 20, 13, 10, 50]
    >>> values(('CHICKEN', 'KOI', 'COW', 'DOG', 'CHEETAH', 'LOBSTER'), 'data.txt', field=1)
    [7, 3, 3, 3, 7, 7]
    >>> values(('CHICKEN', 'KOI', 'COW', 'DOG', 'CHEETAH', 'LOBSTER'), 'data.txt', field=3)
    [-1, 7, 2, 4, 2, 1]
    """
    table = read_properties(location)
    result = []
    for name in names:
        result.append(table[name][field])
    return result


#def arrange(names, location, field=0, descending=False):
    #table = read_properties(location)
    # create a new dictionary only contain names of given as key
    #new_dic = dict((key,value) for key, value in table.items() if key in names)
    # sort by field
    #word_dic = sorted(new_dic.items(), key=lambda item:item[field],reverse=descending)


if __name__ == '__main__':
    import doctest
    doctest.testmod()