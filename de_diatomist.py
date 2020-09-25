# https://dodona.ugent.be/nl/courses/359/series/3485/activities/1633935550
# input
import math
r_small = float(input())
r_big = float(input())

# calculate
n = math.floor(0.83 * (r_big**2 / r_small**2) - 1.9) # 向下取整
percentage = float((100 * (n * math.pi * r_small**2) / (math.pi * r_big**2), 2))
##
# output
print(f'{n} smaller circles cover {percentage}% of the larger circle')