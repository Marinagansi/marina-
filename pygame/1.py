import pygame
import random
import math


#initialize pygame
pygame.init()

#create the screen
screen=pygame.display.set_mode((800,600))
#create backggroung
background=pygame.image.load("sb.png")

#title and icon
pygame.display.set_caption("space invader")
icon=pygame. image.load('facebook.png')
pygame.display.set_icon(icon)

#adding playyer
playerImg= pygame.image.load('spaceship.png')
playerX=370
playerY=480
playerX_change=0

#adding enemy
enemyImg=pygame.image.load("foot-clan (1).png")
enemyX=random.randint(0,800)
enemyY=random.randint(50,150)
#increase the speed of enemy according to need
enemyX_change=1
enemyY_change=10

#addin bullet
bulletImg=pygame.image.load("bullet.png")
bulletX=0
bulletY=480
bulletX_change=0
bulletY_change=3

#ready state= you can't see bullet on screen
#fire state= bullet moving currently
bullet_state= "ready"
score=0



def player(x,y):

    #blit--draw
    screen.blit(playerImg,(x,y))

def enemy(x,y):
    #blit---draw
    screen.blit(enemyImg,(x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bulletImg,(x+16,y+10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2)) + (math.pow(enemyY - bulletY,2)))
    if distance < 27:
        return True
    else:
        return False



running =True

while running:
#rgb clor background
    screen.fill((108, 0, 58))

#background img makes speed low----> need to increase speed
    screen.blit(background,(0,-70))

    # playerX +=0.1
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
#coonect to keyboard
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerX_change=-1
            if event.key==pygame.K_RIGHT:
                playerX_change=1
            if event.key== pygame.K_SPACE:
                #get the current  x coordinate of spaceship
                bulletX=playerX
                fire_bullet(bulletX,bulletY)
        if event.type==pygame.KEYUP:

            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerX_change=0

    playerX +=playerX_change

# Collision
    collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        # Reset the bullet
        bulletY = 480
        bullet_state = "ready"
        score += 1
        print(score)
        enemyX = random.randint(0,735)
        enemyY = random.randint(50,150)
#creating boundaries
    if playerX<=0:
        playerX=0
    elif playerX>=736:
        playerX=736
    #enemy movemnet
    enemyX += enemyX_change
#bullet movement

    if bulletY <=0:
        bulletY=480
        bullet_state="ready"

    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change
    #creating boundaries
    if enemyX <=0:
        enemyX_change=2
        enemyY +=enemyY_change
    elif enemyX >=736:
        enemyX_change=-2
        enemyY +=enemyY_change

    player(playerX,playerY)
    enemy(enemyX,enemyY)

    pygame.display.update()