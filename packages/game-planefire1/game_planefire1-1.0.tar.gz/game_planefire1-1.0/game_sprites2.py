import pygame,random,time,math
SCREEN_SIZE = (512,768)
SCREEN_RECT = pygame.Rect(0,0,*SCREEN_SIZE)
ENEMY_CREATE = pygame.USEREVENT

class GameSprite(pygame.sprite.Sprite):
    def __init__(self,image_path,speed = 0):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed

class BackgroundSprite(GameSprite):

    def __init__(self,image_path,prepare = False):
        super().__init__(image_path, speed=2)

        if prepare:
            self.rect.y = -SCREEN_SIZE[1]

    def update(self):
        super().update()
        if self.rect.y > SCREEN_SIZE[1]:
            self.rect.y = -SCREEN_SIZE[1]

class HeroSprite(GameSprite):

    def __init__(self,image_path,x,y):
        super().__init__(image_path, speed=0)
        self.rect.centerx = x
        self.rect.y = y
        self.butters = pygame.sprite.Group()
        self.index = 0
        self.bld = 5

    def update(self):
        #水平距离判断
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= SCREEN_RECT.width-self.rect.width:
            self.rect.x = SCREEN_RECT.width - self.rect.width

        #垂直距离判断
        if self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.y >= SCREEN_RECT.height - self.rect.height:
            self.rect.y = SCREEN_RECT.height - self.rect.height
    def fires(self,image_path):
        self.index += 10
        butter = BulletSprite(image_path,(self.rect.centerx - 100)  + 30*math.sin(self.index),self.rect.y)
        self.butters.add(butter)

class BulletSprite(GameSprite):
    def __init__(self,image_path,x,y,speed = -8):
        super().__init__(image_path)
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def update(self):
        super().update()
        if self.rect.y < -self.rect.height:
            self.kill()

        elif self.rect.y > SCREEN_RECT.height + self.rect.height:
            self.kill()

    def __del__(self):
        print("子弹已从精灵组中销毁!!")

class EnemySprite(GameSprite):
    '''敌方飞机'''

    def __init__(self,image_path):
        # 初始化敌方飞机的数据：图片，速度
        super().__init__(image_path, speed=random.randint(3, 5))
        # 初始化敌方飞机的位置
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)
        self.rect.y = -self.rect.height
        self.buttles = pygame.sprite.Group()
        self.bomb_image_list = []
        self.index = 0

    def update(self):
        # 调用父类的方法直接运动
        super().update()
        # 边界判断
        if self.rect.y > SCREEN_RECT.height:
            # 飞机一旦超出屏幕，销毁！
            self.kill()

    def fires(self):
        self.index += 1
        super().update()
        butter = BulletSprite("./images/bullet3.png", self.rect.centerx-38, self.rect.y, speed=10)
        self.buttles.add(butter)
        clock = pygame.time.Clock()
        clock.tick(30)

class BuJi(GameSprite):
    def __init__(self):
        super().__init__("./images/81.png",speed=10)
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)
        self.rect.y = -self.rect.height
        self.buji = pygame.sprite.Group()

    def update(self):
        super().update()
        if self.rect.y > SCREEN_RECT.height:
            self.kill()

class HuanQiang(GameSprite):
    def __init__(self):
        super().__init__("./images/kongtou.png",speed=10)
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)
        self.rect.y = -self.rect.height
        self.huanqing1 = pygame.sprite.Group()

    def update(self):
        super().update()
        if self.rect.y > SCREEN_RECT.height:
            self.kill()

class Blood(GameSprite):

    def __init__(self,x,y):
        super().__init__("./images/xin.png",speed=0)
        self.rect.x = x
        self.rect.y = y


class Dazhao(GameSprite):
    def __init__(self,image_path):
        super().__init__(image_path,speed=-100)
        self.rect.x = SCREEN_RECT.centerx - 230
        self.rect.y = SCREEN_RECT.height
        self.da = pygame.sprite.Group()

    def update(self):
        super().update()
        if self.rect.y < -self.rect.height:
            self.kill()

    def fire(self):
        butter = BulletSprite("./images/dazhao.png", self.rect.x, self.rect.y)
        self.da.add(butter)

class Boss(GameSprite):
    def __init__(self,life):
        super().__init__("./images/666.png",speed=0)
        self.rect.x = 100
        self.rect.y = self.rect.height - 200
        self.buttless = pygame.sprite.Group()
        self.life = life
        self.index = 1


    def fire(self):
        self.index += 0.5
        butter = BulletSprite("./images/bullet3.png", (self.rect.centerx - 38) + 45*math.sin(self.index), self.rect.y, speed=10)
        self.buttless.add(butter)
        clock = pygame.time.Clock()
        clock.tick(30)



