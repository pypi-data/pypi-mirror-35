
import time
import pygame
import sys
import math
import random
import os

# 正常开发
pygame.init()
SCREEN_SIZE = (512, 768)
SCREEN_RECT = pygame.Rect(0,0,*SCREEN_SIZE)
# 将生成的敌人存放在列表当中
enemyList = []
# 补给品列表
goodsList=[]
# 子弹列表
bulletList = []

class GameSprite(pygame.sprite.Sprite):
    """所有类的基类"""
    def __init__(self,image_name,pos,screen,speed):
        super().__init__()
        self.screen = screen
        self.image = image_name
        self.rect = self.image.get_rect()
        self.x, self.y = pos
        self.speed = speed

    def move(self):
        '''通用移动方法'''
        self.rect.y += self.speed
class GameBG:
    '''背景类'''
    # 鼠标是否在暂停按钮范围内
    isInSide = False
    def __init__(self, img, screen, speed=1, pos=(0, 0)):
        self.screen = screen
        self.img1 = img
        self.img1Rect = self.img1.get_rect()
        self.img1Rect.x, self.img1Rect.y = pos
        self.img2 = self.img1.copy()
        self.img2Rect = self.img2.get_rect()
        self.img2Rect.x, self.img2Rect.y = (0, -self.img2Rect.h)
        self.speed = speed

    def display(self):
        # 调用rect的move方法
        self.img1Rect = self.img1Rect.move(0, self.speed)
        self.img2Rect = self.img2Rect.move(0, self.speed)
        # 两张背景图的位置
        if self.img1Rect.y >= SCREEN_RECT.height:
            self.img1Rect.y = -SCREEN_RECT.height
        if self.img2Rect.y >= SCREEN_RECT.height:
            self.img2Rect.y = -SCREEN_RECT.height
        # 渲染两张背景图
        self.screen.blit(self.img1, self.img1Rect)
        self.screen.blit(self.img2, self.img2Rect)
        # 渲染暂停按钮
        if isPause == False:
            GameBG.isInSide = self.screen.blit(playpauseImage[0], (430, 0)).collidepoint(pygame.mouse.get_pos())
        else:
            GameBG.isInSide = self.screen.blit(playpauseImage[1], (430, 0)).collidepoint(pygame.mouse.get_pos())


heroImages = [pygame.image.load("./image/hero1.png"),
              pygame.image.load("./image/hero2.png")]

