# 导入模块
import pygame, random

# 定义常量
SCREEN_SIZE = (1600, 900)
SCREEN_RECT = pygame.Rect(0, 0, *SCREEN_SIZE)


class GameSprite(pygame.sprite.Sprite):
    """游戏精灵对象"""
    def __init__(self, image_path, speed=1):
        # 调用父类初始化函数
        super().__init__()
        # 创建一个图片对象
        self.image = pygame.image.load(image_path)
        # 获取精灵位置对象
        self.rect = self.image.get_rect()
        # 速度
        self.speed = speed
        self.hp = 5

    def update(self):
        """通用默认移动"""
        self.rect.y += self.speed
        # if self.life <= 0:
        #     self.kill()


class BackgroundSprite(GameSprite):
    """背景精灵"""
    def __init__(self, image_path, next=False):
        super().__init__(image_path, speed=10)

        if next:
            self.rect.y = -SCREEN_SIZE[1]

    def update(self):
        # 调用父类的update让其移动
        super().update()
        # 判断位置
        if self.rect.y > SCREEN_SIZE[1]:
            self.rect.y = -SCREEN_SIZE[1]


class HeroSprite(GameSprite):
    """英雄精灵对象"""
    def __init__(self, image_path, x, y):
        # 初始化英雄飞机的图片、速度
        super().__init__(image_path, speed=10)
        # 初始化英雄飞机的位置
        self.rect.x = x
        self.rect.y = y
        # 设置生命值
        self.hp = 5
        self.score = 0
        self.bullets = pygame.sprite.Group()

    def update(self):
        # 水平边界判断
        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.x >= SCREEN_RECT.width - self.rect.width:
            self.rect.x = SCREEN_RECT.width - self.rect.width

        # 垂直边界判断
        if self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.y >= SCREEN_RECT.height - self.rect.height:
            self.rect.y = SCREEN_RECT.height - self.rect.height

        # 英雄生命值
        if self.hp <= 0:
            self.kill()
            # pygame.quit()
            # exit()

    def fire(self):
        """飞机攻击"""
        # 创建子弹对象
        bullets = BulletSprite(self.rect.centerx-61, self.rect.y)
        # bullet2 = BulletSprite(self.rect.centerx-61, self.rect.y)

        # 添加到精灵组对象
        self.bullets.add(bullets)


class BulletSprite(GameSprite):
    """子弹精灵"""
    def __init__(self, x, y):
        image_path = "./images/Bullet1.png"
        super().__init__(image_path, speed=-10)

        self.rect.x = x
        self.rect.y = y

    def update(self):
        # 调用父类的方法进行操作
        super().update()
        # 边界判断
        if self.rect.y <= -self.rect.height:
            # 子弹从精灵组中删除
            self.kill()

    def __del__(self):
        print("子弹对象已经销毁")

    # def music(self):
        # 加入子弹音效
        # self.Bullet_music = pygame.mixer.music.load("./music/button.mp3")
        # pygame.mixer.music.play()


class EnemySprite(GameSprite):
    """敌方飞机"""
    def __init__(self, image_path):
        # 初始化敌方飞机的图片、速度
        # super().__init__("./images/Enemy1.png", speed=random.randint(3, 6))
        super().__init__(image_path, speed=random.randint(11, 15))
        # 初始化敌方飞机位置
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)
        self.rect.y = -self.rect.height
        self.hp = 3

    def update(self):
        # 调用父类的方法直接运动
        super().update()
        # 边界判断
        if self.rect.y > SCREEN_RECT.height:
            # 超出边界，销毁
            self.kill()

        # 敌机生命值
        if self.hp <= 0:
            self.kill()

    def __del__(self):
        self.destroy()

    def destroy(self):
        print("敌方飞机销毁")
        # for img_path in ["./images/Enemy1-1.png", "./images/Enemy1-2.png", "./images/Enemy1-3.png"]:
            # self.image = pygame.image.load(img_path)


class BossSprite(GameSprite):
    """BOSS"""
    def __init__(self, image_path, speed, xspeed):
        super().__init__(image_path, speed)
        # image_path = "images/Boss1.png"
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)
        self.rect.y = -self.rect.height
        self.xspeed = xspeed
        print(self.rect.x,self.rect.y,self.xspeed,self.speed)
        # self.hp = 100

    def update(self):
        self.rect.x += self.xspeed
        self.rect.y += self.speed
        if self.rect.x >= SCREEN_RECT.width - self.rect.width or self.rect.x <= 0:
            self.xspeed = -self.xspeed
        elif self.rect.y >= SCREEN_RECT.height/5:
            self.speed = -5
        elif self.rect.y <= 0:
            self.speed = 11
