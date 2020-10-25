# https://dodona.ugent.be/nl/courses/359/series/3489/activities/620641000
def isISBN(code):

    """
    Geeft True terug als het argument een string is die een geldige ISBN-10 code
    bevat. Anders wordt False teruggegeven.

    >>> isISBN('9971502100')
    True
    >>> isISBN('9971502108')
    False
    >>> isISBN('53WKEFF2C')
    False
    >>> isISBN(4378580136)
    False
    """
    if not (
        isinstance(code, str) and  # code must be a string
        len(code) == 10 and        # code must contain 10 characters
        code[:9].isdigit()         # first nine characters must be digits
    ):
        return False

    # check the check digit
    return checkdigit(code) == code[-1]
def checkdigit(code):
    """
    >>> checkdigit('997150210')
    '0'
    >>> checkdigit('938389293')
    '5'
    """
    check = sum((i+1)*int(code[i]) for i in range(9)) % 11
    return 'X' if check == 10 else str(check)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
