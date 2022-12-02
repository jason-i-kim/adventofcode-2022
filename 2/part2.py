input = open('input', 'r')

running = 0
answer = 0

for line in input:
    l = line.strip()

    # rock = 0, paper = 1, scissors = 2
    opp = ord(l[0]) - 65 # A = 65
    outcome = ord(l[2]) - 88 # X = 88; lose = 0; draw = 1; win = 2

    diff = (outcome + 2) % 3 # change 0 to 2, 1 to 0, 2 to 1
    mine = (opp + diff) % 3 # apply diff to opponent's shape to get my shape

    running += mine + 1 + outcome * 3

print(str(running))