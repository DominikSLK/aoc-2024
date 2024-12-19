def is_valid(towel: str, patterns):
    if towel == "":
        return True

    for pattern in patterns:
        if towel.startswith(pattern):
            if is_valid(towel[len(pattern):], patterns):
                return True

    return False

towels = []

with open("input.txt") as f:
    for line in f.readlines():
        line = line.strip()
        if "," in line:
            patterns = line.split(", ")
            continue
        if line != "":
            towels.append(line)

valid = 0

for towel in towels:
    if is_valid(towel, patterns):
        valid += 1

print(valid)