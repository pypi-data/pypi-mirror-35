'''
所有游戏精灵类型存放的文件
'''

import pygame,random

#定义常量
SREEN_SAZE = (512,768)
SREEN_RECT = pygame.Rect(0,0,*SREEN_SAZE)


class GameSprite(pygame.sprite.Sprite):

    def __init__(self,image_path,speed = 1):

        #调用父类初始化数据
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        '''默认运动更新方法'''
        
        self.rect.y += self.speed


class BackgroundSprite(GameSprite):

    def __init__(self,image_path,next=False):
        super().__init__(image_path,speed=2)
        if next:
            self.rect.y = -SREEN_SAZE[1]

    def update(self):

        #调用父类的方法
        super().update()

        #子类中判断边界
        if self.rect.y > SREEN_SAZE[1]:
            self.rect.y = -SREEN_SAZE[1]


class HeroSprite(GameSprite):
    '''英雄精灵'''

    def __init__(self,image_path):
        super().__init__(image_path,speed=0)

        #初始化英雄飞机的位置
        self.rect.centerx = SREEN_RECT.centerx
        self.rect.centery = SREEN_RECT.centery +260
        self.bullets = pygame.sprite.Group()

    def update(self):

        #水平判断
        if self.rect.x < 0:
            self.rect.x = 0

        if self.rect.x > SREEN_RECT.width - self.rect.width:
            self.rect.x = SREEN_RECT.width - self.rect.width

        #垂直判断
        if self.rect.y < 0:
            self.rect.y = 0

        elif self.rect.y > SREEN_RECT.height - self.rect.height:
            self.rect.y = SREEN_RECT.height - self.rect.height

    def fire(self):
        '''飞机攻击'''
        if len(self.bullets) < 6:
            bullet = BulletSprite(self.rect.centerx-23,self.rect.y)
            self.bullets.add(bullet)


class BulletSprite(GameSprite):
    '''子弹精灵'''
    def __init__(self,x,y):
        super().__init__("./image/bullet3.png",speed=-3)
        self.rect.x = x
        self.rect.y = y

    def update(self):

        #调用父类的方法进行操作
        super().update()

        #边界判断
        if self.rect.y <= -self.rect.height:

            #子弹从精灵组中删除
            self.kill()


class EnemySprite(GameSprite):
    
    #敌方精灵
    def __init__(self):
        super().__init__("./image/diji_2.png",speed=random.randint(3,6))

        #初始化敌方飞机的位置
        self.rect.x = random.randint(0,SREEN_RECT.width-self.rect.width)
        self.rect.y = -self.rect.height

    def update(self):

        #调用父类的方法直接运动
        super().update()

        #边界判断
        if self.rect.y > SREEN_RECT.height:
            self.kill()


class Support(GameSprite):
    
    #支援精灵
    def __init__(self):
        super().__init__("./image/zhi_yuan1.png",speed=5)
        self.rect.x = random.randint(0,SREEN_RECT.width-self.rect.width)
        self.rect.y = -self.rect.height

    def update(self):
        super().update()

        #边界判断
        if self.rect.y > SREEN_RECT.height:
            self.kill()
