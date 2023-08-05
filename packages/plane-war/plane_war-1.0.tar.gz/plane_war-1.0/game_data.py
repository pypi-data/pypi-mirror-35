'''
调用各种素材
'''
import pygame
#屏幕大小
SCREEN_SIZE = (512,768)
SCREEN_RECT = pygame.Rect(0,0,*SCREEN_SIZE)

#自定义事件
ENEMY_CREATE = pygame.USEREVENT
PROPS_CREATE = pygame.USEREVENT + 1
BOMB_CREATE = pygame.USEREVENT + 2
BOOS_CREATE = pygame.USEREVENT + 3

#开始背景
start_img = "./images/img_bg_logo.jpg"
#关卡一背景图片
checkpoint1_img = "./images/img_bg_level_2.jpg"
#关卡二背景图片
checkpoint2_img = "./images/img_bg_level_5.jpg"
#结束页面
game_over_img = "./images/game_over.jpg"
#英雄1图片
hero1_img = "./images/hero_1.png"
hero2_img = "./images/hero_2.png"
#boos图片
boss_img1 = "./images/boss.png"
boss_img2 = "./images/boss2.png"
boss_img3 = "./images/boss3.png"
#boos大招
boss_bullet1 = "./images/boss_bullet.png"
boss_bullet2 = "./images/boss_bullet2.png"
boss_bullet3 = "./images/boss_bullet3.png"
#子弹1图片
bullet1 = "./images/bullet_1.png"
bullet2 = "./images/bullet_2.png"
bullet3 = "./images/bullet_3.png"
bullet4 = "./images/bullet_4.png"
#大招图片
dazhao1 = "./images/dazhao1.png"
dazhao2 = "./images/dazhao2.png"
#炸弹图片
bomb_img = "./images/bomb.png"
#敌机1图片
enemy_plane1 = "./images/img_plane_enemy_2.png"
#敌机2图片
enemy_plane2 = "./images/img_plane_enemy_3.png"

#道具图片1
prop1_img = "./images/hudun_11.png"

#护盾图片
shield1 = "./images/hudun_1.png"
#音乐
#游戏开始音乐
music_start = "./musics/start_music.mp3"
music_one = "./musics/one_music.mp3"
music_two = "./musics/two_music.mp3"
music_bullet = "./musics/bullet.wav"
music_down = "./musics/enemy_down.wav"