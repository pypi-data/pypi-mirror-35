import pygame,game_sprites,random,json



class GameEngine:
    def __init__(self):
        # 初始化模块
        pygame.init()
        pygame.mixer.init()
        pygame.mixer.music.load("music.mp3")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)

    # 创建游戏场景
    def __create_scene (self):


        # 添加背景图片
        bg1 = game_sprites.BackGroundSprite("./images/n_bg.jpg")
        bg2 = game_sprites.BackGroundSprite("./images/n_bg.jpg",next = True)
        # 添加英雄飞机图片
        self.hero = game_sprites.HeroSprite("./images/n_hero.png")
        # self.hd = game_sprites.HDSprite("./images/hd.png")
        self.resource = pygame.sprite.Group(bg1,bg2,self.hero)
        # 定义一个敌人飞机的精灵组对象
        self.enemys = pygame.sprite.Group()
        # 间隔一定的事件，触发一次创建敌机的事件
        pygame.time.set_timer(game_sprites.ENEMY_CREATE, random.randint(100, 500))
        # 空投触发事件
        self.kt = pygame.sprite.Group()
        pygame.time.set_timer(game_sprites.KT_CAEATE, 10000)

    # 更新游戏场景
    def __update_scene(self):
        # 循环场景
        clock = pygame.time.Clock()
        while True:

            # if game_sprites.SOURCE >= random.randint(1,100):
            if game_sprites.SOURCE >= 20:
                # self.t = random.randint(1,19)
                self.t = 30
            elif game_sprites.SOURCE >= 50:
                self.t = 60
            else:
                self.t = 24

            clock.tick(self.t)
            # 背景添加渲染到窗口
            self.resource.update()
            self.resource.draw(self.screen)

            self.__check_event()

            # 子弹渲染到窗口

            self.hero.bullets.update()
            self.hero.bullets.draw(self.screen)

            # 敌机渲染到窗口
            self.enemys.update()
            self.enemys.draw(self.screen)

            self.kt.update()
            self.kt.draw(self.screen)

            # 碰撞事件
            self.__check_collide()

            self.GameOver()

            # 显示生命和得分
            self.HP()
            self.source()
            self.ZD()
            self.his()


            # 显示渲染
            pygame.display.update()


    # 显示历史最高分
    def his(self):
        # 读数据
        his_data = json.load(open("source.txt"))
        source = str(his_data)
        gameOverFont = pygame.font.SysFont('Micosoft YaHei', 24)
        gameOverSurf = gameOverFont.render("history highest:" + source, True, (255, 255, 255))
        gameOverRect = gameOverSurf.get_rect()
        gameOverRect.midtop = (80, 620)
        self.screen.blit(gameOverSurf, gameOverRect)
        pygame.display.flip()

    # 显示目前成绩 默认0
    def source(self):
        source = str(game_sprites.SOURCE)
        gameOverFont = pygame.font.SysFont('Micosoft YaHei', 28)
        gameOverSurf = gameOverFont.render("sorce:" + source, True, (0, 255, 0))
        gameOverRect = gameOverSurf.get_rect()
        gameOverRect.midtop = (60, 20)
        self.screen.blit(gameOverSurf, gameOverRect)
        pygame.display.flip()

    # 显示目前血量，默认3
    def HP(self):
        hp = str(game_sprites.a)
        gameOverFont = pygame.font.SysFont('Micosoft YaHei', 28)
        gameOverSurf = gameOverFont.render("HP:" + hp, True, (255, 0, 0))
        gameOverRect = gameOverSurf.get_rect()
        gameOverRect.midtop = (160, 20)
        self.screen.blit(gameOverSurf, gameOverRect)
        pygame.display.flip()

    # 显示当前剩余子弹，默认10  击中敌人+1 ，撞车 +3 ，空投 +3
    def ZD(self):
        hp = str(game_sprites.i)
        gameOverFont = pygame.font.SysFont('Micosoft YaHei', 28)
        gameOverSurf = gameOverFont.render("Residual:" + hp, True, (0, 0, 255))
        gameOverRect = gameOverSurf.get_rect()
        gameOverRect.midtop = (300, 20)
        self.screen.blit(gameOverSurf, gameOverRect)
        pygame.display.flip()



    # 碰撞检测
    def __check_collide(self):
        if len(pygame.sprite.groupcollide(self.hero.bullets, self.enemys, True, True)) > 0:
            # 己方子弹打中敌人 成绩+1
            game_sprites.SOURCE += 1
            # 己方子弹打中敌人 子弹+1
            game_sprites.i += 1
            # 击中音效
            sound = pygame.mixer.Sound('./敌机坠落.wav')
            sound.play()
            sound.set_volume(0.4)

        if len(pygame.sprite.groupcollide(self.hero.bullets, self.kt, True, True)) >0:
            # 己方子弹打中空投 成绩+3 生命之+1
            game_sprites.i += 3
            game_sprites.a += 1
            # 打中空投音效
            so = pygame.mixer.Sound('kt.wav')
            so.play()
            so.set_volume(1)

        e = pygame.sprite.spritecollide(self.hero, self.enemys, True)
        if len(e) > 0:
            print("与敌机相撞，游戏结束")
            # 默认3条命，撞车一次生命减1，子弹+3
            game_sprites.i += 3
            game_sprites.a -= 1
            sound = pygame.mixer.Sound('./撞击.wav')
            sound.play()
            sound.set_volume(0.7)
            # 如果 生命 == 0 执行游戏结束
            if game_sprites.a == 0:
                game_sprites.z = True
                # 显示本局得分
                print(game_sprites.SOURCE)
                # 读数据
                his = json.load(open("source.txt"))
                # 如果此次数据大于历史数据就存入
                if game_sprites.SOURCE > his:
                    # 存数据
                    HISTORY = json.dump(game_sprites.SOURCE, open("source.txt", "w"))

                self.hero.kill()
                # 暂停1秒
                pygame.time.wait(1000)
                # 播放结束音效
                sound = pygame.mixer.Sound('./游戏结束.wav')
                sound.play()
                # sound.set_volume(1)
                self.GameOver()


    # 游戏结束
    def GameOver(self):
        # 生命值 为0 时  结束游戏
        if game_sprites.z == True:
            while True:
                gm_img = pygame.image.load("./images/over.png")
                self.screen.blit(gm_img, (0, 0))
                pygame.display.update()
                even_list = pygame.event.get()
                # 如果列表大于0 打印出来
                if len(even_list) > 0:
                    # print(even_list)  # 打印
                    for even in even_list:
                        if even.type == pygame.QUIT:
                            sound = pygame.mixer.Sound('./退出.wav')
                            sound.play()
                            sound.set_volume(0.5)
                            pygame.time.wait(2000)
                            # 卸载所有模块
                            pygame.quit()
                            # 退出
                            exit()
                            # 按键 == 回车 是 再来一局 并播放音效
                        if even.type == pygame.KEYDOWN:
                            if even.key == pygame.K_RETURN:
                                sound = pygame.mixer.Sound('./再来一局.wav')
                                sound.play()
                                sound.set_volume(0.5)
                                # 把数据初始化，重新进入游戏
                                game_sprites.z = False
                                game_sprites.SOURCE = 0
                                game_sprites.i = 10
                                game_sprites.a = 3
                                self.start()

    # 事件监听
    def __check_event(self):
        even_list = pygame.event.get()
        # 如果列表大于0 打印出来
        if len(even_list) > 0:
            print(even_list)  # 打印
            # 上述条件成立之后，循环列表
            for even in even_list:
                # 如果循环出来的事件类型 == QUIT：
                if even.type == pygame.QUIT:
                    sound = pygame.mixer.Sound('./退出.wav')
                    sound.play()
                    sound.set_volume(0.5)
                    pygame.time.wait(2000)
                    # 卸载所有模块
                    pygame.quit()
                    # 退出
                    exit()
                if even.type == pygame.KEYDOWN:
                    if even.key == pygame.K_SPACE:
                        if game_sprites.i > 0:
                            sound = pygame.mixer.Sound('./开炮.wav')
                            sound.play()
                            sound.set_volume(0.5)
                            self.hero.fire()
                            print("开火")
                            game_sprites.i -= 1
                        else:
                            sound = pygame.mixer.Sound('./没有子弹.wav')
                            sound.play()
                            sound.set_volume(0.5)

                if even.type  == game_sprites.ENEMY_CREATE:
                    print("创建一架敌方飞机.....")
                    enemy = game_sprites.diji(self.screen)
                    # 添加到敌方飞机精灵组中
                    self.enemys.add(enemy)

                if even.type == game_sprites.KT_CAEATE:
                    ktt = game_sprites.KongTou()
                    self.kt.add(ktt)

        # 获取当前用户键盘上被操作的事件
        key_down = pygame.key.get_pressed()
        if key_down[pygame.K_LEFT]:
            print("左《《《《《《《《")
            self.hero.rect.x -= 6
        elif key_down[pygame.K_RIGHT]:
            print("右》》》》》》》》》")
            self.hero.rect.x += 6
        if key_down[pygame.K_UP]:
            print("上^^^^^^^^^^^^^^")
            self.hero.rect.y -= 2
        elif key_down[pygame.K_DOWN]:
            print("下VVVVVVVVVVVVVV")
            self.hero.rect.y += 2


    def begin(self):
        sound = pygame.mixer.Sound('./欢迎.wav')
        sound.play()
        sound.set_volume(0.5)
        # 创建屏幕窗口
        self.screen = pygame.display.set_mode(game_sprites.SCREEN_SIZE)
        st_img = pygame.image.load("./images/start.png")
        self.screen.blit(st_img, (0, 0))
        while True:

            pygame.display.update()

            for even in pygame.event.get():
                # print(even)
                if even.type == pygame.QUIT:
                    sound = pygame.mixer.Sound('./退出.wav')
                    sound.play()
                    sound.set_volume(0.5)
                    pygame.time.wait(2000)
                    # 卸载所有模块
                    pygame.quit()
                    # 退出
                    exit()
                if even.type == pygame.KEYDOWN:
                    if even.key == pygame.K_RETURN:
                        sound = pygame.mixer.Sound('./开始游戏.wav')
                        sound.play()
                        sound.set_volume(0.5)
                        self.start()




################################################
     # 游戏开始函数
    def start(self):
        self.__create_scene()
        self.__update_scene()

################################################
################################################
engine = GameEngine()
engine.begin()