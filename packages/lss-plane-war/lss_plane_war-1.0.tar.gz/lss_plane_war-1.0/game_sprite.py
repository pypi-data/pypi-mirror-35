'''
飞机大战：
    自己写第一遍，心好累
'''
#导入游戏模块
import pygame
import random

#初始化游戏模块
pygame.init()

#设置常量
SCREEN_SIZE = (460,700)
SCREEN_RECT = pygame.Rect(0,0,*SCREEN_SIZE)
ENEMY_CREATE = pygame.USEREVENT
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
pygame.mixer.init()

class GameSprite(pygame.sprite.Sprite):
    '''创建游戏精灵'''
    def __init__(self,image_path,speed):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        '''从Sprite继承过来的'''
        #负责使精灵行为生效
        self.rect.y += self.speed

class BackgroundSprite(GameSprite):
    '''创建背景精灵'''
    def __init__(self,image_path,prepare=False):
        super().__init__(image_path,speed=2)
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()

        if prepare:
            self.rect.y = -SCREEN_SIZE[1]

    def update(self):
        '''将走完的图片换位置'''
        super().update()
        if self.rect.y > SCREEN_SIZE[1]:
            self.rect.y = -SCREEN_SIZE[1]


class HeroSprite(GameSprite):
    '''创建英雄飞机精灵'''
    def __init__(self,image_path):
        super().__init__(image_path,speed=0)
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.y = SCREEN_RECT.centery + 200

    def update(self):
        '''控制边界'''
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= SCREEN_RECT.width - self.rect.width:
            self.rect.x = SCREEN_RECT.width - self.rect.width
        if self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.y >= SCREEN_RECT.height - self.rect.height:
            self.rect.y = SCREEN_RECT.height - self.rect.height

    def fire(self,bullet_path):
        '''发射子弹'''
        bullet = BulletSprite(bullet_path,-5,self.rect.centerx-10,self.rect.y)
        return bullet


class BulletSprite(GameSprite):
    '''子弹精灵'''
    def __init__(self,image_path,speed,x,y):
        super().__init__(image_path,speed)
        self.image = pygame.image.load(image_path)
        self.rect.x = x - 10
        self.rect.y = y - 30

    def update(self):
        super().update()
        if self.rect.y <= -SCREEN_RECT.height - 50 or self.rect.y >= SCREEN_RECT.height:
            self.kill()

    def __del__(self):
        print("杀死子弹对象")


class EnemySprite(GameSprite):
    '''敌机精灵'''
    def __init__(self,image_path):
        super().__init__(image_path,speed=random.randint(3,4))
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,SCREEN_RECT.width - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed_x = random.randint(5,6)

    def update(self):
        super().update()
        self.rect.x += self.speed_x
        if self.rect.x <= 0:
            self.speed_x = -self.speed_x
        elif self.rect.x >= SCREEN_RECT.width - self.rect.width:
            self.speed_x = -self.speed_x
        if self.rect.y > SCREEN_RECT.height:
            self.kill()

    def __del__(self):
        self.destory()
        print("杀死敌机")

    def destory(self):
        '''爆炸函数'''
        for image_path in ["./boom/boom1.png", "./boom/boom2.png", "./boom/boom3.png", "./boom/boom4.png", "./boom/boom5.png",\
                  "./boom/boom6.png", "./boom/boom7.png", "./boom/boom8.png", "./boom/boom9.png", "./boom/boom10.png",\
                  "./boom/boom11.png", "./boom/boom12.png", "./boom/boom_end.png"]:
            self.image = pygame.image.load(image_path)
            screen.blit(self.image, (self.rect.x,self.rect.y))
            pygame.display.update()

    def fire(self):
        '''发射子弹'''
        enemy_bullet = BulletSprite("./images/bullet2.png",6,self.rect.centerx,self.rect.y+50)
        return enemy_bullet

class BossSprite(GameSprite):
    '''boss精灵类'''
    def __init__(self,image_path,speed):
        super().__init__(image_path,speed)
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,SCREEN_RECT.width - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed_x = 5
        # self.speed = random.randint(3,5)

    def update(self):
        super().update()
        # self.rect.y += self.speed
        self.rect.x += self.speed_x
        if self.rect.x <= 0:
            self.speed_x = -self.speed_x
        elif self.rect.x >= SCREEN_RECT.width - self.rect.width:
            self.speed_x = -self.speed_x
        if self.rect.y <= -self.rect.height:
            self.speed = -self.speed
        elif self.rect.y >= SCREEN_RECT.centery - self.rect.height:
            self.speed = -self.speed

    def fire(self):
        '''发射子弹'''
        boss_bullet = BulletSprite("./images/boss_bullet.png",10,self.rect.centerx-25,self.rect.y+100)
        return boss_bullet


class SkillSprite(GameSprite):
    '''技能精灵'''
    def __init__(self,image_path):
        super().__init__(image_path,speed=random.randint(3,4))
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,SCREEN_RECT.width - self.rect.width)
        self.rect.y = -self.rect.height

    def update(self):
        super().update()
        if self.rect.y > SCREEN_RECT.height:
            self.kill()

    def __del__(self):
        print("杀死敌机")





