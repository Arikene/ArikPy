import pygame
import math
import time
from video_inro import  play_video_intro
from level2 import  level2_level

video = 'final intro.mp4'
bgm = 'final intro.mp3'

play_video_intro(video,bgm)

pygame.init()
pygame.mixer.init()

# Displaying pygame on the screen
screen = pygame.display.set_mode((626, 436))

# Icon
glowingBall = pygame.image.load("1057917_glowing-ball-png.jpg")
pygame.display.set_icon(glowingBall)

# Title
pygame.display.set_caption("Arik's Hockey lab")

# Background image
background = pygame.image.load("2.png")

#music effect
super_bullet_sound = pygame.mixer.Sound("rasengan.mp3")
chidori_sound = pygame.mixer.Sound("fire].mp3")
dunno = pygame.mixer.Sound("naruto.mp3")
come = pygame.mixer.Sound("come.mp3")
half_chakra_sasuke =pygame.mixer.Sound("half chakra.mp3")
fight = pygame.mixer.music.load("Sasuke Fighting Theme.mp3")
lost = pygame.mixer.Sound("sasuke loses (2).mp3")

super_bullet_channel = pygame.mixer.Channel(1)
chidori_channel = pygame.mixer.Channel(1)
dunno_channel = pygame.mixer.Channel(1)
come_channel = pygame.mixer.Channel(1)
half_chakra_channel = pygame.mixer.Channel(1)
sasuke_loses_channel = pygame.mixer.Channel(1)


# Player 1
player1_img = pygame.image.load("naruto2.png")
player1_x = 75
player1_y = 150
player1_speed = 5  # Adjust this value as needed

# Players health
player1_health = 100
player2_health = 100
# Health bar configuration
health_bar_length = 100
health_bar_height = 10
health_bar_color = (255, 255, 255)  # white color

# Function to draw a health bar
def draw_health_bar(x, y, health):
    pygame.draw.rect(screen, health_bar_color, (x, y, health, health_bar_height))

# Player 2
player2_img = pygame.image.load("sasuke.png")
player2_x = 480
player2_y = 150
player2_speed = 5  # Adjust this value as needed

# Bulletimg
bulletimg = pygame.image.load('rasengan.png')
bulletX = 75
bulletY = 150
bulletX_change = 15  # Adjust this value as needed
bulletY_change = 0
bullet_status = "ready"

# Bulletimg for player 2
bulletimg_player2 = pygame.image.load('chidori.png')
bulletX_player2 = 480
bulletY_player2 = 150
bulletX_change_player2 = -15  # Adjust this value as needed
bulletY_change_player2 = 0
bullet_status_player2 = "ready"

#Super Bullet for Super_Powers
super_bullet =pygame.image.load("Odama_rasengan.png")
super_bulletX = 75
super_bulletY = 150
super_bullet_X_change = 7
super_bullet_Y_change = 0
super_bullet_status = "ready"

#Super_Energy_Bar
super_energy = 0
super_energy_bar_length = 100
super_energy_bar_height = 10
super_energy_bar_color = (77, 210, 255)

#Super Bullet for Super_Powers
super_bullet2 =pygame.image.load("fireball.png")
super_bulletX2 = 480
super_bulletY2 = 150
super_bullet_X2_change = -7
super_bullet_Y2_change = 0
super_bullet_status2 = "ready"

#Super_Energy_Bar
super_energy2 = 0
super_energy_bar_length2 = 100
super_energy_bar_height2 = 10
super_energy_bar_color2 = (255, 187, 51)


# Super Energy regeneration variables
regeneration_rate = 1  # health points per second
last_regeneration_time = time.time() #The current time

# Super Energy regeneration variables
regeneration_rate2 = 1  # health points per second
last_regeneration_time2 = time.time()

#supper_bullet_bar
def draw_super_bullet_bar(x, y, super_energy, max_super_energy):
    # Calculate the width of the super energy bar based on the current super energy level
    super_energy_width = (super_energy / max_super_energy) * super_energy_bar_length
    pygame.draw.rect(screen, super_energy_bar_color, (x, y, super_energy_width, super_energy_bar_height))

