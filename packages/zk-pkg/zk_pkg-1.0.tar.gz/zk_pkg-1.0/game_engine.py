#游戏引擎
import game_sprites,pygame,data,time
class GameEngine():
    def __init__(self):
        #定义游戏窗口
        self.scene = pygame.display.set_mode(data.SCREEN_SIZE)
        data.scene = self.scene
        #定义游戏名称
        pygame.display.set_caption("飞机大战")
        #定义时钟
        self.clock = pygame.time.Clock()
        # 间隔一定的时间，触发一次创建敌机的事件
        pygame.time.set_timer(data.ENEMY_CREATE, 2000)
        # 创建一敌机发射子弹的事件
        pygame.time.set_timer(data.ENEMY_ATTACK, 1000)

    def create_scene(self,img_path,img_path2):
        """创建游戏场景"""
        #定义游戏背景精灵
        self.bg1 = game_sprites.BackgroundSprite(img_path)
        self.bg2 = game_sprites.BackgroundSprite(img_path,prepare=True)
        #定义英雄飞机
        self.hero = game_sprites.HeroSprite(img_path2)
        # 定义精灵组对象
        self.resources = pygame.sprite.Group(self.bg1, self.bg2, self.hero)
        #定义一个敌人飞机的精灵组
        self.enemys = pygame.sprite.Group()

    def update_scene(self):
        """更新游戏场景"""
        #精灵组渲染
        self.resources.update()
        self.resources.draw(self.scene)
        data.resources = self.resources
        #英雄子弹精灵组渲染
        self.hero.bullets.update()
        self.hero.bullets.draw(self.scene)
        data.bullets = self.hero.bullets
        #敌机精灵组渲染
        self.enemys.update()
        self.enemys.draw(self.scene)
        data.enemys = self.enemys
        #屏幕更新
        pygame.display.update()

    def check_event(self):
        """监听事件"""
        event_list = pygame.event.get()
        if len(event_list) > 0:
            print(event_list)
            for event in event_list:
                # 如果当前事件是quit事件
                if event.type == pygame.QUIT:
                    # 退出程序
                    pygame.quit()
                    exit()
                elif event.type == data.ENEMY_CREATE:
                    print("创建一个敌机")
                    enemy = game_sprites.EnemySprite()
                    # 添加到敌机精灵组中
                    self.enemys.add(enemy)
                    # c创建一个子弹对象
                    bullets = game_sprites.Bullet_Enemy(enemy.rect.x + 15, enemy.rect.y)
                    # 将子弹对象添加到敌机精灵组中
                    self.enemys.add(bullets)

                elif event.type == data.ENEMY_ATTACK:
                    print("敌机发射子弹")
        # 获取当前用户键盘上被操作的按键
        key_down = pygame.key.get_pressed()
        if key_down[pygame.K_LEFT]:
            print("向左运动<<<<<<")
            self.hero.rect.x -= 5
        elif key_down[pygame.K_RIGHT]:
            print("向右运动>>>>>>")
            self.hero.rect.x += 5
        elif key_down[pygame.K_UP]:
            print("向上运动^^^^^^")
            self.hero.rect.y -= 5
        elif key_down[pygame.K_DOWN]:
            print("向下运动>>>>>>")
            self.hero.rect.y += 5
        elif key_down[pygame.K_SPACE]:
            self.hero.fire()
            print("发射子弹", self.hero.bullets)

    def check_collide(self):
        # 碰撞检测:子弹和敌机之间的碰撞
        bol = pygame.sprite.groupcollide(self.enemys, self.hero.bullets, False, True)
        for i in bol:
            i.destroy()

        # 碰撞检测：英雄飞机和敌方飞机之间的碰撞
        e = pygame.sprite.spritecollide(self.hero, self.enemys, True)
        if len(e) > 0:
            self.hero.destroy()
            print("Game Over")
            pygame.quit()
            exit()

    def start(self):
        """游戏开始"""
        #开场图片
        self.scene = pygame.display.set_mode(data.SCREEN_SIZE)
        flag = False
        while True:
            # 添加一个背景图片
            self.background_image = game_sprites.BackgroundSprite("./image/kc.jpg")
            #将背景图片放到精灵组
            self.resp = pygame.sprite.Group(self.background_image)
            #设置监听
            event_list = pygame.event.get()
            if len(event_list) > 0:
                print(event_list)
                for event in event_list:
                    # 如果当前事件是quit事件
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            flag = True
            # 将背景图片渲染到窗口中展示
            if flag:
                break

            self.resp.update()
            self.resp.draw(self.scene)
            pygame.display.update()
        #初始化游戏数据
        pygame.init()
        # 创建场景
        self.create_scene("./image/bg_img_3.jpg","./image/hero_18.png")
        score = 0
        while True:
            # 定义时钟刷新帧：每秒让循环运行多少次
            self.clock.tick(50)
            #监听事件
            self.check_event()
            #碰撞检测
            self.check_collide()
            if data.score >= 20:
                break
            #更新场景
            self.update_scene()

        #清空精灵组
        self.resources.empty()
        self.hero.bullets.empty()
        self.enemys.empty()
        #初始化所有模块
        super().__init__()
        pygame.init()
        #创建游戏场景
        self.create_scene("./image/bg_img_4.jpg","./image/hero.png")
        #游戏循环
        while True:
            self.clock.tick(50)
            #监听事件
            self.check_event()
            #碰撞检测
            self.check_collide()
            #渲染展示
            self.update_scene()


