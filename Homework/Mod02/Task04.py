def convert_number():
    user_input = input("Введите натуральное число: ")
    if not user_input.isdigit() or int(user_input) <= 0:
        print("Неверный ввод")
        return
    number = int(user_input)
    original_number = number
    def to_base(n, base):
        if n == 0:
            return "0"
        digits = "0123456789ABCDEF"
        result = ""
        while n > 0:
            result = digits[n % base] + result
            n //= base
        return result
    print(f"Двоичная: {to_base(original_number, 2)}")
    print(f"Восьмеричная: {to_base(original_number, 8)}")
    print(f"Шестнадцатеричная: {to_base(original_number, 16)}")
convert_number()
