# https://dodona.ugent.be/nl/courses/359/series/3487/activities/990750894
# input the random number
random = int(input())
# initialize total salary with random number
whole = random
# process salaries of successive workers
worker_salary, worker_num = input(), 0
while worker_salary != 'stop':
    # add salary of worker to total
    worker_num += 1
    whole += int(worker_salary)
    print(f'worker #{worker_num} whispers €{whole}')

    # read salary of next worker!!!
    worker_salary = input()
print(f'average salary: €{(whole - random)/worker_num:.2f}')