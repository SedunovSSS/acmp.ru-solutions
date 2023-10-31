n, facts = input().split()
n = int(n)
result = 1

for i in range(n, 0, -len(facts)):
    result *= n
    n -= len(facts)

print(result)