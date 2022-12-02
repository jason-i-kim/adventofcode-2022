input = open('input', 'r')
highest = 0
runCount = 0

for line in input:
    l = line.strip()
    if not l:
        highest = max(highest, runCount)
        runCount = 0
    else:
        runCount += int(l)

print(max(runCount, highest))