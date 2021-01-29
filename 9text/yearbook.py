# https://dodona.ugent.be/nl/courses/359/series/3493/activities/2083832584
def mendeleev(filename):
    dict = {}
    for line in open(filename, 'r').readlines():
        symbol, name = line.strip().split('\t')
        dict[symbol] = name
    return dict
import re
def symbols(string):
    """
    >>> symbols('IKBeNHeTbEu')
    ['I', 'K', 'Be', 'N', 'He', 'Tb', 'Eu']
    >>> symbols('FIReISFUN')
    ['F', 'I', 'Re', 'I', 'S', 'F', 'U', 'N']
    >>> symbols('IPLaYWIThDyNAmITe')
    ['I', 'P', 'La', 'Y', 'W', 'I', 'Th', 'Dy', 'N', 'Am', 'I', 'Te']
    """
    return re.findall(r'[A-Z][a-z]*', string)

def encode(string, dict):
    assert set(symbols(string)).issubset(set(dict.keys())), 'invalid symbol'
    elements = []
    for key in symbols(string):
        elements.append(dict[key])
    return ' '.join(elements)

def decode(string, table):
    # 先把table的key value对调
    table = {value:key for key, value in table.items()}
    assert set(symbols(string)).issubset(set(table.keys())), 'invalid name'
    names = []
    for key in symbols(string):
        names.append(table[key])
    return ' '.join(names)
if __name__ == '__main__':
    import doctest
    doctest.testmod()