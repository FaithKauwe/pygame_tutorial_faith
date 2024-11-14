# Example 2

# Import and initialize pygame
import pygame
pygame.init()
# Configure the screen
screen = pygame.display.set_mode([500, 500])

class GameObject(pygame.sprite.Sprite):
  def __init__(self, x, y, width, height):
    super(GameObject, self).__init__()
    self.surf = pygame.Surface((width, height))
    self.surf.fill((255, 0, 255))
    self.rect = self.surf.get_rect()
    self.x = x
    self.y = y

  def render(self, screen):
    screen.blit(self.surf, (self.x, self.y))
# Make an instance of GameObject

box = GameObject(120, 300, 50, 50)
# Creat the game loop
running = True
while running:
  # Looks at events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      
  # Draw a circle
  screen.fill((255, 255, 255))
  # Draw box
  box.render(screen)
  
  # Update the window
  pygame.display.flip()