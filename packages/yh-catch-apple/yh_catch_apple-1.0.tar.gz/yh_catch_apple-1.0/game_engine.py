#引入模块
import pygame,models,sys,math

# 自定义一个事件
ENEMY_CREATE = pygame.USEREVENT
ZHADAN_CREATE = pygame.USEREVENT+1

# 定义一个时钟
clock = pygame.time.Clock()


#定义一个游戏引擎类
class GameEngine:

    def __init__(self):
        # 创建一个游戏窗口
        self.screen = pygame.display.set_mode((1068, 810), 0, 32)

        # 背景图片：游戏精灵
        self.bg_1 = models.BackGround()
        self.bg_2 = models.BackGround(prepare=True)

        # 英雄图片：游戏精灵
        self.hero = models.HeroSprite()

        # 创建一个精灵对象组
        self.sprite_group = pygame.sprite.Group(self.bg_1, self.bg_2)

        # 敌人精灵组
        self.enemy_group = pygame.sprite.Group()

        #炸弹精灵组
        self.zhadan_group = pygame.sprite.Group()


        #产生字体对象
        self.font = pygame.font.Font("font/MarkerFelt.ttf",30)

        #历史分数
        self.history = models.HistoryScore()

        #暂停游戏
        self.restart = False

    def check_event(self):
        # 事件监测
        for i in pygame.event.get():
            # 判断为退出
            if i.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # 判断鼠标按下
            if i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1 and self.hero.isInHero == True:
                    self.hero.isMove = True
            # 判断鼠标抬起
            if i.type == pygame.MOUSEBUTTONUP:
                if i.button == 1:
                    self.hero.isMove = False
            # 判断键盘按下
            # if i.type == pygame.KEYDOWN:
            #     if i.key == pygame.K_SPACE:
            #         models.Zha_danSprite().speed = 0
            #         models.BackGround().speed = 0
            #         models.EnemySprite().speed = 0
            # if i.type == pygame.KEYDOWN:
            #     if i.key == pygame.K_SPACE:
            #         self.restart = not self.restart
            #         # 播放
            #         if self.restart:
            #             yx_start().unpase()
            #         # 暂定
            #         else:
            #             yx_start().pause()
            # 创建敌人
            if i.type == ENEMY_CREATE:
                enemy = models.EnemySprite()
                self.enemy_group.add(enemy)
            # 创建炸弹
            if i.type == ZHADAN_CREATE:
                zhadan = models.Zha_danSprite()
                self.zhadan_group.add(zhadan)
            #判断键盘按下
            # if i.type == pygame.KEYDOWN:
            #     if i.key == pygame.K_LEFT:
            #         print("向左移动")
            #         self.hero.rect.x -= 20
            #     if i.key == pygame.K_RIGHT:
            #         print("向右移动")
            #         self.hero.rect.x += 20
            #     if i.key == pygame.K_UP:
            #         print("向上移动")
            #         self.hero.rect.y += 20
            #     if i.key == pygame.K_DOWN:
            #         print("向下移动")
            #         self.hero.rect.y -= 20

    def check_collide(self):
        # 碰撞检测：英雄和敌人组碰撞
        c = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if c:
            self.hero.score += 1
            pygame.mixer.music.load("images/game_achievement.mp3")
            pygame.mixer.music.play()
        # 碰撞检测：英雄和炸弹碰撞
        e = pygame.sprite.spritecollide(self.hero, self.zhadan_group, True)
        #if e:
        if len(e) > 0:
            self.hero.kill()
            pygame.mixer.music.load("images/game_over.mp3")
            pygame.mixer.music.play()
            self.history.ChangeHistory(self.hero.score)
            game_over()

    def update_scene(self):
        # 刷新渲染精灵组各个精灵对象
        self.sprite_group.update()
        self.sprite_group.draw(self.screen)

        #在屏幕中显示分数字体
        score = self.font.render("Score:%s" %self.hero.score,True,(0,0,0))
        self.screen.blit(score,(0,70))

        #在屏幕上显示历史分数字体
        history = self.font.render("History:%s"%self.history.hisScore,True,(0,0,0))
        self.screen.blit(history,(0,105))

        #渲染主角鼠标
        end = self.screen.blit(self.hero.image,self.hero.endPos)
        #判断鼠标是否在图形内
        self.hero.isInHero = end.collidepoint(pygame.mouse.get_pos())
        self.hero.update()

        # 敌人精灵组刷新渲染
        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        #炸弹精灵组刷新渲染
        self.zhadan_group.update()
        self.zhadan_group.draw(self.screen)

        #显示血量字体
        hp1 = self.font.render("Hp:%s" % models.hp, True, (0, 0, 0))
        self.screen.blit(hp1, (0, 35))
        if models.hp == 0:
            self.history.ChangeHistory(self.hero.score)
            game_over()

        # 屏幕更新
        pygame.display.update()


