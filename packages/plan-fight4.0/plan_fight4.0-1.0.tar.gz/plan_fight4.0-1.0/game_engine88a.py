import pygame,game_sprite88a,random
pygame.font.init()
ENEMY_BOOM_SCORE = 10

class GameEngine:

    def __init__(self):
        # 定义背景精灵
        self.bg1 = game_sprite88a.BackgroundSprite("./images/bg_logo.jpg")
        self.bg2 = game_sprite88a.BackgroundSprite("./images/bg_logo.jpg", next=True)

        self.bg3 = game_sprite88a.BackgroundSprite("./images/bg_logo1.jpg")
        self.bg4 = game_sprite88a.BackgroundSprite("./images/bg_logo1.jpg", next=True)

        # 定义英雄精灵
        self.hero = game_sprite88a.HeroSprite("./images/hero.png")
        # 定义英雄补给精灵
        self.power = game_sprite88a.Power("./images/buji.png")
        # 定义敌方精灵
        self.enemy = game_sprite88a.EnemySprite()
        # 定义一个敌人精灵组对象
        self.enemys = pygame.sprite.Group()
        # 定义一个子弹补给精灵组
        self.powers = pygame.sprite.Group()
        # 定义爆炸敌机精灵组
        self.enemys_boom = pygame.sprite.Group()
        # 定义触发血量补给效果精灵组
        self.chufa_xieliang = pygame.sprite.Group()
        self.buji = game_sprite88a.Powerblood("./images/81.png")
        #定义3个血量精灵
        self.blood0 = game_sprite88a.Blood()
        self.blood1 = game_sprite88a.Blood1()
        self.blood2 = game_sprite88a.Blood2()
        # 定义初始血量为3
        self.hero_blood = 3
        #血量精灵定义为列表
        self.k = [self.blood0, self.blood1, self.blood2]
        # 定义精灵组对象
        self.ressources = pygame.sprite.Group(self.bg1, self.bg2, self.hero, *self.k)
        self.ressources1 = pygame.sprite.Group(self.bg3, self.bg4, self.hero, *self.k)

        # 自定义事件
        self.ENEMY_CREATE = pygame.USEREVENT
        self.POWER_CREATE = pygame.USEREVENT + 1
        self.XIELIANG_CREATE = pygame.USEREVENT + 2
        # 间隔一定的时间，触发创建敌机的事件
        pygame.time.set_timer(self.ENEMY_CREATE, 2000)
        # 间隔一定的时间，触发创建触发补给子弹效果的事件
        pygame.time.set_timer(self.POWER_CREATE, random.randint(3000,10000))
        # 间隔一定的时间，触发创建触发血量补给效果的事件
        pygame.time.set_timer(self.XIELIANG_CREATE, random.randint(5000, 10000))

        #积分设置
        self.scroe = 0
        self.game_font = pygame.font.SysFont("fangsong", 18, True)
        self.screen = pygame.display.set_mode(game_sprite88a.SCREEN_SIZE)
        self.screen.blit(self.game_font.render("累计积分：%s" % self.scroe, True, [30, 30, 30]), [20, 20])

        # 屏幕更新
        pygame.display.update()

    def start(self):
        '''游戏开始函数'''

        # 初始化所有模块
        pygame.init()
        pygame.time.set_timer(self.ENEMY_CREATE, 2000)
        # 定义一个时钟对象，来刷新频率
        clock = pygame.time.Clock()
        # 游戏循环场景
        self.create_scene()
        self.create_muse()

        #添加背景音效
        # 初始化所有模块
        pygame.init()
        # pygame.mixer启动
        pygame.mixer.init()
        pygame.mixer.music.load('./mp3/仙剑奇缘.mp3')
        pygame.mixer.music.play(-1, 0)
        pygame.mixer.music.set_volume(0.75)

        while True:
            # 初始化所有模块
            pygame.init()

            # 定义时钟刷新帧：每秒让循环运行多少次！
            clock.tick(30)
            if self.scroe <= 100:
                self.background()
                self.enemy.move()
                self.check_event()
                self.check_collide()
                self.update_scene()
                self.screen.blit(self.game_font.render("当前分数：%s" % self.scroe, True, [0, 0, 255]), [20, 20])
                # 屏幕更新
                pygame.display.update()
            else:
                self.background1()
                self.enemy.move()
                self.check_event()
                self.check_collide()
                self.update_scene()
                self.screen.blit(self.game_font.render("当前分数：%s" % self.scroe, True, [0, 0, 255]), [20, 20])
                # 屏幕更新
                pygame.display.update()

    def create_muse(self):
        '''游戏标题'''
        pygame.display.set_caption('仙剑奇缘')

    def create_scene(self):
        '''创建游戏场景'''

        # 定义游戏窗口
        self.screen = pygame.display.set_mode(game_sprite88a.SCREEN_SIZE)

    def background(self):
        # 精灵组渲染
        self.ressources.update()
        self.ressources.draw(self.screen)
        game_sprite88a.bullets_allowed = 3

    def background1(self):
        # 精灵组渲染
        self.ressources1.update()
        self.ressources1.draw(self.screen)
        game_sprite88a.bullets_allowed = 5

    def update_scene(self):
        '''更新游戏场景'''
        # 补给子弹效果精灵组渲染
        self.hero.bulletpowers.update()
        self.hero.bulletpowers.draw(self.screen)

        # 英雄子弹精灵组渲染
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

        self.hero.bullets1.update()
        self.hero.bullets1.draw(self.screen)

        self.hero.bullets2.update()
        self.hero.bullets2.draw(self.screen)


        # 触发补给子弹精灵组渲染
        self.powers.update()
        self.powers.draw(self.screen)

        # 触发血量补给效果精灵组渲染
        self.chufa_xieliang.update()
        self.chufa_xieliang.draw(self.screen)

        # 敌方子弹精灵组渲染
        self.enemy.buttles.update()
        self.enemy.buttles.draw(self.screen)

        # 渲染敌机精灵组中的所有飞机
        self.enemys.update()
        self.enemys.draw(self.screen)

        # 屏幕更新
        pygame.display.update()

    def boom(self, enemy):
        '''爆炸'''
        for i in range(1, 5):
            clock = pygame.time.Clock()
            clock.tick(30)
            image = pygame.image.load("./images/enemy2_down" + str(3) + ".png")
            self.screen.blit(image, enemy.rect)
            pygame.display.update()
            print(image)

    def check_collide(self):
        '''碰撞检测'''
        # 碰撞检测:子弹和敌方飞机之间的碰撞！
        self.enemys_boom_dict = pygame.sprite.groupcollide(self.hero.bullets, self.enemys, True, True)
        self.scroe += len(self.enemys_boom_dict) * ENEMY_BOOM_SCORE
        self.enemys_boom.add(self.enemys_boom_dict)  # 添加到爆炸精灵组
        for enemy_boom in self.enemys_boom:
            self.boom(enemy_boom)  # 将敌机返回到爆炸组，调用函数
            print("爆炸")
            self.enemys_boom.remove(enemy_boom)
        if len(self.enemys_boom_dict) > 0:
            print("敌机死亡了")
            #敌机爆炸音效
            pygame.init()
            pygame.mixer.init()
            soundwav = pygame.mixer.Sound("./mp3/enemy_down.wav")
            soundwav.play()

        # 碰撞检测:子弹和敌方飞机之间的碰撞！
        self.enemys_boom_dict = pygame.sprite.groupcollide(self.hero.bullets1, self.enemys, True, True)
        self.scroe += len(self.enemys_boom_dict) * ENEMY_BOOM_SCORE
        self.enemys_boom.add(self.enemys_boom_dict)  # 添加到爆炸精灵组
        for enemy_boom in self.enemys_boom:
            self.boom(enemy_boom)  # 将敌机返回到爆炸组，调用函数
            print("爆炸")
            self.enemys_boom.remove(enemy_boom)
        if len(self.enemys_boom_dict) > 0:
            print("敌机死亡了")
            # 敌机爆炸音效
            pygame.init()
            pygame.mixer.init()
            soundwav = pygame.mixer.Sound("./mp3/enemy_down.wav")
            soundwav.play()

        # 碰撞检测:补给和敌方飞机之间的碰撞！
        self.enemys_boom_dict = pygame.sprite.groupcollide(self.hero.bulletpowers, self.enemys, False, True)
        self.scroe += len(self.enemys_boom_dict) * ENEMY_BOOM_SCORE
        self.enemys_boom.add(self.enemys_boom_dict)  # 添加到爆炸精灵组
        for enemy_boom in self.enemys_boom:
            self.boom(enemy_boom)  # 将敌机返回到爆炸组，调用函数
            print("爆炸")
            self.enemys_boom.remove(enemy_boom)
        if len(self.enemys_boom_dict) > 0:
            print("敌机死亡了")
            # 敌机爆炸音效
            pygame.init()
            pygame.mixer.init()
            soundwav = pygame.mixer.Sound("./mp3/enemy_down.wav")
            soundwav.play()

        # 碰撞检测：英雄飞机和敌方飞机之间的碰撞 血量
        if pygame.sprite.spritecollide(self.hero, self.enemys, True):
            self.hero_blood -= 1
            self.k[self.hero_blood].kill()
            if self.hero_blood <= 0:
                self.hero.kill()
                pygame.quit()
                exit()
        #英雄子弹和敌方子弹之间的碰撞检测
        pygame.sprite.groupcollide(self.hero.bullets1, self.enemy.buttles, True, True)
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy.buttles, True, True)

        # 碰撞检测：英雄飞机和敌方飞机子弹之间的碰撞
        o = pygame.sprite.spritecollide(self.hero, self.enemy.buttles, True)
        if len(o) > 0:
            self.hero_blood -= 1
            self.k[self.hero_blood].kill()
            if self.hero_blood <= 0:
                self.hero.kill()
                pygame.quit()
                exit()

        # 碰撞检测：英雄飞机和补给之间的碰撞 血量加
        m = pygame.sprite.spritecollide(self.hero, self.chufa_xieliang, True)
        if len(m) > 0:

            if self.hero_blood >= 3:
                self.hero_blood = 3
            else:
                self.ressources.add(self.k[self.hero_blood])
                self.hero_blood += 1
                print(self.k)
                # 发射子弹音效
                pygame.init()
                pygame.mixer.init()
                soundwav = pygame.mixer.Sound("./mp3/game_buji.wav")
                soundwav.play()

        # 碰撞检测：英雄飞机和补给之间的碰撞 血量加
        p = pygame.sprite.spritecollide(self.hero, self.chufa_xieliang, True)
        if len(p) > 0:

            if self.hero_blood >= 3:
                self.hero_blood = 3
            else:
                self.ressources1.add(self.k[self.hero_blood])
                self.hero_blood += 1
                print(self.k)
                # 发射子弹音效
                pygame.init()
                pygame.mixer.init()
                soundwav = pygame.mixer.Sound("./mp3/game_buji.wav")
                soundwav.play()


        # 碰撞检测：英雄飞机和子弹补给之间的碰撞
        power_b = pygame.sprite.spritecollide(self.hero, self.powers, True)
        if len(power_b) > 0:
            self.hero.firepower()

            # # 添加背景音效
            # # 初始化所有模块
            # pygame.init()
            # # pygame.mixer启动
            # pygame.mixer.init()
            # pygame.mixer.music.load('./mp3/zidan.mp3')
            # pygame.mixer.music.play(0, 1.3)
            # pygame.mixer.music.set_volume(0.74)

    def check_event(self):
        '''事件监听'''
        # 监听所有事件
        event_list = pygame.event.get()
        if len(event_list) > 0:
            print(event_list)
            for event in event_list:
                print(event.type, pygame.KEYDOWN, pygame.K_LEFT)
                # 如果当前的事件：是quit事件
                if event.type == pygame.QUIT:
                    # 卸载所有pygame,退出程序
                    pygame.quit()
                    exit()

                #敌机出现
                if event.type == self.ENEMY_CREATE:
                    print("创建一架飞机。。。")
                    self.enemy = game_sprite88a.EnemySprite()
                    # 添加到敌方飞机精灵组中
                    self.enemys.add(self.enemy)
                #触发血量补给效果出现
                if event.type == self.XIELIANG_CREATE:
                    print("创建血量补给。。。")
                    self.buji = game_sprite88a.Powerblood("./images/81.png")
                    self.chufa_xieliang.add(self.buji)

                #英雄补给
                if event.type == self.POWER_CREATE:
                    print("创建子弹补给。。。")
                    self.power = game_sprite88a.Power("./images/buji.png")
                    self.powers.add(self.power)

                #敌方子弹
                enemy_a = random.randint(1,10)
                if enemy_a < 3 :
                    self.enemy.fires()

                #发射子弹
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.hero.fire()
                        print("发射子弹》》》", self.hero.bullets)

                       #发射子弹音效
                        pygame.init()
                        pygame.mixer.init()
                        soundwav = pygame.mixer.Sound("./mp3/bullet.wav")
                        soundwav.play()

                # 发射子弹
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_z:
                        self.hero.fire1()
                        print("发射子弹》》》", self.hero.bullets1)

                        # 发射子弹音效
                        pygame.init()
                        pygame.mixer.init()
                        soundwav = pygame.mixer.Sound("./mp3/bullet.wav")
                        soundwav.play()

                # 发射子弹
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        self.hero.fire2()
                        print("发射子弹》》》", self.hero.bullets2)

                        # 发射子弹音效
                        pygame.init()
                        pygame.mixer.init()
                        soundwav = pygame.mixer.Sound("./mp3/bullet.wav")
                        soundwav.play()



        # 获取当前用户键盘上被操作的按键
        key_down = pygame.key.get_pressed()
        self.hero.m = 20

        if key_down[pygame.K_LEFT]:
            print("向左移动<<<<<<<<<<<<")
            self.hero.rect.x -= self.hero.m
        elif key_down[pygame.K_RIGHT]:
            print("向右移动>>>>>>>>>>>>")
            self.hero.rect.x += self.hero.m
        elif key_down[pygame.K_UP]:
            print("向上移动^^^^^^^^^^^")
            self.hero.rect.y -= self.hero.m
        elif key_down[pygame.K_DOWN]:
            print("向下移动vvvvvvvvv")
            self.hero.rect.y += self.hero.m
