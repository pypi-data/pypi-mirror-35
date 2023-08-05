import pygame,random
# 需要定义的常量
bullets_allowed = 0
SCREEN_SIZE = (700, 466)
SCREEN_RECT = pygame.Rect(0, 0, *SCREEN_SIZE)
# ENEMY_CREATE = pygame.USEREVENT
# POWER_CREATE = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    '''精灵对象：用于表示游戏的各种元素'''

    def __init__(self,image_path,speed=1):
        # 调用父类初始化数据
        super().__init__()
        self.speed = speed
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()

    def update(self):
        '''默认运动更新方法'''
        self.rect.y += self.speed

class BackgroundSprite(GameSprite):
    '''创建背景'''

    def __init__(self,image_path, next=False):
        super().__init__(image_path)

        if next:
            self.rect.y = -SCREEN_SIZE[1]

    def update(self):
        # 调用父类的方法，执行运动
        super().update()
        #子类中判断边界，背景图片循环
        if self.rect.y > SCREEN_SIZE[1]:
            self.rect.y = -SCREEN_SIZE[1]

class HeroSprite(GameSprite):
    '''英雄精灵对象'''

    def __init__(self,image_path):
        # 初始化英雄飞机的图片、速度
        super().__init__(image_path, speed=80)
        # 初始化英雄飞机的位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.centery = SCREEN_RECT.centery + 200
        #创建子弹精灵组
        self.bullets = pygame.sprite.Group()
        self.bullets1 = pygame.sprite.Group()
        self.bullets2 = pygame.sprite.Group()
        #创建子弹补给精灵组
        self.bulletpowers = pygame.sprite.Group()

        #设置子弹最大数量
    def update(self):
        # 水平边界判断
        if self.rect.x <= 0:
            self.rect.x =0
        elif self.rect.x >= SCREEN_RECT.width - self.rect.width:
            self.rect.x = SCREEN_RECT.width - self.rect.width

        # 垂直边界判断
        if self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.y >= SCREEN_RECT.height - self.rect.height:
            self.rect.y = SCREEN_RECT.height - self.rect.height

    def fire(self):
        '''英雄开火'''
        #创建一个子弹对象
        bullet = BulletSprite(self.rect.centerx-38, self.rect.y)
        #添加到精灵组对象
        if len(self.bullets) < bullets_allowed:
            self.bullets.add(bullet)

    def fire1(self):
        '''英雄开火'''
        #创建一个子弹对象
        bullet = BulletSprite1(self.rect.centerx-38, self.rect.y)
        #添加到精灵组对象
        if len(self.bullets1) < bullets_allowed:
            self.bullets1.add(bullet)

    def fire2(self):
        '''英雄开火'''
        #创建一个子弹对象
        bullet = BulletSprite(self.rect.centerx-38, self.rect.y)
        #添加到精灵组对象
        if len(self.bullets2) < bullets_allowed:
            self.bullets2.add(bullet)

    def firepower(self):
        "英雄补给"
        # 创建一个子弹补给对象
        power = BulletPowerSprite(SCREEN_RECT.centerx, SCREEN_RECT.centery + 200)
        # 添加到精灵组对象
        self.bulletpowers.add(power)

class BulletSprite(GameSprite):
    '''子弹精灵'''
    def __init__(self,x,y,next = False):
        #敌方子弹
        if next:
            super().__init__("./images/bullet4.png", speed=15)
            self.rect.x = x
            self.rect.y = y
        #英雄子弹
        else:
            super().__init__("./images/bullet3.png", speed=-15)
            self.rect.x = x
            self.rect.y = y

    def update(self):
        # 调用父类的方法进行操作
        super().update()
        # 边界判断 子弹销毁
        if self.rect.y <= -self.rect.height:
            # 子弹从精灵组中删除
            self.kill()

