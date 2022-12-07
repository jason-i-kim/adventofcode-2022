input = open('input.txt', 'r')

running = 0

for line in input:
    pairs = line.strip().split(',')
    first = [eval(i) for i in pairs[0].split('-')]
    second = [eval(i) for i in pairs[1].split('-')]

    if ((first[0] < second[0] and second[0] >= first[0] and second[1] <= first[1]) 
        or (second[0] < first[0] and first[0] >= second[0] and first[1] <= second[1])
        or (first[0] == second[0])):    
            running += 1

print(str(running))