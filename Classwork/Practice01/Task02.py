n = int(input("Введите число: "))
nums = list(range(n, n**2 + 1))
roots = [round(x**0.5, 2) for x in nums]

print(f"Числа: {nums}")
print(f"Корни: {roots}")
