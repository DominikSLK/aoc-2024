with open("b.txt", "r") as f:
    a = f.read().replace("\n", "")

b = a.split("mul(")
for i in range(len(b)):
    b[i] = b[i].split(")")[0]

result = 0

for i in b:
    try:
        int(i.replace(",", ""))
        result += int(i.split(",")[0]) * int(i.split(",")[1])
    except:
        pass

print(result)