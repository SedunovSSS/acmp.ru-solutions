n, k = map(int, input().split())
print(k//n, k%n, (n-(k%n) if k % n != 0 else 0))