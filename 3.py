scores = []
result = int(input())
while result != 0:
    scores.append(result)
    result = int(input())
k= sum(scores)/len(scores)
print(k)