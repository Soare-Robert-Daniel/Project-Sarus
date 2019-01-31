import pygame
pygame.font.init()

HEIGHT_JUMP_LIMIT_MAX = 150
FPS = 120

JUMP = 1
WAIT = 0

FAILED = 0
SUCCEEDED = 1

WALL_MAX_HEIGHT = 70
MAX_ROUND = 4
EXTINCTION_COUNTER = 5  # if the max score is the same for 'x' rounds, create a new population
MAX_SCORE_SESSION = MAX_ROUND

SMALL_TEXT = pygame.font.SysFont("monospace", 15)
SKINS = [
    pygame.image.load('resources//Wall.png'),
    pygame.image.load('resources//Wall1.png'),
    pygame.image.load('resources//Wall2.png'),
    pygame.image.load('resources//Wall3.png'),
    pygame.image.load('resources//ThinWall.png')
]

BOT_SKINS = [
    pygame.image.load('resources//bot.png')
]

PLAYER_SKINS = [
    pygame.image.load('resources//player.png')
]

AI_SKINS = [
    pygame.image.load('resources//AI.png')
]
