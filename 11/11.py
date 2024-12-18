from collections import defaultdict

def blink(stones):
    new_stones = defaultdict(int)
    for stone in stones:
        if stone == 0:
            new_stones[1] += stones[stone]
        elif len(str(stone)) % 2 == 0:
            mid = len(str(stone)) // 2
            left, right = int(str(stone)[:mid]), int(str(stone)[mid:])
            new_stones[left] += stones[stone]
            new_stones[right] += stones[stone]
        else:
            new_stones[stone * 2024] += stones[stone]
    return new_stones

stones = defaultdict(int)

with open("b.txt") as f:
    for i in f.read().strip().split():
        stones[int(i)] += 1

for i in range(75):
    if i == 25:
        print(sum(stones.values()))
    stones = blink(stones)

print(sum(stones.values()))