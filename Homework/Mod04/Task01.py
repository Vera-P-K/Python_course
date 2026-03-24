nums = list(map(float, input().split()))
u = len(set(nums))
res = ["1) Все числа равны", "3) Есть равные и неравные числа", "2) Все числа разные"]
print(res[0 if u == 1 else 2 if u == len(nums) else 1])
