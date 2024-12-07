import copy

aa = []

with open("b.txt") as f:
    for i in f.readlines():
        aa.append(list(i.strip()))

guard = []
guard_orig = []

for i in range(len(aa)):
    for j in range(len(aa[0])):
        if aa[i][j] == '^':
            guard = ["^", i, j]
            guard_orig = ["^", i, j]

turns = 0

def turn(guard):
    global turns
    turns += 1
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

used = set()
loops = 0

while True:
    used.add((guard[1], guard[2]))
    if guard[0] == "^":
        guard[1] -= 1
        if guard[1] == 0 and aa[guard[1]][guard[2]] == '.':
            break
        if guard[1] == 0 or aa[guard[1]][guard[2]] == '#':
            turn(guard)
    elif guard[0] == ">":
        guard[2] += 1
        if guard[2] == len(aa[0]) and aa[guard[1]][guard[2]] == '.':
            break
        if aa[guard[1]][guard[2]] == '#':
            turn(guard)
    elif guard[0] == "v":
        guard[1] += 1
        try:
            if guard[1] == len(aa) and aa[guard[1]][guard[2]] == '.':
                break
        except IndexError:
            break
        if aa[guard[1]][guard[2]] == '#':
            turn(guard)
    elif guard[0] == "<":
        guard[2] -= 1
        if guard[2] == 0 and aa[guard[1]][guard[2]] == '.':
            break
        if aa[guard[1]][guard[2]] == '#':
            turn(guard)

for i in range(0, len(used)):
    bb = copy.deepcopy(aa)
    guard = guard_orig.copy()
    turns = 0
    bb[list(used)[i][0]][list(used)[i][1]] = '#'

    while True:
        if turns > len(aa) * 2:
            loops += 1
            break

        if guard[0] == "^":
            guard[1] -= 1
            try:
                if guard[1] == 0 and bb[guard[1]][guard[2]] == '.':
                    break
            except IndexError:
                break
            if guard[1] == 0 or bb[guard[1]][guard[2]] == '#':
                turn(guard)
        elif guard[0] == ">":
            guard[2] += 1
            try:
                if guard[2] == len(bb[0]) and bb[guard[1]][guard[2]] == '.':
                    break
            except IndexError:
                break
            if bb[guard[1]][guard[2]] == '#':
                turn(guard)
        elif guard[0] == "v":
            guard[1] += 1
            try:
                if guard[1] == len(bb) and bb[guard[1]][guard[2]] == '.':
                    break
            except IndexError:
                break
            if bb[guard[1]][guard[2]] == '#':
                turn(guard)
        elif guard[0] == "<":
            guard[2] -= 1
            try:
                if guard[2] == 0 and bb[guard[1]][guard[2]] == '.':
                    break
            except IndexError:
                break
            if bb[guard[1]][guard[2]] == '#':
                turn(guard)

print(loops)