from random import randint
import os
def great_pole():
    print("    1    2    3  ")
    print("   _____________")
    print(" 1 | {} | {} | {} |".format(pole[0], pole[1], pole[2],))
    print("   -------------")
    print(" 2 | {} | {} | {} |".format(pole[3], pole[4], pole[5],))
    print("   -------------")
    print(" 3 | {} | {} | {} |".format(pole[6], pole[7], pole[8],))
    print("   -------------")

name1, name2 = "",""
pole = [" "," "," "," "," "," "," "," "," "]
b = 0

while True:
    print("© 2019. St.")
    print("Программа для игры в крестики и нолики")
    print("----------------------------------------------------")
    if name1 == "" and name2 == "":
        name1 = input("Введите имя первого игрока: ")
        name2 = input("Введите имя второго игрока: ")

    great_pole()
    if b==0:
        print("Ходит игрок {}".format(name1))
    else:
        print("Ходит игрок {}".format(name2))
    xy = input("Введите координаты поля: ")
    if 0 == b:
        if xy == "11" and pole[0] == " ":
            pole[0] = "+"; b = 1
        if xy == "12" and pole[1] == " ":
            pole[1] = "+"; b = 1
        if xy == "13" and pole[2] == " ":
            pole[2] = "+"; b = 1
        if xy == "21" and pole[3] == " ":
            pole[3] = "+"; b = 1
        if xy == "22" and pole[4] == " ":
            pole[4] = "+"; b = 1
        if xy == "23" and pole[5] == " ":
            pole[5] = "+"; b = 1
        if xy == "31" and pole[6] == " ":
            pole[6] = "+"; b = 1
        if xy == "32" and pole[7] == " ":
            pole[7] = "+"; b = 1
        if xy == "33" and pole[8] == " ":
            pole[8] = "+"; b = 1
    else:
        if xy == "11" and pole[0] == " ":
            pole[0] = "O"; b = 0
        if xy == "12" and pole[1] == " ":
            pole[1] = "O"; b = 0
        if xy == "13" and pole[2] == " ":
            pole[2] = "O"; b = 0
        if xy == "21" and pole[3] == " ":
            pole[3] = "O"; b = 0
        if xy == "22" and pole[4] == " ":
            pole[4] = "O"; b = 0
        if xy == "23" and pole[5] == " ":
            pole[5] = "O"; b = 0
        if xy == "31" and pole[6] == " ":
            pole[6] = "O"; b = 0
        if xy == "32" and pole[7] == " ":
            pole[7] = "O"; b = 0
        if xy == "33" and pole[8] == " ":
            pole[8] = "O"; b = 0




    # kol = int(input('Введите количество упрощений : '))
    # prost = int(input('Введите простоту ( от 1 до 4 ) : '))
    # list = []
    # for i in range (1,kol+1):
    #     ran1 = randint(1,20)
    #     ran2 = randint(1,50)
    #     if prost == 1:
    #         u_ran = randint(2, 5)
    #     if prost == 2:
    #         u_ran = randint(2, 10)
    #     if prost == 3:
    #         u_ran = randint(2, 15)
    #     if prost == 4:
    #         u_ran = randint(2, 20)
    #     list.append(ran1)
    #     list.append(ran2)
    #     list.append('')
    #     print("     ",ran1 * u_ran)
    #     print("     ",'---',"       (",i,")")
    #     print("     ",ran2 * u_ran)
    #     print()
    # print(list)
    # print("----------------------------------------------------")
    # kol1 = input('Нажмите клавишу Enter')
    os.system('cls||clear')