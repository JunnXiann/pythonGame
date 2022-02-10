import turtle
import os

#window
win = turtle.Screen()
win.title('Pong')
win.bgcolor('white')
win.setup(width=800, height=600)
win.tracer(0)

#score
score_a = 0 
score_b = 0

#pad1
pad1 = turtle.Turtle()
pad1.speed(0)
pad1.shape('square')
pad1.color('black')
pad1.shapesize(stretch_wid=5, stretch_len=1)
pad1.penup()
pad1.goto(-350, 0)

#pad2
pad2 = turtle.Turtle()
pad2.speed(0)
pad2.shape('square')
pad2.color('black')
pad2.shapesize(stretch_wid=5, stretch_len=1)
pad2.penup()
pad2.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('black')
ball.penup()
ball.goto(0,0)
ball.dx = 0.5
ball.dy = 0.5

#score
score = turtle.Turtle()
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=('Courier',24,'normal'))

#func
def pad1_up():
	y = pad1.ycor()
	y += 40 
	pad1.sety(y)

def pad2_up():
	y = pad2.ycor()
	y += 40 
	pad2.sety(y)

def pad1_down():
	y = pad1.ycor()
	y -= 40 
	pad1.sety(y)

def pad2_down():
	y = pad2.ycor()
	y -= 40 
	pad2.sety(y)

win.listen()
win.onkey(pad1_up, "w")
win.onkey(pad2_up, "Up")
win.onkey(pad1_down, "s")
win.onkey(pad2_down, "Down")

while True:
	 win.update()
	 ball.setx(ball.xcor() + ball.dx)
	 ball.sety(ball.ycor() + ball.dy)

	 if ball.ycor() > 290:
	 	ball.sety(290)
	 	ball.dy *= -1

	 elif ball.ycor() < -290:
	 	ball.sety(-290)
	 	ball.dy *= -1

	 if ball.xcor() > 380:
	 	score_a += 1
	 	score.clear()
	 	score.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=('Courier',24,'normal'))
	 	ball.goto(0,0)
	 	ball.dx *= -1


	 elif ball.xcor() < -380:
	 	score_b += 1
	 	score.clear()
	 	score.write("Player A: {}   Player B: {}".format(score_a, score_b), align="center", font=('Courier',24,'normal'))
	 	ball.goto(0,0)
	 	ball.dx *= -1

	 if ball.xcor() < -340 and ball.ycor() < pad1.ycor() + 50 and ball.ycor() > pad1.ycor() - 50:
	 	ball.dx *= -1

	 elif ball.xcor() > 340 and ball.ycor() < pad2.ycor() + 50 and ball.ycor() > pad2.ycor() - 50:
	 	ball.dx *= -1












