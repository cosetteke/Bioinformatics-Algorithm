# https://dodona.ugent.be/nl/courses/359/series/3489/activities/1266098554
def splitsing(soort):

    """
    Splitst de parameter (str) in een prefix en een suffix, waarbij de prefix
    bestaat uit alle medeklinkers aan het begin van de gegeven string.

    >>> splitsing('schaap')
    ('sch', 'aap')
    >>> splitsing('geit')
    ('g', 'eit')
    """
    # find position of first vowel
    # pos = 0
    # while pos < len(soort) and soort[pos].lower() not in 'aeiou':
    #         pos += 1
    # return soort[:pos], soort[pos:]
    consonants = 'aeiouAEIOU'
    list = []
    for letter in soort:
        if letter in consonants:
            index = soort.index(letter)
            left = soort[:index]
            right = soort[index:]
            break
    list.append(left)
    list.append(right)
    return tuple(list)
def kruising(soort1, soort2):

    """
    Geeft tuple met twee strings terug, waarvan de eerste gevormd wordt door de
    samenstelling van de prefix van de eerste parameter (str) en de suffix van
    de tweede paramter (str), en de tweede gevormd wordt door de prefix van de
    tweede paramter en de suffix van de eerste paramter.

    >>> kruising('schaap', 'geit')
    ('scheit', 'gaap')
    >>> kruising('leeuw', 'tijger')
    ('lijger', 'teeuw')
    >>> kruising('hond', 'kat')
    ('hat', 'kond')
    """
    list = []
    new1 = splitsing(soort1)[0] + splitsing(soort2)[1]
    new2 = splitsing(soort2)[0] + splitsing(soort1)[1]
    list.append(new1)
    list.append(new2)
    return tuple(list)
# # split species names in prefix and suffix
# prefix1, suffix1 = split(species1) prefix2, suffix2 = split(species2)
# # hybridize the species names
# return prefix1 + suffix2, prefix2 + suffix1
if __name__ == '__main__':
    import doctest
    doctest.testmod()