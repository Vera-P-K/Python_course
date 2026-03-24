string = input("Введите число, состоящее из 0 и 1: ")
print("yes" if string.count('0') == string.count('1') else "no")
