domain = input()
while domain:
    domain, dot, part = domain.rpartition('.')
    print(part)
