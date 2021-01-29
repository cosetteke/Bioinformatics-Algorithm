# https://dodona.ugent.be/nl/courses/359/series/3494/activities/341848809
class ISBN13:
    """
    >>> code = ISBN13(9780136110675)
    >>> print(code)
    978-0-13611067-5
    >>> code
    ISBN13(9780136110675, 1)
    >>> code.isvalid()
    True
    >>> code.asISBN10()
    '0-13611067-3'
    """
    def __init__(self, code, length=1):
        assert isinstance(code, int) and 1<= length <= 5, 'invalid ISBN code'

        self.code = str(code).zfill(13)
        self.length = length

    def __int__(self):
        return int(self.code)

    def __str__(self):
        c = self.code
        return '{}-{}-{}-{}'.format(c[:3], c[3:3+self.length], c[3+self.length:-1], c[-1])

    def __repr__(self):
        return 'ISBN13({}, {})'.format(self.code, self.length)

    def isvalid(self):
        c = str(self.code)
        o = sum(list(map(int, list(c[0:11:2]))))
        e = sum(list(map(int, list(c[1::2]))))
        return (10 - (o + 3 * e) % 10) % 10 == int(c[-1]) and c[:3] in ['978', '979']

    def asISBN10(self):
        c = str(self.code)
        if self.isvalid() and c[:3] == '978':
            j = 0
            for i in range(9):
                j += (int(c[i + 3]) * (i + 1))
            j %= 11
            return '{}-{}-{}'.format(c[3:3 + self.length], c[3 + self.length:-1], j if j != 10 else 'X')
        return None
