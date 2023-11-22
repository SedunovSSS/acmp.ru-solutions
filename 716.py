n = int(input())
_min, _max = 30, 4000
first = float(input())

for i in range(1, n):
    frequency, state = input().split()
    frequency = float(frequency)
    mean = (first + frequency) / 2
    if state == 'closer':
        if frequency > first and _min < mean:
            _min = mean
        if frequency < first and _max > mean:
            _max = mean
    if state == 'further':
        if frequency < first and _min < mean:
            _min = mean
        if frequency > first and _max > mean:
            _max = mean
    first = frequency

print(_min, _max)
