import random
import turtle

turtle.speed(0)

turtle.Screen().bgcolor("black")
turtle.shape('circle')

def pen(colour):
    turtle.color(colour)
pen('red')    


    
def firework1(size):
    for num in range(20):
        turtle.forward(size)
        turtle.right(180-(360/20))
        
        


def move():
    turtle.penup()
    x=random.randint(-150,150)
    y=random.randint(-150,150)
    turtle.goto(x,y)
    turtle.pendown()

move()
pen('yellow')
move()
pen('gold')
firework1(200)
move()
pen('silver')
move()
pen('blue')
firework1(33)
move()
pen('purple')
firework1(63)
move()
pen('lightblue')
firework1(45)
move()
pen('dark green')
move()
pen('pink')
firework1(100)
move()
pen('orange')
firework1(19)
move()
pen('violet')
firework1(30)
move()
pen('green')
firework1(99)
move()
pen('pitch')
firework1(309)
move()
pen('lime')
firework1(60)
move()
pen('magenta')