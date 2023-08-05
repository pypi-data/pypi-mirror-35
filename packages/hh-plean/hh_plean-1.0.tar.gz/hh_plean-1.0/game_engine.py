# 引入模块
import pygame, game_sprites
# 初始化模块
pygame.init()
# 音乐初始化
# pygame.mixer.init()
# # 加载音乐路径
# pygame.mixer.music.load("./musics/bg_music2.mp3")
# # 设置音量大小
# pygame.mixer.music.set_volume(0.2)
# 播放次数
# pygame.mixer.music.play(0)
# 添加背景
class GameEngine():

    bg1 = game_sprites.BackgroundSprite("./images/bj.png")
    bg2 = game_sprites.BackgroundSprite("./images/bj.png", True)
    # 添加英雄
    hero = game_sprites.HeroSprite("./images/both2.png")
    # 将精灵添加到精灵组中
    game_sprites.resources.add(bg1, bg2, hero)
    #创建敌机到精灵组
    enemys = game_sprites.EnemySprite()




    def start(self):
        while True:
            # 定义时钟刷新帧
            game_sprites.clock.tick(24)
            # game_sprites.pygame.mixer.music.play()
            # 事件数据获取
            event_list = pygame.event.get()
            if len(event_list) > 0:
                print(event_list)
                for event in event_list:
                    print(event.type)
                    # 判断是否为退出事件
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    # 敌机创建
                    if event.type == game_sprites.ENEMY_CREATE:
                        print("创建一架敌机")
                        enemy = game_sprites.EnemySprite()
                        game_sprites.enemys.add(enemy)
                    # 敌机发射子弹
                    if event.type == game_sprites.ENEMY_CREATES:
                        self.enemys.fire()
                    # 发射大招
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_1:
                            self.hero.fires()
                            self.hero.fires1()
                            self.hero.fires2()
                            print('发射大招', self.hero.fires())
                # 敌机发射子弹
                # self.enemys.fire()
                    # 创建boss
                    if event.type == game_sprites.BOSS_CREATE:
                        print("创建boss")
                        boss = game_sprites.EnemyBase("./images/boss1.png")
                        game_sprites.green.add(boss)


            # 获取用户键盘操作
            key_down = pygame.key.get_pressed()
            if key_down[pygame.K_LEFT]:
                print("向左移动")
                self.hero.rect.x -= 12
            elif key_down[pygame.K_RIGHT]:
                print("向右移动")
                self.hero.rect.x += 12
            elif key_down[pygame.K_UP]:
                print("向上移动")
                self.hero.rect.y -= 8
            elif key_down[pygame.K_DOWN]:
                print("向下移动")
                self.hero.rect.y += 8

            if key_down[pygame.K_CAPSLOCK]:
                print("自动发射子弹")
                self.hero.fire1()
                self.hero.fire2()
            # if key_down[pygame.K_a]:
            #     print("发射大招")
            #     self.hero.fires()



            if key_down[pygame.K_SPACE]:
                print("发射子弹")
                self.hero.fire()


            # 英雄子弹敌机碰撞检测
            b = pygame.sprite.groupcollide(self.hero.bullets, game_sprites.enemys, True, True)

            # 英雄子弹与敌机子弹碰撞
            pygame.sprite.groupcollide(self.hero.bullets1, game_sprites.shot, True, True)
            # 英雄大招与子弹碰撞
            pygame.sprite.groupcollide(self.hero.bullets2, game_sprites.shot, False, True)
            pygame.sprite.groupcollide(self.hero.bullets2, game_sprites.enemys, False, True)
            # 英雄子弹与敌机碰撞
            c = pygame.sprite.groupcollide(self.hero.bullets1, game_sprites.enemys, True, True)
            if len(c or b) > 0:
                game_sprites.hero_score += 1
                print("______%s_______"%game_sprites.hero_score)
            # 英雄与敌机子弹碰撞
            l = pygame.sprite.spritecollide(self.hero, game_sprites.shot, True)
            # 英雄敌机碰撞检测
            e = pygame.sprite.spritecollide(self.hero, game_sprites.enemys, True)
            # 英雄子弹与BOSS碰撞检测
            h = pygame.sprite.groupcollide(self.hero.bullets1, game_sprites.green, True, False)
            j = pygame.sprite.groupcollide(self.hero.bullets, game_sprites.green, True, False)
            k = pygame.sprite.groupcollide(self.hero.bullets2, game_sprites.green, True, False)
            if len(h or j and k) > 0:
                game_sprites.boss_score -= 3
                if game_sprites.boss_score <= 0:
                    game_sprites.boss_score = 300
                    game_sprites.hero_score += 5

                    boss.kill()


            if len(e or l) > 0:
                self.hero.kill()
                pygame.quit()
                exit()




            # 背景英雄飞机精灵组渲染
            game_sprites.resources.update()
            game_sprites.resources.draw(game_sprites.screen)
            # 子弹精灵组渲染
            self.hero.bullets.update()
            self.hero.bullets.draw(game_sprites.screen)
            # 子弹精灵组渲染
            self.hero.bullets1.update()
            self.hero.bullets1.draw(game_sprites.screen)

            self.hero.bullets2.update()
            self.hero.bullets2.draw(game_sprites.screen)
            # 敌机boss渲染
            game_sprites.green.update()
            game_sprites.green.draw(game_sprites.screen)
            # 敌机精灵组渲染
            game_sprites.enemys.update()
            game_sprites.enemys.draw(game_sprites.screen)
            # 敌机子弹精灵组渲染
            game_sprites.shot.update()
            game_sprites.shot.draw(game_sprites.screen)


            # 展示分数
            font = pygame.font.Font("./musics/Marker Felt.ttf", 40)
            a = font.render("score:%s" % game_sprites.hero_score, True, (255, 255, 255))
            game_sprites.screen.blit(a, (350, 40))
            # 屏幕更新
            pygame.display.update()








