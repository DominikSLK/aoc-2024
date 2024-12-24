values = {}
operations = {}

with open("input.txt") as f:
    for line in f.readlines():
        line = line.strip()
        if ":" in line:
            values[line.split(": ")[0]] = int(line.split(": ")[1])
        elif "->" in line:
            operations[line.split(" -> ")[1]] = line.split(" -> ")[0]

def calculate(name):
    if name in values:
        return values[name]
    else:
        operation = operations[name]
        if "AND" in operation:
            values[name] = calculate(operation.split(" AND ")[0]) & calculate(operation.split(" AND ")[1])
        elif "XOR" in operation:
            values[name] = calculate(operation.split(" XOR ")[0]) ^ calculate(operation.split(" XOR ")[1])
        elif "OR" in operation:
            values[name] = calculate(operation.split(" OR ")[0]) | calculate(operation.split(" OR ")[1])
        return values[name]
        
for operation in operations.keys():
    calculate(operation)

v = {}
for value in values.keys():
    if value.startswith("z"):
        v[value] = values[value]
v = dict(sorted(v.items()))

b = ""
for value in v.values():
    b = str(value) + b

print(int(b, 2))