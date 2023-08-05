
import pygame,random,game_sprites2,time


ENEMY_BOOM_SCORE = 50
pygame.font.init()
KAISHI_RECT = pygame.Rect(0,0,30,30)
# pygame.mixer.init()                 #音乐初始化
# pygame.mixer.music.load('./images/ad.mp3')    #游戏背景主题曲
# pygame.mixer.music.play(-1)         #播放背景音乐
# sound = pygame.mixer.Sound('./images/game_over.wav')    #子弹发射音效
# sound.play(-1)

class GameEngine:
    def __init__(self):
        # 定义背景精灵
        self.bg1 = game_sprites2.BackgroundSprite("./images/bg_img_3.jpg")
        self.bg2 = game_sprites2.BackgroundSprite("./images/bg_img_3.jpg",prepare=True)
        self.bg3 = game_sprites2.BackgroundSprite("./images/bg_img_2.jpg")
        self.bg4 = game_sprites2.BackgroundSprite("./images/bg_img_2.jpg",prepare=True)
        self.bg5 = game_sprites2.BackgroundSprite("./images/bg_img_4.jpg")
        self.bg6 = game_sprites2.BackgroundSprite("./images/bg_img_4.jpg", prepare=True)
        # 定义英雄飞机对象
        self.hero = game_sprites2.HeroSprite("./images/hero_188.png", game_sprites2.SCREEN_RECT.centerx - 100,
                                             game_sprites2.SCREEN_RECT.centery + 200)
        self.hero1 = game_sprites2.HeroSprite("./images/hero2.png", game_sprites2.SCREEN_RECT.centerx + 100,
                                              game_sprites2.SCREEN_RECT.centery + 200)
        self.enemy = game_sprites2.EnemySprite("./images/enemy1.png")
        self.enemy1 = game_sprites2.EnemySprite("./images/diji.png")
        self.boss = game_sprites2.Boss(50)
        self.boss_group = pygame.sprite.Group(self.boss)
        self.bl1 = game_sprites2.Blood(game_sprites2.SCREEN_RECT.x+15,game_sprites2.SCREEN_RECT.y+40)
        self.bl2 = game_sprites2.Blood(game_sprites2.SCREEN_RECT.x+55,game_sprites2.SCREEN_RECT.y+40)
        self.bl3 = game_sprites2.Blood(game_sprites2.SCREEN_RECT.x+95,game_sprites2.SCREEN_RECT.y+40)
        self.bl4 = game_sprites2.Blood(game_sprites2.SCREEN_RECT.x + 135, game_sprites2.SCREEN_RECT.y + 40)
        self.bl5 = game_sprites2.Blood(game_sprites2.SCREEN_RECT.x + 175, game_sprites2.SCREEN_RECT.y + 40)

        # 定义初始化精灵组对象
        self.resources = pygame.sprite.Group(self.bg1, self.bg2, self.hero,self.bl1,self.bl2,self.bl3,self.bl4, self.bl5,self.hero1)
        self.resources1 = pygame.sprite.Group(self.bg3, self.bg4, self.hero,self.bl1,self.bl2,self.bl3, self.bl4, self.bl5,self.hero1)
        self.resources2 = pygame.sprite.Group(self.bg5, self.bg6, self.hero, self.bl1, self.bl2, self.bl3, self.bl4, self.bl5,self.boss,self.hero1)
        # 定义一个敌人飞机的精灵组对象
        self.enemys = pygame.sprite.Group()

        self.enemys_boom = pygame.sprite.Group()
        self.enemys_boom = pygame.sprite.Group()  # 爆炸敌机精灵组
        self.buji1 = game_sprites2.BuJi()
        self.scroe = 0
        self.huanqing = game_sprites2.HuanQiang()
        self.game_font = pygame.font.SysFont("fangsong", 16,True)
        self.screen = pygame.display.set_mode(game_sprites2.SCREEN_SIZE)
        self.screen.blit(self.game_font.render("当前分数：%s" % self.scroe, True, [0, 0, 255]), [20, 20])
        self.index = 0
        self.k = [self.bl1,self.bl2,self.bl3,self.bl4,self.bl5]
        self.dazgao = game_sprites2.Dazhao("./images/bullet_2.png")
        pygame.display.update()

    def start1(self):
        pygame.init()
        clock = pygame.time.Clock()
        pygame.time.set_timer(game_sprites2.ENEMY_CREATE, 1000)
        while True:
            clock.tick(66)
            background_image = pygame.image.load("./images/logo.png")
            background_image1 = pygame.image.load("./images/hero2.png")
            self.screen.blit(background_image, (0, 0))
            self.screen.blit(background_image1, (game_sprites2.SCREEN_RECT.centerx - self.hero.rect.width / 2, game_sprites2.SCREEN_RECT.centery))
            self.my_font = pygame.font.SysFont('fangsong', 20)
            self.screen.blit(self.my_font.render(u'qiku 1807 A', False, (255, 165, 0)), [390, 40])
            self.my_font = pygame.font.SysFont('fangsong', 20)
            self.screen.blit(self.my_font.render(u'何威成', False, (255, 165, 0)), [400, 70])
            pygame.display.update()
            event_list = pygame.event.get()
            shubiao = list(pygame.mouse.get_pos())
            for event in event_list:
                if 110 < shubiao[0] < 400 and 504 < shubiao[1] < 616:
                    if event.type == pygame.MOUSEBUTTONUP:
                        self.start()


                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

    def start(self):
        while True:
            if self.scroe < 200:
                self.check_collide()
                self.check_event1()
                self.check_event()
                self.check_kewdown()
                self.background1()
                self.update_scene()
                self.screen.blit(self.game_font.render("当前分数：%s" % self.scroe, True, [0, 0, 255]), [20, 20])
                pygame.display.update()
            elif self.scroe >= 200 and self.scroe < 400:
                self.check_collide()
                self.check_event2()
                self.check_event()
                self.check_kewdown()
                self.background2()
                self.update_scene()
                self.screen.blit(self.game_font.render("当前分数：%s" % self.scroe, True, [0, 0, 255]), [20, 20])
                pygame.display.update()
            elif self.scroe >= 400:
                self.check_collide()
                self.check_event3()
                self.check_event()
                self.check_kewdown()
                self.background3()
                self.update_scene()
                self.boss.buttless.update()
                self.boss.buttless.draw(self.screen)
                self.screen.blit(self.game_font.render("当前分数：%s" % self.scroe, True, [0, 0, 255]), [20, 20])
                pygame.display.update()

    def background1(self):
        self.resources.update()
        self.resources.draw(self.screen)

    def background2(self):
        self.resources1.update()
        self.resources1.draw(self.screen)

    def background3(self):
        self.resources2.update()
        self.resources2.draw(self.screen)

    def update_scene(self):
        pygame.display.set_caption("飞机大战")

        self.hero.butters.update()
        self.hero.butters.draw(self.screen)

        self.hero1.butters.update()
        self.hero1.butters.draw(self.screen)

        self.enemy.buttles.update()
        self.enemy.buttles.draw(self.screen)

        self.enemys.update()
        self.enemys.draw(self.screen)

        self.buji1.update()
        self.buji1.buji.draw(self.screen)

        self.huanqing.update()
        self.huanqing.huanqing1.draw(self.screen)

        self.dazgao.da.update()
        self.dazgao.da.draw(self.screen)

        pygame.display.update()

    def gameover(self):
        if self.hero == None:
            while True:
                background_image = pygame.image.load("./images/gameover.jpg")
                self.screen.blit(background_image, (0, 0))
                self.my_font = pygame.font.SysFont('fangsong', 40)
                self.screen.blit(self.my_font.render(u'score: %s' % self.scroe, False, (127, 255, 0)), [10, 10])
                pygame.display.update()
                event_list = pygame.event.get()
                if len(event_list) > 0:
                    for event in event_list:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if (100 < event.pos[0] < 390) and (660 < event.pos[1] < 730):
                                pygame.quit()
                                exit()
                            elif (100 < event.pos[0] < 390) and (575 < event.pos[1] < 650):
                                self.__init__()
                                self.start1()


    def boom(self, enemy):
        '''爆炸'''
        for i in range(3, 5):
            clock = pygame.time.Clock()
            clock.tick(66)
            image = pygame.image.load("./images/0" + str(i) + ".png")
            self.screen.blit(image, enemy.rect)
            pygame.display.update()
            print(image)

    def check_collide(self):
        self.enemys_boom_dict = pygame.sprite.groupcollide(self.hero.butters, self.enemys, True, True)
        self.da_zgao_dict = pygame.sprite.groupcollide(self.dazgao.da, self.enemys, False, True)
        self.boss_dict = pygame.sprite.groupcollide(self.boss_group, self.hero.butters, False, True)
        pygame.sprite.groupcollide(self.hero.butters, self.enemy.buttles, True, True)
        pygame.sprite.groupcollide(self.dazgao.da, self.enemy.buttles, False, True)
        self.scroe += len(self.enemys_boom_dict) * ENEMY_BOOM_SCORE
        self.scroe += len(self.da_zgao_dict) * ENEMY_BOOM_SCORE
        # self.scroe += len(self.boss_dict) * ENEMY_BOOM_SCORE
        self.enemys_boom.add(self.enemys_boom_dict)# 添加到爆炸精灵组
        self.enemys_boom.add(self.da_zgao_dict)
        # self.enemys_boom.add(self.boss_dict)
        for enemy_boom in self.enemys_boom:
            self.boom(enemy_boom)  # 将敌机返回到爆炸组，调用函数
            self.enemys_boom.remove(enemy_boom)


        # 碰撞检测：英雄飞机和敌方飞机之间的碰撞
        if pygame.sprite.spritecollide(self.hero or self.hero1, self.enemys, True):
            self.hero.bld -= 1
            self.k[self.hero.bld].kill()
            if self.hero.bld < 0:
                self.hero.kill()
                self.hero = None
                self.gameover()

        # 碰撞检测：英雄飞机和敌方飞机子弹之间的碰撞
        o = pygame.sprite.spritecollide(self.hero or self.hero1, self.enemy.buttles, True)
        if len(o) > 0:
            self.hero.bld -= 1
            self.k[self.hero.bld].kill()
            if self.hero.bld < 0:
                self.hero.kill()
                self.hero = None
                self.gameover()
        p = pygame.sprite.spritecollide(self.hero, self.boss.buttless, True)
        if len(p) > 0:
            self.hero.bld -= 1
            self.k[self.hero.bld].kill()
            if self.hero.bld < 0:
                self.hero.kill()
                self.hero = None
                self.gameover()

        # 碰撞检测：英雄飞机和补给之间的碰撞
        m = pygame.sprite.spritecollide(self.hero1 or self.hero, self.buji1.buji, True)
        if len(m) > 0:
            if self.hero.bld >= 5:
                self.hero.bld = 5
            elif self.scroe < 200:
                self.resources.add(self.k[self.hero.bld])
                self.hero.bld += 1
                print(self.k)
                self.buji1.kill()
            elif self.scroe >= 200 and self.scroe < 400:
                self.resources1.add(self.k[self.hero.bld])
                self.hero.bld += 1
                print(self.k)
                self.buji1.kill()
            elif self.scroe >= 400:
                self.resources2.add(self.k[self.hero.bld])
                self.hero.bld += 1
                print(self.k)
                self.buji1.kill()

        h = pygame.sprite.spritecollide(self.boss, self.hero.butters, True)
        if len(h) > 0 :
            self.boss.life -= 10
            if self.boss.life <= 0:
                self.boss.kill()

        # 碰撞检测：英雄飞机和补给枪之间的碰撞
        t = pygame.sprite.spritecollide(self.hero, self.huanqing.huanqing1, True)
        if len(t) > 0:
            self.dazgao.fire()
            self.enemy.kill()


    def check_event(self):
        a = random.randint(1,1000)
        if a > 998:
            self.buji1 = game_sprites2.BuJi()
            self.buji1.buji.add(self.buji1)

        if a > 988 and a < 990:
            self.huanqing = game_sprites2.HuanQiang()
            self.huanqing.huanqing1.add(self.huanqing)

    def check_event1(self):
        event_list = pygame.event.get()
        if len(event_list) > 0:
            for event in event_list:
                if event.type == game_sprites2.ENEMY_CREATE:
                    print("创建一架敌方飞机.....")

                    self.enemy = game_sprites2.EnemySprite("./images/enemy1.png")
                    self.enemy.fires()
                    # 添加到敌方飞机精灵组中
                    self.enemys.add(self.enemy)

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE :
                        self.hero.fires("./images/bullet_1.png")
                        sound = pygame.mixer.Sound('./images/bullet~1.wav')  # 子弹发射音效
                        sound.play(1)

    def check_event2(self):
        event_list = pygame.event.get()
        a = random.randint(1,3)
        if len(event_list) > 0:
            for event in event_list:
                if event.type == game_sprites2.ENEMY_CREATE:
                    print("创建一架敌方飞机.....")

                    self.enemy = game_sprites2.EnemySprite("./images/diji.png")
                    if a == 1:
                        self.enemy1 = game_sprites2.EnemySprite("./images/diji.png")
                        self.enemy.fires()
                        self.enemy1.fires()
                    # 添加到敌方飞机精灵组中
                    self.enemys.add(self.enemy,self.enemy1)

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.hero.fires("./images/bullet_3.png")
                        sound = pygame.mixer.Sound('./images/bullet~1.wav')  # 子弹发射音效
                        sound.play(1)

    def check_event3(self):
        a = random.randint(1,1000)
        if a % 10 == 0:
            self.boss.fire()

        event_list = pygame.event.get()
        if len(event_list) > 0:
            for event in event_list:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.hero.fires("./images/bullet_3.png")
                        sound = pygame.mixer.Sound('./images/bullet~1.wav')  # 子弹发射音效
                        sound.play(-1)

    def check_kewdown(self):
        key_down = pygame.key.get_pressed()
        if key_down[pygame.K_LEFT]:
            print("飞机向左移动")
            self.hero.rect.x -= 8

        if key_down[pygame.K_RIGHT]:
            print("飞机向右移动")
            self.hero.rect.x += 8

        if key_down[pygame.K_UP]:
            print("飞机向上移动")
            self.hero.rect.y -= 8

        if key_down[pygame.K_DOWN]:
            print("飞机向下移动")
            self.hero.rect.y += 8

        if key_down[pygame.K_a]:
            print("飞机向左移动")
            self.hero1.rect.x -= 8

        if key_down[pygame.K_d]:
            print("飞机向左移动")
            self.hero1.rect.x += 8

        if key_down[pygame.K_w]:
            print("飞机向左移动")
            self.hero1.rect.y -= 8

        if key_down[pygame.K_s]:
            print("飞机向左移动")
            self.hero1.rect.y += 8

        if key_down[pygame.K_f]:
            self.hero1.fires("./images/bullet_1.png")
