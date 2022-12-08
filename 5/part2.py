import re

input = open('input.txt', 'r')

running = 0
lineCounter = 0
stacks = [[],[],[],[],[],[],[],[],[]]

for line in input:
    if (lineCounter < 8):
        for i in range(9):
            c = line[1 + 4 * i]
            if (c != ' '): 
                stacks[i] = [c] + stacks[i]
    elif (lineCounter > 9):
        result = re.search(r"move (\d+) from (\d+) to (\d+)", line)
        f = eval(result.group(2)) - 1
        t = eval(result.group(3)) - 1
        n = min(len(stacks[f]), eval(result.group(1)))
        i = len(stacks[f]) - n

        stacks[t] += stacks[f][i:len(stacks[f])]
        stacks[f] = stacks[f][0:i]

    lineCounter += 1

s = ""
for stack in stacks:
    s += stack.pop()

print(s)