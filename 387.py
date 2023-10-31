n = int(input())
m = [input().split('->') for _ in range(n)]
print(len([0 for l, r in m if l == r[0]]))