def check_numbers(nums):    
    unique_nums = set(nums)
    if len(unique_nums) == 1:
        return "1) Все числа равны"
    elif len(unique_nums) == len(nums):
        return "2) Все числа разные"
    else:
        return "3) Есть равные и неравные числа"
input_data = list(map(float, input().split()))
print(check_numbers(input_data))
