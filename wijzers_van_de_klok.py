# https://dodona.ugent.be/nl/courses/359/series/3485/activities/1381266978
# input
hour = int(input())
min = int(input())

# calculation
angle_hour = (hour%12 * 60 + min) / (12*60) * 360
angle_min = min/60 * 360
angle = abs(angle_hour - angle_min)
# output
print(f'At {hour:02d}:{min:02d} both hands form an angle of {angle:.1f}°.')
