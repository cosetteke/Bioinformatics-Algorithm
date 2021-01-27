# https://dodona.ugent.be/nl/courses/359/series/3491/activities/1652372190
def next_letter(v, w):
    """
    >>> next_letter('e', 'HERDSMAN')
    'R'
    >>> next_letter('LC', 'sepulchre')
    'H'
    >>> next_letter('onf', 'Teleconference')
    'E'
    >>> next_letter('EURO', 'DOLLAR')
    ''
    >>> next_letter('LF', 'ALFALFA')
    ''
    >>> next_letter('USE', 'TREEHOUSE')
    ''
    """
    v, w = v.upper(), w.upper()
    if w.count(v) == 1 and w[-len(v):] != v:
        return w[w.find(v)+len(v)]
    return ''

def extend(p, W_):
    """
    >>> extend('Pe', ['HERDSMAN', 'WONDERFUL', 'FURNACE', 'HELIUM', 'PALINDROME', 'PAPERBACK'])
    'PERFUMER'
    >>> extend('ALC', ['sepulchre', 'satchel', 'Bohemian', 'pandemic', 'hemisphere', 'resistor'])
    'ALCHEMIST'
    >>> extend('nonc', ['Teleconference', 'Disinfect', 'Defector', 'Election', 'Section', 'Vibration', 'Pioneer', 'Loner'])
    ''
    """
    result = p.upper()
    letter = p[1:]
    for word in W_:
        next = next_letter(letter, word)
        if not next:
            return ''
        result += next
        letter = letter[1:] + result[-1]
    return result

def profession(word_, length = 2):
    """
    >>> profession(['OPERATOR', 'HERDSMAN', 'WONDERFUL', 'FURNACE', 'HELIUM', 'PALINDROME', 'PAPERBACK'])
    'PERFUMER'
    >>> profession(['falcon', 'sepulchre', 'satchel', 'Bohemian', 'pandemic', 'hemisphere', 'resistor'], length=3)
    'ALCHEMIST'
    >>> profession(['Nonconformist', 'Teleconference', 'Disinfect', 'Defector', 'Election', 'Section', 'Vibration', 'Pioneer', 'Loner'], 4)
    'CONFECTIONER'
    """
    for word in word_:
        word_list = [word[index:index + length] for index in range(len(word)- length + 1)]
        for prefix in word_list:
            word1 = extend(prefix, word_[1:])
            if word1:
                return word1
        return ''


if __name__ == '__main__':
    import doctest
    doctest.testmod()