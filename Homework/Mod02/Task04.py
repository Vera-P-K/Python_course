def to_base(n, b):
    digits = "0123456789ABCDEF"
    return to_base(n // b, b) + digits[n % b] if n > b - 1 else digits[n]

n = input("Число: ")
if n.isdigit() and int(n) > 0:
    num = int(n)
    for name, base in [("Двоичная", 2), ("Восьмеричная", 8), ("Шестнадцатеричная", 16)]:
        print(f"{name}: {to_base(num, base)}")
else:
    print("Неверный ввод")
