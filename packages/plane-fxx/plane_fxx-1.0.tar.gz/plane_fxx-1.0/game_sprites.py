'''
游戏需要的精灵和精灵组类型
'''
import pygame, random, math

# 定义需要的常量
SCREEN_SIZE = (512, 768)
SCREEN_RECT = pygame.Rect(0, 0, *SCREEN_SIZE)
# 自定义一个事件
ENEMY_CREATE = pygame.USEREVENT
ENEMY_CREATE1 = pygame.USEREVENT + 1
a = 3
SOURCE = 0


class GameSprite(pygame.sprite.Sprite):
    '''创建游戏精灵对象：用于表示游戏中的各种元素'''

    def __init__(self, image_path, speed=8):
        # 调用父类初始化数据
        super().__init__()

        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        '''默认运动更新方法'''
        self.rect.y += self.speed


class BackgroundSprite(GameSprite):

    def __init__(self, image_path, next=False):
        super().__init__(image_path)

        if next:
            self.rect.y = -SCREEN_SIZE[1]

    def update(self):
        # 调用父类方法，执行运动
        super().update()
        # 子类中判断边界
        if self.rect.y > SCREEN_SIZE[1]:
            self.rect.y = -SCREEN_SIZE[1]


class HeroSprite(GameSprite):
    '''英雄精灵对象'''

    def __init__(self):
        # 初始化英雄飞机的图片、速度
        super().__init__("./images/h3.png", speed=0)
        # 初始化英雄飞机的位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.y = SCREEN_RECT.centery + 200
        self.index = 0
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
        elif self.rect.y >= SCREEN_RECT.height - self.rect.height:
            self.rect.y = SCREEN_RECT.height - self.rect.height

    def fire(self,image_path):
        '''飞机攻击'''
        self.index+=1
        # 创建一个子弹对象
        bullet = BulletSprite(image_path, self.rect.centerx+40*math.cos(self.index), self.rect.y)
        # 添加到精灵组对象
        self.bullets.add(bullet)



class BulletSprite(GameSprite):
    '''子弹精灵'''
    def __init__(self,image_path ,x, y):
        super().__init__(image_path, speed=-15)
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

class BulletSprite3(GameSprite):
    '''子弹精灵'''

    def __init__(self, x, y,speed=5):
        super().__init__("./images/z1.png")
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def update(self):
        # 调用父类的方法进行操作
        super().update()
        # 边界判断
        if self.rect.y > SCREEN_RECT.height + self.rect.height:
            # 销毁子弹
            self.kill()

    def __del__(self):
        print("敌机子弹已经销毁")


class EnemySprite(GameSprite):

    def __init__(self,image_path):
        # 初始化敌机的数据：图片，速度
        super().__init__(image_path, speed=random.randint(2, 4))

        # 初始化敌方飞机的位置
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)
        self.rect.y = -SCREEN_RECT.height
        self.bullets = pygame.sprite.Group()

    def update(self):
        # 调用父类的方法直接运动
        super().update()
        # 边界判断
        if self.rect.y > SCREEN_RECT.height:
            # 飞机一旦超出屏幕，立刻销毁！
            self.kill()

    def fire(self):
        '''飞机攻击'''

        # 创建一个子弹对象
        bullet3 = BulletSprite3(self.rect.centerx - 10, self.rect.y)
        # 添加到精灵组对象
        self.bullets.add(bullet3)

    def __del__(self):
        self.destroy()

    def destroy(self):
        print("敌机销毁")

class Supply(GameSprite):
    '''随机掉落的补给类型'''
    def __init__(self):
        # 初始化补给的数据：图片、速度
        super().__init__("./images/supply1.png", speed=random.randint(2, 4))
        # 初始化补给出现的位置
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)
        self.rect.y = -SCREEN_RECT.height
        self.index = 0

    def update(self):
        # 调用父类的方法直接运动
        super().update()
        # 边界判断
        if self.rect.y > SCREEN_RECT.height:
            # 飞机一旦超出屏幕，立刻销毁！
            self.kill()

    def Move(self):
        '''补给的移动轨迹'''
        self.index += 0.05
        self.rect = self.rect.move(0 + 10 * math.sin(self.index), self.speed)
        if self.rect.x > 480 - 60:
            self.rect.x = 0 - 10 * math.sin(self.index)
        # self.screen.blit(self.image, self.rect)

    def __del__(self):
        self.destroy()

    def destroy(self):
        print("补给销毁")

class Blood(GameSprite):
    '''随机掉落的补给类型'''

    def __init__(self):
        # 初始化补给的数据：图片、速度
        super().__init__("./images/blood1.png", speed=random.randint(2, 4))
        # 初始化补给出现的位置
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)
        self.rect.y = -SCREEN_RECT.height
        self.index = 0

    def update(self):
        # 调用父类的方法直接运动
        super().update()
        # 边界判断
        if self.rect.y > SCREEN_RECT.height:
            # 补给一旦超出屏幕，立刻销毁！
            self.kill()

    def Move(self):
        '''补给的移动轨迹'''
        self.index += 1
        self.rect = self.rect.move(0 + 10 * math.sin(self.index), self.speed)
        if self.rect.x > 480 - 60:
            self.rect.x = 0 - 10 * math.sin(self.index)


    def __del__(self):
        self.destroy()

    def destroy(self):
        print("补给销毁")

class Blood1(GameSprite):
    def __init__(self):
        super().__init__("./images/blood.png",speed = 0)
        self.rect.x = SCREEN_RECT.x+10
        self.rect.y = SCREEN_RECT.y+10

class Blood2(GameSprite):
    def __init__(self):
        super().__init__("./images/blood.png", speed = 0)
        self.rect.x = SCREEN_RECT.x+50
        self.rect.y = SCREEN_RECT.y+10

class Blood3(GameSprite):
    def __init__(self):
        super().__init__("./images/blood.png", speed = 0)
        self.rect.x = SCREEN_RECT.x+90
        self.rect.y = SCREEN_RECT.y+10

class Dazhao(GameSprite):
    '''大招'''
    def __init__(self):
        super().__init__("./images/z2.png", speed = -5)
        self.rect.x = SCREEN_RECT.centerx - 250
        self.rect.y = SCREEN_RECT.height
        # 定义大招精灵组
        self.dzs = pygame.sprite.Group()

    def update(self):
        # 调用父类的方法直接运动
        super().update()
        # 边界判断
        if self.rect.y < -SCREEN_RECT.height:
            # 补给一旦超出屏幕，立刻销毁！
            self.kill()
    def fire(self,image_path):
        '''大招攻击'''
        # 创建一个子弹对象
        bullet = BulletSprite(image_path, self.rect.x, self.rect.y)
        # 添加到精灵组对象
        self.dzs.add(bullet)

    def __del__(self):
        self.destroy()

    def destroy(self):
        print("大招销毁")