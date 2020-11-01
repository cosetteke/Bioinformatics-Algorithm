# https://dodona.ugent.be/nl/courses/359/series/3487/activities/1765918609
# define a variable to start the loop:
control = True
day = 0
morethan30 = 0
while control:
    temp = input()
    if temp != 'stop':
        temp = float(temp)
        if temp >= 25:
            day += 1
            if temp >= 30:
                morethan30 += 1
        else:
            day = 0
            morethan30 = 0
    else:
        control = False
    if day >= 5 and morethan30 >= 3:
        break
print('heat wave' if day >= 5 and morethan30 >= 3 else 'no heat wave')

# # initialize variables with properties about sequence of successive warm days summer_days = 0 # number of successive days with temperature above 25 rˇC
# tropical_days = 0 # number of days in sequence with temperature above 30 rˇC
# # no heat wave observed until a sequence of successive days is found that meets
# # the criteria of a heat wave
# heat_wave = False
# # loop over days and determine the length of the current sequence of successive # days with a temperature above 25 rˇC, and the number of days in that sequence
# # with a temperature above 30 rˇC
# line = input()
# while not heat_wave and line != ’stop’: # line contains a temperature
# temperature = float(line)
# if temperature >= 25: # extend sequence above 25 rˇC
# summer_days += 1
# if temperature >= 30:
# tropical_days += 1
# # determine if conditions of heat wave have been met
# if summer_days >= 5 and tropical_days >= 3:
# heat_wave = True
# else: # start new sequence above 25 rˇC
# summer_days = 0 tropical_days = 0
# # read next line from input
# line = input()
# # output whether a heat wave was observed during the given period
# print(’heat wave’ if heat_wave else ’no heat wave’)