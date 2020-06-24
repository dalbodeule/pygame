from functools import cmp_to_key
import datetime
import math
import random as rnd
import time
import pickle
import pygame
from Library.bullet import Bullet
from Library.player import Player
from Library.hpbar import HPBar
from Library.score import ScoreObj

def collision(obj1, obj2):
    obj1Pos = obj1.get_pos()
    obj2Pos = obj2.get_pos()

    return bool(math.sqrt((obj1Pos[0] - obj2Pos[0]) ** 2 + (obj1Pos[1] - obj2Pos[1]) ** 2) < 20)

def draw_text(txt, size, pos, color):
    font = pygame.font.Font('Resources/NanumGothic.ttf', size)
    r = font.render(txt, True, color)
    screen.blit(r, pos)

score_list = []

# score file open with read
try:
    with open('scores', 'rb') as f:
        score_list = pickle.load(f)
except:
    print("score file not found")

# pygame init
pygame.init()

# mixer init
pygame.mixer.init()

WIDTH, HEIGHT = 1000, 800
FPS = 60

pygame.display.set_caption("총알 피하기")

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

time_for_adding_bullets = 0

player = Player(WIDTH/2, HEIGHT/2, pygame.mixer)

hpbar = HPBar(screen, player.get_health(), 100)

bg_image = pygame.image.load("Resources/bg.jpg")
bg_pos = (-150, -150)

# get sound main channel (main channel: 0)
mainChannel = pygame.mixer.Channel(0)

# play bgm with main channel
mainChannel.play(pygame.mixer.Sound('Resources/bgm.wav'), -1)

screen.blit(bg_image, bg_pos)
pygame.display.update()

start_time = time.time()

bullets = []

for i in range(10):
    bullets.append(Bullet(0, rnd.random()*HEIGHT, rnd.random()-0.5, rnd.random()-0.5))

# Game Loop
RUNNING = True
GAMEOVER = False
score = 0

bg_goto = (0, 0)

while RUNNING:
    dt = clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.goto(-1, 0)

                # add bg will move direction
                bg_goto = (-1, 0)
            elif event.key == pygame.K_RIGHT:
                player.goto(1, 0)
                bg_goto = (1, 0)
            elif event.key == pygame.K_UP:
                player.goto(0, -1)
                bg_goto = (0, -1)
            elif event.key == pygame.K_DOWN:
                player.goto(0, 1)
                bg_goto = (0, 1)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.goto(1, 0)
            elif event.key == pygame.K_RIGHT:
                player.goto(-1, 0)
            elif event.key == pygame.K_UP:
                player.goto(0, 1)
            elif event.key == pygame.K_DOWN:
                player.goto(0, -1)
            bg_goto = (0, 0)

    # calculate bg move
    bg_pos = (bg_pos[0] + bg_goto[0] * 0.01 * dt, bg_pos[1] + bg_goto[1] * 0.01 * dt)
    screen.blit(bg_image, bg_pos)

    player.update(dt, screen)
    player.draw(screen)

    hpbar.update(player.get_health())
    hpbar.draw(screen)

    for b in bullets:
        b.update_and_draw(dt, screen)

    elapsed_time = time.time() - start_time

    if GAMEOVER:
        txt = "Time: {:.1f} Bullets: {}".format(score, len(bullets))
        draw_text("GAME OVER", 100, (WIDTH/2 - 300, HEIGHT/2 - 70), (255, 255, 255))
        draw_text(txt, 32, (WIDTH/2 - 150, HEIGHT/2 + 50), (255, 255, 255))
    else:
        txt = "Time: {:.1f} Bullets: {} Health: {}".format(elapsed_time, len(bullets), player.get_health())
        draw_text(txt, 32, (10, 10), (255, 255, 255))

    pygame.display.update()

    if not GAMEOVER:
        for b in bullets:
            if collision(player, b):
                if player.hit(b.get_damage()):
                    GAMEOVER = True
                    score = elapsed_time
                    hpbar.hide()

                    # add now score
                    score_list.append(ScoreObj(int(score), len(bullets), datetime.datetime.now().timestamp()))
                    # sort scores
                    score_list = sorted(score_list, key=cmp_to_key(lambda x, y: y.score - x.score if x.score != y.score else x.time - y.time))
                    # splice scores
                    score_list = score_list[0:10]

                    print(score_list)

        time_for_adding_bullets += dt

        if time_for_adding_bullets > 2000:
            bullets.append(Bullet(0, rnd.random()*HEIGHT, rnd.random() - 0.5, rnd.random() - 0.5))
            time_for_adding_bullets -= 2000

print("Quit")

# file open and write scores
with open('scores', 'wb') as f:
    pickle.dump(score_list, f)

pygame.quit()
