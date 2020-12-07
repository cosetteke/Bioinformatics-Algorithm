# input
word = input().lower() #  only consists of letters and put to lower case
reverse = word[::-1]
n = int(input()) # number of lines

# process the following lines
for _ in range(n):
    line = input().lower() # read the line and convert to lower case
    # check if the line contains the word
    if word in line or reverse in line:
        index = line.index(word) if word in line else line.index(reverse)
        print(line[:index] + line[index:index+len(word)].upper() + line[index+len(word):])
    else:
        print(line)
