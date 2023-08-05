import pygame,random,time
import game_sprites,game_event
import game_data

#护盾检测
float = None
float1 = None
#控制游戏循环
num = 0


class GameEngine:

    def __init__(self):

        pygame.init()#初始化游戏模块
        self.screen = pygame.display.set_mode(game_data.SCREEN_SIZE)#初始化屏幕
        self.background_group = pygame.sprite.Group()#初始化背景精灵组
        self.hero_group = pygame.sprite.Group()#初始化英雄飞机精灵组
        self.hero_boom_group = pygame.sprite.Group()#初始化英雄飞机爆炸精灵组
        self.hero_bullet_group = pygame.sprite.Group()#初始化英雄子弹精灵组
        self.enemy_plane_group = pygame.sprite.Group()#初始化敌机精灵组
        self.enemy_boom_group = pygame.sprite.Group()#初始化敌机爆炸精灵组
        self.props_group = pygame.sprite.Group()#初始化道具精灵组
        self.shield_group = pygame.sprite.Group()#初始化护盾精灵组
        self.bomb_group =  pygame.sprite.Group()#炸弹精灵组
        self.dazhao_group = pygame.sprite.Group()#大招精灵组
        self.booses_group = pygame.sprite.Group()#boos精灵组
        self.clock = pygame.time.Clock()# 创建时钟对象
        self.font = pygame.font.SysFont("fangsong",26,True)#字体
        self.fenshu = 0#判断分数

        self.checkevent = game_event.CheckEvent()#检查事件类

    def create_screen(self,back_img):
        '''
        创建背景、英雄
        并添加到精灵组
        :return:
        '''
        #开始画面
        if back_img == "start":
            start_bg = game_sprites.BackgroundSprite(game_data.start_img,0)
            self.background_group.add(start_bg)
        elif back_img == "start_one":
            #单人背景对象
            checkpoint1_bg1 = game_sprites.BackgroundSprite(game_data.checkpoint1_img,3)
            checkpoint1_bg2 = game_sprites.BackgroundSprite(game_data.checkpoint1_img,3,perpare=True)
            #英雄1对象
            self.hero1 = game_sprites.HeroSprite(game_data.hero1_img)
            #添加到对应的精灵组
            self.background_group.add(checkpoint1_bg1,checkpoint1_bg2)
            self.hero_group.add(self.hero1)
        elif back_img == "start_two":
            #双人背景对象
            checkpoint1_bg1 = game_sprites.BackgroundSprite(game_data.checkpoint2_img,5)
            checkpoint1_bg2 = game_sprites.BackgroundSprite(game_data.checkpoint2_img,5,perpare=True)
            #英雄1对象
            self.hero1 = game_sprites.HeroSprite(game_data.hero1_img)
            self.hero2 = game_sprites.HeroSprite(game_data.hero2_img)
            #添加到对应的精灵组
            self.background_group.add(checkpoint1_bg1,checkpoint1_bg2)
            self.hero_group.add(self.hero1,self.hero2)
        elif back_img == "over_game":
            #结束页面
            checkpoint1_bg1 = game_sprites.BackgroundSprite(game_data.game_over_img, 0)
            self.background_group.add(checkpoint1_bg1)

    def __update_screen(self):
        '''
        渲染游戏精灵
        :return:
        '''
        # 添加到屏幕上
        self.background_group.draw(self.screen)
        self.hero_group.draw(self.screen)
        self.hero_bullet_group.draw(self.screen)
        self.enemy_plane_group.draw(self.screen)
        self.props_group.draw(self.screen)
        self.shield_group.draw(self.screen)
        self.bomb_group.draw(self.screen)
        self.hero_boom_group.draw(self.screen)
        self.dazhao_group.draw(self.screen)
        self.booses_group.draw(self.screen)
        # 渲染精灵组对象
        self.background_group.update()
        self.hero_group.update()
        self.hero_bullet_group.update()
        self.enemy_plane_group.update()
        self.props_group.update()
        self.shield_group.update()
        self.bomb_group.update()
        self.hero_boom_group.update()
        self.dazhao_group.update()
        self.booses_group.update()

    def result_ckeck_event(self,click):
        '''
        事件处理
        :param click:
        :return:
        '''
        if click == "exit":
            pygame.quit()
            exit()
        elif click == "dixi":
            print("敌机出现！")
            #判断敌机的随机数
            random_num = random.randint(3,7)
            if random_num < 5:
                self.enemy = game_sprites.EnemySprite(game_data.enemy_plane1, random_num)
            else:
                self.enemy = game_sprites.EnemySprite(game_data.enemy_plane2, random_num)

            self.enemy_plane_group.add(self.enemy)
        elif click == "daoju":
            print("道具出现！")
            self.prop = game_sprites.PropsSprite(game_data.prop1_img, random.randint(7, 9))
            self.props_group.add(self.prop)
        elif click == "zhadan":
            print("炸弹出现！")
            self.bomb = game_sprites.BombSprite(game_data.bomb_img,30)
            self.bomb_group.add(self.bomb)
        elif click == "boos":
            print("boos出现！")
            #boos出现
            boos_random = random.randint(0,21)
            if boos_random < 5:
                self.boos = game_sprites.BoosSprite(game_data.boss_img1,0,100)
                self.booses_group.add(self.boos)
                #boos大招
                boss_bullt = game_sprites.BulletSprite(game_data.boss_bullet1, 14, self.boos.rect.x+100, self.boos.rect.y + 50)
                self.bomb_group.add(boss_bullt)

            elif  5<= boos_random < 9:
                self.boos = game_sprites.BoosSprite(game_data.boss_img2, 0, 150)
                self.booses_group.add(self.boos)
                # boos大招
                boss_bullt1 = game_sprites.BulletSprite(game_data.boss_bullet2, 14, self.boos.rect.x,
                                                       self.boos.rect.y + 50)
                boss_bullt1_1 = game_sprites.BulletSprite(game_data.boss_bullet2, 14, self.boos.rect.x + 100,
                                                        self.boos.rect.y + 50)
                boss_bullt1_2 = game_sprites.BulletSprite(game_data.boss_bullet2, 14, self.boos.rect.x +300,
                                                        self.boos.rect.y + 50)
                self.bomb_group.add(boss_bullt1,boss_bullt1_1,boss_bullt1_2)
            elif  9<= boos_random < 20:
                self.boos = game_sprites.BoosSprite(game_data.boss_img3, 0, 200)
                self.booses_group.add(self.boos)
                # boos大招
                boss_bullt3 = game_sprites.BulletSprite(game_data.boss_bullet3, 14, self.boos.rect.x+50,
                                                        self.boos.rect.y)
                self.bomb_group.add(boss_bullt3)

    def check_enemy_fire(self):

        # 判断发射子弹的随机数
        random_num1 = random.randint(3,70)
        if len(self.enemy_plane_group) >0 and random_num1 < 5 :
            print("敌机发射子弹********************")
            bullt = game_sprites.BulletSprite(game_data.bullet3,12, self.enemy.rect.x, self.enemy.rect.y + 50)
            self.bomb_group.add(bullt)
            bullt1 = game_sprites.BulletSprite(game_data.bullet4, 16, self.enemy.rect.x, self.enemy.rect.y + 50)
            self.bomb_group.add(bullt1)
            pygame.display.update()

    def check_speed(self):
        '''
        控制敌机速度
        :return:
        '''
        if self.fenshu > 30 == 0 and len(self.enemy_plane_group) != 0:
            print("敌机加速*************************")
            self.fenshu += 1
            self.enemy.speed += 1

    def result_collide(self):
        '''
        碰撞处理
        :return:
        '''
        # 碰撞检测:子弹和敌方飞机之间的碰撞！
        self.enemy_boom_group.add(pygame.sprite.groupcollide(self.enemy_plane_group, self.hero_bullet_group, True, True))
        self.enemy_boom_group.add(pygame.sprite.groupcollide(self.enemy_plane_group,self.dazhao_group,True,False))
        for enemy in self.enemy_boom_group:
            print(type(enemy))
            self.__bullet_music(game_data.music_down)
            self.boom(enemy)
            enemy.hp -= 20
            if enemy.hp <= 0:
                enemy.kill()
                self.enemy_boom_group.remove(enemy)
        #碰撞检测：大招与敌机子弹
        pygame.sprite.groupcollide(self.bomb_group,self.dazhao_group,True,False)
        # 碰撞检测：护盾与道具之间
        pygame.sprite.groupcollide(self.shield_group, self.props_group, False, True)
        # 碰撞检测：炸弹与护盾的碰撞
        pygame.sprite.groupcollide(self.shield_group, self.bomb_group, True, True)
        # 碰撞检测：护盾与敌机的碰撞
        pygame.sprite.groupcollide(self.shield_group, self.enemy_plane_group, True, True)
        # 碰撞处理：英雄子弹与boos碰撞
        dict = pygame.sprite.groupcollide(self.booses_group,self.hero_bullet_group,False,True)
        if dict:
            hp = self.boos.hurt(2)
            print("boos受伤%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
            if hp <= 0:
                self.fenshu += 100
                self.booses_group.remove(self.boos)

    def result_collide_hero_shield(self):
        '''
        碰撞检测：英雄飞机和道具的碰撞
        :return:
        '''
        res = None
        e = pygame.sprite.groupcollide(self.hero_group,self.props_group,False,True)
        for i in e:
            self.shield = game_sprites.ShieldSprite(game_data.shield1,i.rect)
            self.shield_group.add(self.shield)
            print("生成护盾*******************************")
            res = True
        return res

    def result_collide_hero(self):
        '''
        英雄飞机碰撞处理
        :return:
        '''
        res = None
        #英雄飞机与boos碰撞
        self.hero_boom_group.add(pygame.sprite.groupcollide(self.hero_group,self.booses_group,True,True))
        # 碰撞检测：英雄飞机和敌机的碰撞
        self.hero_boom_group.add(pygame.sprite.groupcollide(self.hero_group,self.enemy_plane_group,True,True))
        # 碰撞检测：英雄飞机和炸弹之间的碰撞
        self.hero_boom_group.add(pygame.sprite.groupcollide(self.hero_group,self.bomb_group,True,True))
        for hero_plane in self.hero_boom_group:
            self.hero_boom_group.remove(hero_plane)
            res = True
        return res

    def game_over(self,res_life,i):
        '''
        判断是否退出游戏
        :return:
        '''
        global num
        if res_life == True:
            num += 1
        if num == i:
            self.background_group.empty()
            self.hero_group.empty()
            self.hero_boom_group.empty()
            self.hero_bullet_group.empty()
            self.enemy_plane_group.empty()
            self.enemy_boom_group.empty()
            self.props_group.empty()
            self.shield_group.empty()
            self.bomb_group.empty()
            self.dazhao_group.empty()
            self.booses_group.empty()
            self.over_show()

    def result_direction_hero1(self,res,key_down):
        '''
        英雄1方向键移动
        :param res:
        :param key_down:
        :return:
        '''
        global float
        if res:
            float = True
        if key_down[pygame.K_LEFT]:
            if float:
                print("向左移动<<<<<<<<<<<<护盾")
                self.hero1.rect.x -= 20
                self.shield.rect.x = self.hero1.rect.x
            else:
                print("向左移动<<<<<<<<<<<<")
                self.hero1.rect.x -= 20
        if key_down[pygame.K_RIGHT]:
            if float:
                print("向右移动>>>>>>>>>>>>护盾")
                self.hero1.rect.x += 20
                self.shield.rect.x = self.hero1.rect.x
            else:
                print("向右移动>>>>>>>>>>>>")
                self.hero1.rect.x += 20
        if key_down[pygame.K_UP]:
            if float:
                print("向上移动^^^^^^护盾")
                self.hero1.rect.y -= 10
                self.shield.rect.y = self.hero1.rect.y - 10
            else:
                print("向上移动^^^^^^")
                self.hero1.rect.y -= 10
        if key_down[pygame.K_DOWN]:
            if float:
                print("向下移动vvvvvv护盾")
                self.hero1.rect.y += 10
                self.shield.rect.y = self.hero1.rect.y - 10
            else:
                print("向下移动vvvvvv")
                self.hero1.rect.y += 10
        if key_down[pygame.K_KP0]:
            print("发射子弹>>>")
            bullts = self.hero1.fire(game_data.bullet1, -8)
            self.hero_bullet_group.add(*bullts)
            self.__bullet_music(game_data.music_bullet)
        if key_down[pygame.K_KP1]:
            print("发射大招是的分数：" + str(self.fenshu))
            if self.fenshu/3 > 10:
                print("发射大招。。。")
                self.fenshu -= 30
                print("发射大招后的分数：" + str(self.fenshu))
                bullts = self.hero1.fire(game_data.dazhao1, -10)
                self.dazhao_group.add(*bullts)

    def result_direction_hero2(self,res1,key_down):
        '''
        英雄2移动方向键
        :param res1:
        :param key_down:
        :return:
        '''
        global float1
        if res1:
            float1 = True
        if key_down[pygame.K_a]:
            if float1:
                print("向左移动<<<<<<<<<<<<护盾")
                self.hero2.rect.x -= 20
                self.shield.rect.x = self.hero2.rect.x
            else:
                print("向左移动<<<<<<<<<<<<")
                self.hero2.rect.x -= 20
        if key_down[pygame.K_d]:
            if float1:
                print("向右移动>>>>>>>>>>>>护盾")
                self.hero2.rect.x += 20
                self.shield.rect.x = self.hero2.rect.x
            else:
                print("向右移动>>>>>>>>>>>>")
                self.hero2.rect.x += 20
        if key_down[pygame.K_w]:
            if float1:
                print("向上移动^^^^^^护盾")
                self.hero2.rect.y -= 10
                self.shield.rect.y = self.hero2.rect.y - 10
            else:
                print("向上移动^^^^^^")
                self.hero2.rect.y -= 10
        if key_down[pygame.K_s]:
            if float1:
                print("向下移动vvvvvv护盾")
                self.hero2.rect.y += 10
                self.shield.rect.y = self.hero2.rect.y - 10
            else:
                print("向下移动vvvvvv")
                self.hero2.rect.y += 10
        if key_down[pygame.K_SPACE]:
            print("发射子弹>>>")
            bullts = self.hero2.fire(game_data.bullet2, -8)
            self.hero_bullet_group.add(*bullts)
            self.__bullet_music(game_data.music_bullet)
        if key_down[pygame.K_b]:
            print("发射大招时的分数：" + str(self.fenshu))
            if self.fenshu/3 > 10:
                self.fenshu -= 30
                bullts = self.hero2.fire(game_data.dazhao2, -10)
                self.dazhao_group.add(*bullts)

    def boom(self,enemy):
        '''
        爆炸动画
        :return:
        '''
        self.fenshu += 1
        for i in range(1,9):
            image = pygame.image.load("./images/bao{0}.png".format(i))
            self.screen.blit(image,enemy.rect)
            pygame.display.update()
            # print("爆炸 ++++++++++++++++++++++++")

    def __game_music(self,music_path):
        '''
        背景音乐
        :param music_path:
        :return:
        '''
        pygame.mixer.init()
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.play(-1)

    def __bullet_music(self,music_path):
        '''
        特效音乐
        :param music_path:
        :return:
        '''
        pygame.mixer.init()
        s = pygame.mixer.Sound(music_path)
        s.play()

    def start_show(self):
        '''
        展示页面
        :return:
        '''
        self.create_screen("start")

        while True:
            self.clock.tick(24)
            self.__update_screen()
            res = self.checkevent.check_event()
            key_down = self.checkevent.check_event_key()
            if res == "exit":
               return res
            if res == "danren":
                return res
            if res == "shuangren":
                return res
            pygame.display.update()

    def start_one(self):
        '''
        单人模式
        :return:
        '''
        self.fenshu = 0
        self.__game_music(game_data.music_one)
        self.create_screen("start_one")

        while True:

            # 刷新频率
            self.clock.tick(24)
            self.__update_screen()
            click = self.checkevent.check_event()
            self.result_ckeck_event(click)
            self.check_enemy_fire()
            self.result_collide()
            res = self.result_collide_hero_shield()
            key_down = self.checkevent.check_event_key()
            self.result_direction_hero1(res,key_down)
            res_life = self.result_collide_hero()
            self.game_over(res_life, 1)
            self.screen.blit(self.font.render("score:{0}".format(int(self.fenshu/3)), True, (200, 0, 0)), (20, 20))

            pygame.display.update()

    def start_two(self):
        '''
        双人模式
        :return:
        '''
        global num
        num = 0
        self.fenshu = 0
        self.__game_music(game_data.music_two)
        self.create_screen("start_two")
        while True:
            # 刷新频率
            self.clock.tick(24)
            self.__update_screen()
            click = self.checkevent.check_event()
            self.result_ckeck_event(click)
            self.check_enemy_fire()  # shifoukaihuo
            self.result_collide()

            res_life= self.result_collide_hero()
            self.game_over(res_life,2)
            res1 = self.result_collide_hero_shield()
            key_down = self.checkevent.check_event_key()
            self.result_direction_hero1(res1, key_down)

            res_life1 = self.result_collide_hero()
            self.game_over(res_life1,2)
            self.result_direction_hero2(res1, key_down)

            self.screen.blit(self.font.render("score:{0}".format(int(self.fenshu / 3)), True, (255, 0, 0)), (20, 20))

            pygame.display.update()

    def over_show(self):
        '''
        结束页面
        :return:
        '''
        self.__game_music(game_data.music_two)
        self.create_screen("over_game")
        while True:
            self.clock.tick(24)
            self.__update_screen()
            res = self.checkevent.check_event()
            key_down = self.checkevent.check_event_key()
            if res == "exit":
                pygame.quit()
                exit()
            if res == "danren":
                self.background_group.empty()
                self.start()
            if res == "shuangren":
                pygame.quit()
                exit()

            self.screen.blit(self.font.render("{0}".format(int(self.fenshu / 3)), True, (255, 0, 0)), (230, 280))
            pygame.display.update()

    def start(self):

        global num
        num = 0
        self.__game_music(game_data.music_start)
        game_choice = self.start_show()
        if game_choice == "exit":
            pygame.quit()
            exit()
        elif game_choice == "danren":
            self.start_one()
        elif game_choice == "shuangren":
            self.start_two()
        elif game_choice == "tuichu":
            pygame.quit()
            exit()