class Hero(GameSprite):
    '''英雄类'''
    up = False
    down = False
    left = False
    right = False
    # 游戏得分
    score = 0
    # 游戏子弹数量
    bulletCount = 0
    # 全屏炸弹数量
    bombCount = 0
    # buff持有的时间
    buffNum = 0
    # 是否存活
    isLife = True
    # 无敌时间
    invincibleTime = False

    def __init__(self, image_name,heroImages, screen, pos, hp,speed):
        super().__init__(image_name,pos,screen,speed)
        self.heroImages = heroImages
        self.image = self.heroImages[0]
        self.rect = self.heroImages[0].get_rect()
        self.rect.x,self.rect.y = pos
        self.hp = hp
        self.mask = pygame.mask.from_surface(self.image)

        # 调整英雄出场的位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.y = SCREEN_RECT.centery + 200
        # 英雄移动索引变量
        self.index = 0
        # 英雄图片索引
        self.imgIndex = 0

    def move(self):
        # 判断英雄移动
        if Hero.up:
            self.rect = self.rect.move(0, -self.speed)
        elif Hero.down:
            self.rect = self.rect.move(0, self.speed)
        elif Hero.left:
            self.rect = self.rect.move(-self.speed, 0)
        elif Hero.right:
            self.rect = self.rect.move(self.speed, 0)

        # 约束移动位置
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > self.screen.get_width() - self.image.get_width():
            self.rect.x = self.screen.get_width() - self.image.get_width()
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > self.screen.get_height() - self.image.get_height():
            self.rect.y = self.screen.get_height() - self.image.get_height()

    def autofire(self):
        # 发射子弹
        if isPause == False:
            self.index += 1
            # 调整子弹的生成速度，10帧发射一颗子弹
            if self.index % 10 == 0:
                # 没有得到补给品的情况下
                if self.buffNum == 0:
                    # 判断是会为自动发射
                    if isAutoShoot:
                        # 创建子弹对象
                        Bullet(bulletImage[0], (hero.rect.centerx-10,hero.rect.y),screen, -10)
                # 得到补给品
                if 0 < self.buffNum <= 200:
                    if self.bulletCount >= 1 and isAutoShoot:
                        Bullet(bulletImage[1], (hero.rect.centerx-30,hero.rect.y), screen, -8)
                        Bullet(bulletImage[2], (hero.rect.centerx+30,hero.rect.y), screen, -8)
                        self.buffNum -= 2
                        print("buff时间剩余：%s"% self.buffNum)
                elif self.buffNum > 200:
                    if self.bulletCount >= 2 and isAutoShoot:
                        Bullet(bulletImage[0], (hero.rect.centerx,hero.rect.y),
                               screen, -8)
                        Bullet(bulletImage[1], (hero.rect.centerx-30,hero.rect.y), screen, -8)
                        Bullet(bulletImage[2], (hero.rect.centerx+30,hero.rect.y), screen, -8)
                        self.buffNum -= 2
                        print("buff时间剩余：%s"% self.buffNum)

            # 创建完成子弹对象之后让子弹移动
            for i in bulletList:
                i.move()

        # 边移动，边检测碰撞
        if self.isLife == True:
            self.collideEnemy()
            self.collideGoods()

        # 判断英雄血量，是否能继续游戏
        if self.hp <= 0:
            # 播放音效
            Sound.play(soundList[6])
            BGM.pause()

            self.buffNum = 0
            hero.bombCount = 0
            Hero.isLife = False
            self.invincibleTime = 0
            historyScore.changeHistory(self.score)

        else:
            # 子弹图片索引重新规整
            if self.imgIndex == 2:
                self.imgIndex = 0

            # 渲染无敌的图片
            if self.invincibleTime :
                self.screen.blit(shieldImage, (hero.rect.centerx-75, hero.rect.top-30))

        self.screen.blit(self.heroImages[self.imgIndex], self.rect)

    def collideEnemy(self, enemys=enemyList):
        '''英雄碰撞敌机'''
        obj = pygame.sprite.spritecollideany(self, enemys, collided=pygame.sprite.collide_mask)
        if obj in enemyList and obj.state == True and self.invincibleTime == False:
            # 判断敌机型号
            if obj.tag == 1:
                obj.hp = 0
                if self.invincibleTime == 0:
                    self.hp -= 1
            elif obj.tag == 2:
                obj.hp = 0
                if self.invincibleTime == 0:
                    self.hp -= 2
            elif obj.tag == 3:
                obj.hp = 0
                if self.invincibleTime == 0:
                    self.hp -= 5

            if self.buffNum > 200:
                self.buffNum -= 200

            # 增加无敌时间
            self.invincibleTime = True
            # 添加英雄无敌事件
            INVINCIBLETIME = pygame.USEREVENT+3
            # 设置三秒时间
            pygame.time.set_timer(INVINCIBLETIME,3000)

    def collideGoods(self, goods=goodsList):
        obj = pygame.sprite.spritecollideany(self, goods, collided=pygame.sprite.collide_mask)
        if obj in goodsList:
            if obj.tag == "bullet":
                self.bulletCount += 1
                self.buffNum += 200
                Sound.play(soundList[2])
                goodsList.remove(obj)
            elif obj.tag == "bomb":
                self.bombCount += 1
                Sound.play(soundList[3])
                goodsList.remove(obj)
            else:
                self.hp += 1
                Sound.play(soundList[5])
                goodsList.remove(obj)

# 子弹图片
bulletImage = [pygame.image.load("./image/bullet.png"),
               pygame.image.load("./image/bullet1.png"),
               pygame.image.load("./image/bullet2.png")]

