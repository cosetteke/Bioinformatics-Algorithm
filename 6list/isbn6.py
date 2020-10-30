# https://dodona.ugent.be/nl/courses/359/series/3490/activities/1316294687
# https://dodona.ugent.be/nl/courses/359/series/3489/activities/620641000
def isISBN(code):

    """
    Geeft True terug als het argument een string is die een geldige ISBN-10 code
    bevat. Anders wordt False teruggegeven.

    >>> isISBN('9-9715-0210-0')
    True
    >>> isISBN('997-150-210-0')
    False
    >>> isISBN('9-9715-0210-8')
    False
    """
    # first and last group should contain a single digit
    if code[1] != '-' or code[-2] != '-' or code[6] != '-' or code.count('-') != 3:
        return False
    code = code.split('-')
    code = ''.join(code)
    if not (
        len(code) == 10 and        # code must contain 10 characters
        code[:9].isdigit()         # first nine characters must be digits
    ):
        return False
    # check the check digit
    return checkdigit(code) == code[-1]

def checkdigit(code):
    check = sum((i+1)*int(code[i]) for i in range(9)) % 11
    return 'X' if check == 10 else str(check)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
