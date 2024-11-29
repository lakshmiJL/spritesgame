import pgzrun
from pgzhelper import *
from random import randint
WIDTH = 600
HEIGHT = 500

ash = Actor("ash")
ash.pos = (400,350)

pikachu = Actor("pika")
pikachu.pos = (700,800)
score = 0
game_over = False
def resize_actor(actor, new_width, new_heigth):
    # Resize and update the anchor point
    # See: https://www.pygame.org/docs/ref/transform.html#pygame.transform.scale
    actor._surf = pygame.transform.scale(actor._surf, (new_width, new_heigth))
    actor._update_pos()

def draw():
    screen.clear()
    screen.blit("background",(0,0))
    
    ash.draw()
    pikachu.draw()
    screen.draw.text("Score: " + str(score), color="black", topleft=(10,10))

    if game_over:
            screen.fill("pink")
            screen.draw.text("Time's Up! Your Final Score: " + str(score), midtop=(WIDTH/2,10), 
            fontsize=40, color="red")
def place_pikachu():
    pikachu.x = randint((WIDTH-70), 900)
    pikachu.y = randint((HEIGHT-70),900)


    
def time_up():
    global game_over 
    game_over = True

def update():
    global score
    resize_actor(ash,100,100)
    ash.draw()
    resize_actor(pikachu,100,100)
    pikachu.draw()

    if keyboard.left:
        ash.x = ash.x - 2
    if keyboard.right:
        ash.x = ash.x + 2
    if keyboard.up:
        ash.y = ash.y - 2
    if keyboard.down:
        ash.y = ash.y + 2

    pikachu_collected = ash.colliderect(pikachu)

    if pikachu_collected:
        score = score + 10
        place_pikachu()


clock.schedule(time_up, 60.0)
    

pgzrun.go()