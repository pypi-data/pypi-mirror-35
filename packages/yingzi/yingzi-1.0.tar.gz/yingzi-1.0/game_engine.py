#coding:utf-8
import pygame,game_sprites

# #初始化所有模块
pygame.init()
#定义字体大小
score_font=pygame.font.Font("./image/font.ttf",40)

class GameEngine():
    #定义背景精灵
    bg1 = game_sprites.BackgroundSprite("./image/img_1.jpg")
    bg2 = game_sprites.BackgroundSprite("./image/img_1.jpg", prepare=True)
    bg3=game_sprites.BackgroundSprite("./image/level2.jpg")
    bg4=game_sprites.BackgroundSprite("./image/level2.jpg",prepare=True)
    # 定义英雄对象
    hero = game_sprites.HeroSprite()

    # 初始化精灵族对象
    resources = pygame.sprite.Group(bg1, bg2,hero)

    def star(self):
        score=0
    #游戏场景循环
        while True:
            game_sprites.clock.tick(24)

            #监听所有事件
            event_list=pygame.event.get()
            if len(event_list)>0:
                print(event_list)
                for event in event_list:
                    print(event.type,pygame.KEYDOWN,pygame.K_LEFT)
                    if event.type==pygame.QUIT:
                        pygame.quit()
                        exit()

                    if event.type==game_sprites.ENEMY_CREATE:
                        print("创建一架敌军飞机...")

                        enemya=game_sprites.EnemyaSprite()
                        #添加到敌方飞机精灵族

                        game_sprites.enemys.add(enemya)

                        enemya.fire()
                    if event.type == game_sprites.MID_CREATE:
                        enemy = game_sprites.EnemySprite()
                        game_sprites.enemys.add(enemy)
                        enemy.fire()
                    if event.type==game_sprites.BOSS_CREATE:
                        boss = game_sprites.BossSprite()
                        game_sprites.bossa.add(boss)
                        boss.fire()



            #获取当前用户键盘上被操作的按键
            key_down=pygame.key.get_pressed()

            if key_down[pygame.K_LEFT]:
                print("向左移动")
                self.hero.rect.x-=5
            if key_down[pygame.K_RIGHT]:
                print("向右移动")
                self.hero.rect.x+=5
            if key_down[pygame.K_UP]:
                print("向上移动")
                self.hero.rect.y-=5
            if key_down[pygame.K_DOWN]:
                print("向下移动")
                self.hero.rect.y+=5
            if key_down[pygame.K_SPACE]:
                self.hero.fire()
                print("发射子弹",self.hero.bullets)
            #碰撞检测 boss 和英雄飞机子弹
            bs = pygame.sprite.groupcollide(self.hero.bullets, game_sprites.bossa, True, False)

            if len(bs) > 0:
                boss.life -= 1
                if boss.life <= 0:
                    boss.life=15
                    boss+=1
                    boss.kill()

            #碰撞检测 子弹和敌方飞机
            a=pygame.sprite.groupcollide(self.hero.bullets,game_sprites.enemys,True,True)
            #子弹和子弹
            pygame.sprite.groupcollide(self.hero.bullets,game_sprites.enemy_bullets,True,True)
            #敌军子弹和英雄飞机
            p=pygame.sprite.spritecollide(self.hero,game_sprites.enemy_bullets ,True)
            e = pygame.sprite.spritecollide(self.hero, game_sprites.enemys, True)
            if len(e) > 0 or len(p) > 0:
                self.hero.blood -= 1
                if bloods == 0:
                        self.hero.kill()
                #玩家选择继续游戏还是退出游戏
                choice=pygame.image.load('./image/over.jpg')
                game_sprites.screen.blit(choice,[0,0])
                pygame.display.update()
                while True:
                    for event in pygame.event.get():
                        print(event)
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            if 190<=event.pos[0]<=370 and 425 <=event.pos[1]<=490:
                                engine.star()
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            if 190 <= event.pos[0] <= 370 and 550 <= event.pos[1] <= 615:
                                pygame.quit()
                                exit()
                        elif event.type == pygame.QUIT:
                            pygame.quit()
                            exit()

            # 精灵族渲染
            self.resources.update()
            self.resources.draw(game_sprites.screen)

            # 子弹组渲染
            self.hero.bullets.update()
            self.hero.bullets.draw(game_sprites.screen)
            # 敌军所有飞机渲染
            game_sprites.enemys.update()
            game_sprites.enemys.draw(game_sprites.screen)
            # 英雄飞机渲染

            #敌机子弹渲染
            game_sprites.enemy_bullets.update()
            game_sprites.enemy_bullets.draw(game_sprites.screen)
            game_sprites.bossa.update()
            game_sprites.bossa.draw(game_sprites.screen)


            score_text =score_font.render("Score : %s" %str(score), True, (0, 0, 0))
            game_sprites.screen.blit(score_text, (20, 20))
            bloods=self.hero.blood
            hero_blood = score_font.render("blood : %s" % bloods, True, (0, 0, 0))
            game_sprites.screen.blit(hero_blood, (360, 20))
            pygame.display.update()
            if len(a)>0:
                score +=100
                game_sprites.bomb.play()
                if score>5000:

                    self.resources.empty()
                    game_sprites.enemys.empty()
                    game_sprites.enemy_bulltes.empty()
                    while True:
                        game_sprites.clock.tick(24)

                        # 监听所有事件
                        event_list = pygame.event.get()
                        if len(event_list) > 0:
                            print(event_list)
                            for event in event_list:
                                print(event.type, pygame.KEYDOWN, pygame.K_LEFT)
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    exit()

                                if event.type == game_sprites.ENEMY_CREATE:
                                    print("创建一架敌军飞机...")
                                    enemy = game_sprites.EnemySprite()
                                    # 添加到敌方飞机精灵族
                                    game_sprites.enemys.add(enemy)
                                    enemy.fire()


                        # 获取当前用户键盘上被操作的按键
                        key_down = pygame.key.get_pressed()

                        if key_down[pygame.K_LEFT]:
                            print("向左移动")
                            self.hero.rect.x -= 5
                        if key_down[pygame.K_RIGHT]:
                            print("向右移动")
                            self.hero.rect.x += 5
                        if key_down[pygame.K_UP]:
                            print("向上移动")
                            self.hero.rect.y -= 5
                        if key_down[pygame.K_DOWN]:
                            print("向下移动")
                            self.hero.rect.y += 5
                        if key_down[pygame.K_SPACE]:
                            self.hero.fire()
                            print("发射子弹", self.hero.bullets)
                        e = pygame.sprite.spritecollide(self.hero, game_sprites.enemys, True)
                        if len(e)>0:
                            #玩家选择继续游戏还是退出游戏
                            choice=pygame.image.load('./image/over.jpg')
                            game_sprites.screen.blit(choice,[0,0])
                            pygame.display.update()
                            while True:
                                for event in pygame.event.get():
                                    print(event)
                                    if event.type==pygame.MOUSEBUTTONDOWN:
                                        if 190<=event.pos[0]<=370 and 425 <=event.pos[1]<=490:
                                            engine.star()
                                    if event.type==pygame.MOUSEBUTTONDOWN:
                                        if 190 <= event.pos[0] <= 370 and 550 <= event.pos[1] <= 615:
                                            pygame.quit()
                                            exit()
                                    elif event.type == pygame.QUIT:
                                        pygame.quit()
                                        exit()

                        game_sprites.bullet1.update()
                        game_sprites.bullet1.draw(game_sprites.screen)
                        # 精灵族渲染
                        self.resources.update()
                        self.resources.draw(game_sprites.screen)
                        # 子弹组渲染
                        self.hero1.bullets.update()
                        self.hero1.bullets.draw(game_sprites.screen)
                        #英雄飞机渲染
                        self.hero.update()
                        self.hero.draw(game_sprites.screen)
                        # 敌军所有飞机渲染
                        game_sprites.enemys.update()
                        game_sprites.enemys.draw(game_sprites.screen)
                        # 敌机子弹渲染
                        game_sprites.enemy_bullets.update()
                        game_sprites.enemy_bullets.draw(game_sprites.screen)
                        pygame.display.update()


            #碰撞检测 英雄飞机与敌方飞机
            e=pygame.sprite.spritecollide(self.hero,game_sprites.enemys,True)

            if len(e)>0 or len(p)>0:
                self.hero.blood-=1
            #   if bloods==0:
            #        self.hero.kill()
            #     #玩家选择继续游戏还是退出游戏
                choice=pygame.image.load('./image/over.jpg')
                game_sprites.screen.blit(choice,[0,0])
                pygame.display.update()
                while True:
                  for event in pygame.event.get():
                     print(event)
                     if event.type==pygame.MOUSEBUTTONDOWN:
                        if 190<=event.pos[0]<=370 and 425 <=event.pos[1]<=490:
                            engine.star()
                     if event.type==pygame.MOUSEBUTTONDOWN:
                        if 190 <= event.pos[0] <= 370 and 550 <= event.pos[1] <= 615:
                             pygame.quit()
                             exit()
                     elif event.type == pygame.QUIT:
                         pygame.quit()
                         exit()

            # 精灵族渲染
            self.resources.update()
            self.resources.draw(game_sprites.screen)

            # 子弹组渲染
            self.hero.bullets.update()
            self.hero.bullets.draw(game_sprites.screen)
            # 敌军所有飞机渲染
            game_sprites.enemys.update()
            game_sprites.enemys.draw(game_sprites.screen)
            # 英雄飞机渲染

            #敌机子弹渲染
            game_sprites.enemy_bullets.update()
            game_sprites.enemy_bullets.draw(game_sprites.screen)
            game_sprites.bossa.update()
            game_sprites.bossa.draw(game_sprites.screen)
        pygame.quit()
engine=GameEngine()
class Begin:
    #开始界面
    def start(self):
        #用灰色填充
        game_sprites.screen.fill([128,128,128])
        #把变量赋值给导入的图片
        picture=pygame.image.load("./image/start.png")
        #在120，120的地方画出图片
        game_sprites.screen.blit(picture,[126,308])
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                print(event)
                if event.type==pygame.MOUSEBUTTONDOWN and 126<=event.pos[0]<=386\
                 and 308<=event.pos[1]<=460:

                    engine.star()
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
begin=Begin()
begin.start()