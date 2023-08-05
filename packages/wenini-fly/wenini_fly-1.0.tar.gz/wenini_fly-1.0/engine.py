import pygame,model,time,random
#定义需要的常量
SCREEN_SIZE =(512,768)
SCREEN_RECT =pygame.Rect(0,0,*SCREEN_SIZE)
ENEMY_CREATE = pygame.USEREVENT
ENEMY_BOOM_SCORE = 10
ENEMY_BIGBOOM_SCORE = 4

pygame.font.init()
#初始化音效
pygame.mixer.init()
pygame.mixer.music.load("./mp3/menm.mp3")
#初始化音效
pygame.mixer.init()
soundwav = pygame.mixer.Sound("./mp3/da.wav")  # filename.wav文件名
#
pygame.mixer.init()
soundwavs = pygame.mixer.Sound("./mp3/5972.wav")  # filename.wav文件名
#
pygame.mixer.init()
soundwavss = pygame.mixer.Sound("./mp3/6319.wav")  # filename.wav文件名
# 设置音量
pygame.mixer.music.set_volume(50)
pygame.mixer.music.play(1)


# sound = pygame.mixer.Sound('')

class GameEngine:
    def __init__(self):

        # 定义英雄飞机对象
        self.hero = model.HeroSprite("./images/hero_1.png")
        self.hero1 = model.HeroSprite("./images/hero_2.png")
        pygame.display.set_caption("平平飞机大战")

        # 定义一个敌方飞机对象
        # 定义一个敌方大飞机对象
        self.enemy= model.EnemySprite("./images/p02-1.png")
        self.wushi =model.Boos("./images/boss2.png", hp1=20)
        self.bigenemy = model.EnemySprite("./images/big1.png")
         # 定义一个敌人飞机的精灵组对象
        # 定义一个敌人大飞机的精灵组对象
        self.enemys = pygame.sprite.Group()
        self.bigenemys = pygame.sprite.Group()
        self.bosse = pygame.sprite.Group()


        #定义一个补给子弹精灵组
        #定义一个补给血量精灵组
        self.bujib = pygame.sprite.Group()
        self.bujih = pygame.sprite.Group()

        # 爆炸敌机精灵组
        self.enemys_boom = pygame.sprite.Group()

        #定义爆炸飞机字典
        # 定义爆炸大飞机字典
        self.enemys_boom_dict = dict()
        self.bigenemys_boom_dict = dict()

        #创建一个屏幕变量
        self.screen = pygame.display.set_mode(SCREEN_SIZE)

        #引入字体
        self.game_font = pygame.font.SysFont("fangsong",16,True)

        #大飞机生命
        self.ssss = 10
    def show_index(self):
        pygame.init()
        # 添加一个时钟
        clock = pygame.time.Clock()
        while True:
            clock.tick(66)
            bgg_1 = pygame.image.load("./images/bgg2.jpg")
            self.screen.blit(bgg_1,(0,0))
            pygame.display.update()
            event_list = pygame.event.get()
            shubiao = list(pygame.mouse.get_pos())
            for event in event_list:
                if 110 < shubiao[0] < 400 and 504 < shubiao[1] < 616:
                    if event.type == pygame.MOUSEBUTTONUP:
                        self.start()

                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()


    def start(self):
        pygame.init()
        # 添加一个时钟
        clock = pygame.time.Clock()
        # 间隔一定的时间，触发一个创建敌机的事件
        pygame.time.set_timer(ENEMY_CREATE, 2000)
        self.create_scence()
        self.bg()
        self.bg22()
        self.bg33()

        while True:
            if  self.hero.score<100:
                clock.tick(24)
                self._check_collide()
                self._check_event()
                self.create_ran()
                self.check_kewdown()
                # 精灵组渲染
                self.resources.update()
                self.resources.draw(self.screen)
                self.update()
                pygame.display.update()

            elif self.hero.score>=100 and self.hero.score<1200:
                clock.tick(24)
                self._check_collide()
                self._check_event()
                self.create_ran()
                self.check_kewdown()

                # 精灵组渲染
                self.resources2.update()
                self.resources2.draw(self.screen)
                self.update()

                pygame.display.update()
    def create_scence(self):
        self.screen = pygame.display.set_mode(SCREEN_SIZE)

    def _check_event(self):

        #添加监听程序
        event_list = pygame.event.get()
        if len(event_list)>0:
            print(event_list)
            for event in event_list:
                print(event.type, pygame.KEYDOWN, pygame.K_LEFT)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                #创建敌方小飞机
                if event.type == ENEMY_CREATE:
                    print("创建一家敌方飞机。。。。。")
                    self.enemy = model.EnemySprite("./images/p02-1.png")
                    self.enemys.add(self.enemy)
            self.enemy.send_bullet()
