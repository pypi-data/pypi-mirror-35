'''
游戏引擎：控制游戏运行流程
'''
import pygame, game_sprites,time,random

#音乐加载
pygame.mixer.init()
sound1 = pygame.mixer.Sound('./music/bullet~1.wav')    #读取wav, agg
sound2 = pygame.mixer.Sound('./music/enemy1_down.wav')
pygame.mixer.music.load('./music/kmj.mp3')     #读取mp3


class GameEngine:

    def __init__(self):
        '''初始化函数：控制界面初始化操作'''
        # # 首页？、
        # self.shou_ye()
        # 定义背景精灵
        self.bg1 = game_sprites.BackgroundSprite("./images/b1.jpg")
        self.bg2 = game_sprites.BackgroundSprite("./images/b1.jpg", next=True)
        self.bg3 = game_sprites.BackgroundSprite("./images/b2.jpg")
        self.bg4 = game_sprites.BackgroundSprite("./images/b2.jpg", next=True)
        # 定义英雄飞机对象
        self.hero = game_sprites.HeroSprite()
        # 定义敌机对象
        self.enemy = game_sprites.EnemySprite("./images/a3.png")
        # 定义补给对象
        self.supply = game_sprites.Supply()
        self.blood = game_sprites.Blood()
        # 定义血量对象
        self.blood1 = game_sprites.Blood1()
        self.blood2 = game_sprites.Blood2()
        self.blood3 = game_sprites.Blood3()
        # 定义大招对象
        self.dz = game_sprites.Dazhao()

        # 定义精灵组对象
        self.resources = pygame.sprite.Group(self.bg1, self.bg2, self.hero,self.blood1, self.blood2,self.blood3)
        self.resources1 = pygame.sprite.Group(self.bg3, self.bg4, self.hero,self.blood1, self.blood2,self.blood3)
        # 定义敌机的精灵组对象
        self.enemys = pygame.sprite.Group()
        # 爆炸敌机精灵组
        self.enemys_boom = pygame.sprite.Group()
        self.enemys_boom_dict = dict()
        # 定义补给的精灵组对象
        self.supplys = pygame.sprite.Group()
        self.bloods = pygame.sprite.Group()

    # def shou_ye(self):
    #     # 初始化所有模块
    #     pygame.init()
    #     self.create_scene()
    #     while True:
    #         st_img = pygame.image.load("./images/shouye.jpg")
    #         self.screen.blit(st_img, (0, 0))
    #         pygame.display.update()
    #         event_list = pygame.event.get()
    #         for event in event_list:
    #             if event.type == pygame.QUIT:
    #                 # 卸载所有模块
    #                 pygame.quit()
    #                 # 退出
    #                 exit()
    #             if event.type == pygame.MOUSEBUTTONUP:
    #                 self.start()

    def start(self):
        pygame.init()
        # pygame.mixer.music.play(-1)
        clock = pygame.time.Clock()
        pygame.time.set_timer(game_sprites.ENEMY_CREATE, 1000)
        self.create_scene()
        while True:
            # 定义始终刷新帧：每秒让循环运行多少次！
            clock.tick(60)
            if game_sprites.SOURCE <= 50:
                self.update_scene()
                self.check_collide()
                self.check_event()
                self.keydown()
                self.background1()
                self.update_scene()
                pygame.display.update()
            elif 50 < game_sprites.SOURCE:
                self.update_scene()
                self.check_collide()
                self.check_event()
                self.keydown()
                self.background2()
                self.update_scene()
                pygame.display.update()


    def create_scene(self):
        '''创建游戏场景函数'''
        self.screen = pygame.display.set_mode(game_sprites.SCREEN_SIZE)

    def background1(self):
        self.resources.update()
        self.resources.draw(self.screen)

    def background2(self):
        self.resources1.update()
        self.resources1.draw(self.screen)

    def update_scene(self):
        '''更新游戏场景函数'''
        # 渲染标题
        pygame.display.set_caption("何书记教你打飞机")
        iconImage = pygame.image.load("images/iconimage.jpg")
        pygame.display.set_icon(iconImage)
        # 对每架敌机的子弹进行渲染
        for e in self.enemys:
            # print("-----------", e)
            e.bullets.update()
            e.bullets.draw(self.screen)

        # 子弹精灵组渲染
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

        # 渲染敌机精灵组中的飞机
        self.enemys.update()
        self.enemys.draw(self.screen)
        # 显示分数
        self.source()
        # 渲染补给
        self.supplys.update()
        self.supplys.draw(self.screen)
        self.bloods.update()
        self.bloods.draw(self.screen)
        # 渲染大招
        self.dz.dzs.update()
        self.dz.dzs.draw(self.screen)
        # 定义一个血量列表
        self.bloodlist = [self.blood1, self.blood2, self.blood3]

        # 屏幕更新
        pygame.display.update()

    def source(self):
        source = str(game_sprites.SOURCE)
        my_font = pygame.font.SysFont('arial', 20)
        my_surf = my_font.render("sorce:" + source, True, (255, 255, 255))
        font_rect = my_surf.get_rect()
        font_rect.midtop = (460, 10)
        self.screen.blit(my_surf, font_rect)
        pygame.display.flip()
    # 游戏结束
    def GameOver(self):
        '''游戏结束画面'''
        self.screen.fill([115, 0, 0])
        my_font = pygame.font.SysFont('arial', 50)
        my_surf = my_font.render("Game Over!", True, (0, 255, 0))
        font_rect = my_surf.get_rect()
        font_rect.midtop = (270, 300)
        self.screen.blit(my_surf, font_rect)
        pygame.display.flip()

    def check_collide(self):
        '''碰撞检测函数'''

        # 碰撞检测：己方子弹和敌方飞机发生碰撞
        self.enemys_boom_dict = pygame.sprite.groupcollide(self.hero.bullets, self.enemys, True, True)
        if self.enemys_boom_dict:
            sound2.play()
            game_sprites.SOURCE += 1
        # 添加到爆炸精灵组
        self.enemys_boom.add(self.enemys_boom_dict)
        for enemy_boom in self.enemys_boom:
            # 将敌机返回到爆炸组，调用函数
            self.boom(enemy_boom)
            self.enemys_boom.remove(enemy_boom)
        # 碰撞检测：大招和对方飞机发生碰撞
        self.enemys_boom_dict = pygame.sprite.groupcollide(self.dz.dzs, self.enemys, False, True)
        if self.enemys_boom_dict:
            sound2.play()
            game_sprites.SOURCE += 1
        self.enemys_boom.add(self.enemys_boom_dict)
        for enemy_boom in self.enemys_boom:
            # 将敌机返回到爆炸组，调用函数
            self.boom(enemy_boom)
            self.enemys_boom.remove(enemy_boom)
        # 碰撞检测：己方飞机和敌方子弹发生碰撞
        e  = pygame.sprite.spritecollide(self.hero, self.enemy.bullets, True)
        if len(e)>0:
            game_sprites.a -= 1
            self.bloodlist[game_sprites.a].kill()
            if game_sprites.a <= 0:
                self.GameOver()
                time.sleep(2)
                self.hero.kill()
                pygame.quit()
                exit()
        # 碰撞检测：飞机和补给发生碰撞
        b = pygame.sprite.spritecollide(self.hero, self.supplys, True)
        if len(b) > 0:
            self.dz.fire("./images/z2.png")
            self.enemy.kill()
        b1 = pygame.sprite.spritecollide(self.hero, self.bloods, True)
        if len(b1) > 0:
            if game_sprites.a >= 3:
                game_sprites.a = 3
            elif game_sprites.SOURCE <= 50:
                self.resources.add(self.bloodlist[game_sprites.a])
                game_sprites.a += 1
            elif game_sprites.SOURCE > 50:
                self.resources1.add(self.bloodlist[game_sprites.a])
                game_sprites.a += 1
        # 碰撞检测：飞机之间的碰撞
        if pygame.sprite.spritecollide(self.hero, self.enemys, True):
            game_sprites.a -= 1
            self.bloodlist[game_sprites.a].kill()
            if game_sprites.a <= 0:
                self.GameOver()
                time.sleep(2)
                self.hero.kill()
                pygame.quit()
                exit()
    def check_event(self):
        '''事件监听函数'''
        event_list = pygame.event.get()
        c = random.randint(1, 1000)
        if len(event_list) > 0:
            # print(event_list)
            for event in event_list:
                # print(event.type, pygame.KEYDOWN, pygame.K_LEFT)
                # 如果当前的时间：是QUIT事件
                if event.type == pygame.QUIT:
                    # 卸载所有pygame资源，退出程序
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        sound1.play()
                        self.hero.fire("./images/z1.png")

                elif c > 980:
                    self.supply = game_sprites.Supply()
                    self.supplys.add(self.supply)
                elif c < 10:
                    self.blood = game_sprites.Blood()
                    self.bloods.add(self.blood)


                if event.type == game_sprites.ENEMY_CREATE:
                    # print("创建一架敌机.....")
                    if c <= 390:
                        self.enemy = game_sprites.EnemySprite("./images/a4.png")
                    elif 390 < c < 690:
                        self.enemy = game_sprites.EnemySprite("./images/a3.png")
                    elif c >= 690:
                        self.enemy = game_sprites.EnemySprite("./images/a1.png")
                    # 添加到敌机精灵组中
                    self.enemys.add(self.enemy)

            self.enemy.fire()
                    # print("敌机发射了子弹")

    def boom(self, enemy):
        '''爆炸'''
        for i in range(1,5):
            clock = pygame.time.Clock()
            clock.tick(80)
            image = pygame.image.load("./images/enemy2_down" + str(i) + ".png")
            self.screen.blit(image, enemy.rect)
            pygame.display.update()
            # print(image)

    def keydown(self):
        # 获取当前用户键盘上被操作的按键
        key_down = pygame.key.get_pressed()

        if key_down[pygame.K_LEFT]:
            # print("向左移动<<<<<<<<<<<<")
            self.hero.rect.x -= 20
        if key_down[pygame.K_RIGHT]:
            # print("向右移动>>>>>>>>>>>>")
            self.hero.rect.x += 20
        if key_down[pygame.K_UP]:
            # print("向上移动^^^^^^^^^^^")
            self.hero.rect.y -= 20
        if key_down[pygame.K_DOWN]:
            # print("向下移动vvvvvvvvv")
            self.hero.rect.y += 20
        if key_down[pygame.K_1]:
            # self.hero.fire1()
            sound1.play()
            self.hero.fire("./images/z1.png")
