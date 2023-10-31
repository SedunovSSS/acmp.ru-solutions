def check(values):
    for j, i in enumerate(values):
        if i <= 437:
            return f'Crash {j+1}'
    return 'No crash'


n = int(input())
values = list(map(int, input().split()))
print(check(values))
