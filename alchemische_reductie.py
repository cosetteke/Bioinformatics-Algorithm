# https://dodona.ugent.be/nl/courses/359/series/3488/activities/1515750432
# input
polymer = input()
# build a new polymer
new_polymer = polymer[0]
for (index, char), char_new in zip(enumerate(polymer),new_polymer):
    # set the range
    if index+1 < len(polymer):
        if new_polymer[-1].upper() == polymer[index+1].upper():
            new_polymer1 = new_polymer[:-1]
        else:
            new_polymer1 += polymer[index+1]
        if len(new_polymer1) < len(new_polymer):
            if new_polymer1[-1].upper() == polymer[index + 1].upper():
                new_polymer1 = new_polymer1[:-1]

# output
print(f'{new_polymer1}' + '('+ f'{len(new_polymer1)}' + ')' )