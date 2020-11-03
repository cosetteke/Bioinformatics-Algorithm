# https://dodona.ugent.be/nl/courses/359/series/3489/activities/811362724
alphabet = 'ABCDEFGHIJLMNOPQRSTUVWXYZ'
def encode_letter(letter):
    """
    >>> encode_letter('V')
    (5, 1)
    >>> encode_letter('i')
    (2, 4)
    """
    letter = letter.upper()
    if letter == 'K':
        letter = 'C'
    row = int(alphabet.find(letter)/5 + 1) # 或者 // 5
    column = alphabet.find(letter) % 5 + 1
    return (row, column)

def decode_letter(row, column):
    """
    >>> decode_letter(5, 1)
    'V'
    >>> decode_letter(2, 4)
    'I'
    """
    index = (row-1) * 5 + column - 1
    letter = alphabet[index]
    return letter

def encode(string):
    """
    >>> encode('VICTOR')
    '..... . .. .... . ... .... .... ... .... .... ..'
    >>> encode('Charlie')
    '. ... .. ... . . .... .. ... . .. .... . .....'
    """
    list = []
    for letter in string:
        list.append('.' * encode_letter(letter)[0])
        list.append('.' * encode_letter(letter)[1])
    return ' '.join(list)

def decode(string):
    """
    >>> decode('..... . .. .... . ... .... .... ... .... .... ..')
    'VICTOR'
    >>> decode('. ... .. ... . . .... .. ... . .. .... . .....')
    'CHARLIE'
    """
    list_dot = string.split(' ')
    coordinate = ''
    output = ''
    for item in list_dot:
        coordinate += str(item.count('.'))
    row_str = coordinate[::2]
    column_str = coordinate[1::2]
    for i in range(len(row_str)):
        output += decode_letter(int(row_str[i]), int(column_str[i]))
    return output
