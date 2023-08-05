import pygame,random,time
pygame.mixer.init()
#定义需要的常量
SCREEN_SIZE = (512,768)
SCREEN_RECT = pygame.Rect(0,0,*SCREEN_SIZE)

#自定义一个事件
ENEMY_CREATE = pygame.USEREVENT
ENEMY_ATTACK = pygame.USEREVENT+1
#OTHER_EVENT = pygame.USEREVENT + 1
# 设置bgm
pygame.mixer_music.load("./wav/飞机大战.mp3")
pygame.mixer_music.play(-1, 0)
# 音效
yx = pygame.mixer.Sound("./wav/enemy3_down.wav")

resources = None
bullets = None
enemys = None
scene = None
score = 0