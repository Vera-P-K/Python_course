def power(a, n):
    if n == 0: return 1
    return power(a * a, n // 2) if n % 2 == 0 else a * power(a, n - 1)

try:
    a, n = map(float, input("Введите числа a и n через пробел: ").split())
    print(f"Результат: {power(a, int(n))}")
except:
    print("Ошибка ввода")
