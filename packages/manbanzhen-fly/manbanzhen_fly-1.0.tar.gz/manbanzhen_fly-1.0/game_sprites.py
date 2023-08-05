import pygame,random



# 定义需要的常量
SCREEN_SIZE = (384,640)
SCREEN_RIGHT = pygame.Rect(0,0,*SCREEN_SIZE)
# 自定义一个事件
ENEMY_CREATE = pygame.USEREVENT
KT_CAEATE = pygame.USEREVENT +1
a = 3
i = 10
z = False
SOURCE = 0



class GameSprite(pygame.sprite.Sprite):

    def __init__(self,image_path,speed=2):
        super().__init__()
        # 添加图片
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.speed = speed
    # 传统移动速度
    def update(self):
        self.rect.y += self.speed

class BackGroundSprite(GameSprite):
    def __init__(self,image_path,next = False):
        super().__init__(image_path)

        if next:
            self.rect.y = -SCREEN_SIZE[1]

    def update(self):
        super().update()
        if self.rect.y > SCREEN_SIZE[1]:
            self.rect.y = -SCREEN_SIZE[1]

class HeroSprite(GameSprite):
    def __init__(self,image_path):
        super().__init__(image_path,speed=0)
        self.rect.centerx = SCREEN_RIGHT.centerx
        self.rect.y = SCREEN_RIGHT.centery+100

        self.bullets = pygame.sprite.Group()

    def update(self):
        # 水平判断 距离边界
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= SCREEN_RIGHT.width - self.rect.width:
            self.rect.x = SCREEN_RIGHT.width - self.rect.width

        # 垂直判断
        if self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.y >= SCREEN_RIGHT.height - self.rect.height:
            self.rect.y = SCREEN_RIGHT.height - self.rect.height

    def fire(self):
        '''飞机攻击'''
        #创建一个子弹
        bullet1 = BulletSprit(self.rect.centerx-12.5,self.rect.y)
        # 添加到精灵组对象
        self.bullets.add(bullet1)

class BulletSprit(GameSprite):
    '''子弹精灵'''
    def __init__(self,x,y):
        super().__init__("./images/bullet2.png",speed = -8)
        self.rect.y = y
        self.rect.x = x
    def update(self):
        # 调用父类操作
        super().update()
        if self.rect.y <= -self.rect.height :
            self.kill()
    def __del__(self):
        print("子弹消失")

class diji(GameSprite):
    '''敌机精灵'''
    def __init__(self,screen):
        self.screen = screen
        q = random.randint(1,4)
        if q == 1:
            super().__init__("./images/n_di.png",speed=random.randint(4,9))
            # self.rect.x = random.randint(0, SCREEN_RIGHT.width - self.rect.width)
            # self.rect.y = 0
            # self.bullets2 = pygame.sprite.Group()
        if q == 2:
            super().__init__("./images/n_di2.png",speed=random.randint(5,12))

        if q == 3:
            super().__init__("./images/enemy33.png",speed=random.randint(12,22))

        if q == 4:
            super().__init__("./images/enemy33.png",speed=random.randint(12,22))

        self.rect.x = random.randint(0,SCREEN_RIGHT.width - self.rect.width)
        self.rect.y = 0
        self.bullets = pygame.sprite.Group()



    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RIGHT.height - self.rect.height:
            self.kill()

    # def Difire(self):
    #     # 创建一个子弹
    #     bullet = DiBulletSprit(self.rect.centerx - 12.5, self.rect.y)
    #     # 添加到精灵组对象
    #     self.bullets.add(bullet)

    def boom(self):
        # img = load_image('explosion1.gif')
        # Explosion.images = [img, pygame.transform.flip(img, 1, 1)]
        img = pygame.image.load("./images/boom.gif")
        self.screen.blit(img, (self.rect.x, self.rect.y))
        pygame.time.wait(10)
        pygame.display.update()

    def __del__(self):
        self.boom()
        pygame.time.wait(10)
        print("敌机损坏")

class KongTou(GameSprite):
    def __init__(self):
        super().__init__("./images/kt.png", speed=random.randint(5,9))
        self.rect.x = random.randint(0, SCREEN_RIGHT.width - self.rect.width)
        self.rect.y = 0
        # self.bullets = pygame.sprite.Group()
    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RIGHT.height - self.rect.height:
            self.kill()
