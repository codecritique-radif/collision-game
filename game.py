import pygame
import sys

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))  # Red square for player
        self.rect = self.image.get_rect()
        self.rect.center = (250, 250)

    def update(self):
        # Player movement logic here
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 0, 255))  # Blue square for enemy
        self.rect = self.image.get_rect()
        self.rect.center = (400, 400)

    def update(self):
        # Enemy movement logic here
        self.rect.x -= 2

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Create player and enemy objects
player = Player()
enemy = Enemy()

# Create sprite groups
all_sprites = pygame.sprite.Group()
all_sprites.add(player, enemy)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update player and enemy
    all_sprites.update()

    # Check for collision
    if pygame.sprite.collide_rect(player, enemy):
        print("Collision detected! Game Over.")
        running = False

    # Render
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

# Quit the game
pygame.quit()
sys.exit()