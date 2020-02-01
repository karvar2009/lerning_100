from turtle import *

c = Turtle()
c.shape('turtle')
c.color('BLUE')
c.pensize(2)

def d(picsel):
 c.fd(picsel)

def r(gradusr):
 c.rt(gradusr)

def l(gradusl):
 c.lt(gradusl)

def up():
 c.penup()

def down():
 c.pendown()

def a_letter():
     down()
     l(90)
     r(15)
     d(50)
     r(150)
     d(50)
     r(180)
     d(20)
     r(280)
     d(15)
     up()
     d(-15)
     r(-280)
     d(-20)
     r(-180)
     r(-90)
     r(15)
     d(10)

def b_letter ():
    down()
    r(-90)
    d(40)
    for k in range (1,50):
        d(1)
        r(5)
    up()
    l(120)
    # d(15)
    down()
    for p in range (1,57):
        d(1)
        r(3)
    r(85)
    up()
    r(72)
    d(40)
    l(90)
    d(4)
    r(90)

def c_letter():
    down()
    r(180)
    for g in range (1,60):
        d(1)
        r(3)
    up()
    r(90)
    d(20)
    l(90)
    d(50)



def d_letter ():
    l(90)
    down()
    d(40)
    r(90)
    for gg in range (1,61):
        d(1)
        r(3)
    up()
    l(180)
    d(70)
    l(90)
    d(10)
    r(90)


def e_letter ():
    down()
    r(180)
    for g in range (1,81):
        d(1)
        r(3)
    r(105)
    d(40)
    up()
    l(90)
    d(10)
    l(90)
    d(80)
    r(20)
def f_letter ():
    down()
    l(90)
    d(20)
    r(90)
    d(20)
    d(-20)
    l(90)
    d(20)
    r(90)
    d(18)
    up()
    r(90)
    d(30)
    l(90)
    d(40)



def g_letter ():
    l(90)
    d(40)
    l(90)
    down()
    for g in range (1,91):
        d(1)
        l(3)
    l(90)
    d(20)
    up()
    r(180)
    d(60)



def h_letter ():
    down()
    l(90)
    d(20)
    r(90)
    d(15)
    r(180)
    d(15)
    r(90)
    d(20)
    r(90)
    up()
    d(15)
    r(90)
    down()
    d(40)
    l(90)
    up()
    d(40)
    l(90)
    d(10)
    r(90)




def i_letter ():
    down()
    l(90)
    d(25)
    up()
    d(14)
    down()
    d(1)
    up()
    r(180)
    d(30)
    l(90)
    d(40)



def j_letter ():
    up()
    d(20)
    l(90)
    d(40)
    down()
    r(180)
    d(25)
    for ggg in range (1,31):
        d(1)
        r(5)
    r(110)
    up()
    d(45)
    l(90)
    d(5)
    r(93)


def k_letter ():
    down()
    l(90)
    d(20)
    r(140)
    d(25)
    l(180)
    d(25)
    r(90)
    d(25)
    l(180)
    d(25)
    r(135)
    d(20)
    r(180)
    d(30)
    up()
    l(90)
    d(60)


def l_letter ():
    up()
    l(90)
    d(40)
    r(180)
    down()
    d(40)
    l(90)
    d(15)
    up()
    d(40)
    l(90)
    d(10)
    r(90)



def m_letter ():
    down()
    l(75)
    d(43)
    r(150)
    d(43)
    l(150)
    d(43)
    r(150)
    d(43)
    l(75)
    up()
    d(40)
    l(90)
    d(10)
    r(90)



def n_letter ():
    down()
    l(90)
    d(40)
    r(140)
    d(48)
    l(140)
    d(40)
    up()
    d(-30)
    r(90)
    d(40)



def o_letter():
    down()
    for gggg in range (1,121):
        d(1)
        l(3)
    up()
    d(40)
    l(90)
    d(10)
    r(90)




