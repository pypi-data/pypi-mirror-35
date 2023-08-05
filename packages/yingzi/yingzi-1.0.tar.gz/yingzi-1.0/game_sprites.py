#coding:utf-8
import pygame,random
pygame.mixer.init()
pygame.font.init()
#定义常量
SCREEN_SIZE=(512,768)
SCREEN_RECT=pygame.Rect(0,0,*SCREEN_SIZE)

#定义游戏窗口
screen=pygame.display.set_mode(SCREEN_SIZE)

#游戏窗口设置标题
pygame.display.set_caption('飞机大战')

#自定义事件
ENEMY_CREATE=pygame.USEREVENT
BOSS_CREATE=pygame.USEREVENT+1
MID_CREATE=pygame.USEREVENT+2

#定义一个时钟对象
clock=pygame.time.Clock()

#定义游戏精灵
class GameSprite(pygame.sprite.Sprite):
    def __init__(self,image_path,speed=1):
        super().__init__()
        self.image=pygame.image.load(image_path)
        self.rect=self.image.get_rect()
        self.speed=speed
    def update(self):
        self.rect.y+=self.speed


#定义背景精灵
class BackgroundSprite(GameSprite):
    def __init__(self,image_path,prepare=False):
        super().__init__(image_path,speed=2)
        if prepare:
            self.rect.y=-SCREEN_SIZE[1]
    def update(self):
        super().update()
        if self.rect.y>SCREEN_SIZE[1]:
            self.rect.y=-SCREEN_SIZE[1]

#定义英雄精灵
class HeroSprite(GameSprite):
    def __init__(self):
        super().__init__("./image/img_2.png",speed=0)
        #初始化飞机位置
        self.rect.centerx=SCREEN_RECT.centerx
        self.rect.y=SCREEN_RECT.centery+200
        self.bullets=pygame.sprite.Group()
        self.blood=3
    def update(self):
        #水平边界判断
        if self.rect.x<=0:
            self.rect.x=0
        elif self.rect.x>=SCREEN_RECT.width-self.rect.width:
            self.rect.x=SCREEN_RECT.width-self.rect.width
        #垂直边界判断
        if self.rect.y<=0:
            self.rect.y=0
        elif self.rect.y>=SCREEN_RECT.height-self.rect.height:
            self.rect.y = SCREEN_RECT.height - self.rect.height

    def fire(self):
        #创建子弹对象
        bullet=BulletSprite(self.rect.centerx-6,self.rect.y,speed=-20)
        #将子弹加到精灵族对象
        self.bullets.add(bullet)
        #开火音乐
        bullet_fire.play()

#定义子弹精灵对象
class BulletSprite(GameSprite):
    def __init__(self,x,y,speed):
        super().__init__("./image/37.png")
        self.rect.x=x
        self.rect.y=y
        self.speed = speed

    def update(self):
        super().update()
        #边界判断
        if self.rect.y<=-768:
            self.kill()

    def __del__(self):
        print("子弹已经销毁")


#定义敌方飞机
class EnemySprite(GameSprite):
    def __init__(self):
        super().__init__("./image/enemy2.png",speed=random.randint(3,5))
        #初始化敌方飞机位置
        self.rect.x=random.randint(0,SCREEN_RECT.width-self.rect.width)
        self.rect.y=-self.rect.height

    def update(self):
        super().update()
        #边界判断
        if self.rect.y > SCREEN_RECT.height:
            self.kill()

    def boom(self):
        boom1=pygame.image.load("./image/boom1.png")
        boom2=pygame.image.load("./image/boom2.png")
        boom3=pygame.image.load("./image/boom3.png")
        boom4=pygame.image.load("./image/boom4.png")

        num=0
        while True:

            num+=4
            if num==12:
                screen.blit(boom1,(self.rect.x,self.rect.y))
            elif num==20:
                screen.blit(boom2,(self.rect.x,self.rect.y))
            elif num==40:
                screen.blit(boom3,(self.rect.x,self.rect.y))
            elif num==60:
                screen.blit(boom4,(self.rect.x,self.rect.y))
                break
            pygame.display.update()

    def __del__(self):
        print('敌机销毁')
        self.boom()

    def fire(self):
        #创建子弹对象
        bullet = EnemyBullet(self.rect.centerx -12, self.rect.y,speed=6)
        enemy_bullets.add(bullet)
        print('敌机发射子弹')
