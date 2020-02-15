import math
import pygame as py

py.init()


def isColission(x1, y1, x2, y2, dis=27):
    distance = math.fabs((((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5)
    if distance < dis:
        return True
    else:
        return False


def twopoints(x1, y1, x2, y2):
    distance = math.fabs((((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5)
    return distance


class Object:
    def __init__(self, pic=None):
        self.pic = pic
        self.x = -10000000
        self.y = -10000000
        self.x_change = 0
        self.y_change = 0
        self.color = (255, 255, 255)
        self.state = "None"

    def aimove(self, tx, ty):
        if self.x < tx:
            self.x_change = 0.1
            self.y_change = 0
            if self.x >= 780:
                self.x = 780
        if tx < self.x:
            self.x_change = -0.1
            self.y_change = 0
            if self.x <= 20:
                self.x = 20
        if ty < self.y:
            self.y_change = -0.1
            self.x_change = 0
            if self.y <= 20:
                self.y = 20
        if self.y < ty:
            self.y_change = 0.1
            self.x_change = 0
            if self.y >= 580:
                self.y = 580
        if self.pic.cond is None:
            py.draw.rect(root, self.color, [self.x, self.y, 32, 32])
        else:
            root.blit((playerx, playery), self.pic)


class living(object):
    def __init__(self, pic):
        self.pic = pic
        self.x = 0
        self.y = 0
        self.x_change = 0
        self.y_change = 0
        self.color = (255, 255, 255)
        self.health = 100
        self.damage = 50


class enemy(living):
    enemys = []

    def __init__(self, pic):
        self.pic = pic
        self.x = 0
        self.y = 0
        self.x_change = 0
        self.y_change = 0
        self.color = (255, 255, 255)
        self.health = 100
        self.damage = 50
        self.enemys.append(self)


root = py.display.set_mode((800, 600), py.FULLSCREEN)
py.display.set_caption("The Swordmaster Beta 5")
ico = py.image.load("sword.png")
py.display.set_icon(ico)

playerx = 400
playery = 500
playerx_change = 0
playery_change = 0
ssm = False
pcolor = (0, 255, 0)

swordy = 0
swordx = 0
ss = "in"
sr = "up"

fb = Object()
fb.state = "ready"
fb.rot = "none"

enemyx = 400
enemyy = 200
enemyx_change = 0
enemyy_change = 0
es = "living"

stamina = 200
health = 100
mana = 100

roundn = 1

running = True
idle = False
while running:
    root.fill((0, 0, 0))
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        if event.type == py.KEYDOWN:
            if event.key == py.K_w:
                playery_change = -0.1
                sr = "up"
            if event.key == py.K_s:
                playery_change = 0.1
                sr = "down"
            if event.key == py.K_d:
                playerx_change = 0.1
                sr = "right"
            if event.key == py.K_a:
                playerx_change = -0.1
                sr = "left"
            if event.key == py.K_ESCAPE:
                idle = True
            if event.key == py.K_LSHIFT:
                if stamina >= 2000:
                    if sr == "up":
                        playery -= 100
                    if sr == "down":
                        playery += 100
                    if sr == "right":
                        playerx += 100
                    if sr == "left":
                        playerx -= 100
                    stamina -= 2000
        if event.type == py.KEYUP:
            if event.key == py.K_w:
                playery_change = 0
            if event.key == py.K_s:
                playery_change = 0
            if event.key == py.K_d:
                playerx_change = 0
            if event.key == py.K_a:
                playerx_change = 0
        if event.type == py.MOUSEBUTTONDOWN:
            if event.button == 1:
                if not ssm:
                    ss = "out"
                if ssm and mana >= 55:
                    fb.state = "fire"
                    mana -= 50
                    if sr == "up":
                        fb.rot = "up"
                    if sr == "down":
                        fb.rot = "down"
                    if sr == "right":
                        fb.rot = "right"
                    if sr == "left":
                        fb.rot = "left"

            if event.button == 3:
                ssm = True

        if event.type == py.MOUSEBUTTONUP:
            if event.button == 1:
                ss = "in"
                swordx = -1000000
                swordy = -1000000
            if event.button == 3:
                ssm = False
    while idle:
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
            if event.type == py.KEYDOWN:
                if event.key == py.K_ESCAPE:
                    running = False
                    idle = False
                else:
                    idle = False

    playerx += playerx_change
    playery += playery_change
    py.draw.rect(root, pcolor, [playerx, playery, 20, 20])
    if playery <= 0:
        playery = 0
    if playery >= 580:
        playery = 580
    if playerx <= 0:
        playerx = 0
    if playerx >= 780:
        playerx = 780
    pcolor = (0, 255, 0)

    if ssm:
        pcolor = (0, 0, 255)
        mana -= 0.01
    if ssm and fb.state != "fire":
        fb.x = playerx
        fb.y = playery
    if fb.state == "fire":
        if fb.rot == "up":
            fb.y_change = -0.3
            fb.y += fb.y_change
            py.draw.rect(root, (255, 0, 0), [fb.x, fb.y, 10, 10])
        elif fb.rot == "down":
            fb.y_change = 0.3
            fb.y += fb.y_change
            py.draw.rect(root, (255, 0, 0), [fb.x, fb.y, 10, 10])
        elif fb.rot == "right":
            fb.x_change = 0.3
            fb.x += fb.x_change
            py.draw.rect(root, (255, 0, 0), [fb.x, fb.y, 10, 10])
        elif fb.rot == "left":
            fb.x_change = -0.3
            fb.x += fb.x_change
            py.draw.rect(root, (255, 0, 0), [fb.x, fb.y, 10, 10])
    if fb.y <= 0 or fb.y >=580 or fb.x<=0 or fb.x >= 780 or isColission(fb.x, fb.y, enemyx, enemyy):
        fb.state = "ready"
        fb.x = -10000
        fb.y = -10000

    if stamina > 0:
        if ss == "out" and sr == "up":
            swordy = playery - 30
            swordx = playerx + 15
            py.draw.rect(root, (0, 0, 255), [swordx, swordy, 6, 30])
            stamina -= 0.02
        if ss == "out" and sr == "down":
            swordy = playery + 20
            swordx = playerx
            py.draw.rect(root, (0, 0, 255), [swordx, swordy, 6, 30])
            stamina -= 0.02
        if ss == "out" and sr == "right":
            swordy = playery + 15
            swordx = playerx + 20
            py.draw.rect(root, (0, 0, 255), [swordx, swordy, 30, 6])
            stamina -= 0.02
        if ss == "out" and sr == "left":
            swordy = playery
            swordx = playerx - 30
            py.draw.rect(root, (0, 0, 255), [swordx, swordy, 30, 6])
            stamina -= 0.02
    if ss != "out":
        stamina += 0.01
    health += 0.01
    if not ssm:
        mana += 0.01
    if stamina >= 200:
        stamina = 200
    if stamina <= 0:
        stamina = 0
        ss = "in"
    if health >= 200:
        health = 200
    if mana >= 200:
        mana = 200
    if mana <= 0:
        mana = 0
        ssm = False
    if health <= 0:
        running = False

    py.draw.rect(root, (0, 255, 0), [580, 580, stamina, 10])
    py.draw.rect(root, (255, 0, 0), [300, 580, health, 10])
    py.draw.rect(root, (0, 0, 255), [20, 580, mana, 10])

    if es == "living":
        if ss == "out" and twopoints(enemyx, enemyy, swordx, swordy) <= 50:
            if enemyx < swordx:
                enemyx -= 0.3
                if enemyx <= 20:
                    enemyx = 20
            if swordx < enemyx:
                enemyx += 0.3
                if enemyx >= 780:
                    enemyx = 780
            if swordy < enemyy:
                enemyy += 0.3
                if enemyy >= 580:
                    enemyy = 580
            if enemyy < swordy:
                enemyy -= 0.3
                if enemyy <= 20:
                    enemyy = 20
        else:
            if enemyx < playerx:
                enemyx += 0.1
                if enemyx >= 780:
                    enemyx = 780
            if playerx < enemyx:
                enemyx -= 0.1
                if enemyx <= 20:
                    enemyx = 20
            if playery < enemyy:
                enemyy -= 0.1
                if enemyy <= 20:
                    enemyy = 20
            if enemyy < playery:
                enemyy += 0.1
                if enemyy >= 580:
                    enemyy = 580
        py.draw.rect(root, (255, 0, 0), [enemyx, enemyy, 20, 20])
        if isColission(playerx, playery, enemyx, enemyy, 20):
            health -= 50
            if sr == "up":
                playery += 100
            if sr == "down":
                playery -= 100
            if sr == "right":
                playerx += 100
            if sr == "left":
                playerx -= 100
    if isColission(swordx, swordy, enemyx, enemyy, 20):
        es = "died"
    py.display.update()
