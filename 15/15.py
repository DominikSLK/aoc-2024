warehouse = []
moves = ""

with open("input.txt") as f:
    m = False
    for line in f.readlines():
        line = line.strip()
        if line != "" and not m:
            warehouse.append(list(line))
        if line == "":
            m = True
        if line != "" and m:
            moves += line

def get_robot_pos(warehouse):
    for i in range(len(warehouse)):
        for j in range(len(warehouse[i])):
            if warehouse[i][j] == "@":
                return (i, j)

def get_str_rep(warehouse, start=None):
    s = ""
    if start:
        s += start + "\n"
    for i in range(len(warehouse)):
        for j in range(len(warehouse[i])):
            s += warehouse[i][j]
        s += "\n"
    return s

robot_pos = get_robot_pos(warehouse)

#print(get_str_rep(warehouse, "Initial state:"))

for move in moves:
    robot_pos = get_robot_pos(warehouse)
    if move == "^":
        if warehouse[robot_pos[0] - 1][robot_pos[1]] == ".":
            warehouse[robot_pos[0] - 1][robot_pos[1]] = "@"
            warehouse[robot_pos[0]][robot_pos[1]] = "."
        elif warehouse[robot_pos[0] - 1][robot_pos[1]] == "O":
            found = False
            for i in range(len(warehouse), -1, -1):
                if i >= robot_pos[0]:
                    continue
                item = warehouse[i]
                if item[robot_pos[1]] == "#":
                    break
                if item[robot_pos[1]] == ".":
                    warehouse[i][robot_pos[1]] = "O"
                    found = True
                    break
            if found:
                warehouse[robot_pos[0] - 1][robot_pos[1]] = "@"
                warehouse[robot_pos[0]][robot_pos[1]] = "."
    if move == "v":
        if warehouse[robot_pos[0] + 1][robot_pos[1]] == ".":
            warehouse[robot_pos[0] + 1][robot_pos[1]] = "@"
            warehouse[robot_pos[0]][robot_pos[1]] = "."
        elif warehouse[robot_pos[0] + 1][robot_pos[1]] == "O":
            found = False
            for i, item in enumerate(warehouse):
                if i <= robot_pos[0]:
                    continue
                if item[robot_pos[1]] == "#":
                    break
                if item[robot_pos[1]] == ".":
                    warehouse[i][robot_pos[1]] = "O"
                    found = True
                    break
            if found:
                warehouse[robot_pos[0] + 1][robot_pos[1]] = "@"
                warehouse[robot_pos[0]][robot_pos[1]] = "."
    if move == "<":
        if warehouse[robot_pos[0]][robot_pos[1] - 1] == ".":
            warehouse[robot_pos[0] ][robot_pos[1] - 1] = "@"
            warehouse[robot_pos[0]][robot_pos[1]] = "."
        elif warehouse[robot_pos[0]][robot_pos[1] - 1] == "O":
            found = False
            for i in range(len(warehouse[robot_pos[0]]), -1, -1):
                if i > robot_pos[1]:
                    continue
                item = warehouse[robot_pos[0]][i]
                if item == "#":
                    break
                if item == ".":
                    warehouse[robot_pos[0]][i] = "O"
                    found = True
                    break
            if found:
                warehouse[robot_pos[0] ][robot_pos[1] - 1] = "@"
                warehouse[robot_pos[0]][robot_pos[1]] = "."
    if move == ">":
        if warehouse[robot_pos[0]][robot_pos[1] + 1] == ".":
            warehouse[robot_pos[0]][robot_pos[1] + 1] = "@"
            warehouse[robot_pos[0]][robot_pos[1]] = "."
        elif warehouse[robot_pos[0]][robot_pos[1] + 1] == "O":
            found = False
            for i, item in enumerate(warehouse[robot_pos[0]]):
                if i <= robot_pos[1]:
                    continue
                if item == "#":
                    break
                if item == ".":
                    warehouse[robot_pos[0]][i] = "O"
                    found = True
                    break
            if found:
                warehouse[robot_pos[0]][robot_pos[1] + 1] = "@"
                warehouse[robot_pos[0]][robot_pos[1]] = "."
    #print(get_str_rep(warehouse, f"Move {move}:"))
    #print(robot_pos)
    #input()

gps_sum = 0

for i in range(len(warehouse)):
    for j in range(len(warehouse[i])):
        if warehouse[i][j] == "O":
            gps_sum += 100 * i + j

print(gps_sum)