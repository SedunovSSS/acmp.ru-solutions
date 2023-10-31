_sum_ = 0
n = int(input())
vals = list(map(int, input().split()))
k = int(input())

for i in vals:
    _sum_ += min(i, k)

print(_sum_)
