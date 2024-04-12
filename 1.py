scores = []
result = int(input())
while result != -1:
    scores.append(result)
    result = int(input())

winner = scores[0]
for score in scores:
    if score > winner:
        winner = score

print(winner)