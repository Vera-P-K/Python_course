n = int(input("Введите количество имен: "))
names = []
for _ in range(n):
    names.append(input("Введите имя: "))
uni = list({len(name): name for name in reversed(names)}.values())[::-1]
print("Исходный список:", names)
print("Список с уникальной длиной:", uni)
