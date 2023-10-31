nums, smbls = ['1', '2', '3', '4', '5', '6', '7', '8'], ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
m = [[s+n for s in smbls] for n in nums]

def check(m, cord_1, cord_2):
    cord_1_i = None
    cord_1_j = None
    cord_2_i = None
    cord_2_j = None

    for index, i in enumerate(m):
        if cord_1 in i:
            cord_1_i = index
            cord_1_j = i.index(cord_1)
        if cord_2 in i:
            cord_2_i = index
            cord_2_j = i.index(cord_2)

    if cord_1_i is None or cord_1_j is None or cord_2_i is None or cord_2_j is None:
        return 'ERROR'

    if (abs(cord_1_i - cord_2_i) == 2 and abs(cord_1_j - cord_2_j) == 1) or (abs(cord_1_i - cord_2_i) == 1 and abs(cord_1_j - cord_2_j) == 2):
        return 'YES'
    else:
        return 'NO'

try:
    cord_1, cord_2 = input().split('-')
    print(check(m, cord_1=cord_1, cord_2=cord_2))
except:
    print('ERROR')