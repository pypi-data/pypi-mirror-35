#游戏引擎：控制游戏流程
import models,pygame,random,sys,traceback
from pygame.locals import *
# import os
# CMD = r'D:\ImageMagick-7.0.8-Q16-HDRI\convert.exe'   #ImageMagick安装目录下convert.exe所在目录
# SOURCE_PATH = r'E:\作业练习\游戏开发\bg'                          #png图片所在目录
#
# def doStrip(path):
#     data = {}
#     print(path)v
#     for root, dir
# s, files in os.walk(path):
#         for file in files:
#             name = file.lower()
#             if name.find('.png') != -1:
#                 path = os.path.join(root, file)
#                 os.system('"{0}" {1} -strip {1}'.format(CMD, path, path))
# doStrip(SOURCE_PA
# 添加背景音乐
# pygame.mixer.init()
# pygame.mixer.music.load("毛毛 - 奇迹再现.mp3")
# pygame.mixer.music.set_volume(0.5)  #设置音量



#对要用到的颜色进行宏定义
color_black = (0,0,0)
color_green = (0,255,0)
color_red = (255,0,0)
color_white = (255,255,255)
color_blue = (0,0,255)

class Game_Engine():
    def __init__(self):
        #引擎类型中，初始化服务对象

        #定义背景精灵
        self.bg1 = models.BackgroundSprite()
        self.bg2 = models.BackgroundSprite(next = True)
        #定义英雄飞机对象
        self.hero = models.HeroSprite()
        #定义英雄飞机对象总血量
        self.energy = self.hero.energy

        #定义补给一（子弹强化）对象
        self.supply1 = models.Supply1()
        #定义补给二（神圣护盾）对象
        self.supply2 = models.Supply2()
        #定义一个补给一（子弹强化）的精灵组对象
        self.supply_first = pygame.sprite.Group(self.supply1)
        #定义一个补给二（神圣护盾）的精灵组对象
        self.supply_sencond = pygame.sprite.Group(self.supply2)
        #定义一个敌机对象
        self.enemy = models.EnemySprite()

        #定义一个敌机boss对象
        self.enemy_boss = models.Enemy_Boss()

        #定义初始化精灵组对象
        self.resources = pygame.sprite.Group(self.bg1,self.bg2,self.hero)

        #再创建一个英雄飞机精灵组，，用来实现英雄飞机与敌方boss飞机之间的碰撞
        self.hero_boss = pygame.sprite.Group(self.hero)


        # 定义一个敌机的精灵组对象
        self.enemys = pygame.sprite.Group()

        #定义一个boss敌机的精灵组对象
        self.enemys_boss = pygame.sprite.Group()

        #定义一个敌机被摧毁的精灵组对象
        self.destroy_images =  pygame.sprite.Group()
        #同时创建一个字典用以保存被摧毁的敌机的数据
        self.destroy_images_dict = {}

    def start(self):
        # 初始化所有模块
        pygame.init()
        clock = pygame.time.Clock()
        #设定敌机出现的时间
        pygame.time.set_timer(models.ENEMY_CREATE,2000)
        #设定boss敌机出现的时间（在游戏进行一分钟时出现）
        pygame.time.set_timer(models.ENEMY_CREATE +1,20000)
        self.create_scene()
        #游戏场景循环
        while True:
            # pygame.mixer.music.play(-1)  # 循环播放
            #定义时钟刷新帧：每秒让循环运行多少次！
            clock.tick(24)
            self.update_scene() #创建游戏场景并渲染精灵组
            self.check_event() #监听所有的事件&获取当前用户在键盘上操作的按键
            self.check_collide() #碰撞检测
            self.blood_groove()  #对英雄飞机绘制血槽
            self.boss_blood_groove() #对敌方boss飞机绘制血槽
            self.create_enetgy_list()  #绘制能量表
    def blood_groove(self):
    #对英雄飞机生命值绘制血槽
        pygame.draw.line(self.screen, color_blue, (self.hero.rect.left, self.hero.rect.top - 5),
                        (self.hero.rect.right, self.hero.rect.top - 5), 15)
        energy_remain = self.hero.blood_volume / 30  # 英雄飞机当前血量除以英雄飞机总血量
        if energy_remain > 0.4:  # 如果血量大于百分之二十则为绿色，否则为红色
            energy_color = color_green
        else:
            energy_color = color_red
        pygame.draw.line(self.screen, energy_color,
        (self.hero.rect.left, self.hero.rect.top - 5),
        (self.hero.rect.left + self.hero.rect.width * energy_remain, self.hero.rect.top - 5),
        2)
        #更新血槽图片
        pygame.display.update()

    def boss_blood_groove(self):
        #对敌方boss飞机生命值绘制血槽
        pygame.draw.line(self.screen,color_blue,(self.enemy_boss.rect.left,self.enemy_boss.rect.top -5),
                         (self.enemy_boss.rect.right,self.enemy_boss.rect.top -5),15)
        energy_remain_boss = self.enemy_boss.boss_blood_volume / 200 #敌方boss飞机当前血量除以敌方boss飞机总血量
        if energy_remain_boss > 0.4:  #如果血量大于百分之四十则为绿色，否则为红色
            energy_color = color_green
        else:
            energy_color = color_red
        pygame.draw.line(self.screen,energy_color,(self.enemy_boss.rect.left,self.enemy_boss.rect.top -5),
                         (self.enemy_boss.rect.left + self.enemy_boss.rect.width * energy_remain_boss,self.enemy_boss.rect.top-5),2)
        #更新血槽图片
        pygame.display.update()

    def create_scene(self):
        #创建游戏场景
        self.screen = pygame.display.set_mode(models.SCREEN_SIZE)
        # 窗口名称的设置
        pygame.display.set_caption("塑料版飞机大战")

    def create_enetgy_list(self):
        # 使用系统字体
        self.fonts = pygame.font.SysFont("fangsong", 20, True)
        # 加粗
        self.fonts.set_bold(True)
        # 斜体
        self.fonts.set_italic(True)
        #创建一个能量表，用以积蓄能量
        self.screen.blit(self.fonts.render("当前能量：%s" % self.hero.energy, True, color_blue, color_red),[10,10])
        #刷新游戏场景
        pygame.display.update()

    def update_scene(self):
        #新增英雄飞机精灵组渲染
        self.hero_boss.update()
        self.hero_boss.draw(self.screen)

        #精灵组渲染
        self.resources.update()
        self.resources.draw(self.screen)

        #英雄子弹精灵组渲染
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)
        #英雄加强版子弹精灵组渲染
        self.hero.strengthen_bullets.update()
        self.hero.strengthen_bullets.draw(self.screen)

        #普通敌机子弹精灵组渲染
        self.enemy.destroy_bullets.update()
        self.enemy.destroy_bullets.draw(self.screen)
        #boss敌机子弹精灵组渲染
        self.enemy_boss.enemy_boss_bullets.update()
        self.enemy_boss.enemy_boss_bullets.draw(self.screen)

        #渲染敌机精灵组中的所有飞机
        self.enemys.update()
        self.enemys.draw(self.screen)

        #渲染boss敌机精灵组中的所有飞机
        self.enemys_boss.update()
        self.enemys_boss.draw(self.screen)

        #补给精灵组一渲染
        self.supply_first.update()
        self.supply_first.draw(self.screen)
        #补给精灵组二渲染
        self.supply_sencond.update()
        self.supply_sencond.draw(self.screen)

        # 更新游戏场景
        pygame.display.update()

    def check_collide(self):
        #碰撞检测
        #碰撞检测：子弹与敌方飞机之间的碰撞
        self.destroy_images_dict  =  pygame.sprite.groupcollide(self.hero.bullets,self.enemys,True,True)
        #将被毁灭的敌机添加到敌机被摧毁的精灵组中
        self.destroy_images.add(self.destroy_images_dict)
        for destroy_image in self.destroy_images:

            #调整帧率，实现慢速爆炸的效果
            clock = pygame.time.Clock()
            clock.tick(20)

            self.destroy(destroy_image)#将敌机返回到敌机被摧毁的精灵组中，调用函数
            print("爆炸>>>>>>>")
            self.destroy_images.remove(destroy_image)
        while len(self.destroy_images_dict) > 0:
            self.hero.energy += 5
            break

        #英雄加强版子弹与敌机之间的碰撞
        self.destroy_images_dict = pygame.sprite.groupcollide(self.hero.strengthen_bullets, self.enemys, True, True)
        # 将被毁灭的敌机添加到敌机被摧毁的精灵组中
        self.destroy_images.add(self.destroy_images_dict)
        for destroy_image in self.destroy_images:
            # 调整帧率，实现慢速爆炸的效果
            clock = pygame.time.Clock()
            clock.tick(20)

            self.destroy(destroy_image)  # 将敌机返回到敌机被摧毁的精灵组中，调用函数
            print("爆炸>>>>>>>")
            self.destroy_images.remove(destroy_image)
        while len(self.destroy_images_dict) > 0:
            self.hero.energy += 5
            break

        # 调整帧率，以实现英雄飞机与敌方boss碰撞时英雄飞机慢速减血的效果
        clock = pygame.time.Clock()

        #碰撞检测：英雄飞机子弹与敌方boss飞机之间的碰撞
        u = pygame.sprite.groupcollide(self.hero.bullets,self.enemys_boss,True,False)
        while len(u) > 0:

            clock.tick(24)

            self.enemy_boss.boss_blood_volume -= 1
            if self.enemy_boss.boss_blood_volume > 0: #判断敌方boss飞机血量
                print("敌方boss剩余血量" , self.enemy_boss.boss_blood_volume)
                break
            elif self.enemy_boss.boss_blood_volume == 0:
                self.enemy_boss.kill()
                pygame.quit()
                exit()

        #碰撞检测：英雄飞机与敌方boss飞机之间的碰撞
        e = pygame.sprite.groupcollide(self.hero_boss,self.enemys_boss,False,False)
        while len(e) > 0: #判断英雄飞机血量
            self.hero.blood_volume -= 1
            if self.hero.blood_volume > 0:  #判断英雄飞机血量
                print("剩余生命：", self.hero.blood_volume)
                break
            elif self.hero.blood_volume == 0:
                self.hero.kill()
                pygame.quit()
                exit()

        #碰撞检测： 英雄飞机与敌方boss子弹之间的碰撞
        b = pygame.sprite.spritecollide(self.hero,self.enemy_boss.enemy_boss_bullets,True)
        while len(b) > 0:
            self.hero.blood_volume -= 1
            if self.hero.blood_volume > 0:  #判断英雄飞机血量
                print("剩余生命：", self.hero.blood_volume)
                break
            elif self.hero.blood_volume == 0:
                # 判断英雄飞机血量
                self.hero.kill()
                pygame.quit()
                exit()
        #英雄飞机与补给物品一（子弹强化）之间的碰撞
        x = pygame.sprite.spritecollide(self.hero,self.supply_first,True)
        if len(x) > 0:
            self.hero.strengthen_fire()
        #英雄飞机与补给物品二（神圣护盾）之间的碰撞
        z = pygame.sprite.spritecollide(self.hero,self.supply_sencond,True)
        if len(z) > 0:
            pass#英雄飞机得到一个护盾，在六秒钟内达到无敌的效果

        #碰撞检测：英雄飞机和敌方飞机之间的碰撞
        e = pygame.sprite.spritecollide(self.hero,self.enemys,True)
        while len(e) >0:
            self.hero.blood_volume -= 1
            if self.hero.blood_volume > 0:  #判断英雄飞机血量
                print("剩余生命：",self.hero.blood_volume)
                break
            elif self.hero.blood_volume == 0:
                self.hero.kill()
                pygame.quit()
                exit()

        #碰撞检测：英雄飞机和敌机子弹之间的碰撞
        c = pygame.sprite.spritecollide(self.hero,self.enemy.destroy_bullets,True)
        while len(c) >0:
            self.hero.blood_volume -= 1
            if self.hero.blood_volume > 0:  #判断英雄飞机血量
                print("剩余生命：",self.hero.blood_volume)
                break
            elif self.hero.blood_volume == 0:
                self.hero.kill()
                pygame.quit()
                exit()

    def destroy(self,enemy):
        # 敌机被摧毁
        print("敌机销毁")
        # 添加飞机被摧毁的过程图
        for i in range(2,5):
            clock = pygame.time.Clock()
            clock.tick(35)
            destroy_image = pygame.image.load("./bg/destroy_images" + str(i) + ".png")
            self.screen.blit(destroy_image,enemy.rect)
            pygame.display.update()
            print(destroy_image)

    #让pygame完全控制鼠标
    sprite_speed = 300
    sprite_rotation = 0
    sprite_rotation_speed = 360


    def check_event(self):
        #监听所有的事件
        event_list = pygame.event.get()
        if len(event_list) > 0:
            print(event_list)
            for event in event_list:
                print(event.type,pygame.KEYDOWN,pygame.K_LEFT)
                #如果当前的事件，是QUIT事件
                if event.type == pygame.QUIT:
                    #卸载所有pygame资源 ，退出程序
                    pygame.quit()
                    exit()

                elif event.type == models.ENEMY_CREATE:
                    print("创建一架敌方飞机....")
                    self.enemy = models.EnemySprite()
                    #添加到敌方飞机精灵组中
                    self.enemys.add(self.enemy)
                elif event.type == models.ENEMY_CREATES:
                    print("创建一架敌方boss飞机....")
                    self.enemy_boss = models.Enemy_Boss()
                    #添加到敌方boss飞机精灵组中
                    self.enemys_boss.add(self.enemy_boss)


             #添加敌机子弹到敌机对象中
            self.enemy.destroy_fire()
        # # 自动发射子弹的实现
        # self.hero.fire()
        # print("发射子弹》》》", self.hero.bullets)

        # #使用鼠标来操控飞机
        # pos = pygame.mouse.get_pos()
        # self.hero.rect.x = pos[0] - self.he
        # self.hero.rect.y = pos[1] - self.he
        # pygame.mouse.set_visible(False)

        # pressed_keys = pygame.key.get_pressed()
        # #定位鼠标的x.y坐标&获取当前用户鼠标的操作
        # pressed_mouse = pygame.mouse.get_pressed()
        # #通过移动偏移量计算移动
        # rotation_direction = pygame.mouse.get_rel()[0] /2.0
        # if pressed_mouse[0]:
        #     print("向左移动<<<<<<<<<<<<")
        #     self.hero.rect.x -= 15
        # elif pressed_mouse[2]:
        #     print("向右移动>>>>>>>>>>>>")
        #     self.hero.rect.x += 15
        # elif pressed_mouse[1]:
        #     print("向上移动^^^^^^^^^^^")
        #     self.hero.rect.y -= 15
        # elif pressed_mouse[1]:
        #     print("向下移动vvvvvvvvvvv")
        #     self.hero.rect.y += 15

        #获取当前用户键盘上被操作的按键
        key_down = pygame.key.get_pressed()

        if key_down[pygame.K_LEFT]:
            print("向左移动<<<<<<<<<<<<")
            self.hero.rect.x -= 15
        elif key_down[pygame.K_RIGHT]:
            print("向右移动>>>>>>>>>>>>")
            self.hero.rect.x += 15
        elif key_down[pygame.K_UP]:
            print("向上移动^^^^^^^^^^^")
            self.hero.rect.y -= 15
        elif key_down[pygame.K_DOWN]:
            print("向下移动vvvvvvvvv")
            self.hero.rect.y += 15

        if key_down[pygame.K_SPACE]:
            self.hero.fire()
            print("发射子弹》》》", self.hero.bullets )
        if key_down[pygame.K_q]:
            self.hero.strengthen_fire()
            print("发射强化版子弹》》》", self.hero.strengthen_bullets)