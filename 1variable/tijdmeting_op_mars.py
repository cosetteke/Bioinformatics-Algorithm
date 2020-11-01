# https://dodona.ugent.be/nl/courses/359/series/3485/activities/1813154454
import math
# input
sol = int(input())
# calculation
## 可以把total second 先int了 之后就不需要这么多次转换
## 从second开始算min hour 这样的代码干净易懂
# # express number of sol in seconds
# seconds = int(sol * (((24 * 60) + 39) * 60 + 35.244))
# # convert seconds into minutes and seconds
# minutes = seconds // 60
# seconds %= 60
# # convert minutes into hours and minutes
# hours = minutes // 60
# minutes %= 60
# # convert hours into days and hours
# days = hours // 24 hours %= 24
total_second = sol * 24 * 60 * 60 + sol * 39 * 60 + sol * 35.244
day = int(total_second // (60 * 60 * 24))
hour = int((total_second - day * 24 * 60 * 60) // (60 * 60))
min = int((total_second- day * 24 * 60 * 60 - hour * 60 * 60) // 60)
sec = math.floor(total_second - day * 24 * 60 * 60 - hour * 60 * 60 - min * 60)
# output
print(f'{sol} sols = {day} days, {hour} hours, {min} minutes and {sec} seconds')