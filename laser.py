import pygame

# Define the cloud object by extending pygame.sprite.Sprite
# Use an image for a better-looking sprite
class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Laser, self).__init__()
        self.surf = pygame.Surface((15, 2))
        self.surf.fill((255, 50, 50))
        self.rect = self.surf.get_rect()
        self.rect.left = x
        self.rect.top = y

    # Move the cloud based on a constant speed
    # Remove the cloud when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(10, 0)
        if self.rect.right < 0:
            self.kill()
