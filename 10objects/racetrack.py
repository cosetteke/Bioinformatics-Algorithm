# https://dodona.ugent.be/nl/courses/359/series/3494/activities/2145526972
class Block:
    """
    >>> rock = Block(5, 2, 3)
    >>> rock
    Block(length=5, height=2, width=3, position=(0, 0))
    >>> rock.area()
    62.0
    >>> rock.volume()
    30.0
    >>> rock.diagonal()
    6.164414002968976
    """
    def __init__(self, l, h, w):
        self.l = l
        self.h = h
        self.w = w
        self.position = (0,0)
        self._area = 2.0 * (l * w + l * h + h * w)
        self._volume = float(l * h * w)
        self._diagonal = (l**2 + h **2 + w ** 2) ** 0.5
    def __repr__(self):
        return "Block(length={}, height={}, width={}, position={})".format(self.l,self.h,self.w,self.position)

    def area(self):
        return self._area

    def volume(self):
        return self._volume

    def diagonal(self):
        return self._diagonal



if __name__ == '__main__':
    import doctest
    doctest.testmod()