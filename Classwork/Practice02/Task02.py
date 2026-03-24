import re
text = "Варианты адресов: e-mail@site.ru, task_test@work.com или info@firma.org"

email_pattern = r'[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+'
emails = re.findall(email_pattern, text)

print("Найденные email-адреса:")
for email in emails:
    print(email)
