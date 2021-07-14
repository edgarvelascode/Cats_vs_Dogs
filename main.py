import pygame
import os
pygame.font.init()
pygame.mixer.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 240, 0)

WIDTH, HEIGHT = 1500, 900
FPS = 60
CHAR_WIDTH, CHAR_HEIGHT = 150, 150
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Game")

CAT_CHAR_IMAGE = pygame.image.load("cat.png")
CAT_CHAR = pygame.transform.rotate(pygame.transform.scale(CAT_CHAR_IMAGE, (CHAR_WIDTH, CHAR_HEIGHT)), 0)
DOG_CHAR_IMAGE = pygame.image.load("corgi.png")
DOG_CHAR = pygame.transform.rotate(pygame.transform.scale(DOG_CHAR_IMAGE, (CHAR_WIDTH, CHAR_HEIGHT)), 0)

DOGBONE_CHAR_IMAGE = pygame.image.load("dogbone.png")
DBONE_CHAR = pygame.transform.scale(DOGBONE_CHAR_IMAGE, (60,30))
FISHBONE_CHAR_IMAGE = pygame.image.load("fishbone.png")
FBONE_CHAR = pygame.transform.scale(FISHBONE_CHAR_IMAGE, (60,30))

VEL = 10

BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

DOG_HIT_SOUND = pygame.mixer.Sound('growl.mp3')
DOG_FIRE_SOUND = pygame.mixer.Sound('bark.mp3')
CAT_FIRE_SOUND = pygame.mixer.Sound('hiss.mp3')
CAT_HIT_SOUND = pygame.mixer.Sound('meow.mp3')

HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

BULLETS_VEL = 10
MAX_BULLETS = 3

CAT_HIT = pygame.USEREVENT + 1
DOG_HIT = pygame.USEREVENT + 2

YARD = pygame.transform.scale(pygame.image.load("yard.jpg"), (WIDTH, HEIGHT))


def draw_window(DOG, CAT, DOG_bullets, CAT_bullets, DOG_health, CAT_health):
    WIN.blit(YARD, (0,0))
    pygame.draw.rect(WIN, BLACK, BORDER)

    DOG_health_text = HEALTH_FONT.render('Health: ' + str(DOG_health), 1, YELLOW)
    CAT_health_text = HEALTH_FONT.render('Health: ' + str(CAT_health), 1, YELLOW)
    WIN.blit(DOG_health_text, (WIDTH - DOG_health_text.get_width() - 10, 10))
    WIN.blit(CAT_health_text, (10, 10))
    WIN.blit(CAT_CHAR, (CAT.x, CAT.y))
    WIN.blit(DOG_CHAR, (DOG.x, DOG.y))

    for bullet in DOG_bullets:
        WIN.blit(DBONE_CHAR, (bullet.x, bullet.y))

    for bullet in CAT_bullets:
        WIN.blit(FBONE_CHAR, (bullet.x, bullet.y))

    pygame.display.update()


def CAT_handle_movement(keys_pressed, CAT):
    if keys_pressed[pygame.K_a] and CAT.x - VEL > 0:  # left
        CAT.x -= VEL
    if keys_pressed[pygame.K_d] and CAT.x + VEL + CAT.width < BORDER.x:  # right
        CAT.x += VEL
    if keys_pressed[pygame.K_w] and CAT.y - VEL > 0:  # up
        CAT.y -= VEL
    if keys_pressed[pygame.K_s] and CAT.y + VEL + CAT.height < HEIGHT:  # down
        CAT.y += VEL


def DOG_handle_movement(keys_pressed, DOG):
    if keys_pressed[pygame.K_LEFT] and DOG.x - VEL > BORDER.x + BORDER.width:  # left
        DOG.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and DOG.x + VEL + DOG.width < WIDTH:  # right
        DOG.x += VEL
    if keys_pressed[pygame.K_UP] and DOG.y - VEL > 0:  # up
        DOG.y -= VEL
    if keys_pressed[pygame.K_DOWN] and DOG.y + VEL + DOG.height < HEIGHT:  # down
        DOG.y += VEL


def handle_bullets(CAT_bullets, DOG_bullets, CAT, DOG):
    for bullet in CAT_bullets:
        bullet.x += BULLETS_VEL
        if DOG.colliderect(bullet):
            pygame.event.post(pygame.event.Event(DOG_HIT))
            CAT_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            CAT_bullets.remove(bullet)

    for bullet in DOG_bullets:
        bullet.x -= BULLETS_VEL
        if CAT.colliderect(bullet):
            pygame.event.post(pygame.event.Event(CAT_HIT))
            DOG_bullets.remove(bullet)

        elif bullet.x < 0:
            DOG_bullets.remove(bullet)


def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000)


def main():
    DOG = pygame.Rect(1200, 350, CHAR_WIDTH, CHAR_HEIGHT)
    CAT = pygame.Rect(200, 350, CHAR_WIDTH, CHAR_HEIGHT)

    DOG_bullets = []
    CAT_bullets = []

    DOG_health = 10
    CAT_health = 10

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RCTRL and len(DOG_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(DOG.x, DOG.y + DOG.height//2 - 2, 10, 5)
                    DOG_bullets.append(bullet)
                    DOG_FIRE_SOUND.play()

                if event.key == pygame.K_f and len(CAT_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(CAT.x + CAT.width, CAT.y + CAT.height // 2 - 2, 10, 5)
                    CAT_bullets.append(bullet)
                    CAT_FIRE_SOUND.play()

            if event.type == DOG_HIT:
                DOG_health -= 1
                DOG_HIT_SOUND.play()

            if event.type == CAT_HIT:
                CAT_health -= 1
                CAT_HIT_SOUND.play()

        winner_text = ""
        if DOG_health <= 0:
            winner_text = 'CAT Wins!'

        if CAT_health <= 0:
            winner_text = "DOG Wins!"

        if winner_text != "":
            draw_winner(winner_text)
            main()

        keys_pressed = pygame.key.get_pressed()
        DOG_handle_movement(keys_pressed,DOG)
        CAT_handle_movement(keys_pressed,CAT)

        handle_bullets(CAT_bullets, DOG_bullets, CAT, DOG)

        draw_window(DOG, CAT, DOG_bullets, CAT_bullets, DOG_health, CAT_health)




if __name__ == "__main__":
    main()
