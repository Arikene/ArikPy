import pygame
import math

# Initialize pygame
pygame.init()

# Displaying pygame on the screen
screen = pygame.display.set_mode((626, 436))

# Icon
glowingBall = pygame.image.load("1057917_glowing-ball-png.jpg")
pygame.display.set_icon(glowingBall)

# Title
pygame.display.set_caption("Arik's Hockey lab")

# Background image
background = pygame.image.load("2.png")

# Player 1
player1_img = pygame.image.load("naruto2.png")
player1_x = 75
player1_y = 150
player1_speed = 5  # Adjust this value as needed

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
bulletX_change_player2 = -10  # Adjust this value as needed
bulletY_change_player2 = 0
bullet_status_player2 = "ready"

# Function to draw a bullet for player 2
def draw_bullet_player2(x, y, img):
    screen.blit(img, (x, y))


#score
score_value = 0
font = pygame.font.SysFont('freesansbold.ttf', 32)
textX = 600
textY = 100


# Create a clock object to control frame rate
Clock = pygame.time.Clock()

# Function to draw a player
def draw_player(x, y, img):
    screen.blit(img, (x, y))

# Function to draw a bullet
def draw_bullet(x, y, img):
    screen.blit(img, (x, y))

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


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255,255,255))
    screen.fill((0,0,0))
    screen.blit(score, (x, y))

def game_over():
    go = font.render("GAME OVER", True, (255,255,255))
    screen.blit(go, (290, 300))




# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player 1 movement (arrow keys)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player1_x -= player1_speed
    if keys[pygame.K_RIGHT]:
        player1_x += player1_speed
    if keys[pygame.K_UP]:
        player1_y -= player1_speed
    if keys[pygame.K_DOWN]:
        player1_y += player1_speed

    # Boundary checking for player 1
    player1_x = max(0, min(player1_x, 626 - 70))
    player1_y = max(0, min(player1_y, 436 - 76))

    # Handle player 2 movement (WASD keys)
    if keys[pygame.K_a]:
        player2_x -= player2_speed
    if keys[pygame.K_d]:
        player2_x += player2_speed
    if keys[pygame.K_w]:
        player2_y -= player2_speed
    if keys[pygame.K_s]:
        player2_y += player2_speed
    # Boundary checking for player 2
    player2_x = max(0, min(player2_x, 626 - 78))
    player2_y = max(0, min(player2_y, 436 - 76))

    # Check for collision between bullet and player2
    collision = iscollision(player2_x, player2_y, bulletX, bulletY)
    if collision:
        bullet_status = "ready"  # Reset Player 1's bullet
        score_value += 1  # Increase the score

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
        bullet_status_player2 = "ready"  # Reset Player 2's bullet
        # Perform actions when player1 is hit by player2's bullet (e.g., decrease player1's health)

    # Bullet loop for player 2
    if keys[pygame.K_RSHIFT]:
        if bullet_status_player2 == "ready":
            bulletX_player2 = player2_x - 30  # Adjusted the starting position of Player 2's bullet
            bulletY_player2 = player2_y
            bullet_status_player2 = "fire"

    # Move Player 2's bullet
    if bullet_status_player2 == "fire":
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

    # Update the display
    pygame.display.update()

    # Control frame rate
    Clock.tick(60)

pygame.quit()
