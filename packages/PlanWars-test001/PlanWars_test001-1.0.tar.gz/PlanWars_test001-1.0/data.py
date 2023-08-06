# coding:utf-8
import pygame



# 自定义一个事件
# 创建敌机事件
ENEMY_CREATE = pygame.USEREVENT
# 敌机开火事件
ENEMY_FIRE = pygame.USEREVENT + 1   # 自定义下一个事件
# 间隔一定的时间，触发一次创建敌机的事件
pygame.time.set_timer(ENEMY_CREATE, 2000)   # 毫秒
# 间隔一定时间，敌机发射子弹
pygame.time.set_timer(ENEMY_FIRE, 1000)


SCREEN_SIZE = (512, 768)    # 游戏窗口大小宽高
SCREEN_RECT = pygame.Rect(0, 0, *SCREEN_SIZE)  # 定义屏幕资源位置   ---长方形资源x,y,width,height
# 创建窗口参数
screen_parameter = (SCREEN_SIZE, 0, 32)  # 游戏区域、整数参数控制是否全屏、图片颜色深度[8bit/16bit/24/32]
# 游戏窗口标题
game_name = '飞机大战'
# 时钟刷新帧
game_tick = 24

# 精灵与精灵组
# hero_group = None
# resources = None
# enemys = None
# 当前展示屏幕
screen = None

first = True    # 是否第一次开始游戏

'''bg_path, bg_music, bg_speed,hero_path'''
# sceen1 = ['./images/bg_img_1.jpg', './music/fight.wav', 1, './images/hero_1.png']
# sceen2 = ['./images/bg_img_2.jpg', './music/fight.wav', 2, './images/hero_2.png']
sceen = (
    None,
    ('./images/bg_img_1.jpg', './music/fight.wav', 1, './images/hero_1.png'),
    ('./images/bg_img_2.jpg', './music/fight.wav', 2, './images/hero_2.png')
         )


#敌机初始参数
enemy_hp = 100
enemy_atk = 20

# 英雄飞机初始参数
hero_hp = 300   # 血量
hero_speed = 5  # 速度
hero_atk = 50   # 攻击力
hero_upgrade2 = 40   # 升级分数条件
hero_bullet_nums = 4   # 子弹个数
score = 0   # 英雄飞机分数
now = 1 # 英雄飞机等级
get_score = 10  # 击毁一架敌机的得分

