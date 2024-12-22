def mix(value, secret):
    return value ^ secret

def prune(secret):
    return secret % 16777216

def next_secret(secret):
    secret = prune(mix(secret * 64, secret))
    secret = prune(mix(secret // 32, secret))
    secret = prune(mix(secret * 2048, secret))
    return secret

buyers = []
with open("input.txt") as f:
    for line in f.readlines():
        buyers.append(int(line.strip()))

for i, buyer in enumerate(buyers):
    for j in range(2000):
        buyers[i] = next_secret(buyers[i])

print(sum(buyers))