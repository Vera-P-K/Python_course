ef gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
try:    
    num1, num2 = map(int, input("Введите два числа через пробел: ").split())
    result = gcd(num1, num2)
    print(f"НОД чисел {num1} и {num2} равен: {result}")
except ValueError:
    print("Ошибка! Это не числа.")
