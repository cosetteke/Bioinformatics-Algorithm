# https://dodona.ugent.be/nl/courses/359/series/3487/activities/990750894
# input the random number
random = int(input())
worker_num = 0
worker_salary = 0
while worker_salary != 'stop':
    worker_salary = input()
    if worker_salary == 'stop':
        break
    else:
        sum = random + int(worker_salary)
        worker_num += 1
        print(f'worker #{worker_num} whispers €{sum}')

average = (sum - random) / worker_num
print(f'average salary: €{average:.2f}')