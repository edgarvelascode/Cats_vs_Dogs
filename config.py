import pygame
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 240, 0)

WIDTH, HEIGHT = 1500, 900

#set framerate
clock = pygame.time.Clock()
FPS = 60

x = 200
y = 200


screen = pygame.display.set_mode((WIDTH, HEIGHT))


pygame.display.set_caption("Game")

YARD = pygame.transform.scale(pygame.image.load("yard.png"), (WIDTH, HEIGHT))

# define player action variables
moving_left = False
moving_right = False
moving_up = False
moving_down = False
shoot = True
specials = False
specials_thrown = False

moving_left2 = False
moving_right2 = False
moving_up2 = False
moving_down2 = False
shoot2 = False
specials2 = False
specials_thrown2 = False



CHAR_WIDTH, CHAR_HEIGHT = 80, 80
# CAT_CHAR_IMAGE = pygame.image.load("cat.png")
# CAT_CHAR = pygame.transform.rotate(pygame.transform.scale(CAT_CHAR_IMAGE, (CHAR_WIDTH, CHAR_HEIGHT)), 0)
# DOGBONE_CHAR_IMAGE = pygame.image.load("dogbone.png")
# DBONE_CHAR = pygame.transform.scale(DOGBONE_CHAR_IMAGE, (50,30))
# DSPECIAL_CHAR = pygame.transform.scale(DOGBONE_CHAR_IMAGE, (200,100))
# FISHBONE_CHAR_IMAGE = pygame.image.load("fishbone.png")
# FBONE_CHAR = pygame.transform.scale(FISHBONE_CHAR_IMAGE, (60,30))
# CSPECIAL_CHAR = pygame.transform.scale(FISHBONE_CHAR_IMAGE, (30,15))

VEL = 10

# DOG_HIT_SOUND = pygame.mixer.Sound('growl.mp3')
# DOG_FIRE_SOUND = pygame.mixer.Sound('bark.mp3')
# CAT_FIRE_SOUND = pygame.mixer.Sound('hiss.mp3')
# CAT_HIT_SOUND = pygame.mixer.Sound('meow.mp3')
#
# HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
# WINNER_FONT = pygame.font.SysFont('comicsans', 150)
# SPECIAL_FONT = pygame.font.SysFont('comicsans', 50)

BULLETS_VEL = 10
CAT_BULLET_VEL = 10
DBOMB_VEL = 5
CBOMB_VEL = 15
MAX_BULLETS = 3
MAX_DOG_BULLETS = 3
MAX_DBOMB_BULLETS = 1
MAX_CAT_BULLETS = 3
MAX_CBOMB_BULLETS = 5

CAT_HIT = pygame.USEREVENT + 1
CBOMB_HIT = pygame.USEREVENT + 2
DOG_HIT = pygame.USEREVENT + 3
DBOMB_HIT = pygame.USEREVENT + 4



