string = input()
zeros = string.count('0')
ones = string.count('1')
if zeros == ones:
    print("yes")
else:
    print("no")
