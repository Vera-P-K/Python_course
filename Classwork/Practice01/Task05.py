prices = list(map(int, input("Введите цены через пробел ").split()))
k = int(input("Введите число рублей, с которых считается скидка "))
m = int(input("Введите число рублей-скидку "))

discount = [p - (p // k) * m if p >= k else p for p in prices]
print("Цены до:", prices)
print("Цены после:", discount)
