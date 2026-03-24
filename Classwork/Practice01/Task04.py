input_data = input("Введите фразы через ';': ")
phrases = [phrase.strip() for phrase in input_data.split(';')]
lengths = [len(phrase.split()) for phrase in phrases]
print("Исходный список:", phrases)
print("Количество слов во фразах:", lengths)
