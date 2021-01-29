# https://dodona.ugent.be/nl/courses/359/series/3493/activities/286850454
def invert(string):
    """
    >>> invert('God bless our brave Confederates, Lord!')
    'Dro lseta red efnoc Evarbruossel, Bdog!'
    >>> invert('Dro lseta red efnoc Evarbruossel, Bdog!')
    'God bless our brave Confederates, Lord!'
    >>> invert('Lee, Johnson, Smith, and Beauregard!')
    'Dra, Geruaeb, Dnaht, ims Nosnhojeel!'
    >>> invert('Help Jackson, Smith, and Johnson Joe,')
    'Eojn Osnhojd, Nahti, msn Oskcajp Leh,'
    >>> invert('To give them fits in Dixie, oh!')
    'Ho eixi dnis tifm eh Tevig, ot!'
    """
    letters = ''.join(char for char in string[::-1] if char.isalpha())
    inverted = ''
    index = 0
    for char in string:
        if char.isalpha():
            letter = letters[index]
            index += 1
            inverted += letter.upper() if char.isupper() else letter.lower()
        else:
            inverted += char
    return inverted

def codec(infile, outfile = None):
    infile = open(infile, 'r')
    if outfile is not None:
        outfile = open(outfile, 'w')
    for line in infile:
        if outfile is None:
            print(invert(line.rstrip('\n')))
        else:
            outfile.write(invert(line.rstrip('\n')) + '\n')

def filecomp(infile, outfile):
    infile, outfile = open(infile, 'r'), open(outfile, 'r')
    return infile.read() == outfile.read()
if __name__ == '__main__':
    import doctest
    doctest.testmod()