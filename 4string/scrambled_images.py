# https://dodona.ugent.be/nl/courses/359/series/3488/activities/2009241681
# input the separator and number of lines
separator = input()
line_number = int(input())
for _ in range(line_number): # 循环的东西在loop中用不到
    line = input()
    sep_index = line.index(separator)
    # exchange place and combine
    new_line = line[sep_index+1:] + line[:sep_index]
    print(new_line)