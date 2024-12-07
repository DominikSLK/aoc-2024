aa = []

with open("b.txt") as f:
    for i in f.readlines():
        aa.append(list(i.strip()))

guard = []

for i in range(len(aa)):
    for j in range(len(aa[0])):
        if aa[i][j] == '^':
            guard = ["^", i, j]

def turn(guard):
    if guard[0] == "^":
        guard[0] = ">"
        guard[1] += 1
    elif guard[0] == ">":
        guard[0] = "v"
        guard[2] -= 1
    elif guard[0] == "v":
        guard[0] = "<"
        guard[1] -= 1
    elif guard[0] == "<":
        guard[0] = "^"
        guard[2] += 1
    return guard

used = []

while True:
    used.append([guard[1], guard[2]])
    if guard[0] == "^":
        guard[1] -= 1
        if guard[1] == 0 and aa[guard[1]][guard[2]] == '.':
            break
        if guard[1] == 0 or aa[guard[1]][guard[2]] == '#':
            turn(guard)
            print(guard)
    elif guard[0] == ">":
        guard[2] += 1
        if guard[2] == len(aa[0]) and aa[guard[1]][guard[2]] == '.':
            break
        if aa[guard[1]][guard[2]] == '#':
            turn(guard)
            print(guard)
    elif guard[0] == "v":
        guard[1] += 1
        try:
            if guard[1] == len(aa) and aa[guard[1]][guard[2]] == '.':
                break
        except IndexError:
            break
        if aa[guard[1]][guard[2]] == '#':
            turn(guard)
            print(guard)
    elif guard[0] == "<":
        guard[2] -= 1
        if guard[2] == 0 and aa[guard[1]][guard[2]] == '.':
            break
        if aa[guard[1]][guard[2]] == '#':
            turn(guard)
            print(guard)

a = [str(i) for i in used]
print(len(list(set(a))))