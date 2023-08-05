'''
精灵对象库
'''

import pygame, random, math
# 定义需要的常量
screen_size = (512, 768)
screen_rect = pygame.Rect(0, 0, *screen_size)

# 自定义一个事件
enemy_create = pygame.USEREVENT
# other_event = pygame.USEREVENT + 1

# 定义游戏基本元素，作为一个父类使用
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image_path, speed=1):
        # 调用父类， 初始化数据
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.speed = speed
    # 场景默认向下运动
    def update(self):
        self.rect.y += self.speed
# #游戏开始界面
# class StartgameSprite(GameSprite):
#     def __init__(self):
#         super().__init__('bg_img_2.jpg', speed = 0)

# 定义游戏背景 --继承父类
class BackgroundSprite(GameSprite):
    def __init__(self, next=False):
        super().__init__('./images/bg_img_5.jpg', speed =3)
        # 输出完第一张背景图片，第二张图片接力
        if next:
            self.rect.y = -screen_size[1]
    def update(self):
        # 调用父类默认的运动方法
        super().update()
        # 子类中判断边界
        if self.rect.y > screen_size[1]:
            self.rect.y = -screen_size[1]
# 定义我方飞机 精灵
class HeroSprite(GameSprite):
    def __init__(self):
        # 初始化飞机的图片、速度
        super().__init__('./images/hero.png', speed = 0)
        # 初始化飞机的位置
        self.rect.centerx = screen_rect.centerx
        self.rect.centery = screen_rect.height
        self.index = 0
        # 英雄子弹精灵组
        self.bullets = pygame.sprite.Group()
        self.bullets2 = pygame.sprite.Group()
    # 定义飞机活动边界
    def update(self):
        # 定义飞机的x轴边界
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= screen_rect.width - self.rect.width:
            self.rect.x = screen_rect.width - self.rect.width
        # 定义飞机的y轴边界
        if self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.y >= screen_rect.height - self.rect.height:
            self.rect.y = screen_rect.height - self.rect.height
    # 飞机开火
    def hero_fire(self):
        # 创建子弹对象
        bullet = Hero_bulletSprite(self.rect.centerx-3, self.rect.y)
        # 添加到精灵组对象中
        self.bullets.add(bullet)
    def hero_fire2(self):
        self.index += 1
        # # 创建子弹对象
        bullet2 = Hero_bullet2Sprite(0, self.rect.y)
        # bullet = Hero_bullet2Sprite(self.rect.centerx+50*math.sin(self.index), self.rect.y)
        # 添加到精灵组对象中
        self.bullets2.add(bullet2)


# 创建一个我方子弹精灵
class Hero_bulletSprite(GameSprite):
    def __init__(self, x, y):
        super().__init__('./images/zidan.png', speed = -28)
        self.rect.x = x
        self.rect.y = y
    # 发射子弹
    def update(self):
        super().update()
        # 边界判断
        if self.rect.y <= -self.rect.height:
            # 子弹从精灵组中删除
            self.kill()
    def __del__(self):
        self.destroy()
    def destroy(self):
        print("我方子弹销毁")

# 第二个我方大招精灵
class Hero_bullet2Sprite(GameSprite):
    def __init__(self, x, y):
        super().__init__('./images/dazhao.png', speed = -20)
        self.rect.x = x
        self.rect.y = y
    # 发射子弹
    def update(self):
        super().update()
        # 边界判断
        if self.rect.y <= -self.rect.height:
            # 子弹从精灵组中删除
            self.kill()
    def __del__(self):
        self.destroy()
    def destroy(self):
        print("我方子弹销毁")

# 定义敌方飞机
class EnemySprite(GameSprite):
    def __init__(self):
        # 初始化敌方飞机图片，速度
        super().__init__('./images/diji.png', speed = random.randint(4, 7))
        # 初始化敌方飞机的位置
        self.rect.x = random.randint(0, screen_rect.width - self.rect.width)
        self.rect.y = -self.rect.height
        # 敌方子弹精灵组
        self.bullets = pygame.sprite.Group()
    # 敌方飞机开火
    def enemy_fire(self):
        # 创建子弹对象
        bullet = Enemy_BulletSprite(self.rect.centerx , self.rect.y)
        # 添加到子弹精灵组对象中
        self.bullets.add(bullet)
    # def update(self):
    #     # 调运父类方法调用运动轨迹
    #     super().update()
    #     # 边界判断,超出边界就销毁
    #     if self.rect.y > screen_rect.height + self.rect.y:
    #         self.kill()
    # def __del__(self):
    #     print("敌方子弹对象已经销毁")

# 创建敌方子弹精灵对象
class Enemy_BulletSprite(GameSprite):
    def __init__(self, x, y):
        super().__init__('./images/34-1.png', speed = 20)
        self.rect.x = x
        self.rect.y = y
    # 敌方发射子弹
    def update(self):
        super().update()
        # 边界判断
        print("迷之边界",screen_rect.height + self.rect.y)
        if self.rect.y > screen_rect.height + 900 :  #self.rect.height + screen_rect.height:
            # 敌方子弹从精灵组中删除
            print("到达边界，敌方子弹销毁")
            self.kill()
    # def __del__(self):
    #     print("敌方子弹已销毁")
    # def __del__(self):
    #     self.destory()
    # def destory(self):
    #     for img_path in ["./images/enemy2_down1.png"," \
    #                       ./images/enemy2_down2.png"," \
    #                       ./images/enemy2_down3.png"," \
    #                       ./images/enemy2_down4.png"]:
    #         self.image = pygame.image.load(img_path)
    #         screen_rect.blit(self.image, [self.rect.centerx, self.rect.centery])
    #
##############################################################################3

# #计分板
# class Scoring(GameSprite):
#     def __init__(self, x, y):
#         self.
# 血量补给精灵
class HpSprite(GameSprite):
    def __init__(self, x, y):
        super().__init__('./images/50.png',speed = 0)
        self.rect.x = x
        self.rect.y = y
# class HpSprite2(GameSprite):
#     def __init__(self):
#         super().__init__('50.png', speed = 0)
#         self.rect.x = 130
#         self.rect.y = 30
# class HpSprite3(GameSprite):
#     def __init__(self):
#         super().__init__('50.png',speed = 0)
#         self.rect.x = 190
#         self.rect.y = 30
# 补给精灵
class SupplySprite(GameSprite):
    def __init__(self):
        super().__init__('./images/51.png', speed = 7)
        self.rect.x = random.randint(0, screen_rect.width)
        self.rect.y = -self.rect.height
    def update(self):
        self.rect.y += self.speed
# 大招补给精灵
class WarSprite(GameSprite):
    def __init__(self):
        super().__init__('./images/kongtou.png', speed = 7)
        self.rect.x = random.randint(0, screen_rect.width)
        self.rect.y = -self.rect.height
    def update(self):
        self.rect.y += self.speed





















