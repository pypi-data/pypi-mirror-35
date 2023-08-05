"""
存放所有游戏精灵的文件
"""
#引入模块
import pygame, random, math

pygame.mixer.init()

#设定一个常量表示窗口大小
SCREEN_SIZE = (512, 768)

#将窗口设置一个RECT对象
SCREEN_RECT =pygame.Rect(0, 0, *SCREEN_SIZE)

#创建一个游戏窗口
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

#修改窗口游戏名称
pygame.display.set_caption("武俊超的飞机大战")

#创建一个自定义事件
CREATE_ENEMY = pygame.USEREVENT
#创建第二个自定义事件
CREATE_ENEMY2 = pygame.USEREVENT+1
#创建第三个自定义事件
CREATE_BULLET = pygame.USEREVENT+1
#创建第四个自定义事件
CREATE_LB = pygame.USEREVENT+1
#定义一个时钟频率：
clock = pygame.time.Clock()
# 用于计算英雄飞机的得分
hero_score = 0
#boss的血量
boss_score = 100
#定义英雄的生命：
life = 3
#定义一个游戏类型
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image_path, speed=1):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed

#定义一个背景类型
class BackgroundSprite(GameSprite):
    def __init__(self, image_path, speed, next = False):
        super().__init__(image_path)
        self.speed = speed
        if next:
            self.rect.y = -SCREEN_SIZE[1]

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_SIZE[1]:
            self.rect.y = -SCREEN_SIZE[1]

#定义一个英雄类型：
class HeroSprite(GameSprite):
    def __init__(self):
        super().__init__("./images/hero.png", speed=0)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.centery = SCREEN_RECT.centery+200
        self.bullets = pygame.sprite.Group()
        self.flag = 20
        self.attack = 0
        self.rock = 0

    def update(self):
        #英雄边界处理，先处理横向边界
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x >= SCREEN_RECT.width - self.rect.width:
            self.rect.x = SCREEN_RECT.width - self.rect.width

        #英雄边界纵向限制
        if self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.y >= SCREEN_RECT.height - self.rect.height:
            self.rect.y = SCREEN_RECT.height - self.rect.height

    #定义英雄的开火方法
    def fire1(self):
        self.attack += 2
        if self.attack == self.flag:
            self.rock += 0.4
            bullet1 = BulletSprite("./images/bullet1.png", self.rect.centerx-38, self.rect.y, speed=-6)
            bullet1.xspeed = 2
            bullet2 = BulletSprite("./images/bullet1.png", self.rect.centerx - 38, self.rect.y, speed=-6)
            bullet3 = BulletSprite("./images/bullet1.png", self.rect.centerx - 38, self.rect.y, speed=-6)
            bullet3.xspeed = -2
            self.bullets.add(bullet1, bullet2, bullet3)
            gun.play()
            self.attack = 0

    def fire2(self):
        self.rock += 0.4
        bullet = BulletSprite("./images/bullet1.png", (self.rect.centerx-38)+(20*math.sin(self.rock)), self.rect.y, speed=-6)
        self.bullets.add(bullet)
        gun.play()



    #定义英雄的大招
    def da(self):
        dz1 = BulletSprite("./images/da.png", self.rect.centerx-170, self.rect.y, speed=-5)
        dz3 = BulletSprite("./images/da.png", self.rect.centerx-20, self.rect.y, speed=-5)
        self.bullets.add(dz1, dz3)
        gun.play()

    # #定义英雄的保护罩
    # def safe(self):
    #     safe1 = SafeSprite("./images/safe.png", self.rect.centerx-130, self.rect.y-100, speed=0)
    #     self.Safe_resource.add(safe1)
    #

