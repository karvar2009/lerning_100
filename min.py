from random import randint
import os

while True:
    print("© 2019. Den")
    print("Программа для генерации заданий по упрощению дробей")
    print("Предназначена для учеников 5-х классов")
    print("----------------------------------------------------")
    kol = int(input('Введите количество упрощений : '))
    prost = int(input('Введите простоту ( от 1 до 4 ) : '))
    list = []
    for i in range (1,kol+1):
        ran1 = randint(1,20)
        ran2 = randint(1,50)
        if prost == 1:
            u_ran = randint(2, 5)
        if prost == 2:
            u_ran = randint(2, 10)
        if prost == 3:
            u_ran = randint(2, 15)
        if prost == 4:
            u_ran = randint(2, 20)
        list.append(ran1)
        list.append(ran2)
        list.append('')
        print("     ",ran1 * u_ran)
        print("     ",'---',"       (",i,")")
        print("     ",ran2 * u_ran)
        print()
    print(list)
    print("----------------------------------------------------")
    kol1 = input('Нажмите клавишу Enter')
    os.system('cls||clear')