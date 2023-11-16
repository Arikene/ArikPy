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
    dX = (math.pow((player2_X - bulletX), 2))
    dY = (math.pow((player2_Y - bulletY), 2))
    distance = math.sqrt(dX+dY) #Actually it's indicating player's body size, Where the bullet will stop
    if distance <10 :
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




# Game loop
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

        # Check for collision between bullet and player2
    collision = iscollision(player2_x, player2_y, bulletX, bulletY)
    if collision:
        bullet_status = "ready"  # Reset the bullet
        score_value += 1  # Increase the score

    # Bullet loop
    if keys[pygame.K_SPACE]:
        if bullet_status == "ready":
            bulletX = player1_x + 30  # Adjusted the starting position of the bullet
            bulletY = player1_y
            bullet_status = "fire"

    # Move the bullet
    if bullet_status == "fire":
        bulletX += bulletX_change
        # Reset bullet when it goes off the screen
        if bulletX >= 626:
            bullet_status = "ready"

    # Boundary checking for player 2
    player2_x = max(0, min(player2_x, 626 - 78))
    player2_y = max(0, min(player2_y, 436 - 76))

    # Clear the screen
    screen.blit(background, (0, 0))

    # Draw players
    draw_player(player1_x, player1_y, player1_img)
    draw_player(player2_x, player2_y, player2_img)

    # Draw bullet only when it's fired
    if bullet_status == "fire":
        draw_bullet(bulletX, bulletY, bulletimg)

    # Update the display
    pygame.display.update()

    # Control frame rate
    Clock.tick(60)

pygame.quit()
