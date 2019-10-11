import os
while True:

    print("0-программа для счёта мелких денег\n1-вывод меньшего числа\n2-функция sign(x)\n3-скидка\n4-сможете ли вы доехать до следующей заправки\n5-таблица умножения")
    print('6-таблица умножения +\n7-високосный ли год\n8-сколько чисел совпадают?\n9-от первого числа до второго в порядке возастаия\n10-от первого числа до второго в порядке возастаия или от второго до первого в порядке убывания\n11-факториал\n12-лестница из звёздочек')
    qwertyuiop=int(input('введите номер задания от 0 до 12  '))

    """
    Задания для решения в классе.
    Пишите код прямо под описанием заданий.
    """
    '''
    Задание 0. Напишите программу для счета мелких денег. Она должна спрашивать:
        «Сколько у вас монет по 50 копеек?»;
        «Сколько у вас монет по 10 копеек?»;
        «Сколько у вас монет по 5 копеек?»;
        «Сколько у вас монет по 1 копейке?».
    После этого на экране должна появиться общая сумма (сумма денег, а не номиналов).
    '''
    if qwertyuiop==0:
        x=int(input('Сколько у вас монет по 50 копеек? '))
        y=int(input('Сколько у вас монет по 10 копеек? '))
        f=int(input('Сколько у вас монет по 5 копеек? '))
        d=int(input('Сколько у вас монет по 1 копейке? '))
        print(x*0.5+y*0.1+f*0.05+d*0.01)

    ' Задание 1. Даны два целых числа (вводятся пользователем.) Выведите значение наименьшего из них. '
    if qwertyuiop==1:
        x=int(input('введите первое число '))
        y=int(input('введите второе число '))
        if x<y:
            print(x)
        elif x>y:
            print(y)
        elif x==y:
            print('одинаково')

    ''' Задание 2. В математике функция sign(x) (знак числа) определена так: 
    sign(x) = 1, если x > 0, 
    sign(x) = -1, если x < 0, 
    sign(x) = 0, если x = 0.
    Для числа x (вводится пользователем) выведите значение sign(x). 
    Эту задачу желательно решить с использованием каскадных инструкций if... elif... else. 
    '''
    if qwertyuiop==2:
        x=int(input('введите число '))
        if x>0:
            print('sign(x) = 1')
        elif x<0:
            print('sign(x) = -1')
        else:
            print('sign(x) = 0')
    ''' Задание 3.
    В магазине распродажа. На товары за 10 долларов и меньше скидка 10%,
    а на товары дороже 10 долларов — 20 %. Напишите программу, которая 
    будет запрашивать цену товара и показывать размер скидки (10 или 20 %) и итоговую цену.
    '''
    if qwertyuiop==3:
        print('В магазине распродажа. На товары за 10 долларов и меньше скидка 10%, а на товары дороже 10 долларов — 20 %.')
        x=float(input('введите цену  '))
        if x<11:
            print('скидка 10%')
            print(f'цена : {x*0.90}')
        elif x>10:
            print('скидка 20%')
            print(f'цена : {x*0.80}')
    '''Задание 4.
    Путешествуя на автомобиле, вы заехали на заправку. До следующей заправки 200 километров. 
    Напишите программу, которая будет определять, нужно ли вам заправляться или же можно 
    подождать до следующей станции.
    Программа должна спрашивать:
     Каков размер вашего бензобака в литрах?
     Сколько горючего в бензобаке (в процентах)?
     Сколько километров проходит автомобиль НА ОДНОМ ЛИТРЕ бензина? 
    Результат работы программы должен выглядеть примерно так:
       input - Размер бензобака: 60
       input - Заполненность в процентах: 40
       input - Км на литр: 10
       print - Вы можете проехать еще 240 км.
       print - Следующая заправка через 200 км.
       print - Можно подождать следующей заправки.
    '''
    if qwertyuiop==4:
        x=int(input('Каков размер вашего бензобака в литрах? '))
        y=int(input('Сколько горючего в бензобаке (в процентах)? '))
        s=int(input('Сколько километров проходит автомобиль НА ОДНОМ ЛИТРЕ бензина? '))
        print()
        p=(x*(y/100)*s)
        print(f'вы можете поехать ещё {p} км')
        print('следующяя заправка через 200 км')
        if p>200:
            print('вы можете доехать до следующей заправки')
        elif p==200:
            print('вы можете доехать до следующей заправки, но если вы точно уверены что вы на этом расстоянии')
        else:
            print('советуем заправится тут')
    ''' Задание 5.
    Напишите программу, выводящую на экран таблицу умножения.
    Первым делом она должна спрашивать, для какого числа требуется вывести таблицу.
    '''
    if qwertyuiop==5:
        x=int(input('таблицу умножения для кокого числа требуется вывести? '))
        for i in range (1,11):
            print(f'{x}*{i}={x*i}')
    ''' Задание 6.
    Добавьте к предыдущей программе дополнительные детали, 
    уточнив, до какого множителя следует выводить таблицу умножения.
    '''
    if qwertyuiop==6:
        x=int(input('таблицу умножения для кокого числа требуется вывести?(первое число) '))
        y=int(input('до какого множителя требуется вывести таблицу? '))
        for i in range (1,y+1):
            print(f'{x}*{i}={x*i}')
    ''' Задание 7.
    Дано натуральное число. Требуется определить, является ли год с данным номером високосным. 
    Если год является високосным, то выведите YES, иначе выведите NO. 
    Напомню, что в соответствии с григорианским календарем, год является високосным, 
    если его номер кратен 4, но не кратен 100, а также если он кратен 400.
    '''
    if qwertyuiop==7:
        x=int(input('какой год '))
        if x % 4 != 0 or (x % 100 == 0 and x % 400 != 0):
            print('NO')
        else:
            print('YES')

    ''' Задание 8.
    Даны три целых числа. Определите, сколько среди них совпадающих. 
    Программа должна вывести одно из чисел: 3 (если все совпадают), 
    2 (если два совпадает) или 0 (если все числа различны).
    '''
    if qwertyuiop==8:
        x=int(input('введите первое число '))
        y=int(input('введите второе число '))
        s=int(input('введите третье число '))
        if x==y==s:
            print('3 числа одинаковы')
        elif x==y or x==s or y==s:
            print('2 числа одинаковы')
        else:
            print('0 чисел одинаковые')
    ''' Задание 9.
    Даны два целых числа A и B (вводятся пользователем) (при этом A ≤ B). 
    Выведите все числа от A до B включительно.
    '''
    if qwertyuiop==9:
        x=int(input('введите меньшее число '))
        y=int(input('введите большее число '))
        for i in range (x,y):
            print(i)
        print(i+1)

    ''' Задание 10.
    Даны два целых числа A и В. Выведите все числа от A до B включительно, 
    в порядке возрастания, если A < B, или в порядке убывания в противном случае.
    '''
    if qwertyuiop==10:
        a=int(input('введите число '))
        b=int(input('введите число '))
        if a<b:
            for i in range (a,b):
                print(i)
            print(i+1)
        else:
            for i in range(a,b,-1):
                print(i)
            print(i-1)
    ''' Задание 11.
    Факториалом числа n называется произведение 1 × 2 × ... × n. Обозначение: n!.
    По данному натуральному n (вводится пользователем) вычислите значение n!. 
    '''
    if qwertyuiop==11:
        y=1
        n=int(input('введите число '))
        for i in range (1,n+1):
            y*=i
        print(y)
    ''' Задание 12.
    Выведите лесенку из символов звездочки - *. 
    Количество ступеней вводится пользователем.
    '''
    if qwertyuiop==12:
        x=int(input('введите количество ступеней '))
        for i in range (1,x*10,10):
            print()
            print('*'*i)
    """
    Задания для решения в классе.
    Пишите код прямо под описанием заданий.
    """