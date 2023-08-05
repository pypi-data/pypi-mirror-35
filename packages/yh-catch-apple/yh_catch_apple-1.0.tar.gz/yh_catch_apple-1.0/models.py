#引入模块
import pygame,random,os

#定义数据
screen_size = (1068,810)
background_rect = pygame.Rect(0,0,*screen_size)
hp = 20

#定义一个游戏精灵
class GameSprite(pygame.sprite.Sprite):

    #游戏精灵的属性
    def __init__(self,image_path,speed):
        # 初始化父类
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.speed = speed
        self.rect = self.image.get_rect()

    #游戏精灵的行为
    def update(self):
        self.rect.y += self.speed


#定义一个背景精灵
class BackGround(GameSprite):

    #初始化所有属性
    def __init__(self,prepare=False):
        #继承父类
        super().__init__("./images/bg.png",speed=2)
        #备用背景
        if prepare == True:
            self.rect.y = -screen_size[1]

    #该游戏精灵移动（更新）的行为
    def update(self):
        #调用父类移动（更新）的行为
        super().update()
        #屏幕循环
        if self.rect.y > screen_size[1]:
            self.rect.y = -screen_size[1]


#定义一个英雄篮子
class HeroSprite(GameSprite):

    #英雄篮子的属性
    def __init__(self):
        #继承父类
        super().__init__("images/hero1 (1).png",speed=0)
        # 位置
        self.rect.centerx = background_rect.centerx
        self.rect.y = background_rect.centery + 200
        self.endPos = (self.rect.centerx,self.rect.y)
        self.isMove = False
        self.isInHero = False
        self.score = 0

    #英雄精灵的行为
    def update(self):

        #super().update()
        self.rect.x = self.endPos[0]
        self.rect.y = self.endPos[1]

        # 边界判断
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= background_rect.width - self.rect.width:
            self.rect.x = background_rect.width - self.rect.width
        if self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.y >= background_rect.height - self.rect.height:
            self.rect.y = background_rect.height - self.rect.height


#定义一个苹果敌人精灵
class EnemySprite(GameSprite):

    #敌人篮子的属性
    def __init__(self):
        #继承父类
        super().__init__("images/hero1 (4).png",speed=random.randint(20,30))
        self.rect.x = random.randint(0, screen_size[0] - self.rect.width)
        self.rect.y = -self.rect.height
        self.hero = HeroSprite()
    #敌人精灵的行为
    def update(self):
        #继承父类
        super().update()
        self.enemy_miss()

    def enemy_miss(self):
        global hp
        if self.rect.y >= screen_size[1]:
            hp -= 1
            print("____%s____" % hp)
            self.kill()


class Zha_danSprite(GameSprite):

    def __init__(self):
        super().__init__("images/无标题副本.png",speed=random.randint(20,30))
        self.rect.x = random.randint(0, screen_size[0] - self.rect.width)
        self.rect.y = -self.rect.height

    # 敌人精灵的行为
    def update(self):
        # 继承父类
        super().update()

    def enemy_miss(self):
        if self.rect.y >= screen_size[1]:
            self.kill()


# 历史最高分存储类
class HistoryScore:
    hisScore = 0
    def __init__(self, path = "history.txt"):
        self.path = path
        # 判断文件是否存在
        if os.path.exists(path):
            with open(path, "r") as f_r:
                HistoryScore.hisScore = f_r.read()
        else:  # 不存在，创建
            with open(path, "w") as f_w:
                f_w.write("0")
    def ChangeHistory(self, score):
        if score > int(HistoryScore.hisScore):
            with open(self.path, "w") as f_w:
                f_w.write(str(score))
    def ReadHistory(self):
        with open(self.path, "r")as f_r:
            HistoryScore.hisScore = f_r.read()

