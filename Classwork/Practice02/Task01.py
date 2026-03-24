import re

def find_correct_dates(text):
    pattern = r'20\d{2}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\d|3[01]) (?:[01]\d|2[0-3]):[0-5]\d:[0-5]\d'
    
    matches = re.findall(pattern, text)
    return matches

text = """
Событие произошло 2023-10-25 14:30:05, а следующее 
ожидается 2024-02-29 09:00:00. Неверные даты: 1999-12-31 23:59:59, 
2025-13-01 10:00:00 или 2025-10-32 10:00:00 не попадут.
Также должны попасть 2000-12-31 23:59:59, 2001-01-01 00:00:01.
"""

found_correct_dates = find_correct_dates(text)
print(found_correct_dates)
