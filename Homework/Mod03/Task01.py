s = input("Введите три числа через пробел ")
nums = sorted(list(map(int, s.split())))
print("Число посередине", nums[1])
