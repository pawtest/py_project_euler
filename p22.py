f = open("22_input.txt", "r")
names = [name.replace('"','') for name in  f.readline().split(",") ]
names.sort()

total = 0
for i, name in enumerate(names):
    score = 0
    for char in name:
        score += ord(char) - 64
    total += score * (i + 1)
print(total)

