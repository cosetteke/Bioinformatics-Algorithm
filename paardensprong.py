# https://dodona.ugent.be/nl/courses/359/series/3486/activities/56374393
# give the input
start = str(input())
end = str(input())
move = ''
# process
start1, start2 = start
end1, end2 = end
if ord(start1) == ord(end1) or int(start2) == int(end2): # should be L shape
    move = 'cannot'
elif abs(ord(start1)-ord(end1)) + abs(int(start2)-int(end2)) == 3:
    move = 'can'
else:
    move = 'cannot'
# give output
print(f'a knight {move} jump from {start} to {end}')