import random


words_bank = ['автострада', 'бензин', 'инопланетянин', 'самолет',
             'библиотека', 'шайба', 'олимпиада']

secret_word = random.choice(words_bank)
print(secret_word)

gamer_word = ['*'] * len(secret_word)
print(''.join(gamer_word))

errors_cnt = 0

while True:
    letter = input('введи ОДНУ русскую букву: ')
    #letter validation ord(letter) --> unicode code, re
    if len(letter) != 1:
        continue #возвращает вначало цикла

    if letter in secret_word:
        #brute force
        idx = 0
        for symbol in secret_word:
            if symbol == letter:
                gamer_word[idx] = letter
        idx += 1

    else:
        errors_cnt += 1
        print('ошибок допущено', errors_cnt)
        if errors_cnt == 8:
            print('вы проиграли')
            break

    print(''.join(gamer_word))