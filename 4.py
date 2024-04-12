def find_cons_sum(X):
    sums = []
    for i in range(1, X+1):
        summ = 0
        for j in range(1, i+1):
            summ += j
        sums.append(summ)
    return sums

X = 20
result = find_cons_sum(X)
print(result)