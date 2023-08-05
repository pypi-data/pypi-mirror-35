'''
游戏引擎:控制游戏流程
'''
import pygame,game_sprites,time

#初始化所有模块
pygame.init()

# #定义全局变量
# num = 0
#音乐
pygame.mixer.init()
pygame.mixer_music.load("./music/beigin.mp3")
pygame.mixer_music.play(-1)

#自定义一个事件
ENEMY_CREATE = pygame.USEREVENT

class GameEngine():
    def __init__(self):


        # 创建游戏窗口
        self.screen = pygame.display.set_mode(game_sprites.SREEN_SAZE)

        # 间隔一定的事件，触发一次创建敌机的事件
        pygame.time.set_timer(ENEMY_CREATE, 1000)

        # 定义一个时钟对象
        self.clock = pygame.time.Clock()

        # 定义爆炸精灵组
        self.booms_sprite = pygame.sprite.Group()

        #定义分数
        self.num = 0

    def score(self):
        self.font = pygame.font.SysFont("宋体",50,True,True)
        self.goal = self.font.render("score:%s" % self.num,True,(241,185,194))

    #创建精灵的方法
    def creat_sprite(self,i):

        #定义背景精灵
        bg1 = game_sprites.BackgroundSprite("./image/bg.jpg")
        bg2 = game_sprites.BackgroundSprite("./image/bg.jpg",next=True)

        #定义英雄飞机对象
        self.hero = game_sprites.HeroSprite("./image/hero_{0}.png".format(i))

        #定义初始化精灵组对象
        self.resources = pygame.sprite.Group(bg1,bg2,self.hero)

        #定义一个敌人飞机的精灵组对象
        self.enemys = pygame.sprite.Group()

        #定义一个支援物品
        self.supports = pygame.sprite.Group()

    #定义绝技
    def dazhao(self):
        image = pygame.image.load("./image/hudie.png")

        self.screen.blit(image,(50,180))
        self.music_dazhao()
        pygame.display.flip()

    #事件监听
    def event(self):

        # 监听所有事件
        event_list = pygame.event.get()
        for event in event_list:
            # print(event.type, pygame.KEYDOWN, pygame.K_LEFT)
            if event.type == pygame.QUIT:
                # 卸载所有pygame资源，退出程序
                pygame.quit()
                exit()

            # 创建敌方飞机和支援
            if event.type == ENEMY_CREATE:
                enemy = game_sprites.EnemySprite()
                zhi_yuan = game_sprites.Support()
                self.enemys.add(enemy)
                self.supports.add(zhi_yuan)

        # 获取当前用户键盘上被操作的按键
        key_down = pygame.key.get_pressed()

        if key_down[pygame.K_LEFT]:
            self.hero.rect.x -= 5

        if key_down[pygame.K_RIGHT]:
            self.hero.rect.x += 5

        if key_down[pygame.K_UP]:
            self.hero.rect.y -= 5

        if key_down[pygame.K_DOWN]:
            self.hero.rect.y += 5

        if key_down[pygame.K_SPACE]:
            self.hero.fire()
            self.music_bullet()

        if key_down[pygame.K_b]:
            self.dazhao()
            self.enemys.empty()

    def music_bullet(self):
        pygame.mixer.init()
        s = pygame.mixer.Sound("./music/bullt_music.wav")
        s.play()

    def music_boom1(self):
        pygame.mixer.init()
        boom = pygame.mixer.Sound("./music/enemy3_down.wav")
        boom.play()

    def music_dazhao(self):

        pygame.mixer.init()
        s = pygame.mixer.Sound("./music/dazhao.wav")
        s.play()

    def music_zhiyuan(self):
        pygame.mixer.init()
        s = pygame.mixer.Sound("./music/zhiyuan.wav")
        s.play()

    #爆炸效果
    def boom(self,enemy):
        for i in range(1,4):
            image = pygame.image.load("./image/boom{0}.png".format(i))
            self.screen.blit(image,enemy.rect)
            pygame.display.update()

    #碰撞检测
    def check_collide(self):
        # 碰撞检测：子弹和敌机之间的碰撞
        a = pygame.sprite.groupcollide(self.enemys, self.hero.bullets,True, True)
        self.booms_sprite.add(a)
        for enemy_boom in self.booms_sprite:
            self.num += 10
            self.boom(enemy_boom)
            self.booms_sprite.remove(enemy_boom)
            if len(a)>0:
             self.music_boom1()

        # 碰撞检测：英雄飞机和敌机的检测
        e = pygame.sprite.spritecollide(self.hero, self.enemys, True)
        if len(e) > 0:
            # self.hero.kill()
            self.num = 0
            game_over.over()
            pygame.quit()
            exit()

        #碰撞检测：英雄飞机和支援的碰撞
        s = pygame.sprite.spritecollide(self.hero,self.supports,True)

        if len(s) > 0:
            self.music_zhiyuan()
            self.num += 2

    #更新精灵和精灵组
    def update_sprites(self):

        #背景和英雄飞机精灵组更新渲染
        self.resources.update()
        self.resources.draw(self.screen)
        self.screen.blit(self.goal,(10,10))

        # 英雄飞机子弹精灵组更新渲染
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

        # 敌人飞机精灵组更新渲染
        self.enemys.update()
        self.enemys.draw(self.screen)

        self.supports.update()
        self.supports.draw(self.screen)

    def start(self):

        # self.creat_sprite(i)
        self.clock.tick(12)
        #游戏场景循环
        while True:

            #调用分数方法
            self.score()

            #事件监听
            self.event()

            #更新精灵和精灵组
            self.update_sprites()

            # 碰撞检测
            self.check_collide()

            #更新显示
            pygame.display.update()

