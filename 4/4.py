a = []

with open("b.txt") as f:
    for line in f:
        a.append(line.strip())

count = 0
b = []

for i in a:
    for index, j in enumerate(i):
        try:
            b[index] += j
        except:
            b.append(j)
    count += i.count("XMAS") + i[::-1].count("XMAS")

for i in b:
    count += i.count("XMAS") + i[::-1].count("XMAS")

d = []

for diff in range(-len(a) + 1, len(a)):
    diagonal = ""
    for i in range(len(a)):
        j = i + diff
        if 0 <= j < len(a[i]):
            diagonal += a[i][j]
    d.append(diagonal)

for diff in range(len(a) * 2 - 1):
    diagonal = ""
    for i in range(len(a)):
        j = diff - i
        if 0 <= j < len(a[i]):
            diagonal += a[i][j]
    d.append(diagonal)

for i in d:
    count += i.count("XMAS") + i[::-1].count("XMAS")

print(count)
