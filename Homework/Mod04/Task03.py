def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)

try:
    a, b = map(int, input("Введите два числа: ").split())
    print(f"НОД {a} и {b} равен: {gcd(a, b)}")
except:
    print("Ошибка ввода!")
