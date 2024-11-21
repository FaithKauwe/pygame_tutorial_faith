# Import and initialize pygame
import pygame
from random import random, randint, choice
pygame.init()

# Configure the screen
screen = pygame.display.set_mode([500, 500])
# Get the clock
clock = pygame.time.Clock()
lanes = [93, 218, 343]  # Lane positions for player movement

# Game Object Class
class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super(GameObject, self).__init__()
        self.surf = pygame.Surface((width, height))
        self.surf.fill((255, 0, 255))  # Default color, can be changed if using an image
        self.rect = self.surf.get_rect(topleft=(x, y))  # Set the position of the rect
        self.x = x
        self.y = y


    def render(self, screen):
        self.rect.x = self.x  # Update rect's x position
        self.rect.y = self.y  # Update rect's y position
        screen.blit(self.surf, self.rect.topleft)

# Strawberry Class
class Strawberry(GameObject):
    def __init__(self):
        # Load the strawberry image and set its size
        strawberry_image = pygame.image.load('strawberry.png')
        strawberry_width, strawberry_height = strawberry_image.get_size()
        super(Strawberry, self).__init__(randint(50, 400), -64, strawberry_width, strawberry_height)
        self.dy = (randint(0, 200) / 100) + 1

    def move(self):
        self.rect.y += self.dy  # Move down the screen
        if self.rect.y > 500:
            self.reset()

    def reset(self):
        self.rect.x = choice(lanes)  # Reset to one of the lanes
        self.rect.y = -64  # Reset to just above the screen

# Apple Class
class Apple(GameObject):
    def __init__(self):
        # Use the image dimensions instead of 0, 0 for the position
        apple_image = pygame.image.load('apple.png')
        apple_width, apple_height = apple_image.get_size()
        super(Apple, self).__init__(randint(50, 400), -64, apple_width, apple_height)
        self.dy = (randint(0, 200) / 100) + 1



    def move(self):
        self.rect.y += self.dy  # Move down the screen
        if self.rect.y > 500:
            self.reset()

    def reset(self):
        self.rect.x = choice(lanes)  # Reset to one of the lanes
        self.rect.y = -64  # Reset to just above the screen


# Player Class
class Player(GameObject):
    def __init__(self):
        super(Player, self).__init__(0, 0, 50, 50)  # Assuming 50x50 for player
        self.dx = 0
        self.dy = 0
        self.pos_x = 1  # Lane position for player
        self.reset()

    def left(self):
        if self.pos_x > 0:
            self.pos_x -= 1
            self.update_dx_dy()

    def right(self):
        if self.pos_x < len(lanes) - 1:
            self.pos_x += 1
            self.update_dx_dy()

    def move(self):
        self.x = lanes[self.pos_x]  # Update x to current lane
        self.reset()  # Update position based on current lane

    def reset(self):
        self.x = lanes[self.pos_x]
        self.y = 343  # Position player on the lane vertically

    def update_dx_dy(self):
        self.dx = lanes[self.pos_x]

class Bomb(GameObject):
    def __init__(self):
        # Load the bomb image and set its size (assuming bomb.png exists)
        bomb_image = pygame.image.load('bomb.png')  # Replace with your actual bomb image filename
        bomb_width, bomb_height = bomb_image.get_size()
        super(Bomb, self).__init__(randint(50, 400), -64, bomb_width, bomb_height)
        self.dy = (randint(1, 200) / 100) + 2  # Adjust falling speed if needed

    def move(self):
        self.rect.y += self.dy  # Move bomb down the screen
        if self.rect.y > 500:  # Reset bomb position when it goes off screen
            self.reset()

    def reset(self):
        self.rect.x = choice(lanes)  # Reset to a lane
        self.rect.y = -self.rect.height  # Reset to just above the screen


# Create instances of Fruit and Player
apple = Apple()
strawberry = Strawberry()
player = Player()
bomb = Bomb()

# Create groups for sprites
all_sprites = pygame.sprite.Group()
fruit_sprites = pygame.sprite.Group()  # Group for fruit

# Add sprites to the groups
all_sprites.add(player)
all_sprites.add(apple)
all_sprites.add(strawberry)
all_sprites.add(bomb)
fruit_sprites.add(apple)
fruit_sprites.add(strawberry)

# Create the game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_LEFT:
                player.left()
            elif event.key == pygame.K_RIGHT:
                player.right()

    # Clear the screen
    screen.fill((255, 255, 255))

    # Move and render Sprites
    for entity in all_sprites:
        entity.move()  # Update position based on movement logic
        entity.render(screen)  # Render the entity

    # Check for collisions between player and fruit
    fruit = pygame.sprite.spritecollideany(player, fruit_sprites)
    if fruit:
        fruit.reset()  # Reset the fruit if a collision occurs

    # Check collision between player and bomb (if bomb sprite is defined)
    if pygame.sprite.collide_rect(player, bomb):  # Assume bomb is defined somewhere
        running = False  # End game if player collides with the bomb

    # Update the window
    pygame.display.flip()
    clock.tick(60)  # Maintain 60 FPS

# Quit pygame
pygame.quit()

