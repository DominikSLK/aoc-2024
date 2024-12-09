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

def find_consecutive_dots(arr, n):
    result = []
    for i in range(len(arr)-n+1):
        if all(arr[i+j] == '.' for j in range(n)):
            result.append(i)
    return result

c = 0
last = None
for j in range(len(aa)-1, -1, -1):
    if aa[j] != ".":
        try:
            if aa[j] == last:
                c += 1
            else:
                if last != None:
                    try:
                        dot_start = find_consecutive_dots(aa, c)[0]
                    except IndexError:
                        c = 0
                        last = aa[j]
                    for i in range(dot_start, dot_start+c):
                        aa[i] = last

                    for i in range(c):
                        aa[len(aa)-1-aa[::-1].index(last)] = "."

                c = 1
                last = aa[j]
        except:
            pass

checksum = 0
for i, c in enumerate(aa):
    if c == ".":
        continue
    checksum += int(i) * int(c)

print(checksum)