def p_letter():
    down()
    l(90)
    d(40)
    r(90)
    for ggggg in range (1,31):
        d(1)
        r(6)
    l(90)
    up()
    d(10)
    l(90)
    d(50)




def q_letter():
    down()
    for gggggg in range (1,6):
        d(1)
        l(3)
    l(90)
    d(3)
    r(180)
    d(10)
    r(180)
    d(7)
    r(90)
    for ggggggg in range (1,116):
        d(1)
        l(3)
    up()
    d(60)
    l(90)
    d(10)
    r(90)




def r_letter ():
    down()
    l(90)
    d(40)
    r(90)
    for ggggggg in range (1,31):
        d(1)
        r(6)
    l(135)
    d(28)
    l(45)
    up()
    d(40)
    l(90)
    d(10)
    r(90)




def s_letter():
    up()
    l(90)
    d(40)
    r(90)
    down()
    d(7)
    for ggggggg in range (1,31):
        d(-1)
        l(6)
    for gggggggg in range(1, 31):
        d(-1)
        r(6)
    d(7)
    up()
    d(40)
    l(90)
    d(10)
    r(90)




def t_letter():
    up()
    d(10)
    down()
    l(90)
    d(40)
    l(90)
    d(20)
    r(180)
    d(40)
    up()
    d(40)
    r(90)
    d(30)
    l(90)




def u_letter():
    up()
    l(90)
    d(40)
    down()
    r(180)
    d(30)
    for gggggggg in range(1, 31):
        d(1)
        l(6)
    d(30)
    up()
    r(90)
    d(40)
    r(90)
    d(30)
    l(90)




def v_letter():
    up()
    l(90)
    d(40)
    r(180)
    down()
    l(25)
    d(43)
    l(150)
    d(43)
    r(75)
    up()
    r(90)
    d(30)
    l(90)
    d(40)

def w_letter ():
    up()
    l(90)
    d(40)
    r(180)
    down()
    l(25)
    d(43)
    l(150)
    d(43)
    r(165)
    l(25)
    d(43)
    l(150)
    d(43)
    r(75)
    up()
    r(90)
    d(30)
    l(90)
    d(40)




def x_letter ():
    down()
    l(45)
    d(46)
    r(180)
    d(23)
    r(90)
    d(23)
    r(180)
    d(46)
    up()
    l(45)
    d(40)
    l(90)
    d(10)
    r(90)




def y_letter ():
    down()
    l(45)
    d(46)
    r(180)
    d(23)
    r(90)
    d(23)
    up()
    r(180)
    d(46)
    l(45)
    d(40)
    l(90)
    d(10)
    r(90)




def z_letter ():
    up()
    l(90)
    d(40)
    r(90)
    down()
    d(40)
    r(135)
    d(55)
    l(135)
    d(40)
    up()
    d(60)
    l(90)
    d(10)
    r(90)



def space ():
    up()
    d(80)


def letter(text):
    for i in text:
        if i == 'a':
            a_letter()
        if i == 'b':
            b_letter()
        if i == 'c':
            c_letter()
        if i == 'd':
            d_letter()
        if i == 'e':
            e_letter()
        if i == 'f':
            f_letter()
        if i == 'g':
            g_letter()
        if i == 'h':
            h_letter()
        if i == 'i':
            i_letter()
        if i == 'j':
            j_letter()
        if i == 'k':
            k_letter()
        if i == 'l':
            l_letter()
        if i == 'm':
            m_letter()
        if i == 'n':
            n_letter()
        if i == 'o':
            o_letter()
        if i == 'p':
            p_letter()
        if i == 'q':
            q_letter()
        if i == 'r':
            r_letter()
        if i == 's':
            s_letter()
        if i == 't':
            t_letter()
        if i == 'u':
            u_letter()
        if i == 'v':
            v_letter()
        if i == 'w':
            w_letter()
        if i == 'x':
            x_letter()
        if i == 'y':
            y_letter()
        if i == 'z':
            z_letter()


up()
d(-200)
down()
ss = input("Введите текст: ")
letter(ss)
done()