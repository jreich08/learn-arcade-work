import pygame
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
GREEN = (34, 139, 34)
RED = (255, 0, 0)
PLAYER_SPEED = 5

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Amazon Adventure")

# Load images
player_img = pygame.image.load("player.png")  # Placeholder, replace with actual image
jaguar_img = pygame.image.load("jaguar.png")  # Placeholder, replace with actual image
fruit_img = pygame.image.load("fruit.png")  # Placeholder, replace with actual image

# Scale images
player_img = pygame.transform.scale(player_img, (50, 50))
jaguar_img = pygame.transform.scale(jaguar_img, (50, 50))
fruit_img = pygame.transform.scale(fruit_img, (30, 30))

# Player setup
player = pygame.Rect(WIDTH // 2, HEIGHT // 2, 50, 50)

# Jaguar setup
jaguar = pygame.Rect(random.randint(0, WIDTH - 50), random.randint(0, HEIGHT - 50), 50, 50)

# Fruit setup
fruit = pygame.Rect(random.randint(0, WIDTH - 30), random.randint(0, HEIGHT - 30), 30, 30)

# Game loop variables
running = True
score = 0
clock = pygame.time.Clock()

# Main game loop
while running:
    screen.fill(GREEN)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= PLAYER_SPEED
    if keys[pygame.K_RIGHT] and player.x < WIDTH - player.width:
        player.x += PLAYER_SPEED
    if keys[pygame.K_UP] and player.y > 0:
        player.y -= PLAYER_SPEED
    if keys[pygame.K_DOWN] and player.y < HEIGHT - player.height:
        player.y += PLAYER_SPEED

    # Check collision with fruit
    if player.colliderect(fruit):
        score += 1
        fruit.x, fruit.y = random.randint(0, WIDTH - 30), random.randint(0, HEIGHT - 30)

    # Check collision with jaguar
    if player.colliderect(jaguar):
        print("Game Over! Final Score:", score)
        running = False

    # Draw elements
    screen.blit(player_img, (player.x, player.y))
    screen.blit(jaguar_img, (jaguar.x, jaguar.y))
    screen.blit(fruit_img, (fruit.x, fruit.y))

    # Update display
    pygame.display.flip()
    clock.tick(30)

pygame.quit()