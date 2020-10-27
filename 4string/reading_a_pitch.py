# https://dodona.ugent.be/nl/courses/359/series/3488/activities/1628
# input the line and information
line = input()
start_position,skip = int(input()),int(input())
output = ''
# if backwards, make everything as frontwards
if skip <0:
    line = line[::-1]
    skip = -skip
    start_position = - start_position - 1
for i in range(len(line)):
    output += line[(start_position + i * skip) % len(line)]
# output the result
print(output)