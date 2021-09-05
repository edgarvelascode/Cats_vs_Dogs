import os
import pygame
from config import *
from Bullet import *
from main import bullet_group


def draw_bg():
    screen.blit(YARD, (0, 0))


class Player(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, speed, ammo, specials, scale):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.hit = False
        self.char_type = char_type
        self.speed = speed
        self.ammo = ammo
        self.start_ammo = ammo
        self.shoot_cooldown = 0
        self.specials = specials
        self.health = 10
        self.max_health = self.health
        self.direction = 1
        # self.vel.y = 0
        self.flip = False
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

        # load all images for the players
        animation_types = ['Attack', "Bullet", 'Death', 'Hit', 'Idle', 'Moving']
        for animation in animation_types:
            # reset temporary list of images
            temp_list = []
            # count number of files in the folder
            num_of_frames = len(os.listdir(f'chars/{self.char_type}/{animation}'))
            for i in range(num_of_frames):
                img = pygame.image.load(f'chars/{self.char_type}/{animation}/{i}.png').convert_alpha()
                img = pygame.transform.scale(img, (int(img.get_width() * scale), (int(img.get_height() * scale))))
                temp_list.append(img)
            self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def player(self):
        self.player()

    def update(self):
        self.update_animation()
        self.check_alive()
        self.check_hit()

        # update cooldown
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

    def move(self, moving_left, moving_right, moving_up, moving_down):

        # reset movement variables
        dx = 0
        dy = 0

        # assign movement variables if moving left or right
        if moving_left and player_one.rect.x > 30:
            dx = -7
            self.flip = False
            self.direction = 1
        if moving_right and (player_one.rect.x < (WIDTH/2 - 50)):
            dx = 7
            self.flip = False
            self.direction = -1

        if moving_up and player_one.rect.top > 0:
            dy = -7
        if moving_down and player_one.rect.bottom + 100 < 900:
            dy = 7

        self.rect.x += dx
        self.rect.y += dy

    def shoot(self):
        if self.shoot_cooldown == 0 and self.ammo > 0:
            self.shoot_cooldown = 10
            bullet = Bullet(self.rect.centerx + (0.6 * self.rect.size[1] * self.direction), self.rect.centery, self.direction)
            bullet_group.add(bullet)

            # reduce ammo
            self.ammo -= 1

    def update_animation(self):
        # update animation
        ANIMATION_COOLDOWN = 50
        # update img depending on current frame
        self.image = self.animation_list[self.action][self.frame_index]
        # check if enough time has passed since last update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        # if the animation has run out restart from the start
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 3:
                self.frame_index = 0

        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 2:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.frame_index = 0

    def update_action(self, new_action):
        # check if the new action is different to previous
        if new_action != self.action:
            self.action = new_action
            # update animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

    def check_alive(self):
        if self.health <= 0:
            self.health = 0
            self.speed = 0
            self.alive = False
            self.update_action(2)

    def check_hit(self):
        if self.health == (9,0):
            self.hit = True
            self.speed = -1
            self.update_action(3)

    def update_animation(self):
        # update animation
        ANIMATION_COOLDOWN = 50
        # update img depending on current frame
        self.image = self.animation_list[self.action][self.frame_index]
        # check if enough time has passed since last update
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        # if the animation has run out restart from the start
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 3:
                self.frame_index = 0

        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 2:
                self.frame_index = len(self.animation_list[self.action]) - 1
            else:
                self.frame_index = 0

    def update_action(self, new_action):
        # check if the new action is different to previous
        if new_action != self.action:
            self.action = new_action
            # update animation settings
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

    def check_alive(self):
        if self.health <= 0:
            self.health = 0
            self.speed = 0
            self.alive = False
            self.update_action(2)

    def check_hit(self):
        if self.health == (9, 0):
            self.hit = True
            self.speed = -1
            self.update_action(3)


player_one = Player('cat', 200, 350, 5, 30, 10, 3)
player_two = Player('corgi', 1200, 350, 7, 150, 10, 3)