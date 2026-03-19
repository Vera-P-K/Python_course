number = input("Введите номер телефона")
for char in number:
    if char.isdigit():
      print(char, end="")
