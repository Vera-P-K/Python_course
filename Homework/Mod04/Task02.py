def fast_power(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        return fast_power(a * a, n // 2)
    else:
        return a * fast_power(a, n - 1)
try:
    a, n = map(float, input("Введите число и степень через пробел: ").split())
    result = power(a, int(n))
    print(f"Результат: {result}")
except ValueError:
    print("Пожалуйста, введите корректные числа.")
