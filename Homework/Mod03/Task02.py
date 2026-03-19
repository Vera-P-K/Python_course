number = int(input())
if number > 0:
  print(f"Двоичная: {bin(number)[2:]}")
  print(f"Восьмеричная: {oct(number)[2:]}")
  print(f"Шестнадцатеричная: {hex(number)[2:].upper()}")
else:
  print("Неверный ввод")
