import turtle
import random

turtle.hideturtle()
screen = turtle.Screen()
screen.setup(width=600, height=500)
user_bet = screen.textinput(title="Make your bet ", prompt="Which turtle will wim the race? Enter a color: ")
print(user_bet)
color = ['red','orange','yellow','green','blue','purple']
y_positios = [-80,-50,-10,30,70,100]
is_race_on = False

all_turtle = []

for turtle_index in range(0,6):
    turtle_turtle = turtle.Turtle(shape='turtle')
    new_turtle = turtle_turtle
    new_turtle.color(color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-287, y=y_positios[turtle_index])

    all_turtle.append(new_turtle)
  
if user_bet:
    is_race_on=True
    
while is_race_on:
    if turtle.xcor()>249:
        is_race_on=False
        winning_color = turtle.pencolor()
        if winning_color==user_bet:
            print(f"You've won ! The {winning_color} turtle is the winner ")

        else:
            print(f"You've lost ! The {winning_color} turtle is the winner ")
    for turtle in all_turtle:
        random_distance=random.randint(0,10)
        turtle.forward(random_distance)
screen.exitonclick()