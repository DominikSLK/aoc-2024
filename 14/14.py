bots = []
max_x = 101 # 11 for example
max_y = 103 # 7 for example

with open("b.txt") as f:
    for line in f:
        p, v = line.strip().split()
        p = p.replace("p=", "").split(",")
        v = v.replace("v=", "").split(",")
        bots.append([[int(p[0]), int(p[1])], [int(v[0]), int(v[1])]])

def simulate(bot, seconds):
    for i in range(seconds):
        new_x = bot[0][0] + bot[1][0]
        new_y = bot[0][1] + bot[1][1]
        if new_x > max_x-1:
            new_x = new_x - max_x
        elif new_x < -max_x:
            new_x = new_x + max_x
        if new_y > max_y-1:
            new_y = new_y - max_y
        elif new_y < -max_y:
            new_y = new_y + max_y

        bot[0][0] = new_x
        bot[0][1] = new_y

for bot in bots:
    simulate(bot, 100)

a = []
for i in range(max_y):
    b = []
    for j in range(max_x):
        b.append(".")
    a.append(b)

for bot in bots:
    if a[bot[0][1]][bot[0][0]] == ".":
        a[bot[0][1]][bot[0][0]] = "1"
    else:
        a[bot[0][1]][bot[0][0]] = str(int(a[bot[0][1]][bot[0][0]]) + 1)

q1 = 0
q2 = 0
q3 = 0
q4 = 0

for i in range(max_y):
    for j in range(max_x):
        if max_x // 2 > j and max_y // 2 > i:
            if a[i][j] != ".":
                q1 += int(a[i][j])
        elif max_x // 2 < j and max_y // 2 > i:
            if a[i][j] != ".":
                q2 += int(a[i][j])
        if max_x // 2 > j and max_y // 2 < i:
            if a[i][j] != ".":
                q3 += int(a[i][j])
        elif max_x // 2 < j and max_y // 2 < i:
            if a[i][j] != ".":
                q4 += int(a[i][j])

print(q1 * q2 * q3 * q4)