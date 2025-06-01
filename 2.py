import random

# импортируем слова из nltk
# стремные, но я не нашла другой библиотеки
from nltk.corpus import words
vocabulary = [i for i in words.words('en') if len(i) > 3]


# функция для запуска игры
def game():
    # приветствие
    print("Welcome to the Spelling Bee")

    score = 0
    entered_words = []
    allowed_words = []

    # генерация букв
    alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    while not allowed_words:
        letters = random.choices(alph, k=7)
        main_letter = random.choice(letters)
        allowed_words = generate_letters(letters, main_letter)

    # вывод букв
    print(f"Today's letters are {''.join(letters)} and the letter of the day is {main_letter}\n"
          f"Feel free to press XXXXX when you're done playing")

    print(allowed_words)

    # игровой процесс
    user_word = input("Please enter a word: ").upper()
    while user_word != 'XXXXX' and allowed_words != entered_words:
        if check(user_word, letters, main_letter, allowed_words, entered_words):
            score1 = count_score(user_word)
            print(f"Cool! You found the word {user_word} and earned {score1} points!")
            entered_words.append(user_word)
            score += score1
        if not allowed_words == entered_words:
            user_word = input("Please enter a word: ").upper()

    # конец игры если введено XXXXX или перебраны все слова
    if user_word == 'XXXXX':
        print(f"Congrats! Your final score is {score}")
    elif allowed_words == entered_words:
        print(f"Congrats! You found all words. Your final score is {score}")

    return


# проверка на ограничения
def check(entered_word, letters, main_letter, allowed_words, entered_words):
    # проверка на наличие чисел
    if not any(ch.isalpha() for ch in entered_word):
        print("Sorry, those clearly aren't letters")
        return False

    # проверка на наличие лишних букв
    if len(set(entered_word) - set(letters)):
        extra_letters = list(set(entered_word) - set(letters))
        if len(extra_letters) == 1:
            print(f"Sorry, letter {extra_letters[0]} isn't one of today's letters")
        else:
            extra_letters = ', '.join(extra_letters)
            print(f"Sorry, letters {extra_letters} aren't one of today's letters")
        return False

    # проверка на наличие буквы дня
    if main_letter not in entered_word:
        print("Sorry, the letter of the day is missing")
        return False

    # проверка на длину
    if len(entered_word) < 4:
        print("Sorry, this word is too short")
        return False

    # проверка на наличие слова в словаре
    if entered_word not in allowed_words:
        print("Sorry, but we don't know this word yet")
        return False

    # проверка на то, было ли слово введено ранее
    if entered_word in entered_words:
        print("Sorry, you've already used this word. Try another")
        return False

    return True


# подсчет очков
def count_score(entered_word):
    # очки за слово длинее 3 и короче 8 букв
    if 3 < len(entered_word) < 8:
        return len(entered_word)

    # очки за слово длиннее 8 букв
    if len(entered_word) >= 8:
        return len(entered_word) * 2

# создание словаря допустимых слов
def generate_letters(letters, main_letter, vocab=vocabulary):
    allowed_words = []
    for i in vocab:
        i = i.upper()
        if set(i) <= set(letters):
            if main_letter in i:
                allowed_words.append(i)

    return allowed_words if len(allowed_words) >= 5 else []


game()
