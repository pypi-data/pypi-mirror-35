'''
引擎界面：
        ==》GameEngine<class>
            ==》__init__() #初始化函数
            ==》 start()  # 游戏开始函数
            ==》 __create_scene() # 创建游戏精灵
            ==》 __update_scene() # 更新游戏场景
            ==》 __check_collide()# 碰撞检测
            ==》 __check_event()  # 事件监听

'''

import pygame
import game_sprite
import random
#游戏开发
ENEMY_CREATE = pygame.USEREVENT
JINGLING_CREATE = pygame.USEREVENT + 1
#音乐
pygame.mixer.init()
pygame.mixer.music.load("./music/bg_music2.mp3")
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

class GameEngine():
    '''引擎类型'''
    def __init__(self):
        '''初始化函数，控制界面初始化操作'''

        #命名标题
        self.title = pygame.display.set_caption("author@lss")

        #设置触发事件以及时间间隔
        pygame.time.set_timer(ENEMY_CREATE, 1500)

        # 设置技能触发事件以及时间间隔
        pygame.time.set_timer(JINGLING_CREATE, 5000)

        # #设置大Boss向左移动的时间间隔
        # pygame.time.set_timer(BOSS_MOVE_L, 4500)
        #
        # # 设置大Boss向左移动的时间间隔
        # pygame.time.set_timer(BOSS_MOVE_R, 2500)

        #创建时钟对象
        self.clock = pygame.time.Clock()

        #boss受攻击次数
        self.boss_times = 0

        #得分数
        self.score = 0

        self.hp = 0


    def start(self):
        '''游戏流程'''
        res = self.welcome()
        if res:
            self.round_one()
            self.round_two()
            self.round_three()

    def create_scence(self,bg,hero):
        '''创建游戏场景'''
        # 创建背景精灵对象
        self.bg1 = game_sprite.BackgroundSprite(bg)
        self.bg2 = game_sprite.BackgroundSprite(bg,prepare=True)

        # 创建英雄飞机精灵对象
        self.hero = game_sprite.HeroSprite(hero)

        #创建子弹精灵组
        self.bullets = pygame.sprite.Group()

        # 创建敌机子弹精灵组
        self.enemy_bullets = pygame.sprite.Group()

        # 创建敌机精灵组
        self.enemys = pygame.sprite.Group()

        #创建技能精灵组
        self.skill = pygame.sprite.Group()

        #创建大招精灵组
        self.victory_skill = pygame.sprite.Group()

        #创建Boss精灵
        self.boss = game_sprite.BossSprite("./images/boss.png",speed=5)

        #创建一个精灵组存放Boss
        self.boss_sprite = pygame.sprite.Group(self.boss)

        # 创建精灵组
        self.resource = pygame.sprite.Group(self.bg1, self.bg2, self.hero)

    def update_scence(self):
        '''更新游戏界面'''
        # 渲染初始画面
        self.resource.update()
        self.resource.draw(game_sprite.screen)

        #英雄血量
        hp_font = pygame.font.SysFont("微软雅黑", 24, True)
        hp_text = hp_font.render("HP:%s" % self.hp, True, [255, 0, 0])
        game_sprite.screen.blit(hp_text, (350, 10))

        #玩家得分
        hp_font = pygame.font.SysFont("微软雅黑", 24, True)
        hp_text = hp_font.render("SCORE:%s" % self.score, True, [255, 255, 255])
        game_sprite.screen.blit(hp_text, (200, 10))

        #更新按钮
        pause = pygame.image.load("./images/restart.png")
        game_sprite.screen.blit(pause,(0,0))

        # 渲染敌机
        self.enemys.update()
        self.enemys.draw(game_sprite.screen)

        # 渲染子弹
        self.bullets.update()
        self.bullets.draw(game_sprite.screen)

        # 渲染敌机子弹
        self.enemy_bullets.update()
        self.enemy_bullets.draw(game_sprite.screen)

        #渲染大Boss画面
        if self.boss:
            if self.game_times == 2 and self.times > 2:
                self.boss_sprite.update()
                self.boss_sprite.draw(game_sprite.screen)
                pygame.display.update()

        #渲染技能精灵画面
        self.skill.update()
        self.skill.draw(game_sprite.screen)

        #渲染技能大招
        self.victory_skill.update()
        self.victory_skill.draw(game_sprite.screen)

        # 更新显示
        pygame.display.update()

    def check_collide(self):
        '''碰撞检测'''
        # 碰撞检测(子弹与敌机)
        c = pygame.sprite.groupcollide(self.enemys, self.bullets, True, True)
        if len(c) > 0:
            self.score += 10
            self.times += 1
        if self.hero:
            # 碰撞检测
            e = pygame.sprite.spritecollide(self.hero, self.enemys, True)
            if len(e) > 0:
                self.hero.kill()
                self.hero = None

        #碰撞检测（敌方子弹与英雄子弹）
        pygame.sprite.groupcollide(self.enemy_bullets, self.bullets, True, True)
        if self.hero:
            # 碰撞检测（英雄与敌方子弹）
            e = pygame.sprite.spritecollide(self.hero, self.enemy_bullets, True)
            if len(e) > 0:
                self.hp -= 1
                if self.hp == 0:
                    self.hero.kill()
                    self.hero = None

        if self.hero:
        #碰撞检测（英雄与技能）
            c = pygame.sprite.spritecollide(self.hero,self.skill,True)
            if len(c) > 0:
                restart = game_sprite.GameSprite("./images/skill.png", speed=-5)
                restart.rect.x = 0
                restart.rect.y = game_sprite.SCREEN_RECT.height
                self.victory_skill.add(restart)
            s = pygame.sprite.groupcollide(self.enemys, self.victory_skill, True, False)
            if len(s) > 0:
                self.score += 10
            pygame.sprite.groupcollide(self.enemy_bullets, self.victory_skill, True, False)

        #碰撞检测（英雄子弹与Boss）
        if self.boss:
            if self.game_times == 2 and self.times > 2:
                if self.hero:
                    t = pygame.sprite.groupcollide(self.bullets, self.boss_sprite, True,False)
                    if len(t) > 0:
                        self.boss_times += 1
                        if self.boss_times >= 10:
                            self.boss.kill()
                            self.boss = None


    def check_event(self, enemy1_path,enemy2_path,bullet_path):
        '''事件监听'''
        # 监听所有的事件
        event_list = pygame.event.get()
        if len(event_list) > 0:
            print(event_list)
        for event in event_list:

            # 关闭机制
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            self.start_menu = False
            for event1 in event_list:
                #开始页面事件监听
                if event1.type == pygame.MOUSEBUTTONDOWN and 170 <= event.pos[0] <= 285 and \
                        350 <= event.pos[1] <= 380:
                    print(event.type, event.pos)
                    self.start_menu = True
                if event1.type == pygame.MOUSEBUTTONDOWN and 0 <= event.pos[0] <= 120 and \
                        0 <= event.pos[1] <= 30:
                    print(event.type, event.pos)
                    return self.start()
                if event1.type == pygame.MOUSEBUTTONDOWN and 190 <= event.pos[0] <= 270 and \
                        500 <= event.pos[1] <= 530:
                    print(event.type, event.pos)
                    pygame.quit()
                    exit()


            #随机产生敌机
            if event.type == ENEMY_CREATE:
                i = random.randint(1,10)
                if i < 7:
                    enemy = game_sprite.EnemySprite(enemy1_path)
                    self.enemys.add(enemy)
                else:
                    enemy = game_sprite.EnemySprite(enemy2_path)
                    self.enemys.add(enemy)
                #敌军发射子弹
                for enemy1 in self.enemys:
                        bullet = enemy1.fire()
                        self.enemy_bullets.add(bullet)
                #大Boss发射子弹
                if self.game_times == 2 and self.times > 2:
                    for boss1 in self.boss_sprite:
                        self.enemy_bullets.add(boss1.fire())

            #技能精灵触发
            if event.type == JINGLING_CREATE:
                skill = game_sprite.SkillSprite("./images/jineng2.png")
                self.skill.add(skill)

            #英雄发射子弹
            if self.hero:
                if event.type == pygame.KEYDOWN:
                    if event.key == 32:
                        print("发射子弹······")
                        bullet = self.hero.fire(bullet_path)
                        self.bullets.add(bullet)

        if self.hero:
            # 控制飞机移动
            event_list = pygame.key.get_pressed()
            if event_list[pygame.K_UP]:
                print("飞机向上移动^^^^")
                self.hero.rect.y -= 5
            elif event_list[pygame.K_DOWN]:
                print("飞机向下移动vvvv")
                self.hero.rect.y += 5
            elif event_list[pygame.K_LEFT]:
                print("飞机向左移动<<<<")
                self.hero.rect.x -= 5
            elif event_list[pygame.K_RIGHT]:
                print("飞机向右移动>>>>")
                self.hero.rect.x += 5

    def welcome(self):
        '''欢迎界面'''
        while True:
            self.bg_start = pygame.image.load("./images/start2_bg.jpg")
            game_sprite.screen.blit(self.bg_start,(0,0))
            pygame.display.update()
            event_list = pygame.event.get()
            start_menu = False
            for event in event_list:
                # print(event)
                # 关闭机制
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN and 100 <= event.pos[0] <= 350 and \
                        510 <= event.pos[1] <= 600:
                    print(event.type, event.pos)
                    start_menu = True
                if event.type == pygame.MOUSEBUTTONDOWN and 100 <= event.pos[0] <= 350 and \
                        620 <= event.pos[1] <= 650:
                    print(event.type, event.pos)
                    pygame.quit()
                    exit()

            if start_menu:
                return start_menu

    def round_one(self):
        '''第一关'''
        # 创建游戏场景
        self.create_scence("./images/bg_image01.jpg","./images/hero.png")
        # 杀死敌军次数
        self.times = 0
        # 控制游戏关，当game_times = 3 时判定出Boss
        self.game_times = 0
        # # 控制子弹
        # self.ticks = 0
        # 英雄血量
        self.hp = 3
        self.start_menu = None
        while True:
            # 控制游戏帧率
            self.clock.tick(30)
            # 事件监听
            self.check_event("./images/enemy1.png", "./images/enemy2.png","./images/hero_bullet2.png")
            # 碰撞检测
            self.check_collide()
            # 更新游戏场景
            self.update_scence()
            if self.times > 3:
                self.game_times += 1
                break
            if self.hero == None:
                # 询问用户是否继续
                self.draw_choice("./images/restart1.png","./images/restart2.png")
            if self.start_menu:
                self.enemy_bullets.empty()
                self.enemys.empty()
                self.hp = 3
                self.create_scence("./images/bg_image01.jpg","./images/hero.png")

    def round_two(self):
        '''第二关'''
        self.times = 0
        # 创建游戏场景
        self.create_scence("./images/bg_image02.jpg","./images/hero1.png")
        while True:
            # 控制游戏帧率
            self.clock.tick(50)
            # 事件监听
            self.check_event("./images/enemy3.png", "./images/enemy4.png","./images/hero_bullet.png")
            # 碰撞检测
            self.check_collide()
            # 更新游戏场景
            self.update_scence()
            if self.times > 5:
                self.game_times += 1
                break
            if self.hero == None:
                # 询问用户是否继续
                self.draw_choice("./images/restart1.png", "./images/restart2.png")
            if self.start_menu:
                self.enemy_bullets.empty()
                self.enemys.empty()
                self.hp = 3
                self.create_scence("./images/bg_image02.jpg","./images/hero1.png")

    def round_three(self):
        '''第三关'''
        self.times = 0
        self.create_scence("./images/bg.jpg","./images/hero1.png")
        while True:
            # 控制游戏帧率
            self.clock.tick(50)
            # 事件监听
            self.check_event("./images/enemy5.png", "./images/enemy6.png","./images/hero_bullet.png")
            # 碰撞检测
            self.check_collide()
            # 更新游戏场景
            self.update_scence()
            if self.hero == None:
                # 询问用户是否继续
                self.draw_choice("./images/restart1.png", "./images/restart2.png")
            elif self.boss == None:
                self.draw_choice("./images/restart1.png", "./images/restart2.png")
                end_bg = game_sprite.GameSprite("./images/victory.png", speed=0)
                end_bg.rect.centerx = game_sprite.SCREEN_RECT.centerx
                end_bg.rect.y = game_sprite.SCREEN_RECT.centery
                end_bg.rect.centerx = game_sprite.SCREEN_RECT.centerx
                end_bg.rect.y = game_sprite.SCREEN_RECT.centery - 150
                self.enemy_bullets.add(end_bg)

            if self.start_menu:
                self.enemy_bullets.empty()
                self.enemys.empty()
                self.boss_sprite.empty()
                self.hp = 3
                self.times = 0
                self.boss_times = 0
                self.create_scence("./images/bg.jpg","./images/hero1.png")

    def draw_choice(self,choice1,choice2):
        '''在屏幕上绘制、渲染用户选择项'''
        restart = game_sprite.GameSprite(choice1, speed=0)
        close = game_sprite.GameSprite(choice2, speed=0)
        restart.rect.centerx = game_sprite.SCREEN_RECT.centerx
        restart.rect.y = game_sprite.SCREEN_RECT.centery
        close.rect.centerx = game_sprite.SCREEN_RECT.centerx
        close.rect.y = game_sprite.SCREEN_RECT.centery + 150
        self.enemy_bullets.add(restart, close)










