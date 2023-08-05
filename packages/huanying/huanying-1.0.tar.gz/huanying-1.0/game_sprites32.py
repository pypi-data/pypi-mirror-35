import pygame, random,time

# 定义需要的常量
SCREEN_SIZE = (512, 768)
SCREEN_RECT = pygame.Rect(0, 0, *SCREEN_SIZE)



class GameSprite(pygame.sprite.Sprite):
    '''游戏精灵对象：用于表示游戏中的各种元素'''

    def __init__(self, image_path, speed=1):
        # 调用父类初始化数据
        super().__init__()

        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        '''默认运动更新方法'''
        self.rect.y += self.speed


class BackgrounSprite(GameSprite):

    def __init__(self, image_path, next=False):
        super().__init__(image_path)

        if next:
            self.rect.y = -SCREEN_SIZE[1]

    def update(self):
        # 调用父类的方法，执行运动
        super().update()
        # 子类中判断边界
        if self.rect.y > SCREEN_SIZE[1]:
            self.rect.y = -SCREEN_SIZE[1]


class HeroSprite(GameSprite):
    '''英雄精灵对象'''

    def __init__(self):
        # 初始化英雄飞机的图片、速度
        super().__init__("./imag/hero14.png", speed=0)
        # 初始化英雄飞机的位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.y = SCREEN_RECT.centery

        self.bullets = pygame.sprite.Group()

    def update(self):
        # 水平边界判断
        if self.rect.x <= 0:
            self.rect.x =0
        elif self.rect.x >= SCREEN_RECT.width - self.rect.width:
            self.rect.x = SCREEN_RECT.width - self.rect.width

        # 垂直边界判断
        if self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.y >= 768-self.rect.height:
            self.rect.y =  768-self.rect.height

    def fire(self):
        '''飞机攻击'''
        # 创建一个子弹对象
        bullet = BulletSprite("./imag/bullet12.png", self.rect.centerx, self.rect.y)
        # 添加到精灵组对象
        self.bullets.add(bullet)

    def fire1(self):
        butter1 = BulletSprite("./imag/bullt10.png", self.rect.centerx, self.rect.y)
        self.bullets.add(butter1)

    def fire2(self):
        butter2 = BulletSprite("./imag/bullet2.png", self.rect.centerx, self.rect.y)
        self.bullets.add(butter2)

class BulletSprite(GameSprite):
    '''子弹精灵'''
    def __init__(self,immage_path, x, y):
        super().__init__(immage_path,  speed=-4)

        self.rect.centerx = x
        self.rect.y = y - self.rect.y

    # hero = pygame.images.load("./imag/hero.png")
    # hero_rect = pygame.Rect(196, 500, 120, 79)

    def update(self):
        # 调用父类的方法进行操作
        super().update()
        # 边界判断
        if self.rect.y <= -self.rect.height:
            # 子弹从精灵组中删除
            self.kill()

    def __del__(self):
        print("子弹对象已经销毁")



# class BulletSprite(GameSprite):
#     '''子弹精灵'''
#     def __init__(self, x, y, speed=-8):
#         super().__init__("./imag/bullet2.png")
#
#         self.rect.centerx = x
#         self.rect.y = y - self.rect.y
#         print("qqqqqqqqqqqqqqqqqqqqqqqqq")
#     # hero = pygame.images.load("./imag/hero.png")
#     # hero_rect = pygame.Rect(196, 500, 120, 79)
#
#     def update(self):
#         # 调用父类的方法进行操作
#         super().update()
#         # 边界判断
#         if self.rect.y <= -self.rect.height:
#             # 子弹从精灵组中删除
#             self.kill()
#
#         if self.rect.y > SCREEN_RECT.height + self.rect.height:
#             self.kill()
#     def __del__(self):
#         print("子弹对象已经销毁")
class BulletSprit(GameSprite):
    """敌机子弹"""
    def __init__(self,image_path,x,y,speed = -8):
        super().__init__(image_path)
        self.rect.centerx = x
        self.rect.y = y
        self.speed = speed

    def update(self):
        super().update()

        if self.rect.y > SCREEN_RECT.height + self.rect.height:
            self.kill()

    def __del__(self):
        print("敌机子弹销毁")

class EnemySprite(GameSprite):
    '''敌方飞机'''

    def __init__(self):
        # 初始化敌方飞机的数据：图片，速度
        super().__init__("./imag/enemy121.png", speed=2)
        # 初始化敌方飞机的位置
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)
        self.rect.y = -self.rect.height

        self.buttles = pygame.sprite.Group()
        a = random.randint(1, 10)
        if a > 5:
            self.direction = 'right'
        else:
            self.direction = 'left'
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
        # 调用父类的方法直接运动
        super().update()
        # 边界判断
        if self.rect.y > SCREEN_RECT.height:
            # 飞机一旦超出屏幕，销毁！
            self.kill()

    def fires(self):
        butter = BulletSprit("./imag/bullet13.png", self.rect.centerx, self.rect.y, speed=5)
            # butter = BulletSprite(self.rect.centerx-38, self.rect.y, speed=16)
        self.buttles.add(butter)



    def __del__(self):
        self.destroy()

    def destroy(self):
        print("敌机销毁")
        for img_path in ["./imag/enemy2_down1.png","./imag/enemy2_down2.png","./imag/enemy_bomb5.png","./imag/enemy_bomb5.png"]:
            self.image = pygame.image.load(img_path)
