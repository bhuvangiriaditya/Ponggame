import turtle
wn=turtle.Screen()
wn.title("The Pong Game")
wn.bgcolor("cyan")
wn.setup(width=800, height=600)
wn.tracer(0)

#score
scorea=0
scoreb=0

#paddle A
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("yellow")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

#paddle B
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("yellow")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.x = 0.5
ball.y = 0.5

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier",24,"bold"))



#Functions
def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

def paddle_b_up():
    x=paddle_b.ycor()
    x+=20
    paddle_b.sety(x)

def paddle_b_down():
    x=paddle_b.ycor()
    x-=20
    paddle_b.sety(x)

#keyboard
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")



#main func
while (scorea<5 and scoreb<5):
    wn.update()

    ball.setx(ball.xcor() + ball.x)
    ball.sety(ball.ycor() + ball.y)

    if ball.ycor()>290:
        ball.sety(290)
        ball.y *= -1

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.y *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.x *= -1
        scorea+=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(scorea, scoreb), align="center", font=("Courier", 24, "bold"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.x *= -1
        scoreb+=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(scorea, scoreb), align="center", font=("Courier", 24, "bold"))

    if (ball.xcor() > 330 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor()+50 and ball.ycor() > paddle_b.ycor()-50):
        ball.setx(330)
        ball.x *= -1


    if (ball.xcor() < -330 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor()+50 and ball.ycor() > paddle_a.ycor()-50):
        ball.setx(-330)
        ball.x *= -1

if scorea>scoreb:
    print("Player A is the winner" )
elif scorea<scoreb:
    print("Player B is the winner" )
else:
    print("Match tied")