#定义一个敌机类型：
class EnemySprite(GameSprite):
    def __init__(self):
        super().__init__("./images/enemy1.png", speed=3)
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)
        self.rect.y = -self.rect.height


    #定义敌机超出边界销毁
    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()

    #定义敌机的爆炸场景
    # def bomb(self):
    #     print("爆炸场景")
    #     p1 = pygame.image.load("./images/p1.png")
    #     p2 = pygame.image.load("./images/p2.png")
    #     p3 = pygame.image.load("./images/p2.png")
    #     p4 = pygame.image.load("./images/p2.png")
    #     n = 0
    #
    #     while True:
    #         n += 1
    #         if n == 1:
    #             screen.blit(p1, (self.rect.x, self.rect.y))
    #
    #         elif n == 2:
    #             screen.blit(p2, (self.rect.x, self.rect.y))
    #
    #         elif n == 3:
    #             screen.blit(p3, (self.rect.x, self.rect.y))
    #
    #         elif n == 4:
    #             screen.blit(p4, (self.rect.x, self.rect.y))
    #             break
    #         pygame.display.update()

    #敌机开火的方法
    def fire(self):
        bullet = BulletSprite("./images/bullet1.png", self.rect.centerx-38, self.rect.y, speed=5)
        enemy_bullets.add(bullet)
        print("敌机发射子弹")

    def lb(self):
        lb = BulletSprite("./images/lb.png", random.randint(0,450), 0, speed=3)
        lb_resource.add(lb)

    #重写del方法，让敌机爆炸的时候展示爆炸界面
    def __del__(self):
        print("展示爆炸场景")
        #self.bomb()

#定义一个子弹类型
class BulletSprite(GameSprite):

    def __init__(self, image_path,  x, y, speed):
        super().__init__(image_path)     #不同类型类型可以不用空格
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.xspeed = 0

#定义子弹超出边界销毁
    def update(self):
        super().update()
        self.rect.x += self.xspeed
        if self.rect.y < -self.rect.height:
            print("英雄子弹销毁")
            self.kill()
        if self.rect.y > SCREEN_RECT.height:
            print("敌机子弹销毁")
            self.kill()


    #检测子弹是否销毁
    def __del__(self):
        print("子弹销毁")


#创建一个敌机的子弹精灵组
enemy_bullets = pygame.sprite.Group()

#创建英雄和背景的精灵组
resource = pygame.sprite.Group()

#创建一个敌机精灵组：
enemys = pygame.sprite.Group()

#加载背景音乐
pygame.mixer.music.load("./musics/bg.mp3")

# 加载枪声
gun = pygame.mixer.Sound("./musics/gun1.wav")

#间隔一定的时间创建一架敌机：
pygame.time.set_timer(CREATE_ENEMY, 800)
#间隔一定的时间创建一个boss机
pygame.time.set_timer(CREATE_ENEMY2, 6000)
#创建boss飞机的子弹
pygame.time.set_timer(CREATE_BULLET, 1700)
#创建礼包
pygame.time.set_timer(CREATE_LB, 9000)


#创建飞机爆炸的声音
bz = pygame.mixer.Sound("./musics/bz.wav")

# 生成场景
bg1 = BackgroundSprite("./images/bg1.jpg", speed=2)
bg2 = BackgroundSprite("./images/bg1.jpg", speed=2, next=True)
hero =HeroSprite()
#将图片和英雄飞机精灵加入精灵组
resource.add(bg1)
resource.add(bg2)
resource.add(hero)

##################################################################
#关卡2
resource2 = pygame.sprite.Group()

bg3 = BackgroundSprite("./images/bg2.jpg", speed=2)
bg4 = BackgroundSprite("./images/bg2.jpg", speed=2,next=True)
hero2 =HeroSprite()

# 将图片和英雄飞机精灵加入精灵组
resource2.add(bg3)
resource2.add(bg4)
resource2.add(hero2)

#新建一个boss类
class BossSprite(GameSprite):
    def __init__(self):
        super().__init__("./images/boss.png", speed=2)
        self.rect.x = random.randint(0, 312)
        self.rect.y = 0

    # #定义boss机超出边界销毁
    def update(self):
        #self.rect.x += random.randint(-2, +2)
        if self.rect.y == self.rect.height:
            self.rect.y = self.rect.height

    def fire(self):
        bullet1 = BulletSprite("./images/bullet3.png", self.rect.centerx-80, self.rect.y, speed=4)
        bullet2 = BulletSprite("./images/bullet3.png", self.rect.centerx+80, self.rect.y, speed=4)
        enemy_bullets.add(bullet1, bullet2)
        print("boss发射子弹了")

    def __del__(self):
        print("boss爆炸")

#定义英雄保护罩的精灵
class SafeSprite(GameSprite):
    def __init__(self,image_path,  x, y, speed):
        super().__init__(image_path)
        self.image = image_path
        self.x = x
        self.y = y
        self.speed = speed






#boss机的精灵组
boss_resource = pygame.sprite.Group()

#创建一个礼包的精灵组
lb_resource = pygame.sprite.Group()

#创建一个保护罩精灵组
safe_resource = pygame.sprite.Group()
