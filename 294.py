k1, i1, m1 = map(int, input().split())
k2, i2, m2 = map(int, input().split())

bolt_count = int(k1 - k1 * i1 / 100)
gayka_count = int(k2 - k2 * i2 / 100)

used = min(bolt_count, gayka_count)

print(int(k1 - used) * m1 + (k2 - used) * m2)
