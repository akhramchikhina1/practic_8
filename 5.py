def is_perfect(num):
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    return sum(divisors) == num

N = int(input("Введите число N: "))

count_perfect = 0
for i in range(2, N+1):
    if is_perfect(i):
        count_perfect += 1

print("Количество совершенных чисел в интервале от 2 до", N, ":", count_perfect)