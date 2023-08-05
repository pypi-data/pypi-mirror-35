import pygame,random,math
#定义需要的常量
SCREEN_SIZE =(512,768)
SCREEN_RECT =pygame.Rect(0,0,*SCREEN_SIZE)
# 自定义一个事件
ENEMY_CREATE = pygame.USEREVENT
ENEMY_CREATES = pygame.USEREVENT


#定义游戏父类型主类
class GameSprite(pygame.sprite.Sprite):
    """游戏精灵对象：用于表示游戏中各种元素"""
    def __init__(self,image_path,speed=1):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect =self.image.get_rect()
        self.speed = speed

    def update(self):
        "，默认运动更新方法"
        self.rect.y += self.speed


#定义背景图片类型
class BackGround(GameSprite):
    def __init__(self,image_path,next=False):
        super().__init__(image_path,speed=1)
        #初始化边界
        if next:
            self.rect.y = -SCREEN_SIZE[1]

        #调用父类方法
        #更新
    def update(self):
        super().update()
        if self.rect.y > SCREEN_SIZE[1]:
            self.rect.y = -SCREEN_SIZE[1]

#定义我方飞机类型
class HeroSprite(GameSprite):
    def __init__(self,image_path):
        super().__init__(image_path,speed=0)
        # 初始生命值
        self.index = 0
        self.life = 10
        # 初始分值
        self.score = 0

        #初始化飞机位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.y = SCREEN_RECT.centery +200
        #创建一个子弹精灵组
        self.bullets = pygame.sprite.Group()
    #
    def update(self):
        #水平边界判断
        if self.rect.x <= 0:
            self.rect.x =0
        elif self.rect.x >= SCREEN_RECT.width-self.rect.width:
            self.rect.x = SCREEN_RECT.width-self.rect.width


        #垂直边界判断
        if self.rect.y<=0:
            self.rect.y = 0
        elif self.rect.y >= SCREEN_RECT.height -self.rect.height:
            self.rect.y = SCREEN_RECT.height -self.rect.height

    def fire(self):
        self.index +=20

        """飞机开火"""
        #创建一个子弹对象
        bullet = BulletSprite("./images/21.png",self.rect.centerx-15+30*math.cos(self.index),self.rect.centery-90)
        #添加到精灵组对象
        self.bullets.add(bullet)
    def fire3(self):
        self.index +=20

        """飞机开火"""
        #创建一个子弹对象
        bullet2 = BulletSprite("./images/bugizhi.png",self.rect.centerx-15+30*math.cos(self.index),self.rect.centery-90)
        #添加到精灵组对象
        self.bullets.add(bullet2)
    def fire2(self):
        """飞机开火"""
        #创建一个子弹对象

        bujibullet = BulletSprite3(self.rect.centerx-15,self.rect.centery-90)
        self.bullets.add(bujibullet)

#创建一个英雄飞机子弹精灵
class BulletSprite(GameSprite):
    """子弹精灵"""
    def __init__(self,image_path,x,y):
        super().__init__(image_path,speed =-8)
        self.rect.x = x
        self.rect.y = y

    def update(self):
        super().update()
        #边界判断
        if self.rect.y <= -self.rect.height:
            #子弹删除
            self.kill()
    def __del__(self):
        print("子弹对象已经销毁")


#创建一个英雄飞机补给子弹精灵
class BulletSprite3(GameSprite):
    """子弹精灵"""
    def __init__(self,x,y):
        super().__init__("./images/bujiji.png",speed =0)
        self.rect.x = SCREEN_RECT.centerx-230
        self.rect.y = SCREEN_RECT.y

    def update(self):
        super().update()
        #边界判断
        if self.rect.y <= -self.rect.height:
            #子弹删除
            self.kill()
    def __del__(self):
        print("子弹对象已经销毁")


#创建一个敌方飞机子弹精灵
class BulletSprite1(GameSprite):
    """子弹精灵"""
    def __init__(self,image_path,x,y):
        super().__init__(image_path,speed =6)
        self.rect.x = x
        self.rect.y = y

    def update(self):
        super().update()
        #边界判断
        if self.rect.y <= -SCREEN_RECT.height:
            #子弹删除
            self.kill()
    def __del__(self):
        print("子弹对象已经销毁")


#创建敌方飞机类型
class EnemySprite(GameSprite):
    def __init__(self,image_path):
        #初始化敌方飞机数据：图片，速度
        super().__init__(image_path,speed =random.randint(2,5))

        #初始化敌方飞机位置
        self.rect.x = random.randint (0,SCREEN_RECT.width-self.rect.width)
        self.rect.y = -self.rect.height
        self.bulletlist =pygame.sprite.Group()

    def send_bullet(self):
        e = random.randint(1,100)

         # 创建一个子弹对象
        if e >97:
            bullets = BulletSprite1("./images/33.png",self.rect.centerx - 31, self.rect.y)
            self.bulletlist.add(bullets)
    def send_bullet1(self):
         # 创建一个子弹对象
        bullets = BulletSprite1("./images/ez111.png",self.rect.centerx - 31, self.rect.y)
        self.bulletlist.add(bullets)

    def update(self):
        super().update()
        if self.rect.y > SCREEN_RECT.height:
            self.kill()

    def __del__(self):
        self.destroy()

    def destroy(self):
        print("敌机销毁")


##################################3

class buji(GameSprite):
    def __init__(self):
        super().__init__("./images/buji_1.png",speed = 5)
        #初始化补给位置
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)
        self.rect.y = -self.rect.height
    def update(self):
        super().update()
        if self.rect.y > SCREEN_RECT.height:
            self.kill()

    def __del__(self):
        self.destroy()

    def destroy(self):
        print("补给销毁")



class buji1(GameSprite):
    def __init__(self):
        super().__init__("./images/buji_2.png",speed = 3)
        #初始化补给位置
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)
        self.rect.y = -self.rect.height
    def update(self):
        super().update()
        if self.rect.y > SCREEN_RECT.height:
            self.kill()

    def __del__(self):
        self.destroy()

    def destroy(self):
        print("补给销毁")

######################################33
# 定义boss飞机类型
class Boos(GameSprite):
    '''巫师精灵对象'''

    def __init__(self, image_path,hp1):
        # 初始化巫师的图片、速度
        super().__init__(image_path, speed=10)
        # 初始化英雄飞机的位置
        self.rect.centerx = SCREEN_RECT.centerx  # width宽度
        self.rect.y = -self.rect.height
        self.bullets = pygame.sprite.Group()  # group组 bullets子弹
        self.skills = pygame.sprite.Group()
        self.hp1 = hp1
        self.speed2 = random.randint(1, 9)

    def update(self):
        # 调用父类的方法直接运动
        super().update()
        self.rect.x += self.speed2
        if self.rect.x >= SCREEN_RECT.width - self.rect.width:
            self.rect.x = SCREEN_RECT.width - self.rect.width
            self.speed2 = -self.speed2
            # self.speed = -self.speed
        if self.rect.x <= 0:
            self.rect.x = 0
            self.speed2 = -self.speed2
        if self.rect.y >= 0:
            self.rect.y = 0





