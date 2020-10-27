# https://dodona.ugent.be/nl/courses/359/series/3486/activities/1357047316
# input
x = float(input())
y = float(input())

# conditions
if y > 6 and x < 4.65:
    print("red")
elif (2.2 < x < 4 and y <= 2) or (x > 6.3 and 4.1 < y < 6):
    print('blue')
elif x > 6.3 and y <= 2.6:
    print('yellow')
else:
    print('white')