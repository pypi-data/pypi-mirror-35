# 引入模块
import pygame, random
# 音乐加载
pygame.mixer.init()
# 定义常量
SCREEN_SIZE = (512, 768)
SCREEN_RECT = pygame.Rect(0, 0, *SCREEN_SIZE)
hero_score = 0
boss_score = 200
# 自定义事件
ENEMY_CREATE = pygame.USEREVENT
ENEMY_CREATES = pygame.USEREVENT + 1
BOSS_CREATE = pygame.USEREVENT + 2
# 添加窗口
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
# 创建游戏精灵对象
class GameSprite(pygame.sprite.Sprite):
    def __init__(self, image_path, speed=1):
        super().__init__()
        # 调用图片
        self.image = pygame.image.load(image_path)
        # 获取位置大小信息
        self.rect = self.image.get_rect()
        # 速度
        self.speed = speed

    def update(self):
        # 运动图片的更新
        self.rect.y += self.speed

# boss
class EnemyBase(GameSprite):
    def __init__(self, image_path):
        super().__init__(image_path, speed=0)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.centery =180

    def update(self):
        self.rect.x += random.randint(-1, 1)




# 游戏背景精灵
class BackgroundSprite(GameSprite):
    # 背景加载，父类调用
    def __init__(self,image_path, next=False ):
    # 调用父类初始化函数
        super().__init__(image_path, speed=3)
        if next:
            self.rect.y = -SCREEN_SIZE[1]

    def update(self):
        # 调用父类运动
        super().update()
        # 背景边界判断
        if self.rect.y > SCREEN_SIZE[1]:
            self.rect.y = -SCREEN_SIZE[1]
# 英雄飞机精灵
class HeroSprite(GameSprite):
    def __init__(self, image_path):
        super().__init__(image_path, speed=0)
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.y = SCREEN_RECT.centery + 200
        self.bullets = pygame.sprite.Group()
        self.bullets1 = pygame.sprite.Group()
        self.bullets2 = pygame.sprite.Group()
    # 边界判断
    def update(self):
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= SCREEN_RECT.width - self.rect.width:
            self.rect.x = SCREEN_RECT.width - self.rect.width
        if self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.y >= SCREEN_RECT.height - self.rect.height:
            self.rect.y = SCREEN_RECT.height - self.rect.height

    def shield(self):
        pass
    def fire(self):
        # 创建子弹
        bullet = BulletSprite("./images/zd.png", self.rect.centerx-23, self.rect.y, speed=-35)
        # 添加精灵组对象
        self.bullets.add(bullet)
        shotMusic.play()
# 激光
    def fire1(self):
        # 创建子弹
        bullet = BulletSprite("./images/jg.png", self.rect.centerx - 80, self.rect.y + 50, speed=-80)
        # 添加精灵组对象
        self.bullets1.add(bullet)
        pygame.mixer.music.load("./musics/JG.mp3")
        pygame.mixer.music.play(2)
        #shotMusic1.play()
# 激光
    def fire2(self):
        # 创建子弹
        bullet = BulletSprite("./images/jg.png", self.rect.centerx + 70, self.rect.y + 50, speed=-80)
        # 添加精灵组对象
        self.bullets1.add(bullet)
        # shotMusic1.mixer.musice.play()
    # 大招
    def fires(self):
        # 创建子弹
        bullet = BulletSprite("./images/dz3.png", self.rect.centerx-80, self.rect.centery+50, speed=-5)
        # 添加精灵组对象
        self.bullets2.add(bullet)

    # def fires(self):
    #     # 创建子弹
    #     bullet = BulletSprite("./images/21.png", self.rect.centerx - 100, self.rect.centery + 50, speed=-5)
    #     # 添加精灵组对象
    #     self.bullets.add(bullet)
    # 大招1
    def fires1(self):
        # 创建子弹
        bullet = BulletSprite("./images/21.png", self.rect.centerx - 250, self.rect.centery + 100, speed=-5)
        # 添加精灵组对象
        self.bullets2.add(bullet)
    # 大招2
    def fires2(self):
        # 创建子弹
        bullet = BulletSprite("./images/21.png", self.rect.centerx + 100, self.rect.centery + 100, speed=-5)
        # 添加精灵组对象
        self.bullets2.add(bullet)

