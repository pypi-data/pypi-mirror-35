from turtle import *

def canvas(bg='white'):
	screensize(400,300,bg)
	setup(800,600)

def ruler(size=100,color='#F0F0F0'):
	pencolor(color)
	speed(50)
	x = -398
	y = 298
	right(90)
	while x < 400 + size:
		penup()
		goto(x,298)
		pendown()
		forward(600)
		x = x + size
	left(90)
	while y > -300 - size:
		penup()
		goto(-398,y)
		pendown()
		forward(800)
		y = y - size

def my_goto(x, y):
	x = x - 398
	if y <= 298:
		y = 298 - y
	else:
		y = -(y-298)
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
	set_canvas()

	pen_speed(6)
	pen_color('orange')
	fill_color('orange')
	fill_rect(0,0,100,100)
	pen_color('orange')
	fill_color('orange')
	fill_rect(400,400,100,100)

	pen_color('red')
	draw_rect(0,0,100,100)

	pen_color('black')
	fill_color('black')
	fill_circle(450,450,40)


	pen_color('white')
	fill_color('white')
	fill_circle(437,443,15)

	pen_color('white')
	fill_color('white')
	fill_circle(463,443,15)

	pen_color('white')
	fill_color('white')
	fill_circle(450,463,15)

	stop()
