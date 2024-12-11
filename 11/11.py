def blink(stones):
    new_stones = []
    for i in range(len(stones)):
        if stones[i] == "0":
            new_stones.append("1")
        elif len(stones[i]) % 2 == 0:
            new_stones.append(stones[i][0:len(stones[i])//2])
            new_stones.append(str(int(stones[i][len(stones[i])//2:])))
        else:
            new_stones.append(str(int(stones[i]) * 2024))
    return new_stones

with open("b.txt") as f:
    a = f.read().strip().split()

for i in range(25):
    a = blink(a)

print(len(a))