import random

word_list = ["apple", "brain", "crane", "dodge", "eagle", "flame", "grape", "house", "igloo", "joker"]

def play_wordle():
    secret_word = random.choice(word_list)
    max_attempts = 6

    print("Добро пожаловать в Wordle! У вас есть 6 попыток, чтобы угадать секретное слово.")

    for attempt in range(max_attempts):
        guess = input(f"Попытка {attempt + 1}: ").lower()
        feedback = ""

        for i in range(len(secret_word)):
            if guess[i] == secret_word[i]:
                feedback += "●"
            elif guess[i] in secret_word:
                feedback += "○"
            else:
                feedback += "□"
        
        print(f"Результат: {feedback}")

        if guess == secret_word:
            print("Поздравляю! Вы угадали слово!")
            break
    else:
        print(f"Вы проиграли! Секретное слово было: {secret_word}")

    if input("Хотите сыграть снова? (да/нет): ").lower() == 'да':
        play_wordle()

play_wordle()
