

import pygame

from pygame.sprite import Group

from settings import Settings

from ship import Ship

import game_functions as gf

def run_game():
    #初始化pygame,设置和屏幕对象
    pygame.init()#初始化背景设置，让pygame能正常工作
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))#设置一个显示窗口
    pygame.display.set_caption("Alien Invasion")
    #创建一艘飞船
    ship=Ship(ai_settings,screen)

    创建一个用来存储子弹的编组
    bullets=Group()



    #开始游戏的主循 环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.update_bullets(bulletssss)
        gf.update_screen(ai_settings,screen,ship,bullets)
        #让最近绘制的屏幕可见
        pygame.display.flip()
run_game()