def yx_start():
    #初始化模块
    pygame.init()

    #间隔一定的时间，触发一次创建敌机的事件
    pygame.time.set_timer(ENEMY_CREATE, 500)

    #间隔一定的事件，出发一次创建炸弹的事件
    pygame.time.set_timer(ZHADAN_CREATE,2000)

    #因为我我要用引擎中的属性和方法，所以我创建了一个引擎对象
    engine = GameEngine()

    # 循环
    while True:
        # 每秒刷新多少次
        clock.tick(24)

        #判断移动，如果移动，鼠标在哪，图片的中心就在那
        #engine.hero.endPos = (427,605)
        if engine.hero.isMove:
            engine.hero.endPos = (
                pygame.mouse.get_pos()[0] - 107,
                pygame.mouse.get_pos()[1] - 66)

        #事件检测
        engine.check_event()

        #碰撞检测
        engine.check_collide()

        #屏幕更新
        engine.update_scene()

def jm_start():
    # 初始化
    pygame.init()

    # 设置标题
    pygame.display.set_caption("~~接苹果~~")
    # 设置标题图片
    iconImg=pygame.image.load("./images/pingguo.jpg")
    pygame.display.set_icon(iconImg)
    # 来张背景图片
    img1=pygame.image.load("./images/bg.png")
    # 来张背景图片中的名字图片
    img2=pygame.image.load("./images/hero1 (2).png")
    img2_y=0
    # 来张开始按钮图
    img3=pygame.image.load("./images/ks.jpg")

    # 音乐
    pygame.mixer.music.load("./images/bg1.mp3")
    # 播放音乐，音乐循环
    pygame.mixer.music.play(-1)
    # 是否播放
    musicIsPlay=True

    #因为我要用引擎中的属性和方法，所以我创建了一个引擎对象
    engine1 = GameEngine()

    # 4.循环 显示画面
    while True:
        # 事件监测
        for i  in  pygame.event.get():
            #判断为退出
            if i.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            #判断鼠标按下
            if i.type==pygame.MOUSEBUTTONDOWN:
                # 鼠标左键按下
                if i.button == 1:
                    musicIsPlay= not musicIsPlay
                    #播放
                    if musicIsPlay:
                        pygame.mixer.music.unpause()
                    #暂定
                    else:
                        pygame.mixer.music.pause()
                # 鼠标右键按下
                elif i.button == 3:
                    if 422 < pygame.mouse.get_pos()[0] <646 and 600<pygame.mouse.get_pos()[1]<656:
                        yx_start()

            #键盘按下
            if i.type==pygame.KEYDOWN:
               if  i.key==pygame.K_SPACE:
                   musicIsPlay = not musicIsPlay
                   if musicIsPlay:
                       pygame.mixer.music.unpause()
                   else:
                       pygame.mixer.music.pause()

        # 屏幕绘制图片
        engine1.screen.blit(img1,(0,0))
        engine1.screen.blit(img3,((422,600)))
        if musicIsPlay:
            img2_y += 0.05

        engine1.screen.blit(img2,(148,100+50*math.sin(img2_y)))

        #每帧更新画面
        pygame.display.update()

def game_over():
    # 初始化
    pygame.init()

    # 设置标题
    pygame.display.set_caption("~~接苹果~~")
    # 设置标题图片
    iconImg = pygame.image.load("./images/pingguo.jpg")
    pygame.display.set_icon(iconImg)
    # 来张背景图片
    img1 = pygame.image.load("./images/bg.png")
    # 退出游戏图片
    img2 = pygame.image.load("./images/quit (1).png")
    # 继续游戏图片
    img3 = pygame.image.load("./images/quit (2).png")

    engine2 = GameEngine()

    # 音乐
    pygame.mixer.music.load("./images/阿炳 - 二泉映月.mp3")
    # 音乐循环
    pygame.mixer.music.play(-1)
    # 是否播放
    musicIsPlay = True

    # 4.循环 显示画面
    while True:
        # 事件监测
        for i in pygame.event.get():
            # 判断为  退出
            if i.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # 判断鼠标按下
            if i.type == pygame.MOUSEBUTTONDOWN:
                #按下左键
                if i.button == 1:
                    musicIsPlay = not musicIsPlay
                    if musicIsPlay:
                        pygame.mixer.music.unpause()
                    else:
                        pygame.mixer.music.pause()
                #按下右键
                elif i.button == 3:
                    if 369 < pygame.mouse.get_pos()[0] < 699 and 200 < pygame.mouse.get_pos()[1] < 272:
                        sys.exit()
                    if 366 < pygame.mouse.get_pos()[0] < 702 and 600 < pygame.mouse.get_pos()[1] < 684:
                        models.hp = 20
                        yx_start()
            # 键盘按下
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_SPACE:
                    musicIsPlay = not musicIsPlay
                    if musicIsPlay:
                        pygame.mixer.music.unpause()
                    else:
                        pygame.mixer.music.pause()

        # 屏幕绘制图片
        engine2.screen.blit(img1, (0, 0))
        engine2.screen.blit(img2, (369,200))
        engine2.screen.blit(img3, (366,600))

        # 每帧更新画面

        pygame.display.update()
