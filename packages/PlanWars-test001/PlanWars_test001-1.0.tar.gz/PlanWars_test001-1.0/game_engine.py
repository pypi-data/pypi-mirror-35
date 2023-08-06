# coding:utf-8
import pygame
import game_sprites
import data
import time


class GameEngine:
    def __init__(self):
        pygame.init()
        screen = data.screen_parameter
        self.screen = pygame.display.set_mode(*screen)
        pygame.display.set_caption(data.game_name)  # 标题
        # 设置窗口左上角的图标
        ic = pygame.image.load('./images/p.ico')
        pygame.display.set_icon(ic)
        # 定义时钟对象
        self.clock = pygame.time.Clock()
        # 自定义一个事件
        self.ENEMY_CREATE = data.ENEMY_CREATE
        self.ENEMY_FIRE = data.ENEMY_FIRE

        # 写入数据
        data.screen = self.screen

        # 设置字体
        font = pygame.font.SysFont('arial', 28, True)
        # 得分，血量字体
        self.level_font = font
        self.score_font = font
        self.hp_font = font

    def create_scene(self, bg_path, bg_music, bg_speed, hero_path):
        '''
        创建游戏场景
        :param bg_path: 背景图片路径
        :param bg_music: 背景音乐
        :param bg_speed: 背景速度
        :param hero_path: 英雄路径
        :param hero_mul: 英雄倍数
        :return:
        '''
        # 定义背景精灵和游戏精灵
        self.bg1 = game_sprites.BackgroudSprite(bg_path, bg_music, speed=bg_speed)
        self.bg2 = game_sprites.BackgroudSprite(bg_path, bg_music, speed=bg_speed,
                                                prepare=True)
        self.hero = game_sprites.HeroSprite(hero_path=hero_path)
        # 定义精灵组对象
        self.resources = pygame.sprite.Group(self.bg1, self.bg2)
        # 定义英雄飞机精灵组
        self.hero_group = pygame.sprite.Group(self.hero)
        # self.resources = (self.bg1, self.bg2, self.hero)
        # 定义敌机精灵组对象
        self.enemys = pygame.sprite.Group()
        # 初始化英雄飞机得分
        data.score = 0

    def xuanran_zhanshi(self):
        '''
        渲染展示方法
        :return:
        '''
        # 精灵组渲染
        self.resources.update()
        self.resources.draw(self.screen)
        # 文字渲染
        level_text = self.level_font.render('level:%s' % data.now, True, [255, 0, 0])
        self.screen.blit(level_text, (0, 0))
        score_text = self.score_font.render('Score:%s' % data.score, True, [255, 0, 0])
        self.screen.blit(score_text, (0, 25))
        hp_text = self.hp_font.render('HP:%s' % self.hero.hp, True, [255, 0, 0])
        self.screen.blit(hp_text, (0, 50))
        # 英雄飞机渲染
        self.hero_group.update()
        self.hero_group.draw(self.screen)
        # 子弹精灵组渲染
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)
        #  渲染敌机精灵组中的所有飞机
        self.enemys.update()
        self.enemys.draw(self.screen)
        # 敌机子弹精灵组渲染
        for enemy in self.enemys:
            enemy.enemy_bullets.update()
            enemy.enemy_bullets.draw(self.screen)
        # 屏幕更新
        pygame.display.update()

    def check_collide(self):
        '''
         # 碰撞检测方法
        :return:英雄飞机死亡返回首页
        '''
        # 敌机子弹精灵组分别与英雄子弹精灵组、英雄飞机精灵碰撞检测
        for enemy in self.enemys:
            pygame.sprite.groupcollide(enemy.enemy_bullets, self.hero.bullets, True, True)
            e = pygame.sprite.spritecollide(self.hero, enemy.enemy_bullets, True)
            if len(e):
                res = self.hero.bol(data.enemy_atk)  # todo
                if res:
                    return True

        # 敌机精灵组和英雄子弹精灵组碰撞检测
        re1 = pygame.sprite.groupcollide(self.enemys, self.hero.bullets, False, True)
        for i in re1:
            i.bol()

        # 敌机精灵组和英雄飞机精灵碰撞检测
        e = pygame.sprite.spritecollide(self.hero, self.enemys, True)
        if len(e):
            res = self.hero.bol(100*data.now)
            if res:
                return True
        return False

    def check_event(self):
        '''
        # 监听所有的事件
        :return:
        '''

        event_list = pygame.event.get()
        if len(event_list) > 0:
            for event in event_list:
                # 如果当前的事件是QUIT事件
                if event.type == pygame.QUIT:
                    # 卸载所有的pygame资源，退出程序
                    pygame.quit()
                    exit()
                if event.type == self.ENEMY_CREATE:
                    # print('创建一架敌机....')
                    enemy = game_sprites.EnemySprite()
                    # 添加到敌方飞机精灵组中
                    self.enemys.add(enemy)
                if data.now > 1:
                    if event.type == self.ENEMY_FIRE:
                        # print('敌机开火')
                        for i in self.enemys:
                            i.fire()
                # 检测键盘一次按键事件
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        # print('英雄飞机开火...')
                        self.hero.fire()
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        time.sleep(1)
                        exit()

        # 获取当前用户键盘上被操作的案件
        key_down = pygame.key.get_pressed()

        if key_down[pygame.K_LEFT]:
            # print('向左移动《《《《')
            self.hero.rect.x -= self.hero.speed
        if key_down[pygame.K_RIGHT]:
            # print('向右移动》》》》')
            self.hero.rect.x += self.hero.speed
        if key_down[pygame.K_UP]:
            # print('向上移动^^^^^^^^^^')
            self.hero.rect.y -= self.hero.speed
        if key_down[pygame.K_DOWN]:
            # print('向下移动')
            self.hero.rect.y += self.hero.speed

    def sceen_loop(self, status):
        '''
        # 游戏场景循环方法
        :return:
        '''
        while True:
            # 判断是否跳转关卡
            if data.now != status:
                time.sleep(1)
                break
            # 定义时钟刷新帧，每秒让循环运行多少次！
            self.clock.tick(data.game_tick)
            # 事件监听
            self.check_event()
            # 碰撞检测
            res = self.check_collide()
            if res:
                # 英雄飞机死亡
                # 初始化数据
                data.now = 1
                data.score = 0
                time.sleep(2)
                return self.one()
            # 渲染展示
            self.xuanran_zhanshi()

    def one(self):
        '''
        游戏初始界面方法
        :return:
        '''
        data.first = False
        self.bg0 = game_sprites.BackgroudSprite(image_path='./images/theone.jpg',
                                                bg_music='./music/拳皇97开始.wav', speed=0)
        start_m = pygame.mixer.Sound('./music/拳王开始音效.wav')
        self.resources = pygame.sprite.Group(self.bg0)

        while True:
            # 定义时钟刷新帧，每秒让循环运行多少次！
            self.clock.tick(data.game_tick)
            # 监听所有的事件
            event_list = pygame.event.get()
            if len(event_list) > 0:
                # print(event_list)
                for event in event_list:
                    # 如果当前的事件是QUIT事件
                    if event.type == pygame.QUIT:
                        # 卸载所有的pygame资源，退出程序
                        pygame.quit()
                        exit()
                    # 按任意键进入游戏事件
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        start_m.play()
                        time.sleep(3.6)
                        self.resources.remove(self.bg0)
                        self.bg0.kill()
                        return self.start()
            # 精灵组渲染
            self.resources.update()
            self.resources.draw(self.screen)
            # 屏幕更新
            pygame.display.update()

    def start(self):
        '''
        游戏开始方法
        :return:
        '''
        # 游戏初始化
        # pygame.init()
        while True: 
            # 开始界面
            if data.first:
                self.one()
            # 游戏界面
            else:
                # 创建场景
                self.create_scene(*data.sceen[data.now])
                # 游戏场景循环
                self.sceen_loop(status=data.now)
                 # 清空精灵组对象
                self.resources.empty()
                # 清空英雄飞机精灵组
                self.hero_group.empty()
                # self.resources = (self.bg1, self.bg2, self.hero)
                # 清空敌机精灵组对象
                self.enemys.empty()
                # 背景音乐淡出，在time毫秒的时间内音量由初始值渐变为0，最后停止播放。
                pygame.mixer_music.fadeout(500)
                time.sleep(1)

        # 卸载游戏模块
        pygame.quit()

