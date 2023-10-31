def poker(cards):
    setted_cards = list(set(cards))
    if len(setted_cards) == 1:
        return 'Impossible'
    if cards.count(max(cards, key=cards.count)) == 4:
        return 'Four of a Kind'
    if len(setted_cards) == 2:
        if cards.count(setted_cards[0]) in [2, 3] and cards.count(setted_cards[1]) in [2, 3]:
            return 'Full House'
    if cards.count(max(cards, key=cards.count)) == 3:
        return 'Three of a Kind'
    if cards.count(max(cards, key=cards.count)) == 2:
        pairs = set([i for i in cards if cards.count(i) == 2])
        return 'Two Pairs' if len(pairs) == 2 else 'One Pair'
    if sorted(cards) == list(range(min(cards), max(cards)+1)):
        return 'Straight'
    return 'Nothing'


cards = list(map(int, input().split()))
print(poker(cards))
