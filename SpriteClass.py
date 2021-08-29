import os
import pygame
from config import *





def draw_bg():
    screen.blit(YARD, (0,0))


class Player1(pygame.sprite.Sprite):
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
            #reset temporary list of images
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

# class ItemBox(pygame.sprite.Sprite):
#     def __init__(self, item_type, x, y):
#         pygame.sprite.Sprite.__init__(self)
#         self.item_type = item_type
#         self.image = item_boxes[self.item_type]
#         self.rect = self.image.get_rect()
#         self.rect.midtop = (x + TILE_SIZE//2, y + (TILE_SIZE - self.image.get_height()))

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 15
        self.image = cat_bullet
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction

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


class Player2(pygame.sprite.Sprite):
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
            #reset temporary list of images
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

    def update(self):
        self.update_animation()
        self.check_alive()
        self.check_hit()


        # update cooldown
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

    def move2(self, moving_left2, moving_right2, moving_up2, moving_down2):
        # reset movement variables
        dx2 = 0
        dy2 = 0
        if moving_left2 and (player_two.rect.x - (WIDTH/2 + 20)) > 0:
            dx2 = -self.speed
            self.flip = False
            self.direction = -1
        if moving_right2 and (player_two.rect.x < (WIDTH - 80)):
            dx2 = self.speed
            self.flip = False
            self.direction = 1

        if moving_up2 and player_two.rect.top > 30:
            dy2 = -self.speed
        if moving_down2 and player_two.rect.bottom + 100 < 900:
            dy2 = self.speed

        # update rectangle position
        self.rect.x += dx2
        self.rect.y += dy2

    # def shoot2(self):
    #     if self.shoot_cooldown == 0 and self.ammo > 0:
    #         self.shoot_cooldown = 100
    #         bullet = Bullet(self.rect.centerx + (0.6 * self.rect.size[0] * self.direction), self.rect.centery, self.direction)
    #         bullet_group2.add(bullet2)
    #         # reduce ammo
    #         self.ammo -= 1

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

# class ItemBox(pygame.sprite.Sprite):
#     def __init__(self, item_type, x, y):
#         pygame.sprite.Sprite.__init__(self)
#         self.item_type = item_type
#         self.image = item_boxes[self.item_type]
#         self.rect = self.image.get_rect()
#         self.rect.midtop = (x + TILE_SIZE//2, y + (TILE_SIZE - self.image.get_height()))


class Bullet2(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 15
        self.image = cat_bullet
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction

    def update(self):
        # move bullet
        self.rect.x += (self.direction * self.speed)
        # check if bullet has gone off screen
        if self.rect.right < 0 or self.rect.left > WIDTH:
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

# class Specials(pygame.sprite.Sprite):
#     def __init__(self, x, y,speed, image, direction):
#         pygame.sprite.Sprite.__init__(self)
#         self.timer = 35
#         self.speed = speed
#         self.image = image
#         self.rect = self.image.get_rect()
#         self.rect.center = (x, y)
#         self.direction = direction
#
#     def update(self):
#         dx = self.direction * self.speed
#
#         # check for collision with walls
#         if self.rect.left + dx < 0 or self.rect.right + dx > WIDTH:
#             self.kill()
#         # update specials location
#         self.rect.x += dx
#
#         #countdown timer
#         self.timer -= 1
#         if self.timer <= 0:
#             self.kill()
#
#         if pygame.sprite.spritecollide(player_one, specials_group, False):
#             if player_one.alive:
#                 player_one.health -= 1
#                 self.kill()
#         if pygame.sprite.spritecollide(player_two, specials_group, False):
#             if player_two.alive:
#                 player_two.health -= 5
#                 self.kill()

# create sprite groups
bullet_group = pygame.sprite.Group()
bullet_group2 = pygame.sprite.Group()

# Specials group
specials_group = pygame.sprite.Group()

player_one = Player1('cat', 200, 350, 5, 30, 10, 3)

player_two = Player2('corgi', 1200, 350, 7, 150, 10, 3)




cat_bullet = pygame.image.load(f'Bullet/cat.png').convert_alpha()







