
import pygame, models, random
# 游戏启动引擎
#加载音效
pygame.mixer.init()                 # 音乐初始化
pygame.font.init()                  # 字体初始化
pygame.mixer.music.load('./mp3/1.mp3')    # 游戏背景主题曲
pygame.mixer.music.play(-1, start = 2.0)         # 播放背景音乐
#pygame.mixer.music.load('kai_qiang.mp3')    # 游戏开枪
#pygame.mixer.music.play(0, start = 2)    # 游戏开枪

x = 70

class GameEngine:
    def __init__(self):

        # self.kaishi = models.StartgameSprite()
        # self.kaishi_s = pygame.sprite.Group(self.kaishi)

        self.bg1 = models.BackgroundSprite()       # 定义第一张背景图片
        self.bg2 = models.BackgroundSprite(next=True)  # 定义第二张背景图片
        self.hero = models.HeroSprite()  # 定义飞机对象
        self.hero_plane = pygame.sprite.Group(self.hero)  # 定义英雄飞机精灵组对象
        self.enemy_bullet = models.EnemySprite()  # 定义敌机子弹对象
        self.enemys = pygame.sprite.Group()  # 定义敌人飞机精灵组对象
        #敌机爆炸
        self.enemys_boom = pygame.sprite.Group()  # 爆炸敌机精灵组
        self.enemys_boom_dict = dict()

        self.score = 0        # 游戏初始化分数
        self.blood_flow = 3          # 初始化血量
        self.hp = models.HpSprite(x, 30)                # 定义血量对象
        self.hp2 = models.HpSprite(130, 30)                # 定义血量对象
        self.hp3 = models.HpSprite(190, 30)                # 定义血量对象
        self.hp_1 = [self.hp, self.hp2, self.hp3]
        self.hpsprite = pygame.sprite.Group(self.hp_1)
        # print("这是初始化",self.hp_1)
        self.buji = pygame.sprite.Group()   # 补给精灵组
        self.dazhao = pygame.sprite.Group()   # 大招精灵组
        self.bg = pygame.sprite.Group(self.bg1, self.bg2)        # 定义精灵组对象

    def start(self):       # 开始运行
        pygame.init()       # 初始化所有模块
        # pygame.mixer()      # 音乐模块
        self.clock = pygame.time.Clock()        # 定义一个时钟
        #self.screen = pygame.display.set_mode(models.screen_size)  # 创建游戏窗口
        pygame.time.set_timer(models.enemy_create, 1000)  # 间隔一定时间，触发一次 创建敌机 的事件
        self.create_scene()  # 创建游戏场景
        while True:
            self.clock.tick(60)
            # 标题渲染
            pygame.display.set_caption("--飞机大战--")      # 添加窗口标题
            pygame.display.set_icon(pygame.image.load("./images/top.jpg"))  # 读取、渲染窗口图片
            background_image = pygame.image.load("./images/bg_logo.jpg")    # 读取首页背景图
            self.screen.blit(background_image, (0, 0))             # 渲染首页背景图
            kaishi = pygame.image.load("./images/1.png")    # 读取首页开始游戏
            self.screen.blit(kaishi, (110, 444))             # 渲染首页开始游戏
            # tuichu = pygame.image.load("退出游戏.png")    # 读取首页退出游戏
            # self.screen.blit(tuichu, (140, 604))             # 渲染首页退出游戏
            self.my_font = pygame.font.SysFont('arial', 30)
            self.screen.blit(self.my_font.render(u'Python 1807 A', False, (255,165,0)), [340,40])
            self.my_font = pygame.font.SysFont('kaiti', 30)
            self.screen.blit(self.my_font.render(u'范豪言', False, (255,165,0)), [400,70])
            pygame.display.update()
            # 开始界面
            event_list = pygame.event.get()      # 获取
            for event in event_list:
                if event.type == pygame.MOUSEBUTTONUP and 110 < event.pos[0] < 400 and 444 < event.pos[1] < 616:
                    self.panduan()
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    exit()                # 并退出程序

    def panduan(self):
        while True:
            self.update_scene()    # 更新、渲染
            self.check_collide()   # 碰撞检测
            self.check_event()     # 监听事件
            self.check_keydown()   # 键盘操作

    def create_scene(self):  # 创建游戏场景
        self.screen = pygame.display.set_mode(models.screen_size) # screen_size = (512, 768)

    def update_scene(self):     # 更新游戏场景
        # 背景渲染
        self.bg.update()
        self.bg.draw(self.screen)
        # 计分板渲染
        self.my_font = pygame.font.SysFont('arial', 16)
        self.screen.blit(self.my_font.render(u'生命:%s'%self.blood_flow, False, (255,165,0)), [20,40])
        self.screen.blit(self.my_font.render(u'金币:%s'%self.score, False, (255,165,0)), [430,40])
        # 敌机渲染
        self.enemys.update()
        self.enemys.draw(self.screen)
        # 英雄飞机渲染
        self.hero_plane.update()
        self.hero_plane.draw(self.screen)
        # 英雄子弹精灵组渲染
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)
        # 英雄大招精灵组渲染
        self.hero.bullets2.update()
        self.hero.bullets2.draw(self.screen)
        # 敌方子弹精灵组渲染
        self.enemy_bullet.bullets.update()
        self.enemy_bullet.bullets.draw(self.screen)
        # 渲染血量精灵组
        self.hpsprite.update()
        self.hpsprite.draw(self.screen)
        # 渲染补给精灵组
        self.buji.update()
        self.buji.draw(self.screen)
        # 渲染大招补给精灵组
        self.dazhao.update()
        self.dazhao.draw(self.screen)
        # 屏幕更新
        pygame.display.update()

    def check_event(self):

        sj_buji = random.randint(0, 10000)      # 补给的随机事件
        if sj_buji > 9990:
            self.buji.add(models.SupplySprite())   # 把补给加入补给精灵组，渲染
        sj_dazhao = random.randint(0, 10000)    # 大招补给事件
        if sj_dazhao > 9990:
            self.dazhao.add(models.WarSprite())

        event_list = pygame.event.get()       # 监听所有的事件
        for event in event_list:
            # 如果当前事件是  QUIT  事件，卸载所有资源
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()                # 并退出程序
            elif event.type == pygame.KEYDOWN:
                #  D 键向 右 移动,  y轴 + 7
                if event.key == pygame.K_SPACE:
                    self.hero.hero_fire()

            # 触发自定义事件 ，创建战机
            elif event.type == models.enemy_create:
                # self.enemy_bullet = models.EnemySprite()   # 定义敌机对象
                self.enemys.add(self.enemy_bullet)        # 并添加到敌机精灵组中
                self.enemy_bullet.enemy_fire()  # 敌机发射子弹
                pygame.display.update()

    def boom(self, enemy):      # 飞机爆炸
        for i in range(3, 5):
            clock = pygame.time.Clock()
            clock.tick(50)
            image = pygame.image.load("enemy2_down" + str(i) + ".png")
            self.screen.blit(image, enemy.rect)
            pygame.display.update()

    def check_collide(self):  # 碰撞检测
        # 碰撞检测1：我方子弹和敌方飞机相撞
        self.score_dict = pygame.sprite.groupcollide(self.hero.bullets, self.enemys, True, True)
        self.score += len(self.score_dict) * 12
        self.enemys_boom.add(self.score_dict)  # 添加到爆炸精灵组
        for enemy_boom in self.enemys_boom:
            self.boom(enemy_boom)  # 将敌机返回到爆炸组，调用函数
            self.enemys_boom.remove(enemy_boom)

        # 碰撞检测1：我方大招和敌方飞机相撞
        self.score_dict = pygame.sprite.groupcollide(self.hero.bullets2, self.enemys, False, True)
        self.score += len(self.score_dict) * 12
        self.enemys_boom.add(self.score_dict)  # 添加到爆炸精灵组
        for enemy_boom in self.enemys_boom:
            self.boom(enemy_boom)  # 将敌机返回到爆炸组，调用函数
            self.enemys_boom.remove(enemy_boom)

        # 碰撞检测2：我方飞机和敌方飞机相撞
        e1 = pygame.sprite.groupcollide(self.hero_plane, self.enemys, False, True)
        if len(e1):       # 飞机之间碰撞，游戏结束
            if self.blood_flow > 0:
                self.blood_flow -= 1  # 血量-1
                # print("此处减少血量",self.blood_flow)
                self.hp_1[self.blood_flow].kill()
                # print("这是飞机之间的碰撞",self.hp_1)
            if self.blood_flow == 0:
                self.hero.kill()    # 销毁英雄飞机
                pygame.quit()      # 卸载 pygame 资源
                exit()            # 退出游戏

        # 碰撞检测3：我方飞机和敌方子弹相撞
        e2 = pygame.sprite.groupcollide(self.enemy_bullet.bullets, self.hero_plane, True, False)
        if len(e2):
            if self.blood_flow > 0:
                self.blood_flow -= 1  # 血量-1
                print("此处减少血量", self.blood_flow)
                self.hp_1[self.blood_flow].kill()
                print("敌方子弹和我方飞机之间的碰撞", self.hp_1)
            elif self.blood_flow == 0:
                event_list = pygame.event.get()
                for event in event_list:
                    if event.type == pygame.MOUSEBUTTONUP:
                        self.my_font = pygame.font.SysFont('kaiti', 30)
                        self.screen.blit(self.my_font.render(u'重新开始游戏', False, (255, 165, 0)), [256, 384])
                        pygame.display.update()
                        self.panduan()
                    # 如果当前事件是  QUIT  事件，卸载所有资源
                    elif event.type == pygame.QUIT:
                        self.hero.kill()    # 销毁英雄飞机
                        pygame.quit()
                        exit()                # 并退出程序

        # 碰撞检测四：加血补给碰撞
        e3 = pygame.sprite.groupcollide(self.hero_plane, self.buji, False, True)
        if len(e3):
            if self.blood_flow >3:
                self.blood_flow = 3
            elif 1 <= self.blood_flow <= 2 :
                self.hpsprite.add(self.hp_1[self.blood_flow])
                self.blood_flow += 1

        # 碰撞检测四：大招补给碰撞
        e4 = pygame.sprite.groupcollide(self.hero_plane, self.dazhao, False, True)
        if len(e4):
            self.hero.hero_fire2()  # 发射大招


    # 控制飞机移动
    def check_keydown(self):  # 监听键盘操作
        # 获取当前用户键盘上被操作的按键
        key_down = pygame.key.get_pressed()
        #  W 键向 上 移动,  y轴 - 7
        if key_down[pygame.K_w]:
            self.hero.rect.y -= 10
        #  S 键向 下 移动,  y轴 + 7
        elif key_down[pygame.K_s]:
            self.hero.rect.y += 10

        #  A 键向 左 移动,  x轴 - 7
        elif key_down[pygame.K_a]:
            self.hero.rect.x -= 10

        #  D 键向 右 移动,  y轴 + 7
        elif key_down[pygame.K_d]:
            self.hero.rect.x += 10

        #  A 键向 左上 移动,  x轴 - 7
        if key_down[pygame.K_a] and key_down[pygame.K_w]:
            self.hero.rect.x -= 7
            self.hero.rect.y -= 7

        #  A 键向 右上 移动,  x轴 - 7
        if key_down[pygame.K_w] and key_down[pygame.K_d]:
            self.hero.rect.x += 7
            self.hero.rect.y -= 7

        #  A 键向 右下 移动,  x轴 - 7
        if key_down[pygame.K_s] and key_down[pygame.K_d]:
            self.hero.rect.x += 7
            self.hero.rect.y += 7

        #  A 键向 左上 移动,  x轴 - 7
        if key_down[pygame.K_s] and key_down[pygame.K_a]:
            self.hero.rect.x -= 7
            self.hero.rect.y += 7

