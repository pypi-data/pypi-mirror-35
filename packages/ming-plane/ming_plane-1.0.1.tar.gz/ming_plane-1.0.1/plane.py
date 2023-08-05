#coding:utf-8
"""
用户键盘监听操作
"""

#引入需要的模块
import pygame,random

#定义常量
SCREEN_SIZE = (512, 768)
SCREEN_RECT = pygame.Rect(0, 0, *SCREEN_SIZE)
#初始化混音器
pygame.mixer.init()
#自定义事件
ENEMY_CREATE = pygame.USEREVENT


#游戏精灵对象，用来表示游戏中的各种元素
class GameSprite(pygame.sprite.Sprite):

    def __init__(self, image_path, speed = 1):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.speed = speed

    #默认运动方法
    def update(self):
        self.rect.y += self.speed


#背景精灵
class BackgrounSprite(GameSprite):

    def __init__(self, image_path, next=False):
        super().__init__(image_path)

        if next:
            self.rect.y = -SCREEN_SIZE[1]

    def update(self):
        #调用父类的方法执行运动
        super().update()
        #子类中判断边界
        if self.rect.y > SCREEN_SIZE[1]:
            self.rect.y = -SCREEN_SIZE[1]


#英雄精灵
class HeroSprite(GameSprite):

    def __init__(self):
        super().__init__("./tupian/hero.png", speed = 1)
        #初始化英雄飞机的位置

        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.y = 768

        self.bullets = pygame.sprite.Group()

    def update(self):
        self.rect.y -= 1
        if self.rect.y < 500:
            self.rect.y += 1
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
        #创建一个子弹对象
        bullet = BulletSprite(self.rect.centerx-35 , self.rect.y-75)
        self.bullets.add(bullet)

    # def score(self, score):
    #     self.score = 0



#子弹精灵
class BulletSprite(GameSprite):

    def __init__(self, x, y):
        super().__init__("./tupian/31.png", speed = -10)
        self.rect.x = x
        self.rect.y = y

    def update(self):
        #调用父类的方法进行操作
        super().update()
        #边界处理
        if self.rect.y <= -self.rect.height:
            self.kill()

    def __del__(self):
        print("子弹已经销毁")


#敌机精灵
class EnemySprite(GameSprite):

    def __init__(self):
        #初始化敌机
        super().__init__("./tupian/enemy2.png", speed = random.randint(2,5))

        #初始化敌方飞机位置
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)
        self.rect.y = -self.rect.height


    def update(self):
        #调用父类的方法直接运动
        super().update()
        #边界判断
        if self.rect.y > SCREEN_RECT.height:
            self.kill()

    def fire(self):
        bullet = EnemyBullet(self.rect.centerx - 40, self.rect.y + 70)
        bullets.add(bullet)
        print("敌机发射子弹")

    def __del__(self):
        self.destory()

    def destory(self):
        print("敌机销毁")
         # 展示爆炸效果
        for image_path in ["./tupian/enemy2_down1.png", "./tupian/enemy2_down2.png", "./tipian/enemy2_down3.png", \
                           "./tupian/enemy2_down4.png", "./tupian/enemy2_down1.png", "./tupian/enemy2_down2.png", \
                           "./tupian/enemy2_down3.png", "./tupian/enemy2_down4.png", "./tupian/enemy2_down1.png", \
                           "./tupian/enemy2_down2.png", "./tupian/enemy2_down3.png", "./tupian/enemy2_down4.png", \
                           "./tupian/enemy2_down1.png", "./tupian/enemy2_down2.png", "./tipian/enemy2_down3.png", \
                           "./tupian/enemy2_down4.png", "./tupian/enemy2_down1.png", "./tupian/enemy2_down2.png", \
                           "./tupian/enemy2_down3.png", "./tupian/enemy2_down4.png", "./tupian/enemy2_down1.png", \
                           "./tupian/enemy2_down2.png", "./tupian/enemy2_down3.png", "./tupian/enemy2_down4.png"]:
            self.image = pygame.image.load(image_path)
            screen.blit(self.image, (self.rect.x, self.rect.y))
            pygame.display.update()

        #print("展示爆炸效果")

        # 敌方飞机攻击
        # enemy1 = pygame.image.load("./tupian/enemy2_down1.png")
        # enemy2 = pygame.image.load("./tupian/enemy2_down2.png")
        # enemy3 = pygame.image.load("./tupian/enemy2_down3.png")
        # enemy4 = pygame.image.load("./tupian/enemy2_down4.png")
        # num = 0
        #
        # while True:
        #     print("调用1")
        #
        #     num += 7
        #     if num == 14:
        #         screen.blit(enemy1, (self.rect.x, self.rect.y))
        #         print("调用了第一张图片")
        #     elif num == 21:
        #         screen.blit(enemy2, (self.rect.x, self.rect.y))
        #         print("调用了第二张图片")
        #     elif num == 35:
        #         screen.blit(enemy3, (self.rect.x, self.rect.y))
        #         print("调用了第三章图片")
        #     elif num == 56:
        #         screen.blit(enemy4, (self.rect.x, self.rect.y))
        #         print("爆炸执行了")
        #         pygame.display.update()
        #         break


