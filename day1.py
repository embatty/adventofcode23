import regex as re

sumup = []

numbers = "one|two|three|four|five|six|seven|eight|nine"

convertdict = {'one':1,
                'two':2,
                'three':3,
                'four':4,
                'five':5,
                'six':6,
                'seven':7,
                'eight':8,
                'nine':9}

with open("inputfiles/day1.input") as infile:
    for line in infile:
        line = line.strip()
        print(line)
        #loop through the buffer forward and find location of earliest and latest digit
        for i,char in enumerate(line):
            if str.isdigit(char):
                earlydigit=i
                break
        #then loop through backwards
        for i,char in enumerate(line[::-1]):
            if str.isdigit(char):
                latedigit=len(line)-i-1
                break
        print(line[earlydigit])
        print(line[latedigit])

        #then find position of regular expression matches
        numberwords = [x.span() for x in re.finditer(numbers, line, overlapped=True)]
        print(numberwords)
        if numberwords != []: #if there are numberwords, check against digits
            if numberwords[0][0] < earlydigit:
                firstdigit = convertdict[line[numberwords[0][0]:numberwords[0][1]]]
            else:
                firstdigit = line[earlydigit]
            if numberwords[-1][1] > latedigit:
                lastdigit = convertdict[line[numberwords[-1][0]:numberwords[-1][1]]]
            else:   
                lastdigit = line[latedigit]
        else: #if there aren't numberwords we jump here
            firstdigit = line[earlydigit]
            lastdigit = line[latedigit]
        #append the two digit number
        print([firstdigit, lastdigit])
        sumup.append("".join([str(firstdigit), str(lastdigit)]))

total = sum([int(x) for x in sumup])
print("That's numberwang!", total)