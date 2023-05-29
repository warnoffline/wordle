import random
# print('Введите свое значение:')
# print('1 - Камень', '2 - Ножницы', '3 - Бумага', sep="\n")
# player = int(input())
# comp = random.randrange(1, 4)
# if (player == 1 and comp == 2) or (player == 2 and comp == 3):
#     print(player, comp, 'Вы выиграли', sep="\n")
# elif (player == 1 and comp == 3) or (player == 2 and comp == 1):
#     print(player, comp, 'Выиграл компьютер', sep="\n")
# elif (player == comp):
#     print(player, comp, 'Ничья', sep="\n")
# else:
#     print('Введите корректное число')

# print('Введите длину пароля:')
# n = int(input())
# al = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&*"
# par = ''
# for i in range(n):
#     par += random.choice(al)
# print(par)

# tr = True
# while tr:
#     al = ['компьютер', 'телефон', 'город', 'яблоко']
#     k = 0
#     n = 0
#     dn = True
#     ugadan = ''
#     slovo = random.choice(al)
#     print(f'Вам загадали слово из {len(slovo)} букв!', 'У вас есть право на 4 ошибки', sep='\n')
#     while dn:
#         print(f'Вы угадали буквы: {ugadan}')
#         print('Ваша буква: ')
#         a = input()
#         if a in slovo and (not(a in ugadan)):
#             print('Вы угадали букву!')
#             ugadan += a
#             k += 1
#             if k == len(slovo):
#                 dn = False
#         elif a in ugadan:
#             print('Вы уже называли эту букву!')
#         else:
#             n += 1
#             print(f'Вы не угадали букву! Вы ошиблись: {n}')
#             if n == 4:
#                 dn = False
#     if k == len(slovo):
#         print('Вы угадали слово!')
#     else:
#         print('Вы не угадали слово!')
#     print(f'Это слово - {slovo}')
#     print('Начать заново?')
#     zanovo = input()
#     if zanovo == 'Да' or zanovo == 'да' or zanovo == '+':
#         tr = True
#     else:
#         tr = False


# from playsound import playsound
# print('Введите время, когда вас разбудить:')
# hh = int(input('Час: '))
# mm = int(input('Минут: '))
# br = False
# for i in range(25):
#     for j in range(60):
#         print(f'Время: {i} часов {j} минут')
#         if hh == i and mm == j:
#             print('ПРОСЫПАЙТЕСЬ')
#             playsound('C:/Users/hamet/Downloads/Xiaomi Mi Orange.mp3')
#             br = True
#             break
#     if br:
#         break

# def Words_Game(used_words):
#     import random
#     wordlist = []
#     f = open("1.txt", encoding='utf-8')
#
#     rand_word = random.choice(wordlist)
#
#     while rand_word in used_words:
#         rand_word = random.choice(wordlist)
#     mistakes = 5
#     print(wordlist)
#     wrong_ans = 0
#
#     used_letters = []
#
#     words_len_secret = "_" * len(rand_word)
#
#     while wrong_ans < mistakes and words_len_secret != rand_word:
#         print("Использованные буквы: ", used_letters)
#         print("Ваше слово: ", words_len_secret)
#
#         player_letter = input()
#
#         while player_letter in used_letters:
#             print("Вы уже выбирали эту букву:", player_letter)
#             player_letter = input()
#
#         used_letters.append(player_letter)
#
#         if player_letter in rand_word:
#             print("Вы угадали букву!", player_letter)
#             letters_in_word = ''
#             for i in range(len(rand_word)):
#                 if player_letter == rand_word[i]:
#                     letters_in_word += player_letter
#                 else:
#                     letters_in_word += words_len_secret[i]
#             words_len_secret = letters_in_word
#         else:
#             print("Такой буквы нет в слове", player_letter)
#             wrong_ans += 1
#
#     if wrong_ans == mistakes:
#         print("Ты проиграл!")
#     else:
#         print("Ты угадал слово!")
#
#     print("Тебе загадали слово: ", rand_word)
#     return rand_word
#
#
# used_words = []
#
# used_words.append(Words_Game(used_words))
#
# while True:
#     if len(used_words) == 10:
#         print("Слова закончились")
#         break
#     print("Повторить? +/-")
#     x = input()
#     if x == "+":
#         used_words.append(Words_Game(used_words))
#     else:
#         break

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