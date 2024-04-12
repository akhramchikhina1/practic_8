while True:
    num = input("Введите число: ")
    if num.isdigit():
        print("Введено целое число:", num)
        break
    else:
        print("Ошибка. Попробуйте еще раз.")