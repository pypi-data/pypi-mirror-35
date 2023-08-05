#所有游戏精灵类型存放的文件

import pygame,random,traceback
from pygame.locals import *

# #定义需要的常量
SCREEN_SIZE = (512,768)
SCREEN_RECT = pygame.Rect(0,0,*SCREEN_SIZE) #定义游戏场景的大小

# #自定义一个事件
ENEMY_CREATE = pygame.USEREVENT

#自定义一个事件，用来定义敌方boss的出现时间
ENEMY_CREATES = pygame.USEREVENT +1

#时间声明
clock = pygame.time.Clock()


class GameSprite(pygame.sprite.Sprite):
    #游戏精灵对象：用于表示游戏中的各种元素
    def __init__(self,image_path,speed = 1):
        #调用父类初始化数据
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        #默认运动更新方法
        self.rect.y += self.speed

class BackgroundSprite(GameSprite):
    def __init__(self,next = False):
        super().__init__("./bg/img_bg_level_2.jpg",speed = 5)
        if next:
            self.rect.y = - SCREEN_SIZE[1]
    def update(self):
        #调用父类的方法，执行运动
        super().update()
        #子类中判断边界
        if self.rect.y > SCREEN_SIZE[1]:
            self.rect.y = -SCREEN_SIZE[1]
class HeroSprite(GameSprite):
    #英雄飞机精灵对象
    #添加energy成员变量用来表示英雄飞机血量
    # energy = 5
    def __init__(self):
        #初始化英雄飞机的图片、速度
        super().__init__("./bg/hero.png",speed = 0)
        #初始化英雄飞机的位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.y = SCREEN_RECT.centery + 200
        #定义并初始化英雄飞机的血量
        self.blood_volume = 30
        #定义初始化定义英雄飞机的能量
        self.energy = 0
        #创建一个英雄飞机子弹精灵组
        self.bullets = pygame.sprite.Group()

        #创建一个英雄飞机加强版子弹精灵组
        self.strengthen_bullets = pygame.sprite.Group()

    def update(self):
        #水平边界判断
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= SCREEN_RECT.width - self.rect.width:
            self.rect.x = SCREEN_RECT.width - self.rect.width
        #垂直边界判断
        if self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.y >= SCREEN_RECT.height - self.rect.height:
            self.rect.y = SCREEN_RECT.height - self.rect.height

    def fire(self):
        #飞机攻击 &创建一个子弹对象
        bullet = BulletSprite(self.rect.centerx-63,self.rect.y)
        # 添加到精灵组对象
        self.bullets.add(bullet)
    def strengthen_fire(self):
        #飞机攻击  &创建一个加强版子弹对象
        reinforced_bullet = Reinforced_Bullet(self.rect.centerx-10,self.rect.y)
        #将加强版英雄子弹添加到加强版子弹精灵组对象
        self.strengthen_bullets.add(reinforced_bullet)

class BulletSprite(GameSprite):

    #子弹精灵
    def __init__(self,x,y):
        super().__init__("./bg/pic2.png",speed = -8)
        self.rect.x = x
        self.rect.y = y
        #self.speed = speed
    def update(self):
        #调用父类的方法进行操作
        super().update()
        #边界判断
        if self.rect.y <= -self.rect.height:
            #子弹从精灵组中删除
            self.kill()
    def __del__(self):
        print("子弹对象已经销毁")


class Reinforced_Bullet(GameSprite):
    #英雄加强版子弹精灵
    def __init__(self,x,y):
        super().__init__("./bg/bullet1.png",speed = -16)
        self.rect.x = x-180
        self.rect.y = y
    def update(self):
        #调用分类的方法进行操作
        super().update()
        #边界判断
        if self.rect.y <= -self.rect.height:
            #子弹从精灵组中删除
            self.kill()
    def __del__(self):
        print("加强版子弹已经销毁")


class Destroy_Bullet_Sprite(GameSprite):
    #普通敌机子弹精灵
    def __init__(self,x,y):
        super().__init__("./bg/destroy_bullets.png", speed = 16)
        self.rect.x = x
        self.rect.y = y
    def update(self):
        #调用父类的方法进行操作
        super().update()
        #边界判断
        if self.rect.y <= -SCREEN_RECT.height:
            #子弹从精灵组中删除
            self.kill()
    def __del__(self):
        print("敌机子弹已销毁")

