domain = input() 
parts = domain.split('.')
for part in reversed(parts):
  print(part)
