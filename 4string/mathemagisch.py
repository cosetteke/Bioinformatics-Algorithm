# https://dodona.ugent.be/nl/courses/359/series/3488/activities/1260445672
# input the digit, written without leading zeros
digit = input()
total = 0
position = len(digit) + 1
equal = '=' * position
# here is the loop
for index, i in enumerate(digit):
    new_line = digit[:index]+digit[index+1:]
    total += int(new_line)
    if new_line.startswith('0'):
        new_line = str(int(new_line))
    # do some edition on the last line
    if index == len(digit) - 1:
        print('+'+f'{new_line:>{position-1}s}')
    else:
        print(f'{new_line:>{position}s}')
    # print(f’{"+" if index == length - 1 else " "}{term:{length}d}’)
# output
print(equal)
print(f'{str(total):>{position}s}')