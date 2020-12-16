# https://dodona.ugent.be/nl/courses/359/series/3491/activities/1158810383
def serial_number(serial):
    """
    >>> serial_number(834783)
    '00834783'
    >>> serial_number('47839')
    '00047839'
    >>> serial_number(834783244839184)
    '834783244839184'
    >>> serial_number('4783926132432*')
    Traceback (most recent call last):
    AssertionError: invalid serial number
    """
    serial = str(serial)
    assert (serial.isdigit()), 'invalid serial number'
    assert (set(list(serial)) != {'0'}), 'invalid serial number'

    if len(serial) < 8:
        serial = '0' * (8 - len(serial)) + serial
    return serial

def solid(number):
    """
    >>> solid(44444444)
    True
    >>> solid('44544444')
    False
    """
    return len(set(list(serial_number(number)))) == 1
## 老师的答案
# number = serial_number(number)
# return number == number[0] * len(number)

def radar(number):
    """
    >>> radar(1133110)
    True
    >>> radar('83289439')
    False
    """
    number = serial_number(number)
    half = len(number) // 2
    return number[:half] == number[half:][::-1] and not solid(number)
## 注意[::是跳过的位置] 不要把它和string 的reverse搞混了！！

def repeater(number):
    """
    >>> repeater(20012001)
    True
    >>> repeater('83289439')
    False
    """
    number = serial_number(number)
    half = len(number) // 2
    return number[:half] == number[half:] and not solid(number)

def radar_repeater(number):
    """
    >>> radar_repeater('12211221')
    True
    >>> radar_repeater('83289439')
    False
    """
    return repeater(number) and radar(number)

def numismatist(listort, kind = solid):
    """
    >>> numismatist([33333333, 1133110, '77777777', '12211221'])
    [33333333, '77777777']
    >>> numismatist([33333333, 1133110, '77777777', '12211221'], radar)
    [1133110, '12211221']
    >>> numismatist([33333333, 1133110, '77777777', '12211221'], kind=repeater)
    ['12211221']
    """
    return [number for number in listort if kind(number)]

if __name__ == '__main__':
    import doctest
    doctest.testmod()