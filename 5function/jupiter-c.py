# https://dodona.ugent.be/nl/courses/359/series/3489/activities/901549572
def reduce(keystring):
    """
    >>> reduce('HUNTSVILLEX')
    'HUNTSVILEX'
    >>> reduce('TRICHINOPHOBIA')
    'TRICHNOPBA'
    """
    return ''.join(sorted(set(keystring), key=keystring.index)) ## sort by index


def encode(number, keystring):
    """
    >>> encode(29, 'HUNTSVILLEX')
    'UE'
    >>> encode(63, 'TRICHINOPHOBIA')
    'NI'
    """
    keystring = reduce(keystring)
    # setting the format of assert error
    assert len(keystring) == 10, 'invalid key'

    letter = ''
    for i in str(number):
        next = keystring[int(i)-1]
        letter += next
    return letter

def decode(encode_str, keystring):
    """
    >>> decode('UE', 'HUNTSVILLEX')
    29
    >>> decode('NI', 'TRICHINOPHOBIA')
    63
    """
    keystring = reduce(keystring)
    assert len(keystring) == 10, 'invalid key'
    number = ''
    for char in encode_str:
        if keystring.find(char) < 9:
            number += str(keystring.index(char) + 1)
        else:
            number += '0'
    return int(number)

def next(encode_str, keystring):
    """
    >>> next('UE', 'HUNTSVILLEX')
    'NX'
    >>> next('NI', 'TRICHINOPHOBIA')
    'NC'
    """
    keystring = reduce(keystring)
    assert len(keystring) == 10, 'invalid key'
    encode_number = decode(encode_str, keystring) + 1
    new_encode = encode(encode_number, keystring)
    return new_encode


if __name__ == '__main__':
    import doctest
    doctest.testmod()