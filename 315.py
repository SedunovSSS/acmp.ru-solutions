def check(string):
    if len([0 for i in string if i not in ascii]) > 0:
        return -1
    max_sys = 2
    for i in string:
        if ascii.index(i) + 1 > max_sys:
            max_sys = ascii.index(i) + 1
    return max_sys


ascii = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
string = input()
print(check(string))
