# https://dodona.ugent.be/nl/courses/359/series/3488/activities/2009241681
# input the separator and number of lines

separator = input()
line_number = int(input())

for i in range(line_number+1):
    try:
        line = input()
        sep_index = line.find(separator)
        # extract the left part of separator
        left = line[:sep_index]
        # extract the right part of separator
        right = line[sep_index+1:]
        # exchange place and combine
        new_line = right + left
        print(new_line)
    except(EOFError):
        break