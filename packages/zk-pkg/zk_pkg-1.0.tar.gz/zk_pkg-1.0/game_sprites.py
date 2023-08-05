import pygame,data,random,time
class GameSprite(pygame.sprite.Sprite):
    """游戏精灵对象"""
    def __init__(self,img_path,speed=1):
        #调用父类初始化数据
        super().__init__()
        self.image = pygame.image.load(img_path)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        """默认运动方法"""
        self.rect.y += self.speed

    def destroy(self):
        print("飞机销毁")
        #音效
        data.yx.play()
        for image_path in ["./image/enemy2_down1.png","./image/enemy2_down2.png",
                           "./image/enemy2_down3.png","./image/enemy2_down4.png",]:
            self.image = pygame.image.load(image_path)
            time.sleep(0.03)
            data.resources.update()
            data.resources.draw(data.scene)
            data.bullets.update()
            data.bullets.draw(data.scene)
            data.enemys.update()
            data.enemys.draw(data.scene)
            pygame.display.update()
        self.kill()
        data.score += 1


class BackgroundSprite(GameSprite):
    def __init__(self,img_path,prepare = False):
        super().__init__(img_path)
        if prepare:
            self.rect.y = -data.SCREEN_SIZE[1]

    def update(self):
        #调用父类的方法进行运动
        super().update()
        #子类中判断边界
        if self.rect.y > data.SCREEN_SIZE[1]:
            self.rect.y = -data.SCREEN_SIZE[1]

class HeroSprite(GameSprite):
    """英雄精灵对象"""
    def __init__(self,img_path):
        #初始化英雄飞机的图片、速度
        super().__init__(img_path,speed=0)
        #初始化英雄飞机的位置
        self.rect.centerx = data.SCREEN_RECT.centerx
        self.rect.y = data.SCREEN_RECT.centery + 200

        #添加子弹对象到精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):
        #水平边界判断
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= data.SCREEN_RECT.width - self.rect.width:
            self.rect.x = data.SCREEN_RECT.width - self.rect.width
        #垂直边界判断
        if self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.y >= data.SCREEN_RECT.height - self.rect.height:
            self.rect.y = data.SCREEN_RECT.height - self.rect.height

    def fire(self):
        """飞机攻击"""
        # 创建一个子弹对象
        bullet = BulletSprite(self.rect.centerx - 60, self.rect.y)
        # 添加到精灵族对象
        self.bullets.add(bullet)

class BulletSprite(GameSprite):
    """子弹精灵"""
    def __init__(self, x, y):
        super().__init__("./image/bullet_1.png", speed=-8)
        self.rect.x = x
        self.rect.y = y

    def update(self):
        # 调用父类的方法进行操作
        super().update()
        # 边界判断
        if self.rect.y <= -self.rect.height:
            # 子弹从精灵组删除
            self.kill()

    def __del__(self):
        print("子弹对象已经销毁")

class EnemySprite(GameSprite):
    """敌方飞机"""

    def __init__(self):
        # 初始化敌方飞机的数据
        super().__init__("./image/enemy2.png", speed=random.randint(3, 5))
        # 初始化敌方飞机的位置
        self.rect.x = random.randint(0, data.SCREEN_RECT.width - self.rect.width)
        self.rect.y = -self.rect.height
        # 将子弹对象添加到精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):
        # 调用父类的方法直接运动
        super().update()
        # 边界判断
        if self.rect.y > data.SCREEN_RECT.height:
            # 飞机一旦超出屏幕，销毁
            self.kill()

class Bullet_Enemy(GameSprite):
    def __init__(self, x, y):
        super().__init__("./image/bullet2.png", speed=8)
        self.rect.x = x
        self.rect.y = y

    def update(self):
        # 调用父类的方法进行操作
        super().update()
        # 边界判断
        if self.rect.y >= data.SCREEN_SIZE[1]:
            # 子弹从精灵组删除
            self.kill()


