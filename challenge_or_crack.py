# https://dodona.ugent.be/nl/courses/359/series/3487/activities/438287311
# input
round = int(input())
chall_point = 0
crack_point = 0
for i in range(round):
    correct = input()
    challenger = input()
    crack = input()
    if correct == challenger:
        chall_point += 1
        if crack == 'correct':
            crack_point += 1
    else:
        if crack == 'wrong':
            crack_point += 1

# give output
if chall_point > crack_point or (crack_point < round/2):
    print(f'challenger wins {chall_point} points against {crack_point}')
elif chall_point == crack_point:
    print(f'ex aequo: both contestants score {chall_point} points')
else:
    print(f'crack wins {crack_point} points against {chall_point}')
