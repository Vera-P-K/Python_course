domain = input() 
parts = []
current_domain = domain
while True:
    dot_index = current_domain.rfind('.')
    if dot_index == -1:
        parts.append(current_domain)
        break
    parts.append(current_domain[dot_index + 1:])
    current_domain = current_domain[:dot_index]
for part in (parts):
    print(part)
