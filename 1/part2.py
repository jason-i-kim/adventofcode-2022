input = open('input', 'r')
first = 0
second = 0
third = 0
runCount = 0

def swapIfGreaterOrEqual(a, b):
    if (a >= b):
        temp = b
        b = a
        a = temp

for line in input:
    l = line.strip()
    if not l:
        if (runCount >= first):
            temp = first
            first = runCount
            runCount = temp
        if (runCount >= second):
            temp = second
            second = runCount
            runCount = temp
        if (runCount >= third):
            temp = third
            third = runCount
            runCount = temp
        runCount = 0
    else:
        runCount += int(l)

print (first + second+ third)