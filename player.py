import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame import K_UP, K_DOWN, K_LEFT, K_RIGHT, RLEACCEL

from laser import Laser

# Define a player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.score = 0
        self.surf = pygame.image.load("player.png").convert_alpha()
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.health = 100

    def update(self, key):
        if key[K_UP]:
            self.rect.move_ip(0, -5)
        if key[K_DOWN]:
            self.rect.move_ip(0, 5)
        if key[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if key[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Keep player on the screen
        self.rect = self.rect.clamp([0, 0, SCREEN_WIDTH, SCREEN_HEIGHT])

    def shoot(self):
        return Laser(self.rect.right, self.rect.centery)

    def hit(self, health):
        self.health -= health
        if self.health <= 0:
            self.kill()

    def health_boost(self):
        self.health += 10
        if self.health > 100:
            self.health = 100
