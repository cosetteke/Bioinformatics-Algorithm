# https://dodona.ugent.be/nl/courses/359/series/3485/activities/1813154454
import math
# input
sol = int(input())
# calculation
total_second = sol * 24 * 60 * 60 + sol * 39 * 60 + sol * 35.244
day = int(total_second // (60 * 60 * 24))
hour = int((total_second - day * 24 * 60 * 60) // (60 * 60))
min = int((total_second- day * 24 * 60 * 60 - hour * 60 * 60) // 60)
sec = math.floor(total_second - day * 24 * 60 * 60 - hour * 60 * 60 - min * 60)
# output
print(f'{sol} sols = {day} days, {hour} hours, {min} minutes and {sec} seconds')