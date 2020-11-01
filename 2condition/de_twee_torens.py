# https://dodona.ugent.be/nl/courses/359/series/3486/activities/2106206433
# give the input
prison1 = str(input())
prison2 = str(input())
tail = 'tail'
head = 'head'
scientist = str(input())
# process
if scientist == 'second':
    scientist2 = prison2
    scientist1 = prison1
    if scientist1 == head:
        scientist1 = tail
    else:
        scientist1 = head
else:
    scientist1 = prison1
    scientist2 = prison2
    if scientist2 == head:
        scientist2 = tail
    else:
        scientist2 = head

# output
print(scientist1)
print(scientist2)

# # read outcome both coin throws; outcomes are converted to Boolean values # (head -> True, tail -> False) in order to ease the implementation
# coin1 = input() == ’head’ coin2 = input() == ’head’
# # read which scientist will say the same as his own outcome
# same = input()
# # determine response of both scientists based on the outcome of their own throws
# # and the agreement who will say the same and who will say the opposite
# if same == ’first’: coin2 = not coin2
# else:
# coin1 = not coin1
# # output response of first scientist
# print(’head’ if coin1 else ’tail’)
# # output response of second scientist
# print(’head’ if coin2 else ’tail’)