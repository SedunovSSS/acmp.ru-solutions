values = [input() for _ in range(4)]
team = ''

for i in values: team = i if 'Team' in i else team

values_without_team = sorted([i for i in values if i != team])

result = team + ': '

for j, i in enumerate(values_without_team):
    result = result + i + ', ' if j < len(values_without_team) - 1 else result + i

print(result)