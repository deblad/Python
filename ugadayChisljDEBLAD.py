# Это игра по угадыванию чисел
import random
# Мы подключили модуль random к программе
print ('Привет , как тебя зовут ?')
myName = input()
# поздоровались , спросили имя , игрок ввел свое имя 
print(myName+", я загадываю число от 1 до 20.")
chislo = random.randint(1,20)
# сказали игроку в каком диапозоне загадываем число и загадали его 
for i in range(3) :
    # даем три попытки 
    print (' Попробуй откадай. Введи число от 1 до 20')
    vybor = input()
    vybor = int(vybor)
    # игрок ыыел число , строку превели в число  записали в переменную 
    if chislo > vybor:
        print('Загаданное число больше')
    if chislo < vybor:
        print('Загаданное число меньше')
    if chislo == vybor:
        break 
# сравниваем числа , даем подсказку , прерываем попытки если игрок угадал число 
if chislo == vybor: 
    print ('Поздравляю! Ты откадал число')
if chislo != vybor:
    print('Увы! Вы проиграли)