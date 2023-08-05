import random

import models, pygame

# 自定义事件
ENEMY_CREATE = pygame.USEREVENT



class GameEngine:
    def __init__(self):
        # 初始化游戏模块
        pygame.init()

        # 创建一个游戏窗口
        self.screen = models.pygame.display.set_mode(models.SCREEN_SIZE)

        # 游戏背景
        background1 = models.BackgroundSprite("./images/background1.jpg")
        background2 = models.BackgroundSprite("./images/background2.jpg", next=True)

        # 定义英雄飞机对象
        self.hero1 = models.HeroSprite("./images/Hero1.png", x=models.SCREEN_RECT.centerx-600, y=models.SCREEN_RECT.centery+276)
        self.hero2 = models.HeroSprite("./images/Hero2.png", x=models.SCREEN_RECT.centerx+300, y=models.SCREEN_RECT.centery+347)

        # 添加背景、英雄精灵组对象
        self.resources = pygame.sprite.Group(background1, background2, self.hero1, self.hero2)

        # 定义BOSS精灵
        # self.boss = models.BossSprite("images/Boss1.png", 15, 3)
        # self.boss.hp = 100

        # 定义敌机精灵组对象
        self.enemys_1 = pygame.sprite.Group()
        self.enemys_2 = pygame.sprite.Group()
        self.enemyss = pygame.sprite.Group()
        self.bosses = pygame.sprite.Group()

        # 定义BOSS精灵组对象
        # self.bosses.add(self.boss)

        # 间隔一定时间，创建敌机事件
        pygame.time.set_timer(ENEMY_CREATE, 1500)

        # 全部子弹精灵组
        self.all_bullets = pygame.sprite.Group()

        # 定义一个时钟对象
        self.clock = pygame.time.Clock()

        # 字体
        self.font = pygame.font.SysFont("楷体", 40, True, True)

        # 创建生命值图片
        self.img_path_list = ["images/HP_1.png", "images/HP_2.png", "images/HP_3.png",
                              "images/HP_4.png", "images/HP_5.png", "images/HP_6.png"]
        # huffle方法随机排序列表
        random.shuffle(self.img_path_list)

        # 初始化两个英雄飞机的分数
        # self.hero1.score1 = 0
        # self.hero2.score2 = 0

        # 生命值
        # self.hero1.heart = 3

    # 游戏循环
    def start(self):
        # 监听所有事件
        event_list = pygame.event.get()
        if len(event_list) > 0:

            # 退出
            for event in event_list:
                # QUIT事件
                if event.type == pygame.QUIT:
                    # 卸载所有pygame资源，退出程序
                    pygame.quit()
                    exit()

                if event.type == ENEMY_CREATE:
                    print("创建敌方飞机......")
                    enemy1 = models.EnemySprite("images/Enemy1.png")
                    enemy2 = models.EnemySprite("images/Enemy2.png")
                    enemy3 = models.EnemySprite("images/Enemy3.png")
                    enemy4 = models.EnemySprite("images/Enemy4.png")
                    enemy5 = models.EnemySprite("images/Enemy5.png")
                    self.create_boss()

                    # 修改敌机生命值
                    enemy3.hp = 9
                    enemy4.hp = 9
                    # boss.hp = 100
                    # boss.speed = 11

                    # 添加到敌方飞机精灵组中
                    self.enemys_1.add(enemy1, enemy2)
                    self.enemys_2.add(enemy3, enemy4, enemy5)
                    self.enemyss.add(self.enemys_1, self.enemys_2)

                # 英雄发射子弹
                if event.type == pygame.KEYDOWN:
                    key_down = pygame.key.get_pressed()
                    if key_down[pygame.K_RCTRL]:
                        self.hero2.fire()
                        self.all_bullets.add(self.hero2.bullets)
                        # print("发射子弹<<<<<<<<<<<<<<<<")

                    if key_down[pygame.K_SPACE]:
                        self.hero1.fire()
                        self.all_bullets.add(self.hero1.bullets)
                        # print("发射子弹<<<<<<<<<<<<<<<<")

        # 二号英雄移动
        key_down = pygame.key.get_pressed()
        if key_down[pygame.K_LEFT]:
            # print("向左移动<<<<<<<<<<<<<<<<")
            self.hero2.rect.x -= 10
        elif key_down[pygame.K_RIGHT]:
            # print("向右移动<<<<<<<<<<<<<<<<")
            self.hero2.rect.x += 10
        elif key_down[pygame.K_UP]:
            # print("向上移动<<<<<<<<<<<<<<<<")
            self.hero2.rect.y -= 10
        elif key_down[pygame.K_DOWN]:
            # print("向下移动<<<<<<<<<<<<<<<<")
            self.hero2.rect.y += 10

        # 监听键盘事件
        # key_down = pygame.key.get_pressed()

        # if key_down[pygame.K_LEFT]:
        #     print("向左移动<<<<<<<<<<<<<<<<")
        #     self.hero2.rect.x -= 10
        # elif key_down[pygame.K_RIGHT]:
        #     print("向右移动<<<<<<<<<<<<<<<<")
        #     self.hero2.rect.x += 10
        # elif key_down[pygame.K_UP]:
        #     print("向上移动<<<<<<<<<<<<<<<<")
        #     self.hero2.rect.y -= 10
        # elif key_down[pygame.K_DOWN]:
        #     print("向下移动<<<<<<<<<<<<<<<<")
        #     self.hero2.rect.y += 10

        # for event in event_list:
        #     if event.type == pygame.KEYDOWN:
        #         if key_down[pygame.K_RCTRL]:
        #             self.hero2.fire()
        #             self.all_bullets.add(self.hero2.bullets)
        #             print("发射子弹<<<<<<<<<<<<<<<<")

        # 一号英雄移动
        if key_down[pygame.K_a]:
            # print("向左移动<<<<<<<<<<<<<<<<")
            self.hero1.rect.x -= 10
        elif key_down[pygame.K_d]:
            # print("向右移动<<<<<<<<<<<<<<<<")
            self.hero1.rect.x += 10
        elif key_down[pygame.K_w]:
            # print("向上移动<<<<<<<<<<<<<<<<")
            self.hero1.rect.y -= 10
        elif key_down[pygame.K_s]:
            # print("向下移动<<<<<<<<<<<<<<<<")
            self.hero1.rect.y += 10
            # for event in event_list:
            #     if event.type == pygame.KEYDOWN:
            #         if key_down[pygame.K_SPACE]:
            #             self.hero1.fire()
            #             self.all_bullets.add(self.hero1.bullets)
            #             print("发射子弹<<<<<<<<<<<<<<<<")

    def render(self):
        # 渲染精灵组
        self.resources.update()
        self.resources.draw(self.screen)

        # 渲染敌机精灵组
        # self.enemys_1.update()
        # self.enemys_1.draw(self.screen)
        # self.enemys_2.update()
        # self.enemys_2.draw(self.screen)
        self.enemyss.update()
        self.enemyss.draw(self.screen)

        # 渲染所有子弹精灵组
        self.all_bullets.update()
        self.all_bullets.draw(self.screen)

        # 渲染分数
        self.current1 = self.font.render("Player1 Score:%s" % self.hero1.score, True, (255, 0, 0))
        self.current2 = self.font.render("%s:Player2 Score" % self.hero2.score, True, (255, 0, 0))
        self.screen.blit(self.current1, (0, 30))
        self.screen.blit(self.current2, (models.SCREEN_RECT.width - 249, 30))

        # 左生命值图片渲染
        self.hp_text = self.font.render("HP:", True, (255, 0, 0))
        self.screen.blit(self.hp_text, (0, 100))

        for i in range(1, self.hero1.hp + 1):
            self.heart = pygame.image.load(self.img_path_list[i-1])
            self.screen.blit(self.heart, (60 * i, 65))

        # 右生命值图片渲染
        self.hp_text = self.font.render(":HP", True, (255, 0, 0))
        self.screen.blit(self.hp_text, (models.SCREEN_RECT.width - 65, 100))

        for i in range(1, self.hero2.hp + 1):
            self.heart = pygame.image.load(self.img_path_list[i - 1])
            self.screen.blit(self.heart, (models.SCREEN_RECT.width - 65 - 60 * i, 65))

        # if self.hero1.score + self.hero1.score == 15:
        #     print("BOSS")
        #     # self.boss.hp = 100
        #     # self.bosses.add(self.boss)
        #     self.bosses.update()
        #     self.bosses.draw(self.screen)
        #     pygame.display.update()


        self.bosses.update()
        self.bosses.draw(self.screen)

        # 屏幕刷新
        pygame.display.update()

        # self.hero1.bullets.update()
        # self.hero1.bullets.draw(self.screen)
        # self.hero2.bullets.update()
        # self.hero2.bullets.draw(self.screen)

    def impact(self):
        # 一号英雄子弹与一等敌机碰撞检测
        a = pygame.sprite.groupcollide(self.enemys_1, self.hero1.bullets, False, True)
        if len(a) > 0:
            for k, v in a.items():
                k.hp -= 3
                self.hero1.score += 1
                # return self.hero1.score
        # 一号英雄子弹与二等敌机碰撞检测
        e = pygame.sprite.groupcollide(self.enemys_2, self.hero1.bullets, False, True)
        if len(e) > 0:
            for k, v in e.items():
                k.hp -= 3
                self.hero1.score += 2
                # return self.hero1.score

        # 一号英雄子弹与boss碰撞检测
        g = pygame.sprite.groupcollide(self.bosses, self.hero1.bullets, False, True)
        if len(g) > 0:
            for k, v in g.items():
                k.hp -= 5
                self.hero1.score += 100

        # 二号英雄子弹与一等敌机碰撞检测
        b = pygame.sprite.groupcollide(self.enemys_1, self.hero2.bullets, False, True)
        if len(b) > 0:
            for k, v in b.items():
                k.hp -= 3
                self.hero2.score += 1
                # return self.hero2.score
        # 二号英雄子弹与二等敌机碰撞检测
        f = pygame.sprite.groupcollide(self.enemys_2, self.hero2.bullets, False, True)
        if len(f) > 0:
            for k, v in f.items():
                k.hp -= 3
                self.hero2.score += 2
                # return self.hero2.score

        # 二号英雄子弹与boss碰撞检测
        h = pygame.sprite.groupcollide(self.bosses, self.hero2.bullets, False, True)
        if len(h) > 0:
            for k, v in h.items():
                k.hp -= 5
                self.hero1.score += 100

        # 一号英雄与敌机碰撞检测
        c = pygame.sprite.spritecollide(self.hero1, self.enemyss, True)
        if len(c) > 0:
            self.hero1.hp -= 1
            if self.hero1.hp <= 0:
                self.hero1.kill()
                print("英雄1销毁")

        # 一号英雄与boss碰撞检测
        i = pygame.sprite.spritecollide(self.hero1, self.bosses, False)
        if len(i) > 0:
            self.hero1.hp -= 5
            if self.hero1.hp <= 0:
                self.hero1.kill()
                print("英雄1销毁")

        # 二号英雄与敌机碰撞检测
        d = pygame.sprite.spritecollide(self.hero2, self.enemyss, True)
        if len(d) > 0:
            self.hero2.hp -= 1
            if self.hero2.hp <= 0:
                self.hero2.kill()
                print("英雄2销毁")

        # 二号英雄与boss碰撞检测
        j = pygame.sprite.spritecollide(self.hero2, self.bosses, False)
        if len(j) > 0:
            self.hero2.hp -= 5
            if self.hero2.hp <= 0:
                self.hero2.kill()
                print("英雄2销毁")

    # # def file(self):
    #     # 英雄生命值
    #     if self.hero1.hp <= 0:
    #         self.hero1.kill()
    #         print("英雄1销毁")
    #     if self.hero2.hp <= 0:
    #         self.hero2.kill()
    #         print("英雄2销毁")

        # 当两个英雄均生命值为零，游戏结束
        if self.hero1.hp <= 0 and self.hero2.hp <= 0:
            pygame.quit()
            print("游戏结束")
            exit()

        # e = pygame.sprite.spritecollide(self.hero1, self.enemys_2, True)
        # f = pygame.sprite.spritecollide(self.hero2, self.enemys_2, True)

        # d = hero1.life
        #     if d <= 0:
        #         hero1.kill()

        # if len(x) > 0:
        #     hero1.kill()
        #     pygame.quit()
        #     exit()
        # elif len(y) > 0:
        #     hero2.kill()
        #     pygame.quit()
        #     exit()

        # 当前屏幕刷新
        # pygame.display.update()

    # 循环方法
    def update_scene(self):
        while True:
            self.clock.tick(60)
            self.start()
            self.impact()
            self.render()


        # basic_Font = pygame.font.SysFont("楷体", 40)
        # # text = basic_Font.render(Score:)
        # hp_text = basic_Font.render("HP:", True, (255, 255, 255))
        # self.screen.blit(text, (0, 0))
        # self.screen.blit(hp_text, (0, 40))
        # for i in range(1, self.hero1.hp + 1):
        #     self.screen.blit(self.heart, (46*1, 40))
        #

    def create_boss(self):
        if self.hero1.score + self.hero2.score >= 20 and len(self.bosses) == 0:
            boss = models.BossSprite("images/Boss1.png", 15, 3)
            boss.hp = 100
            print("boss创建")
            self.bosses.add(boss)


if __name__ == "__main__":
    game_engine = GameEngine()
    game_engine.update_scene()
