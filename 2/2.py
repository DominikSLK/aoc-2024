def distance(a, b):
    if a < b:
        return b - a
    else:
        return a - b

def is_dec_or_inc(a):
    if a[0] < a[-1]:
        b = list(a)
        b.sort()
        if a == b:
            return True
        else:
            return False
    else:
        b = list(a)
        b.sort()
        b.reverse()
        if a == b:
            return True
        else:
            return False

def is_safe(report: list):
    if not is_dec_or_inc(report):
        return False
    for i in range(1, len(report)):
        if i == len(report):
            return True
        dist = distance(report[i-1], report[i]) 
        if dist > 3 or dist < 1:
            return False
    return True

def is_safe2(report: list):
    if is_safe(report):
        return True
    for i in range(len(report)):
        a = report[:i] + report[i+1:]
        if is_safe(a):
            return True
    return False

reports = []
count = 0
count2 = 0

with open("b.txt") as f:
    for line in f.readlines():
        line = line.strip()
        a = [int(i) for i in line.split()]
        reports.append(a)

for i in reports:
    if is_safe(i):
        count += 1
    if is_safe2(i):
        count2 += 1

print(count)
print(count2)