##################################################33

##########################################################3
# 获取键盘的值
    def check_kewdown(self):
        key_down = pygame.key.get_pressed()
        if key_down[pygame.K_LEFT]:
            print("向左移动<<<<<<<<<<")
            self.hero.rect.x -=8
        if key_down[pygame.K_RIGHT]:
            print("向右移动>>>>>>>>>>>")
            self.hero.rect.x += 8
        if key_down[pygame.K_UP]:
            print("向上移^^^^^^^^^^^^^^^")
            self.hero.rect.y -=8
        if key_down[pygame.K_DOWN]:
            print("向下移动vvvvvvvvvvvv")
            self.hero.rect.y +=8
        if  key_down[pygame.K_END]:
            self.hero.fire()
            soundwavs.play()
            print("开火",self.hero.bullets)
        if key_down[pygame.K_a]:
            print("向左移动<<<<<<<<<<")
            self.hero1.rect.x -= 8
        if key_down[pygame.K_d]:
            print("向右移动>>>>>>>>>>>")
            self.hero1.rect.x += 8
        if key_down[pygame.K_w]:
            print("向上移^^^^^^^^^^^^^^^")
            self.hero1.rect.y -= 8
        if key_down[pygame.K_s]:
            print("向下移动vvvvvvvvvvvv")
            self.hero1.rect.y += 8

        elif key_down[pygame.K_f]:
            self.hero1.fire3()
            soundwavs.play()
            print("开火", self.hero1.bullets)

    def boom(self, enemy):
        for i in range(2, 6):
            clock = pygame.time.Clock()
            clock.tick(60)
            image = pygame.image.load("./enemy2_down_" + str(i) + ".png")
            self.screen.blit(image, enemy.rect)
            pygame.display.update()
            print(image)

    def _check_collide(self):
        # 碰撞检测:子弹和敌方飞机之间的碰撞！
        self.enemys_boom_dict= pygame.sprite.groupcollide(self.hero.bullets, self.enemys , True, True)

        #计算得分
        self.hero.score += len(self.enemys_boom_dict)*ENEMY_BOOM_SCORE
        self.enemys_boom.add(self.enemys_boom_dict)  # 添加到爆炸精灵组
        for enemy_boom in self.enemys_boom:
            self.boom(enemy_boom) # 将敌机返回到爆炸组，调用函数
            soundwavss.play()
            print("爆炸")
            self.enemys_boom.remove(enemy_boom)
            self.wu_shi()
        ###########################################################3
        # 碰撞检测:子弹和敌方大飞机之间的碰撞！
        self.bigenemys_boom_dict = pygame.sprite.groupcollide(self.hero.bullets, self.bigenemys, True,True)
        # 计算得分
        self.hero.score += len(self.bigenemys_boom_dict) * ENEMY_BIGBOOM_SCORE
        # 添加到爆炸精灵
        self.enemys_boom.add(self.bigenemys_boom_dict)
        for enemy_boom in self.enemys_boom:
            self.boom(enemy_boom)  # 将敌机返回到爆炸组，调用函数
            soundwavss.play()
            print("爆炸")
            self.enemys_boom.remove(enemy_boom)
        o = pygame.sprite.groupcollide(self.hero1.bullets, self.enemys, True,True)
        if len(o)>0:
            self.enemy.kill()

        #飞机与敌方飞机子弹碰撞
        if pygame.sprite.spritecollide(self.hero and self.hero1,self.enemy.bulletlist,True):
            self.hero.life =self.hero.life-1
            if self.hero.life <=0:
                self.hero.kill()
                self.game_over()
                pygame.quit()
                exit()

        # 碰撞检测：英雄飞机和敌方飞机之间的碰撞
        if pygame.sprite.spritecollide(self.hero and self.hero1, self.enemys, True):
            self.hero.life = self.hero.life - 1
            if self.hero.life <= 0:
                self.hero.kill()
                self.game_over()

        #补给与飞机碰撞
        pe = pygame.sprite.spritecollide(self.hero ,self.bujib,True)
        if len(pe) > 0:
            soundwav.play()
            self.buji.kill()
            self.hero.fire2()
            print("开火", self.hero.bullets)

        #血量补给与飞机碰撞
        if pygame.sprite.spritecollide(self.hero1, self.bujih, True):
            self.hero.life = self.hero.life + 1
            if self.hero.life>10:
                self.hero.life =10

        # 子弹与巫师碰撞
        res2 = pygame.sprite.groupcollide(self.bosse, self.hero.bullets, False, True)
        if len(res2) > 0:
            self.wushi.hp1 -= 1
            if self.wushi.hp1 <= 0:
                self.wushi.kill()


    def update(self):
 #子弹精灵组渲染
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

        self.hero1.bullets.update()
        self.hero1.bullets.draw(self.screen)

        self.bosse.update()
        self.bosse.draw(self.screen)

        # 敌机子弹渲染
        for self.enemy in self.enemys:
            self.enemy.bulletlist.update()
            self.enemy.bulletlist.draw(self.screen)