#敌机子弹精灵组
class EnemyBullet(GameSprite):

    def __init__(self, x, y):
        super().__init__("./tupian/bullet2.png", speed = random.randint(6, 10))
        self.rect.x = x
        self.rect.y = y

    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()

    def __del__(self):
        print("敌机子弹销毁")


#########################################################################
while True:
    #初始化游戏模块
    pygame.init()

    #定义游戏窗口
    screen = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption("飞机大战")

    #定义背景音乐
    pygame.mixer.music.load("./tupian/dangweijun.mp3")
    pygame.mixer.music.play()
    fire = pygame.mixer.Sound("./tupian/hero_fire.wav")

    #定义背景精灵
    bg1 = BackgrounSprite("./tupian/bg_img_4.jpg")
    bg2 = BackgrounSprite("./tupian/bg_img_4.jpg", next = True)

    #定义英雄飞机对象
    hero = HeroSprite()

    #定义死亡背景
    overgame = pygame.image.load("./tupian/bg_logo.jpg")

    #定义精灵组对象
    resources = pygame.sprite.Group(bg1, bg2, hero)

    #定义一个敌机精灵组
    enemys = pygame.sprite.Group()
    #敌机子弹精灵组
    bullets = pygame.sprite.Group()
    #间隔一定的事件，触发一次创建敌机的事件
    pygame.time.set_timer(ENEMY_CREATE, 1000)

    #定义一个时钟
    clock = pygame.time.Clock()


    n = True
    while n is True:

        # 渲染精灵组
        resources.update()
        resources.draw(screen)

        # 定义一种字体
        font = pygame.font.Font("./tupian/MarkerFelt.ttf", 60)
        text_surface = font.render("Aircraft  Battle", True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.topleft = [75, 110]
        screen.blit(text_surface, text_rect)

        font = pygame.font.Font("./tupian/MarkerFelt.ttf", 30)
        text_surface = font.render("Press the space to start the game", True, (230, 230, 230))
        text_rect = text_surface.get_rect()
        text_rect.topleft = [65, 240]
        screen.blit(text_surface, text_rect)

        font = pygame.font.Font("./tupian/MarkerFelt.ttf", 30)
        text_surface = font.render("Press Q to exit the game", True, (230, 230, 230))
        text_rect = text_surface.get_rect()
        text_rect.topleft = [120, 320]
        screen.blit(text_surface, text_rect)

        #屏幕刷新
        pygame.display.update()
        # 监听所有事件
        event_list = pygame.event.get()
        if len(event_list) > 0:
            print(event_list)

            for event in event_list:
                print(event.type, pygame.KEYDOWN)
                # 如果当前事件是QUIT事件
                if event.type == pygame.QUIT:
                    # 卸载所有的pygame模块
                    pygame.quit()
                    exit()

        key_down = pygame.key.get_pressed()
        if key_down[pygame.K_SPACE]:
            print("跳转")
            n = False
            break
        elif key_down[pygame.K_q]:
            pygame.quit()
            print("退出调用了")
            exit()
        else:
            continue

    score = 0
    #游戏场景循环
    while True:

        #定义时钟刷新帧数：每秒让循环运行多少次
        clock.tick(60)
        #监听所有事件
        event_list = pygame.event.get()
        if len(event_list) > 0:
            print(event_list)

            for event in event_list:
                print(event.type, pygame.KEYDOWN, pygame.K_LEFT)
                #如果当前事件是QUIT事件
                if event.type == pygame.QUIT:
                    #卸载所有的pygame模块
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        hero.fire()
                        fire.play()
                        print("哒哒哒", hero.bullets)

                if event.type == ENEMY_CREATE:
                    print("添加一家敌机")
                    enemy = EnemySprite()
                    #添加到敌方飞机精灵组内
                    enemys.add(enemy)
                    enemy.fire()

        #获取当前当前用户键盘上被操纵的按键
        key_down = pygame.key.get_pressed()

        if key_down[pygame.K_LEFT]:
            print("左")
            hero.rect.x -= 5
        if key_down[pygame.K_RIGHT]:
            print("右")
            hero.rect.x += 5
        if key_down[pygame.K_UP]:
            print("上")
            hero.rect.y -= 5
        if key_down[pygame.K_DOWN]:
            print("下")
            hero.rect.y += 5
        # if key_down[pygame.K_SPACE]:
        #     hero.fire()
        #     print("子弹发射", hero.bullets)

        #碰撞检测，子弹与敌机（精灵组与精灵组之间的碰撞）
        f = pygame.sprite.groupcollide(hero.bullets, enemys, True, True)
        #EnemySprite.destory(enemys)
        if len(f) > 0:
            score += 1

        #碰撞检测，敌机与英雄碰撞，（精灵组与精灵碰撞）
        e = pygame.sprite.spritecollide(hero, enemys, True)
        if len(e) > 0:
            hero.kill()
            break

        #子弹与敌机子弹碰撞
        pygame.sprite.groupcollide(hero.bullets, bullets, True, True)

        #敌机子弹与英雄飞机碰撞
        e2 = pygame.sprite.spritecollide(hero, bullets, True)
        if len(e2) > 0:
            hero.kill()
            break

        #渲染精灵组
        resources.update()
        resources.draw(screen)

        #子弹渲染
        hero.bullets.update()
        hero.bullets.draw(screen)

        #敌机渲染
        enemys.update()
        enemys.draw(screen)

        #敌机子弹渲染
        bullets.update()
        bullets.draw(screen)

        # 定义一种字体
        font = pygame.font.Font("./tupian/MarkerFelt.ttf", 30)
        text_surface = font.render("score: %s" %score, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.topleft = [10, 10]
        screen.blit(text_surface, text_rect)

        #屏幕更新
        pygame.display.update()

    n = True
    while n is True:

        # 渲染精灵组
        resources.update()
        resources.draw(screen)

        # 定义一种字体
        font = pygame.font.Font("./tupian/MarkerFelt.ttf", 60)
        text_surface = font.render("game over!", True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.topleft = [120, 150]
        screen.blit(text_surface, text_rect)

        font = pygame.font.Font("./tupian/MarkerFelt.ttf", 23)
        text_surface = font.render("Press the space to return to the start screen", True, (230, 230, 230))
        text_rect = text_surface.get_rect()
        text_rect.topleft = [65, 240]
        screen.blit(text_surface, text_rect)

        font = pygame.font.Font("./tupian/MarkerFelt.ttf", 30)
        text_surface = font.render("Press Q to exit the game", True, (230, 230, 230))
        text_rect = text_surface.get_rect()
        text_rect.topleft = [65, 300]
        screen.blit(text_surface, text_rect)

        font = pygame.font.Font("./tupian/MarkerFelt.ttf", 30)
        text_surface = font.render("Your total score : %s" % score, True, (255, 0, 0))
        text_rect = text_surface.get_rect()
        text_rect.topleft = [65, 400]
        screen.blit(text_surface, text_rect)

        #屏幕刷新
        pygame.display.update()
        # 监听所有事件
        event_list = pygame.event.get()
        if len(event_list) > 0:
            print(event_list)

            for event in event_list:
                print(event.type, pygame.KEYDOWN)
                # 如果当前事件是QUIT事件
                if event.type == pygame.QUIT:
                    # 卸载所有的pygame模块
                    pygame.quit()
                    exit()

        key_down = pygame.key.get_pressed()
        if key_down[pygame.K_SPACE]:
            print("跳转")
            n = False
            break
        elif key_down[pygame.K_q]:
            pygame.quit()
            print("退出调用了")
            exit()
        else:
            continue
    continue
