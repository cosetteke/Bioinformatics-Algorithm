# https://dodona.ugent.be/nl/courses/359/series/3489/activities/534181732
def iskey(k1, k2):
    """
    >>> iskey('THEQUICKBROWN', 'FXJMPSVLAZYDG')
    True
    >>> iskey('ABCDEFGHIJKLM', 'NOPQRSTUVW???')
    False
    >>> iskey('ABCDEFGHIJKLM', 'NOPQRSTUVW')
    False
    """
    all = set(k1.upper() + k2.upper())
    return len(all) == 26 and len(k1) == 13 and len(k2) == len(k1) and k1.isalpha() and k2.isalpha()
def encode_character(m, k1, k2):
    """
    >>> encode_character('Q', 'THEQUICKBROWN', 'FXJMPSVLAZYDG')
    'M'
    >>> encode_character('v', 'THEQUICKBROWN', 'FXJMPSVLAZYDG')
    'c'
    >>> encode_character('?', 'THEQUICKBROWN', 'FXJMPSVLAZYDG')
    '?'
    """
    if not m.isalpha():
        return m
    if m.isupper():
        k1, k2 = k1.upper(), k2.upper()
        if k1.find(m) == -1:
            return k1[k2.find(m)]
        return k2[k1.find(m)]
    m = m.upper()
    k1 = k1.upper()
    k2 = k2.upper()
    if k1.find(m) == -1:
        return k1[k2.find(m)].lower()
    return k2[k1.find(m)].lower()

def encode(string, k1, k2):
    """
    >>> encode('A person who does nothing will enjoy no happiness.', 'THEQUICKBROWN', 'FXJMPSVLAZYDG')
    'B ujziyg dxy wyji gyfxsgn dskk jgeyo gy xbuusgjii.'
    """
    output = ''
    for char in string:
        output += encode_character(char, k1, k2)
    return output

def decode(string, k1, k2):
    """
    >>> decode('B ujziyg dxy wyji gyfxsgn dskk jgeyo gy xbuusgjii.', 'THEQUICKBROWN', 'FXJMPSVLAZYDG')
    'A person who does nothing will enjoy no happiness.'
    """
    output = ''
    for char in string:
        output += encode_character(char, k1, k2)
    return output