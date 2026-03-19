string = input()
length = len(string)
palindrome = string[::-1]
if string == palindrome:
  print(palindrome)
else:
  print("не палиндром")
