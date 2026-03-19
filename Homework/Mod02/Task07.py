s = input("Введите строку")
if not s:
    print(0)
else:
    count = 0
    first_char = s[0]
    for char in s:
        if char == first_char:
            count += 1
        else:
            break        
    print(count)
