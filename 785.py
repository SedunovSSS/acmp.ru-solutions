a, b = map(int, input().split())
print(*[i for i in range(a, b+1) if str(i**2)[len(str(i**2))-len(str(i)):] == str(i)])