# 子弹类
class Bullet(GameSprite):
    '''子弹类'''
    def __init__(self, image, pos, screen, speed, attackNum=1):
        super().__init__(image,pos,screen,speed)
        self.attackNum = attackNum
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos
        # 将发射出去的子弹存入子弹列表当中
        bulletList.append(self)
        # 播放背景音乐
        Sound.play(soundList[1])
        # 子弹索引
        self.suo = 0

    def move(self):
        '''子弹移动的方法'''
        # 郑玄函数索引
        self.suo += 1
        self.rect.y += self.speed
        # self.rect.x += 30*math.sin(self.suo)
        self.screen.blit(self.image, self.rect)
        # 子弹发射出范围后删除
        if self.rect.y > SCREEN_RECT.height:
            bulletList.remove(self)
        # 子弹移动中调用检测是否碰撞敌人方法
        self.collideEnemy()

    def display(self):
        '''渲染子弹'''
        self.screen.blit(self.image, self.rect)

    def collideEnemy(self, enemys=enemyList):
        # 精灵一对多方法，返回一个精灵对象
        obj = pygame.sprite.spritecollideany(self, enemys, collided=pygame.sprite.collide_mask)
        if isinstance(obj, Enemy):
            obj.hp -= 1
            if isinstance(self, Bullet) and self in bulletList:
                bulletList.remove(self)

# 敌人图片
enemy0Images = [pygame.image.load("./image/enemy0.png"),
                pygame.image.load("./image/enemy0_down1.png"),
                pygame.image.load("./image/enemy0_down2.png"),
                pygame.image.load("./image/enemy0_down3.png"),
                pygame.image.load("./image/enemy0_down4.png")]
enemy1Images = [pygame.image.load("./image/enemy1.png"),
                pygame.image.load("./image/enemy1_down1.png"),
                pygame.image.load("./image/enemy1_down2.png"),
                pygame.image.load("./image/enemy1_down3.png"),
                pygame.image.load("./image/enemy1_down4.png"),
                pygame.image.load("./image/enemy1_hit.png")]
enemy2Images = [pygame.image.load("./image/enemy2.png"),
                pygame.image.load("./image/enemy2_down1.png"),
                pygame.image.load("./image/enemy2_down2.png"),
                pygame.image.load("./image/enemy2_down3.png"),
                pygame.image.load("./image/enemy2_down4.png"),
                pygame.image.load("./image/enemy2_down5.png"),
                pygame.image.load("./image/enemy2_down6.png"),
                pygame.image.load("./image/enemy2_hit.png")]