#定义敌方飞机

class EnemyaSprite(GameSprite):
    def __init__(self):
        super().__init__("./image/diji2.png",speed=random.randint(3,5))
        #初始化敌方飞机位置
        self.rect.x=random.randint(0,SCREEN_RECT.width-self.rect.width)
        self.rect.y=-self.rect.height

    def update(self):
        super().update()
        #边界判断
        if self.rect.y>SCREEN_RECT.height:
            self.kill()
    def boom(self):
        boom1=pygame.image.load("./image/boom4.png")
        num = 0
        while True:

            num += 4
            if num == 12:
                screen.blit(boom1, (self.rect.x, self.rect.y))
                break

    def __del__(self):
        print('敌机销毁')

    # def fire(self):
    #     #创建子弹对象
    #     bullet = EnemyBullet(self.rect.centerx -10, self.rect.y,speed=6)
    #     enemy_bullets.add(bullet)
    #     print('敌机发射子弹')
    def fire(self):
        #创建子弹对象
        bullet = BulletSprite(self.rect.centerx - 20, self.rect.y, speed=6)
        enemy_bullets.add(bullet)
        print('敌机发射子弹')

class BossSprite(GameSprite):
    def __init__(self):
        super().__init__("./image/boss1.png",speed=2)
        #初始化敌方飞机位置
        self.rect.x=random.randint(0,SCREEN_RECT.width-self.rect.width)
        self.rect.y=20

        self.life=100
    def update(self):

        self.rect.x=random.randint(-2,+5)
        #边界判断
        if self.rect.y>SCREEN_RECT.height:
            self.kill()
    def boom(self):
        boom1=pygame.image.load("./image/boom4.png")
        boom2=pygame.image.load("./image/boom4.png")
        boom3=pygame.image.load("./image/boom4.png")
        boom4=pygame.image.load("./image/boom4.png")

        num=0
        while True:

            num+=4
            if num==12:
                screen.blit(boom1,(self.rect.x,self.rect.y))
            elif num==20:
                screen.blit(boom2,(self.rect.x,self.rect.y))
            elif num==40:
                screen.blit(boom3,(self.rect.x,self.rect.y))
            elif num==60:
                screen.blit(boom4,(self.rect.x,self.rect.y))
                break
            pygame.display.update()
    def __del__(self):
        print('敌机销毁')

    def fire(self):
        #创建子弹对象
        bullet = BossBullet(self.rect.centerx -30, self.rect.y, speed=6)
        enemy_bullets.add(bullet)
        print('敌机发射子弹')

class EnemyBullet(GameSprite):
    def __init__(self,x,y,speed):
        super().__init__("./image/zidan.png")
        self.rect.x=x
        self.rect.y=y
        self.speed = speed

    def update(self):
        super().update()
        #边界判断
        if self.rect.y<=-768:
            self.kill()

    def __del__(self):
        print("子弹已经销毁")
class BossBullet(GameSprite):
    def __init__(self,x,y,speed):
        super().__init__("./image/big.png")
        self.rect.x=x
        self.rect.y=y
        self.speed = speed

    def update(self):
        super().update()
        #边界判断
        if self.rect.y<=-768:
            self.kill()

    def __del__(self):
        print("子弹已经销毁")
#定义敌机精灵族对象
enemys=pygame.sprite.Group()
#定义敌机子弹精灵组对象
enemy_bullets=pygame.sprite.Group()

#间隔一定时间触发一次敌机事件
pygame.time.set_timer(ENEMY_CREATE,10000)
pygame.time.set_timer(BOSS_CREATE,30000)
pygame.time.set_timer(MID_CREATE,1500)


#添加游戏背景音乐

pygame.mixer.music.load("./musics1/back.mp3")
pygame.mixer.music.play()


bossa=pygame.sprite.Group()
#添加英雄飞机开火音乐
bullet_fire=pygame.mixer.Sound("./musics1/sheji.wav")
#添加敌机爆炸音乐
bomb=pygame.mixer.Sound("./musics1/boom.wav")