#渲染补给
        self.bujib.update()
        self.bujib.draw(self.screen)
# 渲染补给
        self.bujih.update()
        self.bujih.draw(self.screen)
#渲染敌机精灵组中所有飞机
        self.enemys.update()
        self.enemys.draw(self.screen)

        self.screen.blit(self.game_font.render(u"当前分数：%s" % self.hero.score, True, [0, 0, 255]), [20, 20])
        self.screen.blit(self.game_font.render(u"当前生命：%s" % self.hero.life, True, [255, 0, 0]), [400, 20])
        ##################

    #####################################
    # 创建随机生成对象方法
    def create_ran(self):
        c = random.randint(1, 1000)
        # 创建一个敌方大飞机
        if c < 15:
            print("创建一家敌方大飞机。。。。。")
            self.enemyss = model.EnemySprite("./images/big1.png")
            self.enemys.add(self.enemyss)

        elif c > 20 and c < 30:
            print("创建一个补给")
            self.buji = model.buji()
            self.bujib.add(self.buji)

        elif c > 990:
            print("创建一个补给")
            self.buji1 = model.buji1()
            self.bujih.add(self.buji1)
#####################################
    def bg(self):
        # 定义背景精灵组
        self.bg1 = model.BackGround("./images/bg-1.jpg")
        self.bg2 = model.BackGround("./images/bg-1.jpg", next=True)
        # 添加精灵组
        self.resources = pygame.sprite.Group(self.bg1, self.bg2, self.hero,self.hero1)

    # 创建背景对象
    def bg22(self):
        # 定义背景精灵组
        self.bg3 = model.BackGround("./images/bgimage1.jpg")
        self.bg4 = model.BackGround("./images/bgimage1.jpg", next=True)
        # 添加精灵组
        self.resources2 = pygame.sprite.Group(self.bg3, self.bg4, self.hero,self.hero1)

    def bg33(self):
        # 定义背景精灵组
        self.bg5 = model.BackGround("./images/imgbg_4.jpg")
        self.bg6 = model.BackGround("./images/imgbg_4.jpg", next=True)
        # 添加精灵组
        self.resources3 = pygame.sprite.Group(self.bg5, self.bg6, self.hero,self.hero1)

##############################################3

    def game_over(self):
        '''结束'''
        self.create_scence()
        while True:
            self.update()
            self.screen.blit(self.game_font.render("GAME OVER", True, [0, 255, 255]), [80, 200])
            # pygame.time.delay(1000)
            self.screen.blit(self.game_font.render('游戏得分：%s' % self.hero.score, True, [0, 255, 255]), [80, 300])
            # pygame.time.delay(1000)
            self.screen.blit(self.game_font.render("空格继续", True, [0, 255, 255]), [100, 400])

            pygame.display.update()
            event_list = pygame.event.get()
            if event_list:
                for event in event_list:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            # return True
                            # self.show()
                            break
            time.sleep(4)
            break
        pygame.quit()
        exit()
    def wu_shi(self):
        print(self.hero.score)
        if self.hero.score == 120:
            self.bosse.add(self.wushi)

        if self.hero.score == 180:
            self.wushi = model.Boos("./images/boss.png",hp1=40)
            self.bosse.add(self.wushi)





