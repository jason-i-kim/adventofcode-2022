input = open('input', 'r')

outcome = [3, 0, 6]
running = 0

for line in input:
    l = line.strip()

    # rock = 0, paper = 1, scissors = 2
    opp = ord(l[0]) - 65 # A = 65
    mine = ord(l[2]) - 88 # X = 88

    result = ((opp - mine) + 3 ) % 3 # normalize diff to 0, 1/-2, or 2/-1
    running += outcome[result] + mine + 1

print(str(running))