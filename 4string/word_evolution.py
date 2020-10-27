# https://dodona.ugent.be/nl/courses/359/series/3488/activities/1713291174
# input
word = input()
letter_end = input()
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letter_start = word[0]

if letter_end > letter_start:
    length = ord(letter_end) - ord(letter_start) + 1
else:
    length = 26 - (ord(letter_start) - ord(letter_end)) + 1

for index in range(len(word)):
    letter_start = word[index]
    start_index = alphabet.find(letter_start)+1
    end_index = alphabet.find(letter_start)+length
    output = letter_start + alphabet[start_index:end_index]
    if end_index > 26:
        end_index %= 26
        output = letter_start + alphabet[start_index:] + alphabet[:end_index]
        # convert middle part to lower case
    output = output[0] + output[1:-1].lower() + output[-1]
    print(output)