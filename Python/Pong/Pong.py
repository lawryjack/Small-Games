# Simple pong game in python
# 7/15/21

import turtle;

#Basic window setup
window = turtle.Screen();
window.title("Pong");
window.bgcolor("black");
window.setup(width=800, height=600);
window.tracer(0);

#Score
leftPlayerScore = 0;
rightPlayerScore = 0;

#Left paddle
paddleLeft = turtle.Turtle();
paddleLeft.speed(0);
paddleLeft.shape("square");
paddleLeft.color("white");
paddleLeft.shapesize(stretch_wid=5, stretch_len=1);
paddleLeft.penup();
paddleLeft.goto(-350, 0);
leftPlayerScore = 0;


#Right paddle
paddleRight = turtle.Turtle();
paddleRight.speed(0);
paddleRight.shape("square");
paddleRight.color("white");
paddleRight.shapesize(stretch_wid=5, stretch_len=1);
paddleRight.penup();
paddleRight.goto(350, 0);
rightPlayerScore = 0;


#Ball
ball = turtle.Turtle();
ball.speed(0);
ball.shape("circle");
ball.color("white");
ball.penup();
ball.goto(0, 0);
ball.dx = .3;
ball.dy = .3;


#Pen
pen = turtle.Turtle();
pen.speed(0);
pen.color("white");
pen.penup();
pen.hideturtle();
pen.goto(0,260);
pen.write("Left Player: 0  Right Player: 0", align="center", font=("courier", 24, "normal"));



#Functions
def paddleLeftUp():
	y = paddleLeft.ycor();
	y += 40;
	y = paddleLeft.sety(y);
	
def paddleLeftDown():
	y = paddleLeft.ycor();
	y -= 40;
	y = paddleLeft.sety(y);

def paddleRightUp():
	y = paddleRight.ycor();
	y += 40;
	y = paddleRight.sety(y);

def paddleRightDown():
	y = paddleRight.ycor();
	y -= 40;
	y = paddleRight.sety(y);


# Keyboard binding

window.listen();
window.onkeypress(paddleLeftUp, "w");
window.onkeypress(paddleLeftDown, "s");
window.onkeypress(paddleRightUp, "i");
window.onkeypress(paddleRightDown, "k");


# Main Game Loop
while True:
	window.update();
	
	# Moving the ball
	ball.setx(ball.xcor() + ball.dx);
	ball.sety(ball.ycor() + ball.dy);


	# Border checking
	if ball.ycor() > 290:
		ball.sety(290);
		ball.dy *= -1;
	
	if ball.ycor() < -280:
		ball.sety(-280);
		ball.dy *= -1;

	if ball.xcor() > 390:
		ball.goto(0, 0);
		ball.dx *= -1;
		pen.clear();
		rightPlayerScore += 1;
		pen.write("Left Player: {}  Right Player: {}".format(leftPlayerScore, rightPlayerScore), align="center", font=("courier", 24, "normal"));
		
	if ball.xcor() < -390:
		ball.goto(0, 0);
		ball.dx *= -1;
		pen.clear();
		leftPlayerScore += 1;
		pen.write("Left Player: {}  Right Player: {}".format(leftPlayerScore, rightPlayerScore), align="center", font=("courier", 24, "normal"));
	
	# Controlling ball and paddle collisions
	if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < paddleRight.ycor() + 50 and ball.ycor() > paddleRight.ycor() - 50:
		ball.setx(340);
		ball.dx *= -1;
	elif ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < paddleLeft.ycor() + 50 and ball.ycor() > paddleLeft.ycor() - 50:
		ball.setx(-340);
		ball.dx *= -1;


