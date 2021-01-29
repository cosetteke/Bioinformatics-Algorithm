# https://dodona.ugent.be/nl/courses/359/series/3494/activities/657937938
class Necklace:
    """
    >>> necklace = Necklace('Jessica')
    >>> necklace
    Necklace('Jessica')
    >>> print(necklace)
    Jessica
    >>> len(necklace)
    7
    >>> necklace.slide(1)
    Necklace('essicaJ')
    >>> necklace
    Necklace('essicaJ')
    >>> necklace.slide(-2)
    Necklace('aJessic')
    >>> necklace.slide(11)
    Necklace('sicaJes')
    """
    def __init__(self, beads):
        self.beads = beads

    def __str__(self): # for print
        return self.beads

    def __repr__(self):
        return "Necklace('{}')".format(self.beads)

    def __len__(self):
        return len(self.beads)

    def slide(self, count):
        count %= len(self)
        self.beads = self.beads[count:] + self.beads[:count]
        return self

    def forms(self):
        return {str(self.slide(1)).upper() for _ in range(len(self))}

    def normal_form(self):
        return min(self.forms())

    def __eq__(self, other):
        return self.normal_form() == other.normal_form()

    def __add__(self, other):
        assert isinstance(other, int), 'invalid operation'
        return Necklace(str(self)).slide(other)

    def __radd__(self, other):
        return self + other
if __name__ == '__main__':
    import doctest
    doctest.testmod()
