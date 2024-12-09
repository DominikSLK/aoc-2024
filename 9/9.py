with open("b.txt") as f:
    a = f.read().strip()

aa = []

j = 0
for i, c in enumerate(a):
    if i % 2 == 0:
        for i in range(int(c)):
            aa.append(str(j))
        j += 1
    else:
        for i in range(int(c)):
            aa.append(".")

l = len("".join(aa).replace(".", ""))

for j in range(len(aa)-1, -1, -1):
    if aa[j] != ".":
        try:
            ii = aa.index(".")
            aa[ii] = aa[j]
            aa[j] = "."
        except:
            break

checksum = 0
for i, c in enumerate(aa[1:l+1]):
    if c == ".":
        break
    checksum += int(i) * int(c)

print(checksum)