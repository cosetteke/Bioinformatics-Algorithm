# https://dodona.ugent.be/nl/courses/359/series/3486/activities/328212300
import math
# input the body temperature
tem = float(input())
# calculate
approximation = 100 / tem
# comparasion
if approximation < math.e - 0.1:
    print("you have a fever")
elif approximation > math.e + 0.1:
    print("you have hypothermia")
else:
    print("you have a normal body temperature")