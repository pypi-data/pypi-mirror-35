'''

'''
import pygame
import game_data

#自定义事件刷新
pygame.time.set_timer(game_data.ENEMY_CREATE, 1500)
pygame.time.set_timer(game_data.PROPS_CREATE, 5000)
pygame.time.set_timer(game_data.BOMB_CREATE, 7000)
pygame.time.set_timer(game_data.BOOS_CREATE, 20000)

class CheckEvent:
    '''
    检查事件
    '''

    def check_event(self):
        '''
        检查道具、敌机、炸弹和退出的事件
        :return:
        '''
        event_list = pygame.event.get()
        if len(event_list) > 0:
            for event in event_list:
                if event.type == pygame.QUIT:
                    return "exit"
                if event.type == game_data.ENEMY_CREATE:
                    # 敌机出现
                    return "dixi"
                if event.type == game_data.PROPS_CREATE:
                    # 道具出现
                    return "daoju"
                if event.type == game_data.BOMB_CREATE:
                    # 炸弹出现
                    return "zhadan"
                if event.type == game_data.BOOS_CREATE:
                    # boos出现
                    return "boos"
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 160 <= event.pos[0] <= 320 and 360 <= event.pos[1] <= 400:
                        return "danren"
                    if 160 <= event.pos[0] <= 320 and 430 <= event.pos[1] <= 470:
                        return "shuangren"


    def check_event_key(self):
        '''
        检查方向键的事件
        :return:
        '''
        key_down = pygame.key.get_pressed()
        return key_down
