import turtle
import math
import random as rd

screen = turtle.Screen() #creates a screen object
 
#ask user to bet on a color
user_input = screen.textinput(title='Bet', prompt="Which turtle will win the race").lower()

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'] #seq of colors

#sets the pen to draw a finish line
screen.setup(width=500, height=400) #modifies the turtle graphics window
turtle.penup()
turtle.setposition(y=-200, x=220)
turtle.setheading(90)
for l in range(math.ceil(400/60)):
    #draws the end of the race line
    turtle.pendown()
    turtle.fd(30)
    turtle.penup()
    turtle.fd(30)
#part of the end line drawing


turtle_guy_ycoor = [-85, -55, -25, 5, 35, 65, 95] #for the y coordinates of the turtles

all_turtles = [] #lst to contain all turtle objects
win_color = []

for i in range(7):
    #builds multiple objects, and assigns them new color
    turtle.hideturtle()
    turtle_guy = turtle.Turtle()
    turtle_guy.showturtle()
    turtle_guy.color(colors[i])
    turtle_guy.shape("turtle")
    turtle_guy.penup()
    turtle_guy.setposition(x=-230, y=turtle_guy_ycoor[i])
    all_turtles.append(turtle_guy)

game_over = False
while not game_over:
    for turtle_g in all_turtles:
        if turtle_g.xcor() > 220:
            win_color.append(turtle_g)
            if user_input == win_color[0].pencolor():
                print(f'Yon win :{win_color[0].pencolor()}')
            else:
                print(f'You lost {win_color[0].pencolor()} won')
            game_over = True 
        turtle_pace = rd.randint(1, 10)
        turtle_g.fd(turtle_pace)

screen.exitonclick()
