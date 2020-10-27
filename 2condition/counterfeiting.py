# https://dodona.ugent.be/nl/courses/359/series/3486/activities/408865752
# input
first_weight = str(input())
sec_weight = str(input())
coin_num = ''
if first_weight == 'balance':
    if sec_weight == 'balance':
        coin_num = '9'
    elif sec_weight == 'left':
        coin_num = '8'
    else:
        coin_num = '7'
elif first_weight == 'left':
    if sec_weight == 'balance':
        coin_num = '6'
    elif sec_weight == 'left':
        coin_num = '5'
    else:
        coin_num = '4'
else:
    if sec_weight == 'balance':
        coin_num = '3'
    elif sec_weight == 'left':
        coin_num = '2'
    else:
        coin_num = '1'
print(f'coin #{coin_num} is counterfeit')