input = open('input.txt', 'r')

running = 0

for line in input:
    l = line.strip()
    arr = [False] * 52

    for i, c in enumerate(l):
        priority = ord(c) - (97 if c.islower() else 39)
        if (i < len(l) / 2):
            arr[priority] = True
        elif (arr[priority]):
            running += priority + 1
            break

print(str(running))