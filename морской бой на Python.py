from random import randint
# from time import sleep
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
no = []
yes = []
def zero_field():
    field1 = [
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
    def k1 ():
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
    def k2 ():
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
    def k3():
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

    def k4():
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

    k4()
    k3()
    k2()
    k1()


def pretty_print(mas):
    for row in mas:
        print(*row)


def hod ():
    def pr (x,y):
        canon = x * 10 + y
        return canon
    def alll(x12,y12):
        spaceX = x12 * 10 + y12
        for i in range (1,len(no)+1):
            if no == spaceX:
                return False
            else:
                return True
    def bot_attack(x,y):
        if player1[x] [y] != 0:
            player1[x] [y] = 8
        else:
            player1[x][y] = 6

    def bot():
        hello_world = True
        nono = True
        while nono:
            xyz = randint(0,9)
            yz = randint(0,9)
            if alll(xyz,yz):
                if player1 [xyz] [yz] == 0:
                    no.append(pr(xyz,yz))
                    bot_attack(xyz,yz)
                    if no[xyz] [yz] == 0:
                        hello_world = False



    h = True
    while h:
        global field
        pole()
        pretty_print(field)
        vibor1 = input('вам нравится это расположение кораболей ?  ')
        if vibor1 == 'Lf' or vibor1 == 'lf' or vibor1 == 'Да' or vibor1 == 'да':
            h = False
            print('Ваше поле сформировано!')
            player1 = field
            attack_player1 = [
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
        elif vibor1 == 'Ytn' or vibor1 == 'ytn' or vibor1 == 'Нет' or vibor1 == 'нет':
            print('Выводим ещё раз!')
        else:
            print('Мы вас не поняли напишите пожалуйста ответ ещё раз')


    pole()
    botik = field
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

    def player_attack(x,y):
        if botik[x] [y] != 0:
            attack_player1 [x] [y] = 8
        else:
            attack_player1 [x] [y] = 6
    def allll(x12,y12): # yes это список с провереными полями ( строчка - 26 ) [ исключения в yes назначаются в строчке - 282 ]
        spaceY = x12 * 10 + y12 # перевод из двух координат в одну ( тоже самое происходит в {pr} строчка - 171 )
        for i in range (1,len(yes)+1): # если наше исключение равно координате то...
            if yes == spaceY:
                return False
            else:
                return True

    def player():
        Stas = True
        for i in range (1,2):
            nono = True
            while nono:
                pretty_print(attack_player1)
                yz1 = int(input('Введите координату X '))
                xz1 = int(input('Введите координату Y '))
                yz = yz1 - 1
                xyz = xz1 - 1
                if allll(xyz,yz):
                    yes.append(pr(xyz,yz))
                    player_attack(xyz,yz)
                    pretty_print(attack_player1)
                    for i in [1,2,3,4,5]:
                        print()
                    pretty_print(player1)
                    if botik[xyz] [yz] == 0:
                        Stas = False
                else:
                    print('Вы уже проверяли это поле!')







    while True:
        player()
        bot()



    print('hahahahahaha')




hod()