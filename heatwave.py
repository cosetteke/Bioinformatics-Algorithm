# https://dodona.ugent.be/nl/courses/359/series/3487/activities/1765918609
# define a variable to start the loop:
control = True
day = 0
morethan30 = 0
while control:
    temp = input()
    if temp != 'stop':
        temp = float(temp)
        if temp >= 25:
            day += 1
            if temp >= 30:
                morethan30 += 1
        else:
            day = 0
            morethan30 = 0
    else:
        control = False
    if day >= 5 and morethan30 >= 3:
        break
print('heat wave' if day >= 5 and morethan30 >= 3 else 'no heat wave')