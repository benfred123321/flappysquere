import pgzrun
import random

HEIGHT = 800
WIDTH = 800
TITLE = "Flappy squere"
r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255)
randcolor=(r,g,b)
gravity=2000 #pixles per second

class Squere:
    #creating construtor funtion 
    def __init__(self,initial_x,initial_y):
        self.x = initial_x
        self.y = initial_y
        self.velocity_x = 200
        self.velocity_y = 0
        self.width = 40
        self.hight = 40

    def draw(self):
        position = (self.x,self.y)
        rectangle=Rect(position,(self.width,self.hight))
        screen.draw.filled_rect(rectangle,randcolor)
#creating squere object
squere1 = Squere(100,100)

def draw():
    screen.clear()
    squere1.draw()


def update(count):
    #appling constant acceleration formila
    vel_y = squere1.velocity_y
    squere1.velocity_y += gravity * count
    squere1.y += (vel_y + squere1.velocity_y) * count * 2

    #detect and handle bounce
    if squere1.y > HEIGHT - squere1.width/2:
        squere1.y = HEIGHT - squere1.width/2
        squere1.velocity_y = -squere1.velocity_y *0.9
    squere1.x += squere1.velocity_x * count
    if squere1.x < squere1.width/2 or squere1.x > WIDTH - squere1.width/2:
        squere1.velocity_x = -squere1.velocity_x
pgzrun.go()