def get_zeroes_group(line):
    return sorted(line.split('1'))[-1]


inp = input()
print(len(get_zeroes_group(inp)))