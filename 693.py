def check(string1: str, string2: str):
    string1 = sorted(list(string1.lower()))
    string2 = sorted(list(string2.lower()))
    return 'Yes' if string1 == string2 else 'No'


string1, string2 = input().split()
print(check(string1, string2))
