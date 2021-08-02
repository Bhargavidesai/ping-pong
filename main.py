# importing the turtle
import turtle

# screen
wn = turtle.Screen()
# setting the title of the screen
wn.title("PingPong")
# setting the background colour of the screen
wn.bgcolor("#1d6e1b")
# setting the size of the screen
wn.setup(width=1000, height=800)
# this prevents the screen from getting updated
wn.tracer(0)
pen0=turtle.Turtle()
#setting the position of the score
pen0.penup()
pen0.goto(0,350)
pen0.write("--- Ping-Pong Game ---", align="center",font=("Courier",24 , "bold"))
pen0.hideturtle()
score_a=0
score_b=0

def court():
    # for drawing on screen objects
    pen = turtle.Turtle()
    pen.pensize(5)
    pen.color("white")
    pen.penup()
    pen.goto(-390, 290)
    pen.pendown()
    pen.forward(780)
    pen.right(90)
    pen.forward(575)
    pen.right(90)
    pen.forward(780)
    pen.right(90)
    pen.forward(575)
    pen.penup()
    pen.goto(0, 290)
    pen.pendown()
    pen.right(180)
    pen.forward(575)
    pen.hideturtle()



# function to draw the boarder of the game
court()

# paddle A drawing
penA = turtle.Turtle()
penA.speed(0)
penA.shape("square")
penA.color('#f7c707')
penA.shapesize(stretch_wid=5, stretch_len=1)
penA.penup()
penA.goto(-370, 10)

# paddle B drawing
penB = turtle.Turtle()
penB.speed(0)
penB.shape("square")
penB.color('#f7c707')
#resizing the shape
penB.shapesize(stretch_wid=5, stretch_len=1)
penB.penup()
penB.goto(370, 10)

# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color('white')
ball.penup()
ball.goto(-100, -150)


# function for movement of paddle A
def paddleA_up():
    # this will return the y postion of the paddle A
    y = penA.ycor()
    #condition makes the paddle not to cross the board
    if y<230:
        # increasing the value of y to move up
        y += 20
        # setting the y to new value of y after incrementing
        penA.sety(y)


def paddleB_up():
    # this will return the y postion of the paddle B
    y = penB.ycor()
    if y<230:
        # increasing the value of y to move up
        y += 20
        # setting the y to new value of y after incrementing
        penB.sety(y)

# function for movement of paddle A
def paddleA_down():
    # this will return the y postion of the paddle A
    y = penA.ycor()
    if y>-225:
        # increasing the value of y to move up
        y -= 20
        # setting the y to new value of y after incrementing
        penA.sety(y)


def paddleB_down():
    # this will return the y postion of the paddle B
    y = penB.ycor()
    if y>-225:
        # decreasing the value of y to move up
        y -= 20
        # setting the y to new value of y after decrementing
        penB.sety(y)


# keyboard binding
#Set focus on TurtleScreen in order to collect key-events
wn.listen()
#this means on pressing the Up key in the keyboard paddleA_up function is called
wn.onkeypress(paddleA_up, "Up")
wn.onkeypress(paddleB_up,'Left')
wn.onkeypress(paddleA_down, "Down")
wn.onkeypress(paddleB_down,'Right')
#0.5 pixel is added everytime the loop runs this makes the ball to move
ball.changeX=0.5
ball.changeY=0.5

#for drawing the score
pen1=turtle.Turtle()
pen1.speed(0)
pen1.color("black")
pen1.penup()
pen1.hideturtle()
#setting the position of the score
pen1.goto(0,300)
#write is used to write something on the screen with font size,fontstyle,alignment,we can make normal to bold
pen1.write("PlayerA:{}       PlayerB:{}".format(score_a, score_b), align="center",font=("Courier", 24, "bold"))
print("ho")
# main loop
while True:

    #we are adding the certain pixels as mentioned above to the current x and y position of the ball
    ball.setx(ball.xcor()+ball.changeX)
    ball.sety(ball.ycor()+ball.changeY)
    if ball.ycor()>280:
        ball.sety(280)
        #this will reverse the value of y if y=0.5 then ball.dy becomes -0.5 bcz -1 into anything is negative moves in opposite direction by decreasing y value
        #as y value decreases ball moves down
        ball.changeY *= -1

    if ball.ycor()< -280:
        ball.sety(-280)
        #this will reverse the value of y if y=-0.5 then ball.dy becomes +0.5 bcz -1 into negative is positive moves in opposite direction by increasing the value
        #as y value increases ball moves up
        ball.changeY *= -1

    if ball.xcor()>380:
        #if ball goes outside the court then it will respon on center of the screen and start moving
        ball.goto(0,0)
        ball.changeX *= -1
        #incrementing the score
        score_a+=1
        #clear screen is done to avoid over writing of score
        pen1.clear()
        pen1.write("PlayerA:{}        PlayerB:{}".format(score_a, score_b), align="center",font=("Courier", 24, "bold"))

    if ball.xcor()<-380:
        #if ball goes outside the court then it will respon on center of the screen and start moving
        ball.goto(0,0)
        ball.changeX *= -1
        score_b+=1
        pen1.clear()
        pen1.write("PlayerA:{}       PlayerB:{}".format(score_a, score_b), align="center",font=("Courier", 24, "bold"))

    #ball and paddle collision
    #ball will bounce back if it hits the rectangle paddle range is mentioned
    if (ball.xcor()>340 and ball.xcor()<350 ) and (ball.ycor()<penB.ycor()+60 and ball.ycor()>penB.ycor()-60):
        ball.setx(340)
        ball.changeX*=-1
    if (ball.xcor()<-340 and ball.xcor()>-350 ) and (ball.ycor()<penA.ycor()+60 and ball.ycor()>penA.ycor()-60):
        ball.setx(-340)
        ball.changeX*=-1

    # every time the loop runs screen gets updated
    wn.update()
