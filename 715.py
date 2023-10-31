n, m = map(int, input().split())
positive = [input() for _ in range(n)]
input()
negative = [input() for _ in range(n)]
true_negative = [str(i).replace('B', '_').replace('W', 'B').replace('_', 'W') for i in positive]
print(len([0 for a, b in zip(negative, true_negative) for c, d in zip(a, b) if c != d]))
