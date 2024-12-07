numbers_to_check = {}
numbers = []

with open("b.txt", "r") as f:
    for line in f:
        line = line.strip()
        if "|" in line:
            try:
                numbers_to_check[int(line.split("|")[0])].append(int(line.split("|")[1]))
            except:
                numbers_to_check[int(line.split("|")[0])] = [int(line.split("|")[1])]
        if "," in line:
            numbers.append([int(i) for i in line.split(",")])

total = 0

for i in numbers:
    c = []
    ok = True
    for j in i:
        c.append(j)
        try:
            for a in numbers_to_check[j]:
                if a in c:
                    ok = False
                    break
            if not ok:
                break
        except KeyError:
            pass

    if ok:
        total += i[len(i)//2]

print(total)