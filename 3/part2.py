input = open('input.txt', 'r')

running = 0
group = 0
arr = [False] * 52

for line in input:
    l = line.strip()

    for c in l:
        priority = ord(c) - (97 if c.islower() else 39)
        if (group == 0):
            arr[priority] = "a"
        elif (group == 1 and arr[priority] == "a"):
            arr[priority] = 1
        elif (group == 2 and arr[priority] == 1):
            running += priority + 1
            arr = [False] * 52
            break
    
    group = (group + 1) % 3

print(str(running))