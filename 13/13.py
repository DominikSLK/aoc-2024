
claws = []

with open("b.txt") as f:
    i = 0
    for line in f.readlines():
        line = line.strip()
        if line == "":
            i += 1
            continue
        elif line.startswith("Button"):
            try:
                claws[i].append([int(line.split(": ")[1].split(", ")[0].split("+")[1]), int(line.split(": ")[1].split(", ")[1].split("+")[1])])
            except:
                claws.append([[int(line.split(": ")[1].split(", ")[0].split("+")[1]), int(line.split(": ")[1].split(", ")[1].split("+")[1])]])
        elif line.startswith("Prize"):
            claws[i].append([int(line.split(": ")[1].split(", ")[0].split("=")[1]), int(line.split(": ")[1].split(", ")[1].split("=")[1])])

def calculate(btnax, btnay, btnbx, btnby, prizex, prizey):
    for b in range(0, prizex // btnbx + 1):
        if (prizex - btnbx * b) % btnax == 0:
            a = (prizex - btnbx * b) // btnax
            if btnay * a + btnby * b == prizey:
                return (a, b)
    return None

tokens = 0
for i in claws:
    a = calculate(i[0][0], i[0][1], i[1][0], i[1][1], i[2][0], i[2][1])
    if a != None:
        tokens += a[0] * 3 + a[1]

print(tokens)