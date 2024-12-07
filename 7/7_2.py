from itertools import product

def gen(n: int):
    return [''.join(p) for p in product('+*|', repeat=n)]

a = []
with open("b.txt") as f:
    for i in f.readlines():
        i = i.strip()
        a.append([int(i.split(":")[0])] + [int(i) for i in i.split(":")[1].strip().split(" ")])

c = 0

for i in a:
    combinations = gen(len(i[1:])-1)
    for j in range(len(combinations)):
        aa = i[1:][0]
        for k in range(len(combinations[j])):
            if combinations[j][k] == "|":
                try:
                    aa = int(str(aa) + str(i[1:][k+1]))
                except:
                    pass
            elif combinations[j][k] == "+":
                try:
                    aa += i[1:][k+1]
                except:
                    pass
            else:
                try:
                    aa *= i[1:][k+1]
                except:
                    pass

        if aa == i[0]:
            c += i[0]
            break

print(c)