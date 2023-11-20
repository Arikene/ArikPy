import pygame
import math
import time
# Initialize pygame
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
chidori_sound = pygame.mixer.Sound("chidori (.mp3")



super_bullet_channel = pygame.mixer.Channel(0)
chidori_channel = pygame.mixer.Channel(1)


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
bulletX_change = 10  # Adjust this value as needed
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
super_energy_bar_color = (255, 0, 0)

# Super Energy regeneration variables
regeneration_rate = 20  # health points per second
last_regeneration_time = time.time()

#supper_bullet_bar
def draw_super_bullet_bar(x, y, super_energy, max_super_energy):
    # Calculate the width of the super energy bar based on the current super energy level
    super_energy_width = (super_energy / max_super_energy) * super_energy_bar_length
    pygame.draw.rect(screen, super_energy_bar_color, (x, y, super_energy_width, super_energy_bar_height))

# Function to draw a bullet for player 2
def draw_bullet_player2(x, y, img):
    screen.blit(img, (x, y))
#Function to draw the Super Bullet for player 1
def draw_super_bullet(x,y, img):
    screen.blit(img,(x,y))

#score
score_value = 0
score_value2 = 0
font = pygame.font.SysFont('freesansbold.ttf', 32)
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


# def iscollision(player2_X, player2_Y, bulletX, bulletY):
#     if player2_X == bulletX and player2_Y == bulletY:
#         return True
#     else:
#         False
#
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


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255,255,255))
    screen.blit(score, (x, y))
def show_score2(x,y):
    score = font.render("Score: "+str(score_value2),True,(255,255,255))
    screen.blit(score,(x,y))
def game_won():
    won_text = font.render("Player 1 Wins!", True, (174, 167, 167))
    screen.blit(won_text, (200, 300))
    pygame.display.update()
    pygame.time.delay(3000)  # Display the message for 3 seconds

def game_won2():
    won_text = font.render("Player 2 Wins!", True, (174, 167, 167))
    screen.blit(won_text, (200, 300))
    pygame.display.update()
    pygame.time.delay(3000)  # Display the message for 3 seconds

# def game_over():
#     font = pygame.font.SysFont('freesansbold.ttf', 64)
#     go_text = font.render("GAME OVER", True, (255, 255, 255))
#     screen.blit(go_text, (200, 200))
#     pygame.display.update
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
    current_time = time.time()
    time_elapsed = current_time - last_regeneration_time

    if time_elapsed >= 1:  # regenerate every second
        super_energy += regeneration_rate
        super_energy = min(super_energy, 100)  # cap health at 100
        last_regeneration_time = current_time


    # Handle player 1 movement (arrow keys)
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
    player1_x = max(0, min(player1_x, 626 - 70))
    player1_y = max(0, min(player1_y, 436 - 76))

    # Handle player 2 movement (WASD keys)
    if keys[pygame.K_LEFT]:
        player2_x -= player2_speed
    if keys[pygame.K_RIGHT]:
        player2_x += player2_speed
    if keys[pygame.K_UP]:
        player2_y -= player2_speed
    if keys[pygame.K_DOWN]:
        player2_y += player2_speed
    # Boundary checking for player 2
    player2_x = max(0, min(player2_x, 626 - 78))
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
        # Decrease super energy when the super bullet is fired
        super_energy = max(super_energy - 20, 0)
        super_bullet_channel.play(super_bullet_sound)
    # Reset the super_bullet position when it goes off the screen
    if super_bulletX >= 626:
        super_bullet_status = "ready"

    collision3 = iscollision3(player2_x,player2_y,super_bulletX,super_bulletY)
    if collision3:
        super_bulletX = 75
        super_bullet_status = 'ready'
        score_value += 20
        player2_health -= 20

    # Check for collision between bullet and player2
    collision = iscollision(player2_x, player2_y, bulletX, bulletY)
    if collision:
        bulletX = 75
        bullet_status = "ready"  # Reset Player 1's bullet
        score_value += 1  # Increase the score
        player2_health -= 1 # Decrease health when hit
        # Check if player 2 health reaches zero


    # Update health bar position
    health_bar_x1 = player1_x
    health_bar_y1 = player1_y - 20  # Adjust the position above the player
    #Super_energy_bar_position
    super_energy_bar_x1 = player1_x
    super_energy_bar_y1 = player1_y-40
    #Super_Energy_bar_regeneration
    if super_energy == 100:
        super_bullet_status = "ready"

    if super_bullet_status == "fire":
        super_energy = 0

    # Bullet loop for player 1
    if keys[pygame.K_LSHIFT]:
        if bullet_status == "ready":
            bulletX = player1_x + 30  # Adjusted the starting position of Player 1's bullet
            bulletY = player1_y
            bullet_status = "fire"

    # Move Player 1's bullet
    if bullet_status == "fire":
        bulletX += bulletX_change
        # Reset Player 1's bullet when it goes off the screen
        if bulletX >= 626:
            bullet_status = "ready"

    # Check for collision between bullet_player2 and player1
    collision_player2 = iscollision2(player1_x, player1_y, bulletX_player2, bulletY_player2)
    if collision_player2:
        bulletX_player2 = 480
        bullet_status_player2 = "ready"  # Reset Player 2's bullet
        score_value2 += 1
        player1_health -= 1

    if player2_health <= 0:
        game_won()

    if player1_health <= 0:
        game_won2()

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
        bulletX_player2 += bulletX_change_player2
        chidori_channel.play(chidori_sound)
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
    # Draw health bar for player 1
    draw_health_bar(health_bar_x1, health_bar_y1, player1_health)
    draw_health_bar(health_bar_x2,health_bar_y2,player2_health)
    draw_super_bullet_bar(super_energy_bar_x1,super_energy_bar_y1,super_energy,100)

    show_score(10,10)
    show_score2(520,10)
    # Update the display
    pygame.display.update()

    # Control frame rate
    Clock.tick(60)

pygame.quit()
