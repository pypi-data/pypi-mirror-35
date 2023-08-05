import game_sprites32
ENEMY_BOOM_SCORE = 10
import pygame, random,time
# 自定义一个事件
ENEMY_CREATE = pygame.USEREVENT
OTHER_EVENT = pygame.USEREVENT + 1
# engine =GameEngine()
# engine.start()
pygame.init()  # 初始化所有模块


class GameEngine:
    def __init__(self):
        # 定义背景精灵
        self.bg1 = game_sprites32.BackgrounSprite("./images/bkgroud11.png")
        self.bg2 = game_sprites32.BackgrounSprite("./images/bkgroud11.png", next=True)

        # 定义英雄飞机对象
        self.hero = game_sprites32.HeroSprite()

        # 定义初始化精灵组对象
        self.resources = pygame.sprite.Group(self.bg1, self.bg2, self.hero, )
        # 定义一个敌人飞机的精灵组对象
        self.enemys = pygame.sprite.Group()
        # 爆炸敌机精灵组
        self.enemys_boom = pygame.sprite.Group()
        self.clock = pygame.time.Clock()  # 定义一个时钟
        self.create_scene()  # 创建游戏场景
        # self.enemy1 = game_sprites32.EnemySprite()
        self.enemy1 = game_sprites32.EnemySprite()
    def start(self):  # 开始运行


        # self.clock = pygame.time.Clock()  # 定义一个时钟
        #
        # self.create_scene()  # 创建游戏场景
        while True:
            # self.clock.tick(60)
            # 标题渲染

            pygame.display.set_icon(pygame.image.load("./images/top.jpg"))  # 读取、渲染窗口图片
            background_image = pygame.image.load("./images/logo.png")
            self.screen.blit(background_image, (0, 0))

            self.my_font = pygame.font.SysFont('kaiti', 23)  # 字体字号
            self.screen.blit(self.my_font.render('W.S.A.D控制方向，', False, (255, 100, 100)), [170, 300])
            self.my_font = pygame.font.SysFont('kaiti', 23)  # 字体字号
            self.screen.blit(self.my_font.render( ' J.K.L发射子弹', False, (255, 100, 100)), [170, 330])
            pygame.display.update()

            # self.kaishi_s.update()
            # self.kaishi_s.draw(self.screen)
            event_list = pygame.event.get()
            for event in event_list:
                if event.type == pygame.MOUSEBUTTONUP:
                    if (120 < event.pos[0] < 380) and (500 < event.pos[1] < 600):
                        self.start1()
                # 如果当前事件是  QUIT  事件，卸载所有资源
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
    def start1(self):
        pygame.time.set_timer(ENEMY_CREATE, 2500)
        pygame.time.set_timer(OTHER_EVENT, 300)
        # 定义一个时钟对象
        clock = pygame.time.Clock()

        # 定义时钟刷新帧：每秒让循环运行多少次！
        clock.tick(24)
        pygame.init()
        self.create_scene()
        # 游戏场景循环
        while True:
            self.check_event()
            self.check_collide()

            for enemy1 in self.enemys:
                enemy1.move()
            self.update_scene()
    def create_scene(self):#创建游戏场景
        self.screen = pygame.display.set_mode((512, 768), 0, 32)
        pygame.display.set_caption("巨龙争霸")
        self.Music()
    def update_scene(self):#更新游戏场景
        # 精灵组渲染
        self.resources.update()
        self.resources.draw(self.screen)

        # 子弹精灵组渲染
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)
        #敌机子弹精灵渲染
        for enemy1 in self.enemys:
            enemy1.buttles.update()
            enemy1.buttles.draw(self.screen)

        # 渲染敌机精灵组中的所有飞机
        self.enemys.update()
        self.enemys.draw(self.screen)

        # 屏幕更新
        pygame.display.update()

    def boom(self, enemy):
        '''爆炸'''
        for i in range(1, 6):
            clock = pygame.time.Clock()
            clock.tick(30)
            image = pygame.image.load("./imag/enemy_bomb" + str(i) + ".png")
            self.screen.blit(image, enemy.rect)
            pygame.display.update()
            # print(images)

    def check_collide(self):#碰撞检测
        # 碰撞检测:子弹和敌方飞机之间的碰撞！
        # pygame.sprite.groupcollide(self.hero.bullets, self.enemys, True, True)

        self.enemys_boom_dict = pygame.sprite.groupcollide(self.hero.bullets, self.enemys, True, True)
        # self.scroe += len(self.enemys_boom_dict) * ENEMY_BOOM_SCORE
        self.enemys_boom.add(self.enemys_boom_dict)  # 添加到爆炸精灵组
        for enemy_boom in self.enemys_boom:

            self.boom(enemy_boom)  # 将敌机返回到爆炸组，调用函数
            print("爆炸")
            self.enemys_boom.remove(enemy_boom)
        for enemy1 in self.enemys:
            c = pygame.sprite.spritecollide(self.hero, enemy1.buttles, True)
            if len(c) > 0:
                self.hero.kill()
                self.hero = None
                self.endmenus()
                # pygame.quit()
                # exit()

        # 碰撞检测：英雄飞机和敌方飞机之间的碰撞
        e = pygame.sprite.spritecollide(self.hero, self.enemys, True)
        if len(e) > 0:
            self.hero.kill()
            self.hero = None
            self.endmenus()
            # pygame.quit()
            # exit()
    def check_event(self):#事件监听

        # 监听所有的事件
        event_list = pygame.event.get()
        if len(event_list) > 0:
            print(event_list)

            for event in event_list:
                print(event.type, pygame.KEYDOWN, pygame.K_LEFT)
                # 如果当前的事件：是QUIT事件
                if event.type == pygame.QUIT:
                    # 卸载所有pygame资源，退出程序
                    pygame.quit()
                    exit()

                if event.type == ENEMY_CREATE:
                    print("创建一架敌方飞机.....")
                    enemy1 = game_sprites32.EnemySprite()
                    # self.enemy.move() #不能移动
                    # enemy1.fires()
                    #添加到敌方飞机精灵组中

                    self.enemys.add(enemy1)
                    # self.enemy.fires()
                    # a = random.randint(1, 100)
                    # if a > 10:
                    #     self.enemy.fires()
                # if event.type == OTHER_EVENT:
                #     print("创建一架己方飞机.....")
                    # enemy = EnemySprite()
                    # # 添加到敌方飞机精灵组中
                    # enemys.add(enemy)
                    # self.hero.fire()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_k:
                        self.hero.fire()
                        # 敌机爆炸音效
                        pygame.init()
                        pygame.mixer.init()
                        soundwav = pygame.mixer.Sound("./imag/enemy_music.wav")
                        soundwav.play()

                    if event.key == pygame.K_j:
                        self.hero.fire1()
                        # 敌机爆炸音效
                        pygame.init()
                        pygame.mixer.init()
                        soundwav = pygame.mixer.Sound("./imag/enemy_music.wav")
                        soundwav.play()

                    if event.key == pygame.K_l:
                        self.hero.fire2()
                        # 敌机爆炸音效
                        pygame.init()
                        pygame.mixer.init()
                        soundwav = pygame.mixer.Sound("./imag/enemy_music.wav")
                        soundwav.play()
            for enemy1 in self.enemys:
                a = random.randint(1, 100)
                if a > 90:
                    enemy1.fires()


        # 获取当前用户键盘上被操作的按键
        key_down = pygame.key.get_pressed()

        if key_down[pygame.K_a]:
            print("向左移动<<<<<<<<<<<<")
            self.hero.rect.x -= 10
        elif key_down[pygame.K_d]:
            print("向右移动>>>>>>>>>>>>")
            self.hero.rect.x += 10
        elif key_down[pygame.K_w]:
            print("向上移动^^^^^^^^^^^")
            self.hero.rect.y -= 10
        elif key_down[pygame.K_s]:
            print("向下移动vvvvvvvvv")
            self.hero.rect.y += 10

    def Music(self):
        # 背景音乐
        pygame.mixer.init()
        pygame.mixer.music.load("./imag/music.mp3")
        # 循环播放多少次
        pygame.mixer.music.play(1)
        # 设置音量
        pygame.mixer.music.set_volume(100)

    def endmenus(self):
        if self.hero ==None:
        # if self.hero1 == None or self.hero2 == None or self.boss == None:
            self.create_scene()  # 创建游戏场景
            while True:
                # bg = modles.BackGroundSprite("./images/gameover.jpg", 0)
                # pygame.display.set_icon(pygame.image.load("./images/gameover.jpg"))
                # self.resources = pygame.sprite.Group(bg)
                # self.resources.update()
                # self.resources.draw(modles.screen)
                background_image = pygame.image.load("./images/gameover.jpg")


                self.screen.blit(background_image, (0, 0))
                pygame.display.update()
                event_list = pygame.event.get()
                if len(event_list) > 0:
                    print(event_list)
                    for event in event_list:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if (100 < event.pos[0] < 390) and (660 < event.pos[1] < 730):
                                pygame.quit()
                                exit()
                            elif (100 < event.pos[0] < 390) and (575 < event.pos[1] < 650):
                                self.__init__()
                                self.start()
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()