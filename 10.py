def is_perfect(num):
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    return sum(divisors) == num

N = int(input("Введите число N: "))

perfect_numbers = []
for i in range(2, N+1):
    if is_perfect(i):
        perfect_numbers.append(i)

print("Совершенные числа не превышающие", N, "в порядке возрастания:", perfect_numbers)