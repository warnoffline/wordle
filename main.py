import random

tr = True
while tr:
    s = []
    f = open('1.txt', encoding='utf-8')
    for i in f:
        s.append(f.readline())
    words = [i.strip() for i in s]
    mt = 6
    used_word = random.choice(words)
    al_letter = []
    ul = []
    dn = True
    while dn:
        a = input('Введите слово: ')
        used_letter = []
        if len(a) != 5:
            print('Введите корректное слово!')
            continue
        if a == used_word:
            print('Вы угадали слово!')
            print('Хотите продолжить игру? +/-')
            n = input()
            if n != '+':
                tr = False
                break
        for i in range(len(used_word)):
            for j in range(len(used_word)):
                if (a[i] == used_word[j] and i == j):
                    print(f'{a} Правильно расположена буква: {a[i]}')
                    ul.append(a[i])
                    break
                elif (a[i] == used_word[j] and not(a[i] in used_letter)):
                    print(f'{a} Неправильно расположена буква {a[i]}')
                    used_letter.append(a[i])
                    ul.append(a[i])
                elif (a[i] == used_word[j] and not(a[i] in ul)):
                    ul.append(a[i])
            if not(a[i] in al_letter) and not(a[i] in ul):
                al_letter.append(a[i])

        print(f'Неправильные буквы: {al_letter} ')
        mt -= 1
        if mt == 0:
            dn = False
            print('Вы проиграли!')
            print(f'Это слово - {used_word}')
            print('Хотите продолжить игру? +/-')
            n2 = input()
            if n2 != '+':
                tr = False
