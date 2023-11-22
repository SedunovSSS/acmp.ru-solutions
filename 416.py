s = input()
result = []

if chr(ord(s[0])+2) <= 'h' and chr(ord(s[0])+2) >= 'a':
    if chr(ord(s[1])+1) <= '8' and chr(ord(s[1])+1) >= '1':
        result.append(chr(ord(s[0])+2) + chr(ord(s[1])+1))
    if chr(ord(s[1])-1) <= '8' and chr(ord(s[1])-1) >= '1':
        result.append(chr(ord(s[0])+2) + chr(ord(s[1])-1))

if chr(ord(s[0])-2) <= 'h' and chr(ord(s[0])-2) >= 'a':
    if chr(ord(s[1])+1) <= '8' and chr(ord(s[1])+1) >= '1':
        result.append(chr(ord(s[0])-2) + chr(ord(s[1])+1))
    if chr(ord(s[1])-1) <= '8' and chr(ord(s[1])-1) >= '1':
        result.append(chr(ord(s[0])-2) + chr(ord(s[1])-1))

if chr(ord(s[0])+1) <= 'h' and chr(ord(s[0])+1) >= 'a':
    if chr(ord(s[1])+2) <= '8' and chr(ord(s[1])+2) >= '1':
        result.append(chr(ord(s[0])+1) + chr(ord(s[1])+2))
    if chr(ord(s[1])-2) <= '8' and chr(ord(s[1])-2) >= '1':
        result.append(chr(ord(s[0])+1) + chr(ord(s[1])-2))

if chr(ord(s[0])-1) <= 'h' and chr(ord(s[0])-1) >= 'a':
    if chr(ord(s[1])+2) <= '8' and chr(ord(s[1])+2) >= '1':
        result.append(chr(ord(s[0])-1) + chr(ord(s[1])+2))
    if chr(ord(s[1])-2) <= '8' and chr(ord(s[1])-2) >= '1':
        result.append(chr(ord(s[0])-1) + chr(ord(s[1])-2))

print(*sorted(result), sep='\n')
