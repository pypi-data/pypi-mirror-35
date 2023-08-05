
"""
游戏引擎，控制游戏流程
"""
import game_sprites, pygame

pygame.init()


class GameEngine():
    # 播放背景音乐
    game_sprites.pygame.mixer.music.play(-1)


    def start(self):
        # game_sprites.hero_score = 0

        while True:
            # 定义时钟频率
            game_sprites.clock.tick(60)

            #监听键盘上的事件
            key_down = pygame.key.get_pressed()
            if key_down[pygame.K_LEFT]:
                print("向左移动")
                game_sprites.hero.rect.x -= 5

            elif key_down[pygame.K_RIGHT]:
                print("向右移动")
                game_sprites.hero.rect.x += 5

            elif key_down[pygame.K_UP]:
                print("向上移动")
                game_sprites.hero.rect.y -= 5

            elif key_down[pygame.K_DOWN]:
                print("向下移动")
                game_sprites.hero.rect.y += 5

            elif key_down[pygame.K_r]:
                print("发射大招")
                game_sprites.hero.da()

            elif key_down[pygame.K_e]:
                print("英雄触发保护罩")

                game_sprites.hero.safe()

            if key_down[pygame.K_w]:
                print("开s型火")
                game_sprites.hero.fire2()

            if key_down[pygame.K_SPACE]:
                print("开火")
                game_sprites.hero.fire1()

            #监听窗口中的事件
            event_list = pygame.event.get()
            for event in event_list:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

                if event.type == game_sprites.CREATE_ENEMY:
                    #创建一架敌机
                    print("创建一架敌机")
                    enemy = game_sprites.EnemySprite()
                    game_sprites.enemys.add(enemy)
                    #出发敌机的攻击事件
                    enemy.fire()

            #渲染背景和英雄飞机精灵组
            game_sprites.resource.update()
            game_sprites.resource.draw(game_sprites.screen)

            #渲染敌机精灵组
            game_sprites.enemys.update()
            game_sprites.enemys.draw(game_sprites.screen)

            #渲染英雄的子弹精灵组
            game_sprites.hero.bullets.update()
            game_sprites.hero.bullets.draw(game_sprites.screen)

            #渲染敌机的子弹精灵组
            game_sprites.enemy_bullets.update()
            game_sprites.enemy_bullets.draw(game_sprites.screen)

            #英雄子弹和敌军子弹的碰撞
            pygame.sprite.groupcollide(game_sprites.enemy_bullets,game_sprites.hero.bullets, True, True)


            #英雄子弹组和敌机组的碰撞检测
            a = pygame.sprite.groupcollide(game_sprites.hero.bullets, game_sprites.enemys, True, True)
            if len(a) > 0:
                game_sprites.bz.play()
                game_sprites.hero_score += 1

            #英雄飞机和敌机子弹组的碰撞检测
            e = pygame.sprite.spritecollide(game_sprites.hero, game_sprites.enemy_bullets, True)
            if len(e) > 0:

                # 用户选择继续游戏还是退出游戏
                over = pygame.image.load("./images/over.jpg")
                game_sprites.screen.blit(over, (0, 0))
                pygame.display.update()
                while True:
                    for event in pygame.event.get():     #获得事件
                        #继续游戏
                        if event.type == pygame.MOUSEBUTTONDOWN:  # 判断鼠标位置以及是否摁了下去。
                            if 173 <= event.pos[0] <= 360 and 490 <= event.pos[1] <= 557:
                                # 把敌机清屏继续游戏
                                game_sprites.enemys.empty()
                                game_sprites.enemy_bullets.empty()
                                return engine.start()

                        #退出游戏
                        if event.type == pygame.MOUSEBUTTONDOWN:  # 判断鼠标位置以及是否摁了下去。
                            if 173 <= event.pos[0] <= 360 and 602 <= event.pos[1] <= 667:
                                pygame.quit()
                                exit()

                        elif event.type == pygame.QUIT:
                            pygame.quit()
                            exit()

            #英雄和敌机组的碰撞检测
            e = pygame.sprite.spritecollide(game_sprites.hero, game_sprites.enemys, True)
            if len(e) > 0:
                #用户选择继续游戏还是退出游戏
                over = pygame.image.load("./images/over.jpg")
                game_sprites.screen.blit(over, [0, 0])
                pygame.display.update()
                while True:
                    for event in pygame.event.get():  # 获得事件
                        #继续游戏
                        if event.type == pygame.MOUSEBUTTONDOWN:  # 判断鼠标位置以及是否摁了下去。
                            if 173 <= event.pos[0] <= 360 and 490 <= event.pos[1] <= 557:
                                # 把敌机清屏继续游戏。
                                game_sprites.enemys.empty()
                                game_sprites.enemy_bullets.empty()
                                game_sprites.hero_score = 0
                                return engine.start()

                        #退出游戏
                        if event.type == pygame.MOUSEBUTTONDOWN:  # 判断鼠标位置以及是否摁了下去。
                            if 173 <= event.pos[0] <= 360 and 602 <= event.pos[1] <= 667:
                                # 退出游戏
                                pygame.quit()
                                exit()

                        elif event.type == pygame.QUIT:
                            pygame.quit()

            #显示英雄积分
            font = pygame.font.Font("./musics/font.ttf", 40)
            if game_sprites.hero_score < 3:
                a = font.render("score: %s" % game_sprites.hero_score, True, (255, 255, 255))
                game_sprites.screen.blit(a, (350, 40))
                #屏幕渲染
                pygame.display.update()

