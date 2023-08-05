'''
        GameSprite<class>:游戏精灵父类
        BackgroundSprite<class>:背景精灵类
        HeroSprite<class>:英雄飞机精灵类
        EnemySprite<class>:敌机精灵类
        BulletSprite<class>:子弹精灵类
        PropsSprite<class>:道具精灵类
        ShieldSprite<class>:护盾精灵类
        BombSprite<class>:炸弹精灵类
        BoosSprite<class>:boss精灵类
'''

import pygame,random
import game_data

#精灵父类
class GameSprite(pygame.sprite.Sprite):

    def __init__(self,image_path,speed = 0):
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        self.rect.y += self.speed


#背景精灵类
class BackgroundSprite(GameSprite):

    def __init__(self,image_path,speed,perpare = False):
        super().__init__(image_path,speed)

        #判断背景边界
        if perpare:
            self.rect.y = -game_data.SCREEN_SIZE[1]

    def update(self):
        super().update()
        if self.rect.y >= game_data.SCREEN_SIZE[1]:
            self.rect.y = -game_data.SCREEN_SIZE[1]


#英雄飞机精灵类
class HeroSprite(GameSprite):

    def __init__(self,image_path):
        super().__init__(image_path)
        #英雄初始血量
        self.hp = 100
        #英雄子弹伤害
        self.hit_num = 20
        #初始化英雄飞机位置
        self.rect.centerx = game_data.SCREEN_RECT.centerx
        self.rect.centery = game_data.SCREEN_RECT.centery + 200

    def update(self):
        super().update()
        #边界判断
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= game_data.SCREEN_RECT.width - self.rect.width:
            self.rect.x = game_data.SCREEN_RECT.width - self.rect.width

        if self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.y >= game_data.SCREEN_RECT.height - self.rect.height:
            self.rect.y = game_data.SCREEN_RECT.height - self.rect.height

    def fire(self,image_path,speed):
        '''
        英雄开火
        :param image_path: 子弹图片
        :param speed: 子弹速度
        :return: 包含子弹精灵对象的list
        '''
        bullets = list()
        #开火
        bullt = BulletSprite(image_path,speed,self.rect.centerx,self.rect.centery)
        bullets.append(bullt)

        return bullets


#子弹精灵类
class BulletSprite(GameSprite):

    def __init__(self,image_path,speed,x,y):
        super().__init__(image_path,speed,)

        #初始化子弹位置
        self.rect.centerx = x
        self.rect.centery = y

    def update(self):
        super().update()
        #判断子弹边界
        if self.rect.y < -self.rect.height:
            self.kill()


#敌机精灵类
class EnemySprite(GameSprite):

    def __init__(self,image_path,speed):
        '''
        初始化敌机属性
        :param image_path: 图片
        :param speed: 敌机速度
        :param x: 敌机出现横坐标
        '''
        super().__init__(image_path,speed)
        #敌机初始血量
        self.hp = 60
        #敌机子弹伤害
        self.hit_num = 50
        self.speed = speed
        #初始化敌机位置
        self.rect.x = random.randint(0,game_data.SCREEN_RECT.width-self.rect.width)
        self.rect.y = 0

    def update(self):
        super().update()
        #边界处理
        if self.speed > 5:
            self.rect.x += 3
        if self.speed < 5:
            self.rect.x -= 3
        if self.rect.y > game_data.SCREEN_SIZE[1] + self.rect.height:
            self.kill()
        if self.rect.x <= -self.rect.width:
            self.rect.x = game_data.SCREEN_RECT.width
        elif self.rect.x >= game_data.SCREEN_RECT.width:
            self.rect.x =  -self.rect.width


#道具精灵类
class PropsSprite(EnemySprite):

    def __init__(self,image_path,speed):

        super().__init__(image_path,speed)


#护盾精灵类
class ShieldSprite(GameSprite):

    def __init__(self,image_path,rect):
        super().__init__(image_path)

        #初始化位置
        self.rect.centerx = rect.centerx
        self.rect.centery = rect.centery - 10


#炸弹进灵类
class BombSprite(GameSprite):

    def __init__(self,image_path,speed):
        super().__init__(image_path,speed)

        # 初始化炸弹位置
        self.rect.x = random.randint(0, game_data.SCREEN_RECT.width - self.rect.width)
        self.rect.y = 0

    def update(self):
        super().update()
        #边界判断
        if self.rect.y > game_data.SCREEN_SIZE[1]:
            self.kill()


#boos精灵类
class BoosSprite(GameSprite):

    def __init__(self,image_path,speed,hp):
        super().__init__(image_path,speed)
        self.hp = hp

        self.speed = speed
        # 初始化boss位置
        self.rect.x = random.randint(0, game_data.SCREEN_RECT.width - self.rect.width)
        self.rect.y = 0

    def hurt(self,hit_mun):
        '''
        boos受伤
        :param hit_mun:伤害值
        :return:
        '''
        self.hp -= hit_mun
        return self.hp

    def update(self):
        super().update()
        #边界处理
        self.rect.x += 3
        self.rect.y += 3
        if self.rect.y > 200:
            self.rect.y -= 3
        elif self.rect.y < 50:
            self.rect.y += 3
        if self.rect.x <= -self.rect.width:
            self.rect.x = game_data.SCREEN_RECT.width
        elif self.rect.x >= game_data.SCREEN_RECT.width:
            self.rect.x =  -self.rect.width

