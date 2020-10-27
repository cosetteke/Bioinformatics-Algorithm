# read first ISBN-10 code (or the word stop)
code = input()

# read successive ISBN-10 codes until line containing "stop" is read
while code != 'stop':

    # compute check digit
    check_digit = int(code[0])
    for i in range(2, 10):
        check_digit += i * int(code[i - 1])
    check_digit %= 11

    # extract check digit from ISBN-10 code
    x10 = code[-1]

    # check whether computed and extracted check digits are the same
    if (check_digit == 10 and x10 == 'X') or x10 == str(check_digit):
        print('OK')
    else:
        print('WRONG')

    # read next ISBN-10 code (or the word stop)
    code = input()
