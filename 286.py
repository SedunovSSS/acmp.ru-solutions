from decimal import Decimal
a, b = Decimal(input()), Decimal(input())
result = '=' if a == b else '<' if a < b else '>'
print(result)
