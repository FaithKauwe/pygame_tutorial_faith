# Import and initialize pygame
import pygame
from random import random, randint, choice
pygame.init()

# Configure the screen
screen = pygame.display.set_mode([500, 500])
# Get the clock
clock = pygame.time.Clock()
lanes = [93, 218, 343]
class GameObject(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super(GameObject, self).__init__()
        self.surf = pygame.Surface((width, height))
        self.surf.fill((255, 0, 255))  # Default color, can be changed if using an image
        self.rect = self.surf.get_rect(topleft=(x, y))  # Set the position of the rect

    def render(self, screen):
        screen.blit(self.surf, self.rect.topleft)

class Apple(GameObject):
    def __init__(self):
        # Use the image dimensions instead of 0, 0 for the position
        apple_image = pygame.image.load('apple.png')
        apple_width, apple_height = apple_image.get_size()
        super(Apple, self).__init__(random.randint(50, 400), -64, apple_width, apple_height)
        self.dy = (random.randint(0, 200) / 100) + 1

    def move(self):
        self.rect.y += self.dy  # Move down the screen
        # Check the y position of the apple
        if self.rect.y > 500:
            self.reset()

    def reset(self):
        self.x = choice(lanes)
        self.y = -64
   
class Strawberry(GameObject):
    def __init__(self):
        # Load the strawberry image and set its size
        strawberry_image = pygame.image.load('strawberry.png')
        strawberry_width, strawberry_height = strawberry_image.get_size()
        super(Strawberry, self).__init__(random.randint(50, 400), -64, strawberry_width, strawberry_height)
        self.dy = (random.randint(0, 200) / 100) + 1
    
    def move(self):
        self.rect.y += self.dy  # Move down the screen
        if self.rect.y > 500:
            self.reset()
    
    def reset(self):
        self.rect.x = -64  # Reset horizontal position
        self.rect.y = random.randint(50, 400)  # Reset to just above the screen


class Player(GameObject):
  def __init__(self):
        super(Player, self).__init__(0, 0, 'player.png')
        self.dx = 0
        self.dy = 0
        self.pos_x = 1 # new attribute
        self.pos_y = 1 # new attribute
        self.reset()

  def left(self):
    if self.pos_x > 0:
            self.pos_x -= 1
            self.update_dx_dy()

  def right(self):
    if self.pos_x < len(lanes) - 1:
            self.pos_x += 1
            self.update_dx_dy()

  def up(self):
    if self.pos_y > 0:
            self.pos_y -= 1
            self.update_dx_dy()

  def down(self):
    if self.pos_y < len(lanes) - 1:
            self.pos_y += 1
            self.update_dx_dy()

  def move(self):
    self.x -= (self.x - self.dx) * 0.25
    self.y -= (self.y - self.dy) * 0.25

  def reset(self):
        self.x = lanes[self.pos_x]
        self.y = lanes[self.pos_y]
        self.dx = self.x
        self.dy = self.y
  def update_dx_dy(self):
        self.dx = lanes[self.pos_x]
        self.dy = lanes[self.pos_y]
# Create an instance of Apple
apple = Apple()
# create an instance of Strawberry
strawberry = Strawberry()
# make an instance of Player
player = Player()

# Make a group
all_sprites = pygame.sprite.Group()
# Add sprites to group outside the game loop since it only needs to happen once
all_sprites.add(player)
all_sprites.add(apple)
all_sprites.add(strawberry)
# Create the game loop
running = True
while running:
  # Looks at events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    # Check for event type KEYBOARD
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        running = False
      elif event.key == pygame.K_LEFT:
        print('LEFT')
      elif event.key == pygame.K_RIGHT:
        print('RIGHT')
      elif event.key == pygame.K_UP:
        print('UP')
      elif event.key == pygame.K_DOWN:
        print('DOWN')
  
    # Clear screen
screen.fill((255, 255, 255))
# Move and render Sprites
for entity in all_sprites:
	entity.move()
	entity.render(screen)
# Update the window
pygame.display.flip()
    

# Quit pygame
pygame.quit()