class Destroy_Boss_Bullet(GameSprite):
    #boss敌机子弹精灵
    def __init__(self,x,y):
        super().__init__("./bg/destroy_bullets.png", speed = 14)
        self.rect.x = x
        self.rect.y = y
    def update(self):
        #调用父类的方法进行操作
        super().update()
        #边界判断
        if self.rect.y <= -SCREEN_RECT.height:
            #子弹从精灵组中删除
            self.kill()
    def __del__(self):
        print("敌机子弹已销毁")

class EnemySprite(GameSprite):
    #敌方飞机
    def __init__(self):
        #初始化敌方飞机的数据：图片，速度
        super().__init__("./bg/png1.png",speed = random.randint(3,5))
        #初始化敌方飞机的位置
        self.rect.x = random.randint(0,SCREEN_RECT.width - self.rect.width)
        self.rect.y = -self.rect.height
        #创建一个敌方飞机子弹精灵组
        self.destroy_bullets = pygame.sprite.Group()

    def destroy_fire(self):
        #敌机进行攻击 & 创建一个子弹对象
        destroy_bullet = Destroy_Bullet_Sprite(self.rect.centerx -31,self.rect.y)
        #添加到敌机子弹精灵组对象
        self.destroy_bullets.add(destroy_bullet)

    def update(self):
        #调用父类的方法直接运动
        super().update()
        #边界判断
        if self.rect.y > SCREEN_RECT.height:
            #飞机一旦超出屏幕，销毁！
            self.kill()

class Enemy_Boss(GameSprite):
    #敌方boss飞机
    def __init__(self):
        #初始化敌方boss飞机的数据： 图片，速度
        super().__init__("./bg/boss.png",speed = 5)

        #初始化敌方boss飞机的位置
        self.rect.x = random.randint(0,SCREEN_RECT.width - self.rect.width)
        self.rect.y =  - self.rect.height


        # 定义并初始化敌方boss飞机的血量
        self.boss_blood_volume = 200

        #创建一个敌方boss飞机子弹精灵组
        self.enemy_boss_bullets = pygame.sprite.Group()
    def destroy_boss_fire(self):
        #敌方boss进行攻击 & 创建一个boss子弹对象
        destroy_boss_bullets = Destroy_Boss_Bullet(self.rect.centerx -31,self.rect.y)
        #添加到敌机boss子弹精灵组对象
        self.enemy_boss_bullets.add(destroy_boss_bullets)

    def update(self):
        #重写父类方法进行运动
        super().update()
        #边界判断
        self.rect.x -= self.speed
        if self.rect.x <= 0:
            self.rect.x = 0

        elif self.rect.x >= SCREEN_RECT.width - self.rect.width:
            self.rect.x = SCREEN_RECT.width - self.rect.width

        if self.rect.y <= 0:
            self.rect.y = 0
            self.speed = -self.speed
        elif self.rect.y >= SCREEN_RECT.centery - self.rect.height:
            self.rect.y = SCREEN_RECT.centery - self.rect.height


class Supply1(GameSprite):
    def __init__(self):
        #初始化补给物品一（子弹加强）的数据：：图片，速度
        super().__init__("./bg/purple.png" ,speed = random.randint(2,5))
        #初始化补给物品一（子弹加强）的落下位置
        self.rect.x = random.randint(0,SCREEN_RECT.width - self.rect.width)
        self.rect.y = -self.rect.height

    def update(self):
        #调用父类的方法直接运动
        super().update()
        #边界判断
        if self.rect.y > SCREEN_RECT.height:
            #补给一旦超出屏幕，错过也就错过了，所谓爱情，不过如此！
            self.kill()
class Supply2(GameSprite):
    def __init__(self):
        #初始化补给物品二(神圣护盾)的数据，：图片，速度
        super().__init__("./bg/shield_blue.png" , speed = random.randint(2,5))
        #初始化补给物品二（神圣护盾）的落下位置
        self.rect.x = random.randint(0,SCREEN_RECT.width - self.rect.width)
        self.rect.y = -self.rect.height
    def update(self):
        #调用分类的方法直接运动
        super().update()
        #边界判断
        if self.rect.y > SCREEN_RECT.height:
            #补给一旦超出屏幕，错过也就错过了，所谓爱情，不过如此！
            self.kill()




