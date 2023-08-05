#coding:utf-8
import pygame,random,math,time

SCREEN_SIZE = (520,680)
SCREEN_RECT = pygame.Rect(0,0,*SCREEN_SIZE)

#自定义一个事件
ENEMY_CREATE = pygame.USEREVENT
EVENT_CREATE1 = pygame.USEREVENT+1
a = 3


class GameSprite(pygame.sprite.Sprite):
    """游戏精灵对象：用于辨识游戏中的各种元素"""

    def __init__(self,image_path,speed=1):
        super().__init__()

        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed


class BackgroundSprite(GameSprite):

    def __init__(self,image_path,next = False):
        super().__init__(image_path)

        if next:
            self.rect.y = -SCREEN_SIZE[1]
    def update(self):
        super().update()

        if self.rect.y >SCREEN_SIZE[1]:
            self.rect.y = -SCREEN_SIZE[1]


class HeroSprite(GameSprite):

    def __init__(self):
        super().__init__("./images/enmy1.png",speed=0)

        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.y = SCREEN_RECT.centery+500
        self.bullets = pygame.sprite.Group()
        self.index = 0
        # self.hero = pygame.sprite.Group()

    def update(self):
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >=SCREEN_RECT.width - self.rect.width:
            self.rect.x = SCREEN_RECT.width - self.rect.width


        if self.rect.y<=0:
            self.rect.y = 0

        elif self.rect.y >= SCREEN_RECT.height - self.rect.height:
            self.rect.y = SCREEN_RECT.height - self.rect.height

    def fire(self):
        self.index += 0.5
        bullet = BulletSprite(self.rect.centerx+50*math.sin(self.index),self.rect.centery)
        self.bullets.add(bullet)

class BulletSprite(GameSprite):

    def __init__(self,x,y):
        super().__init__("./images/bullet123.png",speed=-5)
        self.rect.x = x-15

        self.rect.y = y-70


    def update(self):
        super().update()
        if self.rect.y<= -self.rect.height:

            self.kill()

    def __del__(self):
        print("子弹木得了")

class EnemySprite(GameSprite):

    def __init__(self):
        super().__init__("./images/enemy1.png",speed=random.randint(2,5))
        self.rect.x = random.randint(0,SCREEN_RECT.width-self.rect.width)
        self.rect.y = -self.rect.height
        self.enemybullets = pygame.sprite.Group()
        # enemybullets = EnemyBulletSprite(self.rect.centerx, self.rect.centery)
        # self.enemybullets.add(enemybullet)
        # super().__init__("./images/a2-1.png", speed=random.randint(3, 6))
        # self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)
        # self.rect.y = -self.rect.height
        # self.enemybullets = pygame.sprite.Group()

    def update(self):
        super().update()

        if self.rect.y > SCREEN_RECT.height:
            self.kill()

    def enemyfire(self):
        bullets = EnemyBulletSprite(self.rect.centerx, self.rect.centery)
        self.enemybullets.add(bullets)

    def __del__(self):
        print("敌军木得了")
        bomb_index = ["./images/0-2.png","./images/0-2.png",
                       "./images/0-2.png","./images/0-2.png",
                       "./images/0-2.png","./images/0-2.png",
                       "./images/0-2.png","./images/0-2.png",
                       "./images/0-2.png","./images/0-2.png",
                       "./images/0-3.png","./images/0-3.png",
                       "./images/0-3.png","./images/0-3.png",
                       "./images/0-3.png","./images/0-3.png",
                       "./images/0-3.png","./images/0-3.png",
                       "./images/0-3.png","./images/0-3.png",
                       "./images/2-0.png","./images/2-0.png",
                       "./images/2-0.png","./images/2-0.png",
                       "./images/2-0.png","./images/2-0.png",
                       # "./images/2-0.png","./images/2-0.png",
                       # "./images/2-0.png","./images/2-0.png",
                       # "./images/2-1.png","./images/2-1.png",
                       # "./images/2-1.png","./images/2-1.png",
                       # "./images/2-1.png","./images/2-1.png",
                       # "./images/2-1.png","./images/2-1.png",
                       # "./images/2-1.png","./images/2-1.png",
                       # "./images/3-0.png","./images/3-0.png",
                       # "./images/3-0.png","./images/3-0.png",
                       # "./images/3-0.png","./images/3-0.png",
                       # "./images/3-0.png","./images/3-0.png",
                       # "./images/3-0.png","./images/3-0.png",
                       "./images/3-1.png","./images/3-1.png",
                       "./images/3-1.png","./images/3-1.png",
                       "./images/3-1.png","./images/3-1.png",
                       "./images/3-1.png","./images/3-1.png",
                       "./images/3-1.png","./images/3-1.png"]
        for image_path in bomb_index:
            self.image = pygame.image.load(image_path)
            screen.blit(self.image,(self.rect.centerx-30,self.rect.centery-30))
            pygame.display.update()
    #
    # def destroy(self):
    #     print("敌机销毁")
    #     for img_path in ["./images/0-3.png,./images/0-3.png,./images/0-3.png,./images/0-3.png"]:
    #         self.image = pygame.image.load(img_path)



class EnemyBulletSprite(GameSprite):

    def __init__(self, x, y):
        super().__init__("./images/bullet111.png", speed= 12)
        self.rect.x = x-20
        self.rect.y = y

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT[3]:
            self.kill()

    def __del__(self):
        print("子弹木得了")


    # def destory(self):
    #     print("敌机挂了")

