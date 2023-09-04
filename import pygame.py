import pygame
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

# Create a clock object to control frame rate
Clock = pygame.time.Clock()

# Function to draw a player
def draw_player(x, y, img):
    screen.blit(img, (x, y))

#Bulletimg
bulletimg = pygame.image.load('rasengan1.png')
bulletX = 75 
bulletY = 150
bulletX_change = 1
bulletY_change = 5
bullet_status = "ready"

def fire_bullet(x, y, img):
    global bullet_status
    bullet_status = "fire"
    screen.blit(bulletimg, (player1_x, player1_y - 10))

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
    player1_x = max(0, min(player1_x, 323 - 70))
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
#Bullet loop
    if keys[pygame.K_SPACE]:
      bullet_status = 'fire'
      bulletX += bulletX_change              

    # Boundary checking for player 2
    player2_x = max(323, min(player2_x, 626-78))
    player2_y = max(0, min(player2_y, 436-76))

    # Clear the screen
    screen.blit(background, (0, 0))

    # Draw players
    draw_player(player1_x, player1_y, player1_img)
    draw_player(player2_x, player2_y, player2_img)
    fire_bullet(bulletX,bulletY, bulletimg)
    # Update the display
    pygame.display.update()

    # Control frame rate
    Clock.tick(60)

pygame.quit()