def draw_super_bullet_bar2(x, y, super_energy2, max_super_energy2):
    # Calculate the width of the super energy bar based on the current super energy level
    super_energy_width2 = (super_energy2 / max_super_energy2) * super_energy_bar_length2
    pygame.draw.rect(screen, super_energy_bar_color2, (x, y, super_energy_width2, super_energy_bar_height2))

# Function to draw a bullet for player 2
def draw_bullet_player2(x, y, img):
    screen.blit(img, (x, y))
#Function to draw the Super Bullet for player 1
def draw_super_bullet(x,y, img):
    screen.blit(img,(x,y))

def draw_super_bullet2(x,y, img):
    screen.blit(img,(x,y))

#score
score_value = 0
score_value2 = 0
font = pygame.font.SysFont('freesansbold.ttf', 32)
game_over_font = pygame.font.SysFont("ROBOTO.ttf",80)
textX = 200
textY = 300


# Create a clock object to control frame rate
Clock = pygame.time.Clock()

# Function to draw a player
def draw_player(x, y, img):
    screen.blit(img, (x, y))

# Function to draw a bullet
def draw_bullet(x, y, img):
    screen.blit(img, (x, y))

#
def iscollision(player2_X, player2_Y, bulletX, bulletY):
    dX = (math.pow((player2_X+20 - bulletX), 2)) #Use +20 , so that the bullet can touch the body
    dY = (math.pow((player2_Y+20 - bulletY), 2)) #Gotta make calculation using graph paper
    distance = math.sqrt(dX+dY) #Actually it's indicating player's body size, Where the bullet will stop
    if distance <25 :
        return True
    else:
        return False

def iscollision2(player1_X, player1_Y, bulletX, bulletY):
    dX = (math.pow((player1_X - bulletX), 2))
    dY = (math.pow((player1_Y+20 - bulletY), 2)) #Gotta make calculation using graph paper
    distance = math.sqrt(dX+dY) #Actually it's indicating player's body size, Where the bullet will stop
    if distance <42 :
        return True
    else:
        return False

def iscollision3(player2_X, player2_Y, super_bulletX, super_bulletY):
    dX = (math.pow((player2_X+20 - super_bulletX), 2)) #Use +20 , so that the bullet can touch the body
    dY = (math.pow((player2_Y+20 - super_bulletY), 2)) #Gotta make calculation using graph paper
    distance = math.sqrt(dX+dY) #Actually it's indicating player's body size, Where the bullet will stop
    if distance <25 :
        return True
    else:
        return False

def iscollision4(player1_X, player1_Y, super_bulletX2, super_bulletY2):
    dX = (math.pow((player1_X - super_bulletX2), 2))
    dY = (math.pow((player1_Y+20 - super_bulletY2), 2)) #Gotta make calculation using graph paper
    distance = math.sqrt(dX+dY) #Actually it's indicating player's body size, Where the bullet will stop
    if distance <42 :
        return True
    else:
        return False
def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255,255,255))
    screen.blit(score, (x, y))
def show_score2(x,y):
    score = font.render("Score: "+str(score_value2),True,(255,255,255))
    screen.blit(score,(x,y))
def game_won():
    won_text = game_over_font.render("Player 1 Wins!", True, (77, 210, 255))
    screen.blit(won_text, (120, 150))
    pygame.display.update()
    pygame.time.delay(3000)  # Display the message for 3 seconds

def game_won2():
    won_text = game_over_font.render("Player 2 Wins!", True, (255, 187, 51))
    screen.blit(won_text, (120, 150))
    pygame.display.update()
    pygame.time.delay(3000)  # Display the message for 3 seconds
    # level2_level()

come_channel.play(come)
pygame.mixer.music.load("Sasuke Fighting Theme.mp3")
pygame.mixer.music.set_volume(0.25)  # Set the volume (0.0 to 1.0)
pygame.mixer.music.play(-1)  # -1 means loop indefinitely


# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Super_energy regeneration logic
    current_time = time.time()  #Time's value is updated to current one's
    time_elapsed = current_time - last_regeneration_time  #The previous value of time when it was stored

    if time_elapsed >= 1/30: #firstly, this is checking if the elapsed time is equal or getter then 1/30 after firing the bullet. if it's true , then super_energy can regenerate. Secondly, it's diving the unit of 1 second to 1/30, if the value was 1 , 1 health point will increase 1 by 1 second
        super_energy += regeneration_rate
        super_energy = min(super_energy, 100)  # cap health at 100
        last_regeneration_time = current_time

    current_time2 = time.time()
    time_elapsed2 = current_time - last_regeneration_time2

    if time_elapsed2 >= 1/30:  # regenerate every second
        super_energy2 += regeneration_rate2
        super_energy2 = min(super_energy2, 100)  # cap health at 100
        last_regeneration_time2 = current_time2


    # Handle player 1 movement (WASD keys)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player1_x -= player1_speed
    if keys[pygame.K_d]:
        player1_x += player1_speed
    if keys[pygame.K_w]:
        player1_y -= player1_speed
    if keys[pygame.K_s]:
        player1_y += player1_speed

    # Boundary checking for player 1
    player1_x = max(0, min(player1_x, 313 - 70))
    player1_y = max(0, min(player1_y, 436 - 76))

    # Handle player 2 movement (arrow keys)
    if keys[pygame.K_LEFT]:
        player2_x -= player2_speed
    if keys[pygame.K_RIGHT]:
        player2_x += player2_speed
    if keys[pygame.K_UP]:
        player2_y -= player2_speed
    if keys[pygame.K_DOWN]:
        player2_y += player2_speed
    # Boundary checking for player 2
    player2_x = max(360-70, min(player2_x, 626 - 78))
    player2_y = max(0, min(player2_y, 436 - 76))


    # Check for space key press to throw super bullet
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] :
        if super_energy >= 100:  # Check if enough energy to fire
         if super_bullet_status == "ready":
            super_bulletX = player1_x
            super_bulletY = player1_y
            super_bullet_status = "fire"

    # Move the super bullet if it's fired
    if super_bullet_status == "fire":
        super_bulletX += super_bullet_X_change
        # super_bullet_channel.play(super_bullet_sound)
        # Decrease super energy when the super bullet is fired
        super_energy = max(super_energy - 20, 0)

    # Reset the super_bullet position when it goes off the screen
    if super_bulletX >= 626:
        super_bullet_status = "ready"

    # Check for space key press to throw super bullet2
    if keys[pygame.K_RCTRL]:
        if super_energy2 >= 100:  # Check if enough energy to fire
            if super_bullet_status2 == "ready":
                super_bulletX2 = player2_x
                super_bulletY2 = player2_y
                super_bullet_status2 = "fire"

        # Move the super bullet2 if it's fired
# I had made an indentation error here and the super_bullet wasn't firing automatically (Learn from Mistake)
    if super_bullet_status2 == "fire":
        super_bulletX2 += super_bullet_X2_change
        # chidori_channel.play(chidori_sound)
            # Decrease super energy when the super bullet is fired
        super_energy2 = max(super_energy2 - 100, 0)

        # Reset the super_bullet2 position when it goes off the screen
    if super_bulletX2 <= 0:
        super_bullet_status2 = "ready"


    collision3 = iscollision3(player2_x,player2_y,super_bulletX,super_bulletY)
    if collision3:
        super_bullet_channel.play(super_bullet_sound)
        super_bulletX = 75
        super_bullet_status = 'ready'
        score_value += 20
        player2_health -= 20