engine = GameEngine()


class ShowIndex():

    def start(self):

        #加载首页图片
        back_image = pygame.image.load("./image/begin.jpg")
        engine.screen.blit(back_image,(0,0))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 180 <= event.pos[0] <= 300 and 350 <= event.pos[1] <= 450:
                        choose.start()

                elif event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

show = ShowIndex()


#选择飞机界面
class Choose_hero():

    def hero1(self):
        hero1 = pygame.image.load("./image/hero_1.png")
        engine.screen.blit(hero1,[100,300])
        pygame.display.flip()

    def hero2(self):
        hero2 = pygame.image.load("./image/hero_2.png")
        engine.screen.blit(hero2,[300,300])
        pygame.display.flip()

    def hero2_press(self):
        hero2 = pygame.image.load("./image/hero21_press.png")
        engine.screen.blit(hero2,[300,300])
        pygame.display.flip()

    def hero1_press(self):
        hero2 = pygame.image.load("./image/hero1_press.png")
        engine.screen.blit(hero2,[100,300])
        pygame.display.flip()

    def start(self):
        engine.screen.fill([242,156,177])       #用pink填充窗口
        begin = pygame.image.load("./image/choose3.png") #加载开始界面的图片
        engine.screen.blit(begin, [0, 200])       #在离x和y多远处渲染图片
        pygame.display.flip()
        while True:
            # if True:
            self.hero1()
            self.hero2()
            for event in pygame.event.get():    #获得事件
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 300 <= event.pos[0] <=400 and 300 <= event.pos[1] <= 400:
                        self.hero2_press()
                        time.sleep(1)
                        engine.creat_sprite(2)
                        engine.start()
                        break
                    elif 100 <= event.pos[0] <= 200 and 300 <= event.pos[1] <= 400:
                        self.hero1_press()
                        time.sleep(1)
                        engine.creat_sprite(1)
                        engine.start()
                        break

                    # elif event.type == pygame.MOUSEBUTTONDOWN:
                    #     if 100 <= event.pos[0] <= 200 and 300 <= event.pos[1] <= 400:
                    #         self.hero1_press()
                    #         time.sleep(1)
                    #         engine.creat_sprite(2)

                # if event.type == pygame.MOUSEBUTTONDOWN:
                #     if 180 <= event.pos[0] <= 300 and 400 <= event.pos[1] <= 500:
                    

                elif event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

choose = Choose_hero()


#游戏结束场景
class GameOver():

    def over(self):
        over_background = pygame.image.load("./image/gameover21.jpg")
        engine.screen.blit(over_background,(0,0))
        engine.screen.blit(engine.goal,(180,250))
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 150 <= event.pos[0] <= 400 and 260 <= event.pos[1] <= 400:
                        choose.start()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 150 <= event.pos[0] <= 400 and 450 <= event.pos[1] <= 550:
                        pygame.quit()
                        exit()

                elif event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

game_over = GameOver()
