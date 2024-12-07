a = []

with open("b.txt") as f:
    for line in f:
        a.append([i for i in line.strip()])

count = 0

for i in range(1, len(a)-1):
    for j in range(1, len(a[i])-1):
        if a[i][j] == "A":
            top_left = a[i-1][j-1]
            bottom_right = a[i+1][j+1]
            top_right = a[i-1][j+1]
            bottom_left = a[i+1][j-1]

            if (top_left == "M" and bottom_right == "S") or (top_left == "S" and bottom_right == "M"):
                if (top_right == "M" and bottom_left == "S") or (top_right == "S" and bottom_left == "M"):
                    count += 1

print(count)
