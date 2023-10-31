def find_number(N):
    if N == 0:
        return 10
    elif N < 10:
        return N
    else:
        result = ""
        for i in range(9, 1, -1):
            while N % i == 0:
                result += str(i)
                N //= i
        if N > 10:
            return -1
        else:
            return int(result[::-1])


N = int(input())
result = find_number(N)
print(result)