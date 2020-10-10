# https://dodona.ugent.be/nl/courses/359/series/3487/activities/1462225048
# input
a = int(input()) # parameter
b = int(input()) # parameter
time1 = int(input()) # time for 1st experiement
cell2 = int(input()) # start number of cells for 2nd experiement
cell1 = 1
time2 = 0
# processing
for i in range(time1):
    cell1 = a * cell1 + b
while cell2 < cell1:
    cell2 = a * cell2 + b
    time2 += 1
# output
print(f'experiment #1: {cell1} cells after {time1} seconds')
print(f'experiment #2: {cell2} cells after {time2} seconds')