class BulletSprite1(GameSprite):
    '''子弹精灵'''
    def __init__(self,x,y,next = False):
        #英雄子弹1
        if next:
            super().__init__("./images/bullet1.png", speed=15)
            self.rect.x = x
            self.rect.y = y
        #英雄子弹2
        else:
            super().__init__("./images/bullet1.png", speed=-15)
            self.rect.x = x
            self.rect.y = y

    def update(self):
        # 调用父类的方法进行操作
        super().update()
        # 边界判断 子弹销毁
        if self.rect.y <= -self.rect.height:
            # 子弹从精灵组中删除
            self.kill()

class BulletPowerSprite(GameSprite):
    '''补给效果精灵'''
    #初始化补给位置
    def __init__(self,x,y):
        super().__init__("./images/zidanbuji.png", speed=-15)
        self.rect.centerx = x
        self.rect.centery = y


    def update(self):
        # 调用父类的方法进行操作
        super().update()
        # 边界判断 子弹销毁
        if self.rect.y <= -self.rect.height:
            # 子弹从精灵组中删除
            self.kill()
            print("子弹已经销毁")
        if self.rect.y > SCREEN_RECT.height + self.rect.y:
            # 子弹从精灵组中删除
            self.kill()
            print("子弹已经销毁")


class EnemySprite(GameSprite):
    '''敌方飞机'''

    def __init__(self):
        # 初始化敌方飞机的数据：图片，速度
        super().__init__("./images/enemy2.png",speed=random.randint(3,5))
        # 初始化敌方飞机的位置
        self.rect.x = random.randint(0,SCREEN_RECT.width - self.rect.width)
        self.rect.y = -self.rect.height
        self.buttles = pygame.sprite.Group()

        self.direction = 'right'

    def move(self):
        if self.direction == 'right':
            self.rect.x += 3
        elif self.direction == 'left':
            self.rect.x -= 3

        if self.rect.x > 512:
            self.direction = 'left'
        elif self.rect.x < 0:
            self.direction = 'right'

    def update(self):
        #调用父类的方法直接运动
        super().update()
        # 边界判断,超出屏幕销毁
        if self.rect.y > SCREEN_RECT.height:
            self.kill()
            print("敌机已经销毁")

    def fires(self):
        #敌方飞机开火
        butter = BulletSprite(self.rect.centerx-38, self.rect.y + 50, next=True)
        self.buttles.add(butter)
        clock = pygame.time.Clock()
        clock.tick(30)

class Power(GameSprite):
    "触发补给效果精灵"
    def __init__(self,image):
        # 初始化补给的数据：图片，速度
        super().__init__(image,speed=8)
        # 初始化补给的位置
        self.rect.x = random.randint(0,SCREEN_RECT.width - self.rect.width)
        self.rect.y = -self.rect.height

    def update(self):
        #调用父类的方法直接运动
        super().update()
        # 边界判断,超出屏幕销毁
        if self.rect.y > SCREEN_RECT.height:
            self.kill()
            print("英雄补给已经消失")



class Powerblood(GameSprite):
    "触发血量补给小效果"
    def __init__(self,image):
        # 初始化补给的数据：图片，速度
        super().__init__(image,speed=8)
        # 初始化补给的位置
        self.rect.x = random.randint(0,SCREEN_RECT.width - self.rect.width)
        self.rect.y =- self.rect.height

    def update(self):
        #调用父类的方法直接运动
        super().update()
        # 边界判断,超出屏幕销毁
        if self.rect.y > SCREEN_RECT.height:
            self.kill()
            print("英雄补给已经消失")

class Blood(GameSprite):

    def __init__(self):
        super().__init__("./images/xin.png", speed=0)
        self.rect.x = SCREEN_RECT.x + 635
        self.rect.y = SCREEN_RECT.y + 400

class Blood1(GameSprite):

    def __init__(self):
        super().__init__("./images/xin.png", speed=0)
        self.rect.x = SCREEN_RECT.x + 590
        self.rect.y = SCREEN_RECT.y + 400

class Blood2(GameSprite):

    def __init__(self):
        super().__init__("./images/xin.png", speed=0)
        self.rect.x = SCREEN_RECT.x + 545
        self.rect.y = SCREEN_RECT.y + 400
