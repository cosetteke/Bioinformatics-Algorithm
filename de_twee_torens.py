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