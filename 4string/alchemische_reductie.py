# https://dodona.ugent.be/nl/courses/359/series/3488/activities/1515750432
# input
polymer = input()
# build a new polymer
new_polymer = ''

for char in polymer:
    # if new polymer is empty, just add the character
    if len(new_polymer) == 0:
        new_polymer += char
    else:
        # if alchemical reaction
        if char != new_polymer[-1].swapcase():
            new_polymer += char
        else:
            new_polymer = new_polymer[:-1]
    ## 这种形式下可以考虑省略一个合并条件
# give the output
print(f'{new_polymer}({len(new_polymer)})')