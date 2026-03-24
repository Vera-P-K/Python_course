number = int(input())
print(f"Двоичная: {bin(number)[2:]}\nВосьмеричная: {oct(number)[2:]}\nШестнадцатеричная: {hex(number)[2:].upper()}" if number > 0 else "Неверный ввод")
