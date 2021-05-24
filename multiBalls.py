import pygame,random,math
pygame.init()

white = 255,255,255
green = 0,255,0
red = 255,0,0
blue = 0,0,255

width = 800
height = 400

class Ball:
    balls_list = []
    def __init__(self):  #initialize the newly created object
        self.x = random.randint(0,width)
        self.y = random.randint(0,height)
        self.moveX = random.randint(1,10) 
        self.moveY = random.randint(1,10)
        self.color = random.randint(0,255) ,random.randint(0,255) ,random.randint(0,255) 
        self.radius = random.randint(10,50)

    def updateBall(self):
        self.x = self.x + self.moveX
        self.y = self.y + self.moveY
        if self.y > height - self.radius:
            self.moveY = random.randint(-10,-1) 
        elif self.x > width - self.radius:
            self.moveX = random.randint(-10,-1) 
        elif self.x < self.radius:
            self.moveX = random.randint(1,10) 
        elif self.y < self.radius:
            self.moveY = random.randint(1,10) 

    def collide(self, ball2):
        if (math.sqrt( ((ball2.x - self.x) **2) + ((ball2.y - self.y) ** 2) ) ) <= ball2.radius + self.radius:
            # ball2.moveX = ball2.moveX * -1
            # ball2.moveY = ball2.moveY * -1
            # self.moveX = self.moveX * -1
            # self.moveY = self.moveY * -1
            ball2.moveX = random.randint(-10,10)
            ball2.moveY = random.randint(-10,10)
            self.moveX = random.randint(-10,10)
            self.moveY = random.randint(-10,10)

screen = pygame.display.set_mode((width,height))

ballsList = [Ball() for i in range(100)]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(white)

    for currentBall in ballsList:
        pygame.draw.circle(screen, currentBall.color, (currentBall.x, currentBall.y), currentBall.radius)
        currentBall.updateBall()

        for ball in ballsList:
            if ball != currentBall:
                currentBall.collide(ball)

    pygame.display.update()
