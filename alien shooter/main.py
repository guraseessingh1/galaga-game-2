import pgzrun
import random



WIDTH = 1200
HEIGHT = 600
WHITE = (255,255,255)
BLUE = (0,0,255)

#creating actors

ship = Actor("galaga")
alien = Actor("bug")

ship.pos = (WIDTH//2,HEIGHT-60)

speed = 5 

0#creating a list for bullets
bullets = []

#creating the list of enemys
enemies = []

score=0
direction=1
ship.dead=False
ship.countdown=90

#creating enemys - 8 coloms and 4 rows

for x in range (8):
    for y in range (4):
        enemy=Actor("bug")
        enemies.append(enemy)
        enemies[-1].x = 100 + 50 * x
        enemies[-1].y = 80 + 50 * y

#updating score
def display_score():
    screen.draw.text(str(score),(30,50))

def gameover():
    screen.draw.text("Game over!!!",(250,300))
    

#pressing spacebar key to shoot bulets
def on_key_down(key):
    if ship.dead == False:
        if key == keys.SPACE:
            bullet = Actor("bullet")
            bullets.append(bullet)
            bullets[-1].x=ship.x
            bullets[-1].y=ship.y-50

def update():
    global score ,direction
    movedown = False
    #move the ship left # or right with arrow keys
    if ship.dead == False:
        if keyboard.left:
            ship.x-=speed
            if ship.x <= 0:
                ship.x = 0
        elif keyboard.right:
            ship.x+=speed
            if ship.x >=WIDTH:
                ship.x = WIDTH
    if keyboard.space:
        bullet = Actor("bullet")
        bullets.append(bullet)
        bullets[-1].x=ship.x
        bullets[-1].y=ship.y-50
    #moving bullets
    for bullet in bullets:
        if bullet.y <= 0:
            bullets.remove(bullet)

        else :
            bullet.y-=10
    for enemy in enemies:
        enemy.y+=5
        if enemy.y>= HEIGHT:
            enemy.y=-100
            enemy.x=random.randint(50,WIDTH-50)

def draw():
    screen.clear()
    screen.fill(BLUE)
    if ship.dead==False:
        ship.draw()
    for enemy in enemies:
        enemy.draw()
    for bullet in bullets:
        bullet.draw()
    if len(enemies) == 0:
        gameover()



pgzrun.go()






        
