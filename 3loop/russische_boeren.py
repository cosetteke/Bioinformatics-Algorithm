# https://dodona.ugent.be/nl/courses/359/series/3487/activities/584449702
# input two numbers
m = int(input())
n = int(input())
sum = 0
while n > 0:
    print(f'{m} {n}')
    if n % 2 == 1:
        sum += m
    m, n = 2 * m, n // 2
# give output
print(sum)