# class Bomb(GameSprite):
#
#     def __init__(self):
#         super().__init__("./images/2-0.png,./images/2-1.png,./images/3-0.png,./images/3-1.png",speed=0)
#         self.rect.x = x
#         self.rect.y = y
#         self.enemybomb = pygame.sprite.Group()
#
#     def update(self):
#         super().update()
#         self.kill()
#     def __del__(self):
#         print("敌机挂了")
class Life(GameSprite):
    def __init__(self, speed=0):
        super().__init__("./images/blood.png", speed=0)
        self.rect.x = SCREEN_RECT.x+10
        self.rect.y = SCREEN_RECT.y + 10
class Life1(GameSprite):
    def __init__(self, speed=0):
        super().__init__("./images/blood.png", speed=0)
        self.rect.x = SCREEN_RECT.x+60
        self.rect.y = SCREEN_RECT.y + 10

class Life2(GameSprite):
    def __init__(self, speed=0):
        super().__init__("./images/blood.png", speed=0)
        self.rect.x = SCREEN_RECT.x + 110
        self.rect.y = SCREEN_RECT.y + 10


# class Life1(GameSprite):
#     def __init__(self):
#         self.rect.centerx = SCREEN_RECT.centerx + 200
#         self.rect.y = SCREEN_RECT.centery + 100

# def over():


def over():
    test = False
    while True:
        start_show = pygame.image.load("./images/GAME.OVER.jpg")
        screen.blit(start_show, (0, 0))
        pygame.display.update()
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and 0 <= event.pos[0] <= 520 and 0 <= event.pos[1] <= 680:
                test = True
        if test == True:
            pygame.quit()
#####################################################

pygame.init()


screen = pygame.display.set_mode(SCREEN_SIZE)

bg1 = BackgroundSprite("./images/bg1_0.jpg")
bg2 = BackgroundSprite("./images/bg1_0.jpg",next = True)



hero = HeroSprite()

# 定义血量
blood1 = Life()
blood2 = Life1()
blood3 = Life2()
bloodlist = [blood1,blood2,blood3]
resources = pygame.sprite.Group(bg1,bg2,hero,blood1,blood2,blood3)
#创建一个敌人
enemys = pygame.sprite.Group()
#enemybullets = pygame.sprite.Group()

pygame.time.set_timer(ENEMY_CREATE,500)
pygame.time.set_timer(EVENT_CREATE1,500)
ticks =0
clock = pygame.time.Clock()
test = False
while True:
    start_show = pygame.image.load("./images/bg_3.png")
    screen.blit(start_show,(0,0))
    pygame.display.update()
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.MOUSEBUTTONDOWN and 130<=event.pos[0]<=380 and 310<=event.pos[1]<=370:
            test = True
    if test == True:
        break




pygame.mixer.init()
pygame.mixer.music.load("./music/180.wav")
pygame.mixer.music.set_volume(100)
pygame.mixer.music.play(100)
while True:

    clock.tick(60)
    ticks += 1
    resources.update()
    resources.draw(screen)



    # event_list = pygame.event.get()
    # if len(event_list)>0:
    #     print(event_list)

    if ticks % 20 == 0:
        hero.fire()

    event_list = pygame.event.get()
    if len(event_list) > 0:
        print(event_list)
        for event in event_list:
            print(event.type,pygame.KEYDOWN,pygame.K_LEFT)
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == ENEMY_CREATE:
                print("一架飞机出来了")
                enemy = EnemySprite()
                enemy.enemyfire()
                print("敌人攻击了")
                enemys.add(enemy)

    # for e in enemys:
    #     if ticks % 50 == 0:
    #         e.enemyfire()
    #         e_b_g = e.enemybullets
    #         e_b_g.update()
    #         e_b_g.draw(screen)
    #         i = pygame.sprite.spritecollide(hero, e.enemybullets, True)
    #         if len(i) > 0:
    #             hero.kill()
    #             pygame.quit()
    #             print("你ko了")
    #             exit()


    key_down = pygame.key.get_pressed()
    if key_down[pygame.K_LEFT]:
        print("左")
        hero.rect.x -=5
    elif key_down[pygame.K_RIGHT]:
        print("右")
        hero.rect.x +=5
    elif key_down[pygame.K_UP]:
        print("上")
        hero.rect.y -=5
    elif key_down[pygame.K_DOWN]:
        print("下")
        hero.rect.y +=5
    elif key_down[pygame.K_SPACE]:
        hero.fire()
        print("射",hero.bullets)
    # elif key_esc[pygame.quit]:
    #     exit()

    pygame.sprite.groupcollide(hero.bullets,enemys,True,True)

    e = pygame.sprite.spritecollide(hero,enemys,True)
    if len(e)>0:
        a -= 1
        bloodlist[a].kill()
        if a <= 0:
            hero.kill()
            over()
            # pygame.quit()
            exit()
    # resources.update()
    # resources.draw(screen)
    for e in enemys:
        # if ticks %5 ==  0:
        e_b_g = e.enemybullets
        e_b_g.update()
        e_b_g.draw(screen)
        i = pygame.sprite.spritecollide(hero, e.enemybullets, True)
        if len(i) > 0:
            a -= 1
            bloodlist[a].kill()
            if a <= 0:
                hero.kill()
                over()
                pygame.quit()
                print("你被ko了")
                exit()

    enemys.update()

    enemys.draw(screen)

    hero.bullets.update()
    hero.bullets.draw(screen)
    # bomb_sound = pygame.mixer.Sound("./images/kill.wav")
    # bomb_sound.set_volume(100)


    pygame.display.update()

    #         pygame.quit()