'''
存放飞机大战中所有精灵类型的文件
author:jiaojiao
time:2018/8/5
'''
import pygame,random

# 定义需要的常量
SCREEN_SIZE = (500, 700)
SCREEN_RECT = pygame.Rect(0, 0, *SCREEN_SIZE)


# 定义游戏精灵类型
class GameSprite(pygame.sprite.Sprite):
    """游戏精灵对象，用于表示游戏中的各个元素"""

    def __init__(self,image_path,speed=0):
        # 初始化数据
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        # 默认运动更新方式
        self.rect.y += self.speed


# 定义游戏背景类型
class BackgroundSprite(GameSprite):

    def __init__(self, image_path, speed, perpare=False):
        # 继承父类
        super().__init__(image_path, speed)

        if perpare:
            self.rect.y = -SCREEN_SIZE[1]

    def update(self):
        # 调用父类方法，执行运动
        super().update()
        # 判断背景图片
        if self.rect.y > SCREEN_SIZE[1]:
            self.rect.y = -SCREEN_SIZE[1]


# 定义英雄飞机类型
class HeroSprite(GameSprite):
    """英雄飞机精灵对象"""

    def __init__(self, image_path, speed):
        # 初始化英雄飞机的图片，速度
        super().__init__(image_path, speed=0)
        self.speed = speed
        # 初始化英雄飞机的位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.centery = SCREEN_RECT.centery + 200
        # 子弹精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):
        # 水平边界判断
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= SCREEN_RECT.width - self.rect.width:
            self.rect.x = SCREEN_RECT.width - self.rect.width


        # 垂直边界判断
        if self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.y > SCREEN_RECT.height - self.rect.height:
            self.rect.y = SCREEN_RECT.height - self.rect.height

    def fire(self):
        """英雄飞机发射子弹"""
        # 创建一个子弹对象
        if len(self.bullets) < 7:
            bullet = BulletSprite(self.rect.centerx, self.rect.y)
            # 将子弹加到精灵组对象
            self.bullets.add(bullet)


class BulletSprite(GameSprite):
    """子弹精灵"""
    def __init__(self, x, y):
        # 获取子弹图片
        super().__init__("./images/hero_bullet.png", speed=-4)
        self.rect.x = x - 20
        self.rect.y = y

    def update(self):
        # 调用父类方法进行操作
        super().update()
        # 边界判断
        if self.rect.y <= -self.rect.height:
            self.kill()

    def __del__(self):
        print("子弹对象销毁")


class EnemySprite(GameSprite):
    """敌机精灵对象"""

    def __init__(self):
        # 初始化敌机数据：图片，速度
        super().__init__("./images/enemy.png", speed=random.randint(2, 3))
        # 初始化敌方飞机位置
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)
        self.rect.y = -self.rect.height

    def update(self):
        # 调用父类方法，执行运动
        super().update()
        # 子类中判断边界
        if self.rect.y > SCREEN_RECT.height:
            # 飞机一旦超出屏幕就销毁
            self.kill()

    def __del__(self):
        self.destroy()

    def destroy(self):
        print("敌方飞机销毁")


class Music:
    """游戏中音乐，音效"""

    def back_music(self):
        music1 = pygame.mixer.Sound("./music/game_music.wav")
        music1.play()

    def bullet_music(self):
        music2 = pygame.mixer.Sound("./music/bullet.wav")
        music2.play()

    def bomb_music(self):
        music3 = pygame.mixer.Sound("./music/enemy_down.wav")
        music3.play()


class Index(GameSprite):
    """定义首页类"""

    def __init__(self, image_path):
        # 继承父类
        super().__init__(image_path, speed=0)

    def update(self):

        super().update()


class EnemyBulletSprite(GameSprite):
    """敌机子弹精灵"""

    def __init__(self, x, y):
        # 获取子弹图片
        super().__init__("./images/enemy_bullet.png", speed=4)
