k, n = map(int, input().split())

page_number = (n - 1) // k + 1
line_number = (n - 1) % k + 1

print(page_number, line_number)