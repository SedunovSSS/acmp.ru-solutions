m, n = map(int, input().split())
f, s = list(map(int, input().split())), list(map(int, input().split()))
 
print(1 if sorted(list(set(f))) == sorted(list(set(s))) else 0)