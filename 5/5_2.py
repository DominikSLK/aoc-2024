numbers_to_check = {}
numbers = []

with open("b.txt", "r") as f:
    for line in f:
        line = line.strip()
        if "|" in line:
            try:
                numbers_to_check[int(line.split("|")[0])].append(int(line.split("|")[1]))
            except KeyError:
                numbers_to_check[int(line.split("|")[0])] = [int(line.split("|")[1])]
        if "," in line:
            numbers.append([int(i) for i in line.split(",")])

total = 0

for i in numbers:
    c = i.copy()
    ok = True
    changed = True

    while changed:
        changed = False
        for j in range(len(c)):
            try:
                for a in numbers_to_check[c[j]]:
                    if a in c:
                        i1 = c.index(a)
                        i2 = j
                        if i1 < i2:
                            c[i1], c[i2] = c[i2], c[i1]
                            changed = True
                            ok = False
            except KeyError:
                pass

    if not ok:
        total += c[len(c)//2]

print(total)
