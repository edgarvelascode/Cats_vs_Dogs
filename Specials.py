import pygame

class Specials(pygame.sprite.Sprite):
    def __init__(self, x, y,speed, image, direction):
        pygame.sprite.Sprite.__init__(self)
        self.timer = 35
        self.speed = speed
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction

    def update(self):
        dx = self.direction * self.speed

        # check for collision with walls
        if self.rect.left + dx < 0 or self.rect.right + dx > WIDTH:
            self.kill()
        # update specials location
        self.rect.x += dx

        #countdown timer
        self.timer -= 1
        if self.timer <= 0:
            self.kill()

        if pygame.sprite.spritecollide(player_one, specials_group, False):
            if player_one.alive:
                player_one.health -= 1
                self.kill()
        if pygame.sprite.spritecollide(player_two, specials_group, False):
            if player_two.alive:
                player_two.health -= 5
                self.kill()