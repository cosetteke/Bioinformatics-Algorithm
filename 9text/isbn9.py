# https://dodona.ugent.be/nl/courses/359/series/3493/activities/2055708402
def isISBN13(code):
    """
    Returns a Boolean value that indicates whether the given ISBN-13 code is
    valid.

    >>> isISBN13('9789743159664')
    True
    >>> isISBN13('9787954527409')
    False
    >>> isISBN13('8799743159665')
    False
        """
    if not (isinstance(code, str) and  # check whether entered code is a string
            len(code) == 13 and
            code.isdigit()):
        return False

    # check prefix of the given code
    if code[:3] not in {'978', '979'}:
        return False

    checkdigit = sum((3 if i % 2 else 1) * int(code[i]) for i in range(12))
    checkdigit = (10 - checkdigit) % 10
    return checkdigit == int(code[-1])


def remove_tags(s):
    # remove all xml tags from the given string
    s = s.strip()
    while s.find('<') >= 0:
        start = s.find('<')
        stop = s.find('>')
        if stop == -1:
            stop = len(s)
        s = s[:start] + s[stop + 1:]
        # remove leading and trailing whitespace and returns the modified string
    return s.strip()


def display_book_info(code):
    """
    >>> display_book_info('9780136110675')
    Title: The Practice of Computing using Python
    Authors: William F Punch, Richard Enbody
    Publisher: Addison Wesley
    >>> display_book_info('9780136110678')
    Wrong ISBN-13 code
    """
    if not isISBN13(code):
        print('Wrong ISBN-13 code')
    else:
        # open web page
        import urllib.request
        url = 'https://pythia.ugent.be/pythia-share/exercises/isbn9/books.php?isbn='
        parameters = code.strip()
        info = urllib.request.urlopen(url + parameters)  # file object

        # extract and output selected book info from XML
        for line in info:
            line = line.decode('utf-8')
            if line.startswith('<Title>'):
                print(f"Title: {remove_tags(line)}")
            elif line.startswith('<AuthorsText>'):
                print(f"Authors: {remove_tags(line).rstrip(',')}")  # to remove comma
            elif line.startswith('<PublisherText '):
                print(f"Publisher: {remove_tags(line).rstrip(',')}")
        # close the webpage
        info.close()

if __name__ == '__main__':
    import doctest
    doctest.testmod()