##########################################################################################

            elif game_sprites.hero_score >= 3:

                game_sprites.resource.empty()
                game_sprites.enemys.empty()
                game_sprites.enemy_bullets.empty()

                boss_flag = False
                while True:

                    # 监听键盘上的事件
                    key_down = pygame.key.get_pressed()
                    if key_down[pygame.K_LEFT]:
                        print("向左移动")
                        game_sprites.hero2.rect.x -= 5


                    elif key_down[pygame.K_RIGHT]:
                        print("向右移动")
                        game_sprites.hero2.rect.x += 5

                    elif key_down[pygame.K_UP]:
                        print("向上移动")
                        game_sprites.hero2.rect.y -= 5

                    elif key_down[pygame.K_DOWN]:
                        print("向下移动")
                        game_sprites.hero2.rect.y += 5

                    elif key_down[pygame.K_r]:
                        print("发射大招")
                        game_sprites.hero2.da()

                    # elif key_down[pygame.K_e]:
                    #     print("英雄触发保护罩")
                    #     game_sprites.hero2.safe()
                    # 定义英雄的保护罩
                    elif key_down[pygame.K_e]:
                        print("创建一个保护罩")
                        safe1 = game_sprites.SafeSprite("./images/safe.png", game_sprites.hero2.rect.centerx - 130, game_sprites.hero2.rect.y - 100, speed=0)
                        game_sprites.safe_resource.add(safe1)

                    if key_down[pygame.K_w]:
                        print("英雄触发s型子弹")
                        game_sprites.hero2.fire2()

                    if key_down[pygame.K_SPACE]:
                        print("开火")
                        game_sprites.hero2.fire1()


                    # 监听窗口中的事件
                    event_list = pygame.event.get()
                    for event in event_list:
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()

                        if event.type == game_sprites.CREATE_ENEMY:
                            # 创建一架敌机
                            print("创建一架敌机")
                            enemy = game_sprites.EnemySprite()
                            game_sprites.enemys.add(enemy)
                            # 出发敌机的攻击事件
                            n = 0
                            while True:
                                n += 1
                                if n < 10:
                                    enemy.fire()
                                    pygame.display.update()
                                else:
                                    break

                        # 创建一架boss机
                        if event.type == game_sprites.CREATE_ENEMY2:
                            print("创建一架boss机")
                            boss = game_sprites.BossSprite()
                            game_sprites.boss_resource.add(boss)
                            boss_flag = True
                            # 创建boss的子弹：

                        #创建一个boss子弹
                        if event.type == game_sprites.CREATE_BULLET:
                            print("创建boss的子弹")
                            if boss_flag:
                                boss.fire()


                        # #创建一个礼包
                        if event.type == game_sprites.CREATE_LB:
                            print("创建一个礼包")
                            enemy.lb()


                    #第二关英雄和背景的渲染
                    game_sprites.resource2.update()
                    game_sprites.resource2.draw(game_sprites.screen)

                    #第二关敌机的渲染
                    game_sprites.enemys.update()
                    game_sprites.enemys.draw(game_sprites.screen)

                    # 第二关渲染英雄的子弹精灵组
                    game_sprites.hero2.bullets.update()
                    game_sprites.hero2.bullets.draw(game_sprites.screen)

                    game_sprites.boss_resource.update()
                    game_sprites.boss_resource.draw(game_sprites.screen)

                    # 第二关渲染敌机的子弹精灵组
                    game_sprites.enemy_bullets.update()
                    game_sprites.enemy_bullets.draw(game_sprites.screen)

                    #渲染礼包的精灵组
                    game_sprites.lb_resource.update()
                    game_sprites.lb_resource.draw(game_sprites.screen)

                    #渲染保护套
                    # game_sprites.safe_resource.update()
                    # game_sprites.safe_resource.draw(game_sprites.screen)
                    #


                    #设置boss机精灵组和英雄子弹组的碰撞
                    a = pygame.sprite.groupcollide(game_sprites.boss_resource, game_sprites.hero2.bullets, False, True)
                    if len(a) > 0:
                        game_sprites.boss_score -= 1
                        if game_sprites.boss_score <= 0:
                            game_sprites.boss_score = 150
                            game_sprites.hero_score += 1
                            boss.kill()

                    #英雄子弹组和敌机组的碰撞检测
                    a = pygame.sprite.groupcollide(game_sprites.hero2.bullets, game_sprites.enemys, True, True)
                    if len(a) > 0:
                        game_sprites.bz.play()
                        game_sprites.hero_score += 1

                        #分数封顶之后显示的胜利界面
                        if game_sprites.hero_score == 50:
                            over = pygame.image.load("./images/win.png")
                            game_sprites.screen.blit(over, [0, 0])
                            pygame.display.update()
                            while True:
                                for event in pygame.event.get():  # 获得事件
                                    # 继续游戏
                                    if event.type == pygame.MOUSEBUTTONDOWN:  # 判断鼠标位置以及是否摁了下去。
                                        if 173 <= event.pos[0] <= 360 and 490 <= event.pos[1] <= 557:
                                            # 把敌机清屏继续游戏
                                            game_sprites.enemys.empty()
                                            game_sprites.enemy_bullets.empty()
                                            game_sprites.boss_resource.empty()
                                            game_sprites.hero_score = 0

                                            return engine.start()

                                    # 退出游戏
                                    if event.type == pygame.MOUSEBUTTONDOWN:  # 判断鼠标位置以及是否摁了下去。
                                        if 173 <= event.pos[0] <= 360 and 602 <= event.pos[1] <= 667:
                                            pygame.quit()
                                            exit()

                                    elif event.type == pygame.QUIT:
                                        pygame.quit()
                                        exit()




                    # 第二关英雄飞机和敌机子弹组的碰撞检测
                    e = pygame.sprite.spritecollide(game_sprites.hero2, game_sprites.enemy_bullets, True)
                    if len(e) > 0:
                        # 用户选择继续游戏还是退出游戏
                        over = pygame.image.load("./images/over.jpg")
                        game_sprites.screen.blit(over, (0, 0))
                        pygame.display.update()
                        while True:
                            for event in pygame.event.get():  # 获得事件
                                # 继续游戏
                                if event.type == pygame.MOUSEBUTTONDOWN:  # 判断鼠标位置以及是否摁了下去。
                                    if 173 <= event.pos[0] <= 360 and 490 <= event.pos[1] <= 557:
                                        # 把敌机清屏继续游戏
                                        game_sprites.enemys.empty()
                                        game_sprites.enemy_bullets.empty()
                                        game_sprites.boss_resource.empty()
                                        pygame.display.update()
                                        #game_sprites.hero_score = 0
                                        return engine.start()
                                        # interface.start()

                                # 退出游戏
                                if event.type == pygame.MOUSEBUTTONDOWN:  # 判断鼠标位置以及是否摁了下去。
                                    if 173 <= event.pos[0] <= 360 and 602 <= event.pos[1] <= 667:
                                        pygame.quit()
                                        exit()

                                elif event.type == pygame.QUIT:
                                    pygame.quit()
                                    exit()

                    # 第二关英雄和敌机组的碰撞检测
                    e = pygame.sprite.spritecollide(game_sprites.hero2, game_sprites.enemys, True)
                    if len(e) > 0:

                        # 用户选择继续游戏还是退出游戏
                        over = pygame.image.load("./images/over.jpg")
                        game_sprites.screen.blit(over, [0, 0])
                        pygame.display.update()
                        while True:
                            for event in pygame.event.get():  # 获得事件
                                # 继续游戏
                                if event.type == pygame.MOUSEBUTTONDOWN:  # 判断鼠标位置以及是否摁了下去。
                                    if 173 <= event.pos[0] <= 360 and 490 <= event.pos[1] <= 557:
                                        # 把敌机清屏继续游戏。
                                        game_sprites.enemys.empty()
                                        game_sprites.enemy_bullets.empty()
                                        game_sprites.boss_resource.empty()
                                        #game_sprites.hero_score = 0
                                        engine.start()

                                # 退出游戏
                                if event.type == pygame.MOUSEBUTTONDOWN:  # 判断鼠标位置以及是否摁了下去。
                                    if 173 <= event.pos[0] <= 360 and 602 <= event.pos[1] <= 667:
                                        # 退出游戏
                                        pygame.quit()
                                        exit()

                                elif event.type == pygame.QUIT:
                                    pygame.quit()

                    #第二关英雄子弹和敌机子弹的碰撞之后小飞机的子弹可以销毁：
                    pygame.sprite.groupcollide(game_sprites.hero2.bullets, game_sprites.enemy_bullets, True, True)


                    #礼包和英雄的碰撞检测
                    a = pygame.sprite.spritecollide(game_sprites.hero2, game_sprites.lb_resource, True)
                    if len(a) > 0:
                        game_sprites.hero2.da()


                    #显示积分
                    font = pygame.font.Font("./musics/font.ttf", 40)
                    a = font.render("score: %s" % game_sprites.hero_score, True, (255, 255, 255))
                    game_sprites.screen.blit(a, (350, 40))
                    pygame.display.update()



#创建引擎对象
engine = GameEngine()


#游戏开始选择界面
class Interface():
    def start(self):
        # game_sprites.hero_score = 0
        game_sprites.screen.fill([128, 128, 128])       #用灰色填充窗口
        begin = pygame.image.load("./images/start.jpg") #加载开始界面的图片
        game_sprites.screen.blit(begin, [0, 200])       #在离x和y多远处渲染图片
        pygame.display.flip()
        while True:
            for event in pygame.event.get():    #获得事件
                if event.type == pygame.MOUSEBUTTONDOWN:           #判断鼠标位置以及是否摁了下去。
                    if event.button == 1:  #鼠标左键，3是鼠标右键
                        if 180 <= event.pos[0] <= 360 and 292 <= event.pos[1] <= 365:
                            #开始游戏
                            engine.start()

                elif event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

interface =Interface()
