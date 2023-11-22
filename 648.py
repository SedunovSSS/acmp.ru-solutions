n = int(input())
cards = sorted(list(map(int, input().split())))
 
sum_shrek = sum(cards[n//2:n+1])
sum_croupye = sum(cards[0:n//2])
 
print(sum_shrek-sum_croupye)