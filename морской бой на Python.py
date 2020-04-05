from random import randint
from time import sleep
'''
KOLICHECTBO_KOPABLIKOB --- количество корабликов(однопалубные)
TWO_KOPABLIK --- количество корабликов(двухпалубные)
TRETIY_KORABLIK --- количество корабликов(трёхпалубные)
MAX_KOPABLIK --- количество кораблей (четырёхпалубные)
'''
KOLICHECTBO_KOPABLIKOB = 4
TWO_KOPABLIK = 3
TRETIY_KORABLIK = 2
MAX_KOPABLIK = 1
field = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

def pole ():
    def tr(x1, y1):
        try:
            COVID19 = field[x1][y1] == 0
        except IndexError:
            COVID19 = True
        return COVID19

    def tro(x1, y1):
        try:
            COVID19 = field[x1][y1] == 0
        except IndexError:
            COVID19 = False
        return COVID19

    """ расставляем однопалубные корабли, их 4 штуки, соответственно
    мы случайным образом находим координаты и проверям чтоб рядом небыло 
    других кораблей. Алгоритм простой и по логике расстановку кораблей 
    можно было бы сделать процедурой, но пока сделаем в основном коде"""
    kol_KRB = KOLICHECTBO_KOPABLIKOB  # количество корабликов
    while kol_KRB:  # ведь когда станет 0, то по языку Python это False! ➝ А-а-а-а
        x, y = randint(0, 9), randint(0, 9)  # можно и так писать - в одну строку
        # при x >=1 и х <= 8 и y >=1 и y <= 8 проверям все по кругу относительно точки
        # 1 = x-1,y 2 = x-1,y+1 3 = x,y+1 4 = x+1,y+1 5 = x+1,y  6 = x+1,y-1 7 = x,y-1 8 = x-1,y-1
        if field[x][y] == 0:
            if (x >= 1 and x <= 8 and y >= 1 and y <= 8):
                if (field[x - 1][y] == 0 and field[x - 1][y + 1] == 0 and field[x][y + 1] == 0 and field[x + 1][
                    y + 1] == 0 and field[x + 1][y] == 0 and field[x + 1][y - 1] == 0 and field[x][y - 1] == 0 and
                        field[x - 1][y - 1] == 0):
                    field[x][y] = 1
                    kol_KRB -= 1
            elif (x == 0 and y >= 1 and y <= 8):
                if (field[x][y + 1] == 0 and field[x + 1][y + 1] == 0 and field[x + 1][y] == 0 and field[x + 1][
                    y - 1] == 0 and field[x][y - 1] == 0):
                    field[x][y] = 1
                    kol_KRB -= 1
            elif (x == 9 and y >= 1 and y <= 8):
                if (field[x - 1][y] == 0 and field[x - 1][y + 1] == 0 and field[x][y + 1] == 0 and field[x][y - 1] == 0 and
                        field[x - 1][y - 1] == 0):
                    field[x][y] = 1
                    kol_KRB -= 1
            elif (x >= 1 and x <= 8 and y == 0):
                if (field[x - 1][y] == 0 and field[x - 1][y + 1] == 0 and field[x][y + 1] == 0 and field[x][y - 1] == 0 and
                        field[x - 1][y - 1] == 0):
                    field[x][y] = 1
                    kol_KRB -= 1
            elif (x >= 1 and x <= 8 and y == 9):
                if (field[x - 1][y] == 0 and field[x - 1][y - 1] == 0 and field[x + 1][y] == 0 and field[x][y - 1] == 0 and
                        field[x + 1][y - 1] == 0):
                    field[x][y] = 1
                    kol_KRB -= 1

    kol_KRB2 = TWO_KOPABLIK
    while kol_KRB2:  # ведь когда станет 0, то по языку Python это False! ➝ А-а-а-а
        x, y = randint(0, 9), randint(0, 9)
        pologenie = randint(1, 2)
        # можно и так писать - в одну строку
        # при x >=1 и х <= 8 и y >=1 и y <= 8 проверям все по кругу относительно точки
        # 1 = x-1,y 2 = x-1,y+1 3 = x,y+1 4 = x+1,y+1 5 = x+1,y  6 = x+1,y-1 7 = x,y-1 8 = x-1,y-1
        if field[x][y] == 0:
            if pologenie == 2:
                if (x >= 2 and x <= 7 and y >= 1 and y <= 8):
                    if (field[x - 1][y] == 0 and field[x - 1][y + 1] == 0 and field[x][y + 1] == 0 and field[x + 1][
                        y + 1] == 0 and field[x + 1][y] == 0 and field[x + 1][y - 1] == 0 and field[x][y - 1] == 0 and
                            field[x - 1][y - 1] == 0 and field[x + 2][y] == 0 and field[x + 2][y + 1] == 0 and field[x + 2][
                                y - 1] == 0 and field[x + 2][y] == 0):
                        field[x][y] = 2
                        field[x + 1][y] = 2
                        kol_KRB2 -= 1

            elif pologenie == 1:
                if (x >= 1 and x <= 8 and y >= 2 and y <= 7):
                    if (field[x - 1][y] == 0 and field[x - 1][y + 1] == 0 and field[x][y + 1] == 0 and field[x + 1][
                        y + 1] == 0 and field[x + 1][y] == 0 and field[x + 1][y - 1] == 0 and field[x][y - 1] == 0 and
                            field[x - 1][y - 1] == 0 and field[x][y + 2] == 0 and field[x + 1][y + 2] == 0 and field[x - 1][
                                y + 2] == 0 and field[x][y + 2] == 0):
                        field[x][y] = 2
                        field[x][y + 1] = 2
                        kol_KRB2 -= 1

    kol_KRB3 = TRETIY_KORABLIK
    while kol_KRB3:  # ведь когда станет 0, то по языку Python это False! ➝ А-а-а-а
        x, y = randint(0, 9), randint(0, 9)
        pologenie = randint(1,2)
        if pologenie == 2:
            if (tr(x - 1, y) and tr(x - 1, y + 1) and tro(x, y + 1) and tr(x + 1, y + 1) and tr(
                    x + 1, y - 1) and tr(x, y - 1) and tr(x - 1, y - 1) and tr(x + 2, y) and (x + 2, y + 1) and tr(
                    x + 2, y - 1) and tr(x + 3, y) and (x + 3, y + 1) and tr(x + 3, y - 1) and tro(x+2,y) and tro(x + 1, y) and tro(x,y) == True):
                field[x][y] = 3
                field[x + 1][y] = 3
                field[x + 2][y] = 3
                kol_KRB3 -= 1


        elif pologenie == 1:
            if (tr(x+1,y-1) and  tr(x+1,y-1) and tr(x+1,y) and tr(x-1,y) and tr(x+1,y+1) and tr(x-1,y+1) and tr(x+1,y+2) and tr(x-1,y+2) and tr(x+1,y+3) and tr(x-1,y+3) and tr(x+1,y+4) and tr(x-1,y+4) and tr(x,y-1) and tr(x,y+4) and tro(x,y+1) and tro(x,y+2) and tro(x,y+3)) == True:
                field[x][y + 1] = 3
                field[x][y + 2] = 3
                field[x][y + 3] = 3
                kol_KRB3 -= 1



    kol_KRB4 = MAX_KOPABLIK
    while kol_KRB4:  # ведь когда станет 0, то по языку Python это False! ➝ А-а-а-а
        x, y = randint(0, 9), randint(0, 9)
        pologenie = randint(1,2)
        if pologenie == 2:
            if (tr(x,y+1) and tr(x,y) and tr(x,y-1) and tr(x+1,y+1) and tr(x+1,y-1) and tr(x+2,y+1) and tr(x+2,y-1) and tr(x+3,y+1) and tr(x+3,y-1) and tr(x+4,y+1) and tr(x+4,y-1) and tr(x+5,y+1) and tr(x+5,y-1) and tr(x+5, y) and tro(x+1,y) and tro(x+2,y) and tro(x+3,y) and tro(x+4,y)) == True:
                field[x + 1][y] = 4
                field[x + 2][y] = 4
                field[x + 3][y] = 4
                field[x + 4][y] = 4
                kol_KRB4 -= 1


        elif pologenie == 1:
            if (tr(x,y) and tr(x+1,y-1) and  tr(x+1,y-1) and tr(x+1,y) and tr(x-1,y) and tr(x+1,y+1) and tr(x-1,y+1) and tr(x+1,y+2) and tr(x-1,y+2) and tr(x+1,y+3) and tr(x-1,y+3) and tr(x+1,y+4) and tr(x-1,y+4) and tr(x,y-1) and tr(x,y+5) and tr(x+1,y+5) and tr(x-1,y+5) and tro(x,y+1) and tro(x,y+2) and tro(x,y+3) and tro(x,y+4)) == True:
                field[x][y + 1] = 4
                field[x][y + 2] = 4
                field[x][y + 3] = 4
                field[x][y + 4] = 4
                kol_KRB4 -= 1





    def pretty_print(mas):
        for row in mas:
            print(*row)

    pretty_print(field)

def hod ():

    h = True
    hh = True
    while h:
        pole()
        vibor1 = input('вам нравится это расположение кораболей ?  ')
        if vibor1 == 'Lf' or 'lf' or 'Да' or 'да':
            h = False
            z = input('Передайте другому игроку и попросите его нажать Enter')
            while hh:

                if z == '':
                    hh = False
        elif vibor1 == 'Ytn' or 'ytn' or 'Нет' or 'нет':
            pass
        else:
            print('Мы вас не поняли напишите пожалуйста ответ ещё раз')



        print('hahahahahaha')




hod()