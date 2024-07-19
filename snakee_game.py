import turtle
import random
import time

delay = 0.1
sc = 0
hs = 0
# creating a body of snake 
bodies = []

# creating screen 
s = turtle.Screen()
s.title("Snake Game")
s.bgcolor("light blue")  # Corrected color name
s.setup(width=600, height=600)  # Size of the screen

# Creating head 
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("blue")
head.fillcolor("red")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Creating food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("black")
food.fillcolor("red")
food.penup()
food.goto(0, 100)

# Creating a score board
sb = turtle.Turtle()
sb.speed(0)
sb.color("black")
sb.penup()
sb.hideturtle()
sb.goto(-250, 250)
sb.write(" Creater : Farhan ur Rasool \nScore: 0  |  Highest Score: 0")

# Moving in the all directions
def moveUp():
    if head.direction != "down":
        head.direction = "up"

def moveDown():
    if head.direction != "up":
        head.direction = "down"

def moveLeft():
    if head.direction != "right":
        head.direction = "left"

def moveRight():
    if head.direction != "left":
        head.direction = "right"

def moveStop():
    head.direction = "stop"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Event handling
s.listen()
s.onkey(moveUp, "Up")
s.onkey(moveDown, "Down")
s.onkey(moveLeft, "Left")
s.onkey(moveRight, "Right")
s.onkey(moveStop, "space")

# Main loop
while True:
    s.update()  # to update the screen in 
    # check collision with border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        for body in bodies:
            body.goto(1000, 1000)  # move the body off-screen
        bodies.clear()

        sc = 0
        delay = 0.1

        sb.clear()
        sb.write(" Creater : Farhan ur Rasool \n Score: {}  |  Highest Score: {}".format(sc, hs))

    # check collision with food
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # increase the body
        body = turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        body.color("red")
        bodies.append(body)  # append the new body to the list

        sc += 10  # increase the score
        delay -= 0.001  # increase the speed

        if sc > hs:
            hs = sc  # update the highest score
        sb.clear()
        sb.write(" Creater : Farhan ur Rasool \n Score: {}  |  Highest Score: {}".format(sc, hs))

    # move the snake body
    for i in range(len(bodies) - 1, 0, -1):
        x = bodies[i - 1].xcor()
        y = bodies[i - 1].ycor()
        bodies[i].goto(x, y)

    if len(bodies) > 0:
        x = head.xcor()
        y = head.ycor()
        bodies[0].goto(x, y)

    move()

    # check collision with the snake body
    for body in bodies:
        if body.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            for body in bodies:
                body.goto(1000, 1000)  # move the body off-screen
            bodies.clear()

            sc = 0
            delay = 0.1

            sb.clear()
            sb.write(" Creater : Farhan ur Rasool \n Score: {}  |  Highest Score: {}".format(sc, hs))

    time.sleep(delay)

s.mainloop()
