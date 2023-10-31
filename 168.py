num = input()

nrn = ''
i = 1

while not (num in nrn):
    nrn += str(i)
    i += 1

print(nrn.index(num)+1)
