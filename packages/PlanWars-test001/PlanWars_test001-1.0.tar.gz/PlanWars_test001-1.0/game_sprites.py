# coding:utf-8
import pygame
import random
import data
import time


class GameSprite(pygame.sprite.Sprite):
    '''游戏精灵对象：用于表示游戏中的各种元素'''
    def __init__(self, image_path, speed=1):
        '''
        :param image_path: 图片路径
        :param speed: 图片速度
        '''
        # 调用父类初始化数据
        super().__init__()
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        '''默认运动更新方法'''
        self.rect.y += self.speed


class BackgroudSprite(GameSprite):
    '''背景精灵'''
    def __init__(self, image_path, bg_music, speed=1, prepare=False):
        '''
        :param image_path: 背景图片路径
        :param bg_music: 背景音乐
        :param speed: 背景图片速度
        :param prepare: 是否是第二张图片
        '''
        super().__init__(image_path, speed)
        # 判断是否是第二张背景
        if prepare:
            self.rect.y = -data.SCREEN_SIZE[1]
        else:
            # bgm
            pygame.mixer_music.load(bg_music)
            pygame.mixer_music.play(-1)

    def update(self):
        # 调用父类的方法，执行运动
        super().update()
        # 子类中判断边界
        if self.rect.y > data.SCREEN_SIZE[1]:
            self.rect.y = -data.SCREEN_SIZE[1]


class BulletSprite(GameSprite):
    '''子弹精灵'''
    def __init__(self, x, y, bullet_path='./images/bullet1.png', speed=-5):
        '''

        :param x: 子弹的X坐标
        :param y: 子弹的Y坐标
        :param bullet_path: 子弹的图片路径
        :param speed: 子弹的速度
        '''
        super().__init__(bullet_path, speed=speed)
        self.rect.x = x - self.rect.width/2
        if speed < 0:
            self.rect.y = y - self.rect.height
        else:
            self.rect.y = y

    def update(self):
        # 调用父类分方法进行操作
        super().update()
        # 边界判断
        if self.rect.y <= -self.rect.height:
            # 子弹从精灵组中删除
            self.kill()


class Plan(GameSprite):
    def __init__(self, image_path, speed, hp):
        '''

        :param image_path: 飞机图片地址
        :param speed: 飞机速度
        :param hp: 飞机血量
        '''
        super().__init__(image_path, speed)
        self.hp = hp
        # 音效
        self.bol_m = pygame.mixer.Sound('./music/bol1.wav')  # 爆炸音效
        if data.now == 1:
            self.fire_m = pygame.mixer.Sound('./music/枪声1.wav')  # 英雄飞机开火音效
        elif data.now == 2:
            self.fire_m = pygame.mixer.Sound('./music/the98k.wav')  # 英雄飞机开火音效

    def bol(self, x, y):
        '''
        飞机爆炸及特效
        :return:
        '''
        self.bol_m.play()
        self.kill()
        for img in ['./images/enemy2_down3.png', './images/enemy2_down3.png',
                    './images/enemy2_down3.png', './images/enemy2_down3.png',
                    './images/enemy2_down4.png', './images/enemy2_down4.png']:
            self.image = pygame.image.load(img)
            time.sleep(0.02)
            data.screen.blit(self.image, (x, y))
            pygame.display.update()

    def fire(self):
        '''飞机开火'''
        self.fire_m.play()  # 开火音效


class HeroSprite(Plan):
    '''英雄精灵对象'''
    def __init__(self, hero_path):
        '''

        :param hero_path: 英雄飞机图片路径
        '''
        hero_speed = data.hero_speed * data.now
        hero_hp = data.hero_hp * data.now

        super().__init__(image_path=hero_path, speed=hero_speed, hp=hero_hp)
        # 初始化英雄飞机的位置
        self.rect.x = data.SCREEN_RECT.centerx
        self.rect.y = data.SCREEN_RECT.centery + 300
        self.bullets = pygame.sprite.Group()

    def update(self):
        # 水平边界判断
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= data.SCREEN_RECT.width - self.rect.width:
            self.rect.x = data.SCREEN_RECT.width - self.rect.width
        # 垂直边界判断
        if self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.y >= data.SCREEN_RECT.height - self.rect.height:
            self.rect.y = data.SCREEN_RECT.height - self.rect.height

    # def __del__(self):
    #     # self.bol()
    #     print('英雄飞机销毁...')

    def fire(self):
        '''英雄飞机攻击'''
        # 限制子弹个数
        if len(self.bullets) < data.hero_bullet_nums*data.now:
            bullet_path = './images/bullet{}.png'.format(str(data.now))
            # 创建子弹
            bullet = BulletSprite(self.rect.centerx, self.rect.y, bullet_path=bullet_path)
            self.bullets.add(bullet)
            super().fire()

    def bol(self, hurt=data.enemy_atk):
        self.hp -= hurt
        if self.hp <= 0:
            # self.kill()
            super().bol(self.rect.x, self.rect.y)
            return True
        return False


class EnemySprite(Plan):
    '''敌方飞机'''
    def __init__(self):
        ''''''
        # 初始化敌方飞机的数据：图片、速度
        hp = data.enemy_hp*data.now
        super().__init__('./images/enemy2.png', speed=random.randint(1+data.now, 3+data.now), hp=hp)

        # 初始化敌方飞机的位置
        self.rect.x = random.randint(0, data.SCREEN_RECT.width - self.rect.width)
        self.rect.y = -self.rect.height
        # self.hp = hp*data.now
        self.enemy_bullets = pygame.sprite.Group()

    def update(self):
        super().update()
        # 边界判断
        if self.rect.y > data.SCREEN_RECT.height:
            # 敌方飞机超出屏幕销毁
            self.kill()

    def bol(self, hurt=data.hero_atk):
        self.hp -= hurt
        if self.hp <= 0:
            data.score += data.get_score*data.now
            if data.score >= data.hero_upgrade2:
                data.now = 2
            super().bol(self.rect.x, self.rect.y)

    def fire(self):
        '''敌机开火'''
        bullet = BulletSprite(self.rect.centerx, self.rect.y+self.rect.height, speed=self.speed+2)
        self.enemy_bullets.add(bullet)

