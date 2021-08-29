import pygame
import os
import pygame.sprite
import pygame.display
from SpriteClass import *
from config import *

Corg_Special_img = pygame.image.load(f'Bullet/dog.png')
Cat_Special_img = pygame.image.load(f'Bullet/cat.png')
Corg_Special = pygame.transform.scale(Corg_Special_img, (200,100))
Cat_Special = pygame.transform.scale(Cat_Special_img, (200,100))

pygame.init()

run = True

while run:
    clock.tick(FPS)
    draw_bg()

    player_one.update()

    player_two.update()

    player_one.draw()
    player_two.draw()




    #update and draw groups
    bullet_group.update()
    bullet_group.draw(screen)
    bullet_group2.update()
    bullet_group2.draw(screen)
    specials_group.update()
    specials_group.draw(screen)


    # update player actions
    if player_one.alive:
        # shoot bullets
        if shoot:
            player_one.shoot()
        # #throw specials
        # elif specials and specials_thrown is False and player_one.specials > 0:
        #     specials = Specials((player_one.rect.centerx + (0.5 * player_one.rect.size[0] * player_one.direction)), player_one.rect.top, 10, Corg_Special, player_one.direction)
        #     specials_group.add(specials)
        #
        #     #reduce Specials
        #     specials_thrown = True
        #     player_one.specials -= 1

        if moving_left or moving_right or moving_up or moving_down:
            player_one.update_action(5) #1 means run
        else:
            player_one.update_action(4) # 0 is idle
        player_one.move(moving_left, moving_right, moving_up, moving_down)

        for event in pygame.event.get():
            # quit game
            if event.type == pygame.QUIT:
                run = False
            # keyboard presses
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    moving_left = True
                if event.key == pygame.K_d:
                    moving_right = True
                if event.key == pygame.K_w:
                    moving_up = True
                if event.key == pygame.K_s:
                    moving_down = True
                if event.key == pygame.K_SPACE:
                    shoot = True
                if event.key == pygame.K_f:
                    specials = True
                if event.key == pygame.K_ESCAPE:
                    run = False

            # keyboard button release
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    moving_left = False
                if event.key == pygame.K_d:
                    moving_right = False
                if event.key == pygame.K_w:
                    moving_up = False
                if event.key == pygame.K_s:
                    moving_down = False
                if event.key == pygame.K_SPACE:
                    shoot = False
                if event.key == pygame.K_f:
                    specials = False
                    specials_thrown = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    moving_left2 = True
                if event.key == pygame.K_RIGHT:
                    moving_right2 = True
                if event.key == pygame.K_UP:
                    moving_up2 = True
                if event.key == pygame.K_DOWN:
                    moving_down2 = True
                if event.key == pygame.K_RCTRL:
                    shoot2 = True
                if event.key == pygame.K_RSHIFT:
                    specials2 = True

            # keyboard button release
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    moving_left2 = False
                if event.key == pygame.K_RIGHT:
                    moving_right2 = False
                if event.key == pygame.K_UP:
                    moving_up2 = False
                if event.key == pygame.K_DOWN:
                    moving_down2 = False
                if event.key == pygame.K_RCTRL:
                    shoot2 = False
                if event.key == pygame.K_RSHIFT:
                    specials2 = False
                    specials_thrown2 = False

        if moving_left2 or moving_right2 or moving_up2 or moving_down2:
            player_two.update_action(5)  # 1 means run
        else:
            player_two.update_action(4)  # 0 is idle
        player_two.move2(moving_left2, moving_right2, moving_up2, moving_down2 )


        pygame.display.update()
