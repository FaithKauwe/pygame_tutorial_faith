# Import and initialize pygame
import pygame
import random  # Use random instead of randint
pygame.init()

# Configure the screen
screen = pygame.display.set_mode([500, 500])
# Get the clock
clock = pygame.time.Clock()

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
        self.rect.x = random.randint(50, 400)
        self.rect.y = -self.rect.height  # Reset to just above the screen

# Create an instance of Apple
apple = Apple()

# Create the game loop
running = True
while running:
    # Look at events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
  
    # Draw a circle
    screen.fill((255, 255, 255))
  
    # Move and draw the apple
    apple.move()  # Move the apple
    apple.render(screen)  # Render the apple
  
    # Update the window
    pygame.display.flip()
    # Tick the clock!
    clock.tick(60)

# Quit pygame
pygame.quit()

