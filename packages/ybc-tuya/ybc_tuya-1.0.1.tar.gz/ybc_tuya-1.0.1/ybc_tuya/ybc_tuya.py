from turtle import *
from ybc_jiqimao import jiqimao
from ybc_xzpq import xzpq

def set_canvas(bg='white'):
	screensize(400,300,bg)
	setup(800,600)

def my_goto(x, y):
	x = x - 398
	if y <= 300:
		y = 300 - y
	else:
		y = -(y-300)
	penup()
	goto(x, y)
	pendown()

def hide():
	hideturtle()

# def show():
# 	showturtle()

def stop():
	hide()
	mainloop()


def pen_size(x=6):
    pensize(x)

def pen_color(color='black'):
	pencolor(color)

def pen_speed(x=3):
	speed(x)


def draw_circle(x,y,size):
	y = y + size
	my_goto(x,y)
	circle(size)

def fill_circle(x,y,size):
	_beginf()
	y = y + size
	my_goto(x,y)
	circle(size)
	_endf()

def draw_rect(x,y,width,height):
	my_goto(x,y)
	forward(width)
	right(90)
	forward(height)
	right(90)
	forward(width)
	right(90)
	forward(height)
	right(90)

def fill_rect(x,y,width,height):
	_beginf()
	my_goto(x,y)
	forward(width)
	right(90)
	forward(height)
	right(90)
	forward(width)
	right(90)
	forward(height)
	right(90)
	_endf()

def fill_color(color='white'):
	fillcolor(color)

def _beginf():
	begin_fill()

def _endf():
	end_fill()

if __name__ == '__main__':
	# jiqimao()
	xzpq()
