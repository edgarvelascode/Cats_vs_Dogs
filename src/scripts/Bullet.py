import pygame
from config import *
from Player import *
from main import bullet_group


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 15
        self.image = cat_bullet
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction
        self.player_one = player_one
        self.player_two = player_two

    def update(self):
        # move bullet
        self.rect.x += (self.direction * self.speed)

        # check if bullet has gone off screen
        if self.rect.right > WIDTH or self.rect.left < 0:
            self.kill()

        # check collision with characters
        if pygame.sprite.spritecollide(player_one, bullet_group, False):
            if player_one.alive:
                player_one.health -= 1
                self.kill()
        if pygame.sprite.spritecollide(player_two, bullet_group, False):
            if player_two.alive:
                player_two.health -= 1
                self.kill()
