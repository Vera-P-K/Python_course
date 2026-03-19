a = float(input("Введите длину стороны: "))
perimeter = 2 * (a + a)
area = a * a
diagonal = (a**2 + a**2)**0.5
print(f"Периметр: {round(perimeter, 2)}")
print(f"Площадь: {round(area, 2)}")
print(f"Диагональ: {round(diagonal, 2)}")