class Enemy(GameSprite):
    '''敌机类'''
    def __init__(self, iamge_name,imgs,screen, pos, hp, speed, tag):
        super().__init__(iamge_name,pos,screen,speed)
        self.imgs = imgs
        self.image = imgs[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = pos
        self.hp = hp
        self.speed = speed
        self.tag = tag

        # 敌人状态 True为活着，False为死亡
        self.state = True
        # 产生的敌人加入到敌人列表
        enemyList.append(self)

        # 死亡帧频索引
        self.index = 0
        # 死亡图片索引
        self.imageIndex = 0
    @staticmethod
    def creatEnemy():
        # 根据难度生成敌机
        # 10分之内只生成小飞机

        if hero.hp :
            # 玩家分数小于10分时，只生成小飞机
            if hero.score <= 10:
                ranWidth = random.randint(0, (screen.get_width() - enemy0Images[0].get_width()))
                Enemy(enemy0Images[0], enemy0Images, screen, (ranWidth, -enemy0Images[0].get_height()), 1, 10, 1)
            # 玩家分数大于10分时，生成中飞机
            elif hero.score > 10 and hero.score <= 30:
                ranNum = random.randint(1, 900)
                # 随机生成小飞机
                if ranNum <= 600:
                    ranWidth = random.randint(0, (screen.get_width() - enemy0Images[0].get_width()))
                    Enemy(enemy0Images[0], enemy0Images, screen, (ranWidth, -enemy0Images[0].get_height()), 1, 10, 1)
                # 随机生成中飞机
                elif ranNum <= 800:
                    ranWidth = random.randint(0, (screen.get_width() - enemy1Images[0].get_width()))
                    Enemy(enemy1Images[0], enemy1Images, screen, (ranWidth, -enemy1Images[0].get_height()), 3, 6, 2)
                # 随机生成小飞机
            # 玩家分数大于30分时，生成大飞机
            elif hero.score >= 30:
                ranNum = random.randint(1, 1000)
                if ranNum <= 700:
                    ranWidth = random.randint(0, (screen.get_width() - enemy0Images[0].get_width()))
                    Enemy(enemy0Images[0], enemy0Images, screen, (ranWidth, -enemy0Images[0].get_height()), 1, 10, 1)
                # 随机生成中飞机
                elif ranNum <= 950:
                    ranWidth = random.randint(0, (screen.get_width() - enemy1Images[0].get_width()))
                    Enemy(enemy1Images[0], enemy1Images, screen, (ranWidth, -enemy1Images[0].get_height()), 3, 6, 2)
                # 随机生成大飞机
                else:
                    ranWidth = random.randint(0, (screen.get_width() - enemy2Images[0].get_width()))
                    Enemy(enemy2Images[0], enemy2Images, screen, (ranWidth, -enemy2Images[0].get_height()), 10, 2, 3)

    @staticmethod
    def allEnemyMove():
        for i in enemyList:
            if isinstance(i, Enemy):
                i.move()

    def move(self):
        self.rect = self.rect.move(0, self.speed)
        # 敌人移出屏幕范围死亡
        if self.rect.y >= 750:
            enemyList.remove(self)
        # 判断敌人血量，调用死亡方法
        if self.hp <= 0:
            self.state = False
            self.dead()
        else:
            # 渲染存活画面
            self.screen.blit(self.image, self.rect)

    def dead(self):
        # 执行敌人死亡动画
        self.index += 1
        if self.index % 3 == 0: # 每3帧更新一次
            if self.tag == 1:
                self.imageIndex += 1
                if self.imageIndex == 4:
                    if self in enemyList:
                        Hero.score += 1
                        enemyList.remove(self)
            elif self.tag == 2:
                self.imageIndex += 1
                if self.imageIndex == 4:
                    if self in enemyList:
                        Hero.score += 5
                        enemyList.remove(self)
            elif self.tag == 3:
                self.imageIndex += 1
                if self.imageIndex == 6:
                    if self in enemyList:
                        Hero.score += 10
                        enemyList.remove(self)
        # 渲染死亡画面
        self.screen.blit(self.imgs[self.imageIndex], self.rect)
        # 生命状态
        self.state = False

# 开始界面所有图片
StartImage = [
              pygame.image.load("./image/load.jpg"),
              pygame.image.load("./image/LOGO.png"),
              pygame.image.load("./image/kaishi.jpg"),
              pygame.image.load("./image/bg.png")
                ]

# 开始界面图片类
class StartInterface:
    # 鼠标是否在开始按钮区域
    isInside = False
    def __init__(self, StartImage, screen):
        self.bgImage = StartImage[0]
        self.nameImage = StartImage[1]
        self.startImage = StartImage[2]
        self.screen = screen

        # 名字图片运动变量
        self.index = 0
    def display(self):
        # 游戏开始界面
        # 背景图片
        screen.blit(self.bgImage, (0, 0))
        # 游戏名字动图
        self.index += 0.09
        screen.blit(self.nameImage, (50, 100+40*math.sin(self.index)))
        # 开始游戏按钮图片
        buttonRect = screen.blit(self.startImage, (160, 480))
        StartInterface.isInside = buttonRect.collidepoint(pygame.mouse.get_pos())

# 历史最高分类
class HistoryScore:
    hisScore = 0
    def __init__(self, path = "./history.txt"):
        self.path = path
        # 判断文件是否存在
        if os.path.exists(path):
            with open(path, "r") as f_r:
                HistoryScore.hisScore = f_r.read()
        else:  # 不存在，创建
            with open(path, "w") as f_w:
                f_w.write("0")
    def changeHistory(self, score):
        if score > int(HistoryScore.hisScore):
            with open(self.path, "w") as f_w:
                f_w.write(str(score))
    def readHistory(self):
        with open(self.path, "r")as f_r:
            HistoryScore.hisScore = f_r.read()

goodsImage= [pygame.image.load("./image/prop_type_0.png"),
             pygame.image.load("./image/prop_type_1.png"),
             pygame.image.load("./image/plane.png")]

# 补给品类
class Goods:
    def __init__(self, image, screen, pos, speed, tag):
        self.image = image
        self.rect = self.image.get_rect()
        self.screen = screen
        self.rect.topleft = pos
        self.speed = speed
        self.tag = tag
        goodsList.append(self)

    def move(self):
        self.rect = self.rect.move(0, self.speed)
        self.screen.blit(self.image, self.rect)
        # 物资移出屏幕范围消失
        if self.rect.y >= 750:
            goodsList.remove(self)
    @staticmethod
    def creatGoods():
        ranNum = random.randint(1, 1000)
        # 随机生成物资
        if ranNum <= 100:
            ranWidth = random.randint(0, (screen.get_width() - goodsImage[2].get_width()))
            Goods(goodsImage[2], screen, (ranWidth, -goodsImage[2].get_height()), 10, "plane")
        elif ranNum <= 650:
            ranWidth = random.randint(0, (screen.get_width() - goodsImage[0].get_width()))
            Goods(goodsImage[0], screen, (ranWidth, -goodsImage[0].get_height()), 8, "bullet")
        else:
            ranWidth = random.randint(0, (screen.get_width() - goodsImage[1].get_width()))
            Goods(goodsImage[1], screen, (ranWidth, -goodsImage[1].get_height()), 8, "bomb")
    @staticmethod
    def goodsmanager():
        for i in goodsList:
            i.move()
# 开始界面背景音乐
pygame.mixer.init()
bgmList = [pygame.mixer.music.load("./sound/纯音乐-太阳的眼睛.mp3")]
# 背景音乐类
class BGM:
    @staticmethod
    def play():
        pygame.mixer.music.play(2)
    @staticmethod
    def pause():
        pygame.mixer.music.pause()

# 音效
soundList = [pygame.mixer.Sound("./sound/button.ogg"),
             pygame.mixer.Sound("./sound/bullet.wav"),
             pygame.mixer.Sound("./sound/get_double_laser.ogg"),
             pygame.mixer.Sound("./sound/get_bomb.ogg"),
             pygame.mixer.Sound("./sound/use_bomb.ogg"),
             pygame.mixer.Sound("./sound/plane.wav"),
             pygame.mixer.Sound("./sound/game_over.ogg")]
# 背景音效类
class Sound:
    @staticmethod
    def play(sound):
        sound.play()

# 主程序
pygame.init()
pygame.display.init()
# 设置窗口大小
screen = pygame.display.set_mode(SCREEN_SIZE)
# 设置游戏标题名字
pygame.display.set_caption("~飞机大战~")
# 背景音乐播放
BGM.play()
# 开始界面对象
startInterface = StartInterface(StartImage, screen)
# 游戏界面暂停与播放图片
playpauseImage = [pygame.image.load("./image/game_pause_nor.png"),
                  pygame.image.load("./image/game_resume_nor.png")]
# 游戏背景图片
gameBG = pygame.image.load("./image/bg2.jpg")

# 死亡后背景图片
die = pygame.image.load("./image/load.jpg")

# 重新开始图片
restart = pygame.image.load("./image/restart_nor.png")

# 退出游戏图片
quitgame = pygame.image.load("./image/quit_nor.png")

# 保护盾图片
shield = pygame.image.load("./image/shield.png")
shieldImage = pygame.transform.scale(shield, (150, 150))

# 英雄对象
hero = Hero(heroImages[0],heroImages, screen, (200, 500), 5, 8)

# 游戏背景对象
bg = GameBG(gameBG, screen, 3)

# 炸弹图片
bombImage = pygame.image.load("./image/bomb.png")

# 英雄血量图片
heartImage = pygame.image.load("./image/heart2.png")

# 历史最高分对象
historyScore = HistoryScore()

# 设置计时器,产生敌人
pygame.time.set_timer(pygame.USEREVENT+1, 1000)

# 设置计时器,产生物资
pygame.time.set_timer(pygame.USEREVENT+2, 8000)

# 产生字体对象
font = pygame.font.Font("./font/MarkerFelt.ttf", 30)

# 声明时间
clock = pygame.time.Clock()


# 是否自动射击
isAutoShoot = True

# 是否开始游戏
isPlay = False

# 是否暂停游戏
isPause = False

# 检测事件
def EventDection():
    global isPlay
    global isPause
    global isAutoShoot
    for event in pygame.event.get():
        # 检测退出事件
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # 时间计时器检测产生敌人
        if event.type == pygame.USEREVENT+1 and isPause == False:
            Enemy.creatEnemy()
        # 时间计时器检测产生物资
        if event.type == pygame.USEREVENT+2 and isPause == False:
            Goods.creatGoods()
        # 检测英雄无敌时间
        if event.type == pygame.USEREVENT+3 and isPause == False:
            hero.invincibleTime = False
        # 检测鼠标事件
        if event.type == pygame.MOUSEBUTTONDOWN:
            # 开始游戏
            if event.button == 1 and StartInterface.isInside and isPlay == False:
                Sound.play(soundList[0])
                BGM.play()
                hero.hp = 5
                Hero.score = 0
                hero.imgIndex = 0
                historyScore.readHistory()
                goodsList.clear()
                enemyList.clear()
                bulletList.clear()
                isPlay = True
            # 检测是否重新开始游戏
            if event.button == 1 and Hero.isLife == False and GameBG.isInSide1:
                Sound.play(soundList[0])
                BGM.play()
                hero.hp = 5
                Hero.score = 0
                hero.imgIndex = 0
                historyScore.readHistory()
                goodsList.clear()
                enemyList.clear()
                bulletList.clear()
                isPlay = True
                Hero.isLife = True
                main()
            # 检测是否退出游戏
            if event.button == 1 and Hero.isLife == False and GameBG.isInSide:
                pygame.quit()
                sys.exit()
            # 检测是否暂停游戏
            if event.button == 1 and isPlay == True and GameBG.isInSide:

                isPause = not isPause
                if isPause:
                    hero.speed=0
                    bg.speed=0
                    BGM.pause()
                    for i in enemyList:
                        i.speed = 0
                    for j in goodsList:
                        j.speed = 0
                    Sound.play(soundList[0])
                else:
                    BGM.play()
                    hero.speed = 10
                    bg.speed = 3
                    for i in enemyList:
                        if i.tag == 1:
                            i.speed = 10
                        elif i.tag == 2:
                            i.speed = 6
                        elif i.tag == 3:
                            i.speed = 2
                    for j in goodsList:
                        j.speed = 8
                    Sound.play(soundList[0])
            # 检测是否自动射击
            if event.button == 3:
                isAutoShoot = not isAutoShoot
        # 检测键盘事件
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_ESCAPE:
                Sound.play(soundList[0])
                isPlay = False
                Hero.score = 0
            # 按q键全屏爆炸
            if event.key == pygame.K_q:
                if hero.bombCount != 0:
                    hero.bombCount -= 1
                    Sound.play(soundList[4])
                    for i in enemyList:
                        i.hp = 0
        # 英雄移动操作
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                Hero.up = True
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                Hero.down = True
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                Hero.left = True
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                Hero.right = True
        # 松开键盘，英雄不移动
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                Hero.up = False
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                Hero.down = False
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                Hero.left = False
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                Hero.right = False
# 主函数
def main():
    while True:
        EventDection()
        # 游戏界面
        if isPlay and Hero.isLife:
            bg.display()
            Enemy.allEnemyMove()
            Goods.goodsmanager()
            hero.move()
            hero.autofire()
            # 渲染血量图片
            for i in range(0, hero.hp):
                screen.blit(heartImage, (30 * i + 100, 10))
            # 显示血量字体
            bloodFont = font.render("    Hp  :", True, (0, 0, 0))
            screen.blit(bloodFont, (0, 5))
            # 显示分数字体
            scoreFont = font.render(" Score :%s" % Hero.score, True, (0, 0, 0))
            screen.blit(scoreFont, (0, 35))
            # 显示历史分数字体
            historyFont = font.render("History:%s" % historyScore.hisScore, True, (0, 0, 0))
            screen.blit(historyFont, (0, 65))
            # 显示炸弹字体
            bombFont = font.render(" X :%s" % hero.bombCount, True, (0, 0, 0))
            screen.blit(bombFont, (65, 720 - 40))
            # 渲染炸弹图片
            screen.blit(bombImage, (0, 720 - 53))
        elif Hero.isLife == False:

            # 渲染死亡画面，游戏结束
            screen.blit(die, (0, 0))
            GameBG.isInSide1 = screen.blit(restart, (200, 200)).collidepoint(pygame.mouse.get_pos())
            GameBG.isInSide = screen.blit(quitgame, (200, 400)).collidepoint(pygame.mouse.get_pos())
        else:
            # 开始界面
            startInterface.display()
        # 更新界面
        pygame.display.update()
        # 设置帧频速率
        clock.tick(60)

if __name__ == "__main__":
    main()