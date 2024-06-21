# from turtle import *
# state = {'turn': 0}
# def spinner():
#     clear()
#     angle = state['turn']/10
#     right(angle)
#     forward(100)
#     dot(120, 'red')
#     back(100)
#     right(120)
#     forward(100)
#     dot(120, 'green')
#     back(100)
#     right(120)
#     forward(100)
#     dot(120, 'blue')
#     back(100)
#     right(120)
#     update()
# def animate():
#     if state['turn']>0:
#         state['turn']-=1

#     spinner()
#     ontimer(animate, 20)
# def flick():
#     state['turn']+=10

# setup(420, 420, 370, 0)
# hideturtle()
# tracer(False)
# width(20)
# onkey(flick, 'space')
# listen()
# animate()
# done()




import turtle as t

# Create screen and spinner objects
screen = t.Screen()
spinner = t.Turtle()

# Function to draw the fidget spinner
def draw_spinner():
    spinner.clear()
    spinner.width(3)
    
    for _ in range(3):
        spinner.forward(100)
        spinner.stamp()
        spinner.backward(100)
        spinner.right(120)
        
    spinner.right(spinner.angle)

# Function to animate the spinner
def animate():
    if spinner.speed:
        spinner.angle += spinner.speed
        draw_spinner()
        screen.ontimer(animate, 20)

# Functions to control the spinner
def spin_fast():
    spinner.speed += 10

def spin_slow():
    spinner.speed -= 10

def stop_spin():
    spinner.speed = 0

# Initial setup
spinner.speed = 0
spinner.angle = 0

screen.setup(width=600, height=600)
screen.bgcolor("white")

# Draw the initial spinner
draw_spinner()

# Set up controls
screen.onkey(spin_fast, "Up")
screen.onkey(spin_slow, "Down")
screen.onkey(stop_spin, "space")
screen.listen()

# Start the animation
animate()

# Start the main event loop
screen.mainloop()
