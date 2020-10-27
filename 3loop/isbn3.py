# https://dodona.ugent.be/nl/courses/359/series/3487/activities/1898834779
# https://dodona.ugent.be/nl/courses/359/series/3486/activities/182880102
first = input()
while first != 'stop':
    sum = int(first)
    for index in range(2, 10):
        next_digit = int(input())
        sum += index * next_digit
    sum %= 11
    ten = int(input())
    print('OK' if ten == sum else 'WRONG')
    # read next ten
    first = input()