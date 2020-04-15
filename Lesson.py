# -*- coding: utf-8 -*-
from tkinter import *
import random


def tst(x, y, position, number_of_squares, square_number):
    Test = True
    if position == True:
        for x1 in range(x - square_number + 1, x - square_number + number_of_squares + 1):
            Test = square_list[x1 * 10 + y].test_free()
            if Test == False:
                break
    else:
        for y1 in range(y - square_number + 1, y - square_number + number_of_squares + 1):
            Test = square_list[x * 10 + y1].test_free()
            if Test == False:
                break
    if Test == True:
        if position == True:
            for y1 in range(y - 1, y + 2):
                for x1 in range(x - square_number, x - square_number + number_of_squares + 2):
                    square_list[x1 * 10 + y1].sink()
        else:
            for x1 in range(x - 1, x + 2):
                for y1 in range(y - square_number, y - square_number + number_of_squares + 2):
                    square_list[x1 * 10 + y1].sink()


class Square():
    def __init__(self, x, y, framesquare):
        self.square = Button(framesquare, width=2, height=1, bg='grey', command=self.miss)
        self.x = x
        self.y = y
        self.square.grid(row=x, column=y)
        self.free = True
        self.number_of_squares = 0
        self.horisontell = True
        self.square_number = 0
        self.shooting = self.missing = 0

    def new_game(self, number_of_squares, position, square_number):
        self.free = False
        self.square['bg'] = 'red'
        self.square['command'] = self.shoot
        self.horisontell = position
        self.free = False
        self.number_of_squares = number_of_squares
        self.square_number = square_number

    def sink(self):
        if self.missing == 0:
            self.square['bg'] = 'orange'

    def test_free(self):
        if self.missing == 1:
            return True
        else:
            return False

    def reset(self):
        self.square['bg'] = 'grey'
        self.free = True
        self.square['command'] = self.miss
        self.shooting = self.missing = 0

    def test(self):
        if self.free == True:
            return True
        else:
            return False

    def miss(self):
        self.square['bg'] = 'green'
        self.missing = 1

    def shoot(self):
        self.square['bg'] = 'blue'
        self.shooting = 1
        self.missing = 1
        tst(self.x, self.y, self.horisontell, self.number_of_squares, self.square_number)

    def skill1(self):
        return self.missing

    def skill2(self):
        return self.shooting


def skill():
    miss = shoot = 0
    for y in range(10):
        for x in range(10):
            miss += square_list[x * 10 + y].skill1()
            shoot += square_list[x * 10 + y].skill2()
    lab = Label(root, text=(shoot / (miss + 0.000000000001) * 100), font="Arial 10")
    lab.pack(side='left')


def new_game():
    for y in range(10):
        for x in range(10):
            square_list[x * 10 + y].reset()
    horisontell = [True, False]
    for number_of_squares in range(1, 5):
        for numbers in range(5 - number_of_squares):
            square_number = 1
            test = False
            while test == False:
                position = random.choice(horisontell)
                if position == True:
                    x = random.randrange(0, 11 - number_of_squares)
                    y = random.randrange(10)
                    for y1 in range(y - 1, y + 2):
                        x1 = x - 1
                        for a in range(number_of_squares + 2):
                            if y1 < 0:
                                y1 += 1
                            if y1 > 9:
                                y1 -= 1
                            if x1 < 0:
                                x1 += 1
                            if x1 > 9:
                                x1 -= 1
                            test = square_list[x1 * 10 + y1].test()
                            x1 += 1
                            if test == False:
                                break
                        if test == False:
                            break
                else:
                    y = random.randrange(0, 11 - number_of_squares)
                    x = random.randrange(10)
                    for x1 in range(x - 1, x + 2):
                        y1 = y - 1
                        for a in range(number_of_squares + 2):
                            if y1 < 0:
                                y1 += 1
                            if y1 > 9:
                                y1 -= 1
                            if x1 < 0:
                                x1 += 1
                            if x1 > 9:
                                x1 -= 1
                            test = square_list[x1 * 10 + y1].test()
                            y1 += 1
                            if test == False:
                                break
                        if test == False:
                            break

            for numbers in range(number_of_squares):
                square_list[x * 10 + y].new_game(number_of_squares, position, square_number)
                square_number += 1
                test = False
                if position == True:
                    x += 1
                else:
                    y += 1


root = Tk()
root.title('S&#228;nka skepp')
frame = Frame()
frame.pack()
"""text="F&#246;r att b&#246;rja nytt spell, tryck Meny-New Game! \n =)"
lab = Label(root, text=text, font="Arial 10")
lab.pack(side='left')
ent = Entry(frame, text=’’, width=20,bd=3)
ent.pack()"""
menubar = Menu(frame)

menu = Menu(menubar)
menu.add_command(label="New game", command=new_game)
menu.add_command(label="Reset", )
menu.add_command(label='Quit', command=root.destroy)
menu.add_command(label="Skill", command=skill)

help_menu = Menu(menubar)
help_menu.add_command(label='About')
help_menu.add_command(label='Rules')

menubar.add_cascade(label="Menu", menu=menu)
menubar.add_cascade(label="About", menu=help_menu)
root.config(menu=menubar)

square_list = []
framesquare = Frame(root)
# framesquare.pack()
for y in range(10):
    for x in range(10):
        b = Square(x, y, framesquare)
        square_list.append(b)
framesquare.pack()

root.mainloop()