#Collsion for Super Bullet 2
    collision4 = iscollision4(player1_x,player1_y,super_bulletX2,super_bulletY2)
    if collision4:
        chidori_channel.play(chidori_sound)
        super_bulletX2 = 480
        super_bullet_status2 = 'ready'
        score_value2 += 20
        player1_health -= 20

    # Check for collision between bullet and player2
    collision = iscollision(player2_x, player2_y, bulletX, bulletY)
    if collision:
        dunno_channel.play(dunno)
        bulletX = 75
        bullet_status = "ready"  # Reset Player 1's bullet
        score_value += 1  # Increase the score
        player2_health -= 1 # Decrease health when hit
        # Check if player 2 health reaches zero
        if player2_health == 30 :
            half_chakra_channel.play(half_chakra_sasuke)
        if player2_health <= 20:
            half_chakra_channel.play(half_chakra_sasuke)
        if player2_health <=10:
            sasuke_loses_channel.play(lost)


    # Update health bar position
    health_bar_x1 = player1_x
    health_bar_y1 = player1_y - 20  # Adjust the position above the player
    #Super_energy_bar_position
    super_energy_bar_x1 = player1_x
    super_energy_bar_y1 = player1_y-40
    #super energy bar 2 position
    super_energy_bar_x2 = player2_x
    super_energy_bar_y2 = player2_y - 40
    #Super_Energy_bar_regeneration
    if super_energy == 100:
        super_bullet_status = "ready"

    if super_bullet_status == "fire":
        super_energy = 0

        # Super_Energy_bar_regeneration2
    if super_energy2 == 100:
        super_bullet_status2 = "ready"

    if super_bullet_status2 == "fire":
        super_energy2 = 0

    # Bullet loop for player 1
    if keys[pygame.K_LSHIFT]:
        if bullet_status == "ready":
            bulletX = player1_x + 30  # Adjusted the starting position of Player 1's bullet
            bulletY = player1_y
            bullet_status = "fire"

    # Move Player 1's bullet
    if bullet_status == "fire":
        # dunno_channel.play(dunno)
        bulletX += bulletX_change
        # Reset Player 1's bullet when it goes off the screen
        if bulletX >= 626:
            bullet_status = "ready"

    # Check for collision between bullet_player2 and player1
    collision_player2 = iscollision2(player1_x, player1_y, bulletX_player2, bulletY_player2)
    if collision_player2:
        dunno_channel.play(dunno)
        bulletX_player2 = 480
        bullet_status_player2 = "ready"  # Reset Player 2's bullet
        score_value2 += 1
        player1_health -= 1

    if player2_health <= 0:

        game_won()


    if player1_health <= 0:
        game_won2()
        # level2_level()
        # Perform actions when player1 is hit by player2's bullet (e.g., decrease player1's health)
        # Update health bar position
    health_bar_x2 = player2_x
    health_bar_y2 = player2_y - 20  # Adjust the position above the player


    # Bullet loop for player 2
    if keys[pygame.K_RSHIFT]:
        if bullet_status_player2 == "ready":
            bulletX_player2 = player2_x - 30  # Adjusted the starting position of Player 2's bullet
            bulletY_player2 = player2_y
            bullet_status_player2 = "fire"

    # Move Player 2's bullet
    if bullet_status_player2 == "fire":
        # dunno_channel.play(dunno)
        bulletX_player2 += bulletX_change_player2

        # Reset Player 2's bullet when it goes off the screen
        if bulletX_player2 <= 0:
            bullet_status_player2 = "ready"



    # Clear the screen
    screen.blit(background, (0, 0))

    # Draw players
    draw_player(player1_x, player1_y, player1_img)
    draw_player(player2_x, player2_y, player2_img)

    # Draw bullets
    if bullet_status == "fire":
        draw_bullet(bulletX, bulletY, bulletimg)
    if bullet_status_player2 == "fire":
        draw_bullet_player2(bulletX_player2, bulletY_player2, bulletimg_player2)
    if super_bullet_status == "fire":
        draw_super_bullet(super_bulletX,super_bulletY,super_bullet)
    if super_bullet_status2 == "fire":
        draw_super_bullet2(super_bulletX2,super_bulletY2,super_bullet2)
    # Draw health bar for player 1
    draw_health_bar(health_bar_x1, health_bar_y1, player1_health)
    draw_health_bar(health_bar_x2,health_bar_y2,player2_health)
    draw_super_bullet_bar(super_energy_bar_x1,super_energy_bar_y1,super_energy,100)
    draw_super_bullet_bar2(super_energy_bar_x2,super_energy_bar_y2,super_energy2,100)

    show_score(10,10)
    show_score2(520,10)
    # Update the display
    pygame.display.update()

    # Control frame rate
    Clock.tick(60)



pygame.quit()
