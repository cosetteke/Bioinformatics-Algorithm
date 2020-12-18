def alphabet(string):
    """
    >>> alphabet('BEAR + RARE + ERE = RHYME')
    'ABEHMRY'
    >>> alphabet('BRUTUS + STABS = CAESAR')
    'ABCERSTU'
    """
    alphabet = set(i for i in string if i.isalpha()) # built a unsorted set
    return ''.join(sorted(alphabet)) # convert to a sorted string

def number(word_, alpha, solution):
    """
    >>> number('BEAR', 'ABEHMRY', '5790813')
    7951
    >>> number('RARE', 'ABEHMRY', '5790813')
    1519
    >>> number('ERE', 'ABEHMRY', '5790813')
    919
    >>> number('RHYME', 'ABEHMRY', '5790813')
    10389
    """
    number = ''
    for letter in word_:
        number += solution[alpha.find(letter)]
    return int(number)

def numbers(alphametic, alpha, solution):
    """
    >>> numbers('BEAR + RARE + ERE', 'ABEHMRY', '5790813')
    (7951, 1519, 919)
    >>> numbers('BRUTUS + STABS', 'ABCERSTU', '75638921')
    (581219, 92759)
    """
    # create a word list for alphametic
    word_list = [word_ for word_ in alphametic.split() if word_.isalpha()]
    # find corresponding number solution for each word
    return tuple(number(word_, alpha, solution) for word_ in word_list)

def word(num, alpha, solution):
    """
    >>> word(7951, 'ABEHMRY', '5790813')
    'BEAR'
    >>> word(1519, 'ABEHMRY', '5790813')
    'RARE'
    >>> word(919, 'ABEHMRY', '5790813')
    'ERE'
    >>> word(10389, 'ABEHMRY', '5790813')
    'RHYME'
    """
    word_ = ''
    for letter in str(num):
        word_ += alpha[solution.find(letter)]
    return word_

def outcome(left, alpha, solution):
    """
    >>> outcome('BEAR + RARE + ERE', 'ABEHMRY', '5790813')
    'RHYME'
    >>> outcome('BRUTUS + STABS', 'ABCERSTU', '75638921')
    'CAESAR'
    """
    # calculate the sum result of left side words
    left_sum = sum(numbers(left, alpha, solution))
    # find the result based on left side
    return word(left_sum, alpha, solution)

def issolution(string, problem):
    """
    >>> issolution('5790813', 'BEAR + RARE + ERE = RHYME')
    True
    >>> issolution('75638921', 'BRUTUS + STABS = TIBERIUS')
    False
    """
    alpha = alphabet(problem)
    word_list = [word_ for word_ in problem.split() if word_.isalpha()]
    leftside = ' + '.join(word_list[:-1])
    rightside = word_list[-1]
    try:
        result = outcome(leftside, alpha, string) == rightside
    except IndexError:
        return False
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()
