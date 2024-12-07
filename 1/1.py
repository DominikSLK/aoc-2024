def distance(a, b):
    if a < b:
        return b - a
    else:
        return a - b

a = []
b = []

with open('b.txt') as f:
    for line in f.readlines():
        line = line.strip().split("   ")
        a.append(int(line[0]))
        b.append(int(line[1]))

a.sort()
b.sort()

aaa = 0
bbb = 0

for i in range(len(a)):
    aaa += distance(a[i], b[i])
    bbb += a[i] * b.count(a[i])

print(aaa)
print(bbb)