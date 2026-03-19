a = float(input())
b = float(input())
c = float(input())
if (b <= a <= c) or (c <= a <= b):
    middle = a
elif (a <= b <= c) or (c <= b <= a):
    middle = b
else:
    middle = c
print(middle)