# 我方子弹
class BulletSprite(GameSprite):
    def __init__(self, image_path, x, y, speed):
        super().__init__(image_path)  # 不同类类型可以不用空格
        self.speed = speed
        self.rect.x = x
        self.rect.y = y

    # 定义子弹超出边界销毁
    def update(self):
        super().update()
        if self.rect.y < -self.rect.height:
            self.kill()
    # 检测子弹是否销毁
    def __del__(self):
        print("子弹销毁")
# 敌机子弹
class BulletSprite1(GameSprite):
    def __init__(self, image_path,  speed):
        super().__init__(image_path)  # 不同类类型可以不用空格
        self.speed = speed
        # self.rect.x = x
        # self.rect.y = y

    # 定义子弹超出边界销毁
    def update(self):
        super().update()
        if self.rect.y > SCREEN_SIZE[1]+self.rect.height:
            self.kill()
    # 检测子弹是否销毁
    def __del__(self):
        print("敌机子弹销毁")
# 创建敌机
class EnemySprite(GameSprite):
    def __init__(self):
        super().__init__("./images/dj2.png", speed=random.randint(4, 6))
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)
        self.rect.y = -self.rect.height

    # 出界销毁
    def update(self):
        super().update()
        if self.rect.y > SCREEN_RECT.height:
            self.kill()

    def fire(self):
        # 创建子弹
        shots = BulletSprite1("./images/小子弹1.png", speed=random.randint(6, 15))
        shots.rect.x = random.randint(0, SCREEN_RECT.width - shots.rect.width)
        shots.rect.y = -shots.rect.height
        # 添加精灵组对象
        shot.add(shots)
        print("敌机发射子弹")

    # def fire(self):
    #     # 创建子弹
    #     shots = BulletSprite1("./images/小子弹1.png", self.rect.centerx -23, self.rect.y, speed=19)
    #     # 添加精灵组对象
    #     shot.add(shots)
    #     print("敌机发射子弹")

        # 爆炸效果
    def explode(self):
        p1 = pygame.image.load("./images/wsp1.png")
        p2 = pygame.image.load("./images/wsp2.png")
        n = 0
        while True:
            n += 4
            if n ==10:
                screen.blit(p1, (self.rect.x, self.rect.y))
                pygame.display.update()
            elif n == 16:
                screen.blit(p2, (self.rect.x, self.rect.y))
                pygame.display.update()
            elif n == 22:
                screen.blit(p1, (self.rect.x, self.rect.y))
                pygame.display.update()
            elif n == 28:
                screen.blit(p2, (self.rect.x, self.rect.y))
                pygame.display.update()
            elif n == 34:
                screen.blit(p1, (self.rect.x, self.rect.y))
                pygame.display.update()
            elif n == 40:
                screen.blit(p2, (self.rect.x, self.rect.y))
                pygame.display.update()
            elif n == 46:
                screen.blit(p1, (self.rect.x, self.rect.y))
                pygame.display.update()
            elif n == 52:
                screen.blit(p2, (self.rect.x, self.rect.y))
                pygame.display.update()
            elif n == 58:
                screen.blit(p1, (self.rect.x, self.rect.y))
                pygame.display.update()
            elif n == 64:
                screen.blit(p2, (self.rect.x, self.rect.y))
                pygame.display.update()
                break

    def __del__(self):
        print("展示爆炸")
        self.explode()


# 创建背景精灵组
resources = pygame.sprite.Group()
# 添加敌机精灵组
enemys = pygame.sprite.Group()
# 敌机子弹精灵组
shot = pygame.sprite.Group()
# 创建BOSS精灵组
green = pygame.sprite.Group()
# 间隔时间触发创建敌机事件
pygame.time.set_timer(ENEMY_CREATE, 2000)
# 间隔时间触发创建子弹事件
pygame.time.set_timer(ENEMY_CREATES, 1600)
# 间隔事件触发boss事件
pygame.time.set_timer(BOSS_CREATE, 15000)
# 定义时钟对象
clock = pygame.time.Clock()
# # 间隔时间触发创建敌机事件
# pygame.time.set_timer(ENEMY_CREATE, 2000)
# 发射子弹音乐
shotMusic = pygame.mixer.Sound("./musics/bullet.wav")





