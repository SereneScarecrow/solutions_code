import re

with open('задание 1 хардкор.txt', 'r', encoding='utf-8') as f:
    full_text = f.read()
    clean_text = re.sub(r'[^а-яёА-я\d.,]',  ' ', full_text)
    words = clean_text.split()
    message = []
    for word in words:
        if words.count(word) < 10:
            message.append(word)
    print(' '.join(message))