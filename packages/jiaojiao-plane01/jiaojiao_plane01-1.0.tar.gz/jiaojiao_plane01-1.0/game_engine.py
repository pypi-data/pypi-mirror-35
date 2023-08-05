'''
游戏引擎：控制游戏流程
'''
import game_sprites
import pygame
import time

# 自定义一个事件
ENEMY_CREATE = pygame.USEREVENT
pygame.time.set_timer(ENEMY_CREATE, 1000)


class GameEngine:
    """游戏引擎类型"""

    def __init__(self):
        # 初始化所有模块
        pygame.init()

        # 定义游戏窗口
        self.screen = pygame.display.set_mode(game_sprites.SCREEN_SIZE)

        # 定义背景和英雄飞机精灵组对象
        self.resources = pygame.sprite.Group()

        # 定义敌人飞机精灵组对象
        self.enemys = pygame.sprite.Group()

        # 定义时钟对象
        self.clock = pygame.time.Clock()

        # 音乐精灵组
        self.music = game_sprites.Music()

        # 敌机爆炸精灵组
        self.bombs = pygame.sprite.Group()

        # 定义份数
        self.num = 0

    def fen_shu(self):

        self.font = pygame.font.SysFont("宋体", 50, True, True)
        self.score = self.font.render("score: %s" % self.num, True, (255, 0, 255))

    def create_scene(self):
        """创建游戏背景、英雄飞机
            把游戏中的精灵添加到精灵组中
        """
        # self.resources.empty()
        bg1 = game_sprites.BackgroundSprite("./images/bg_img_1.jpg", 1)
        bg2 = game_sprites.BackgroundSprite("./images/bg_img_1.jpg", 1, perpare = True)
        self.hero = game_sprites.HeroSprite("./images/hero_1.png", speed=0)
        self.resources.add(bg1, bg2, self.hero)
        # 将精灵对象添加到精灵组对象中

    def update_scene(self):
        """渲染场景:把精灵组渲染到屏幕中"""

        # 背景和英雄飞机精灵组更新渲染
        self.resources.update()
        self.resources.draw(self.screen)
        self.screen.blit(self.score, (10, 10))

        # 英雄飞机子弹精灵组更新渲染
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

        # 敌人飞机精灵组更新渲染
        self.enemys.update()
        self.enemys.draw(self.screen)

    def check_collide(self):
        """碰撞检测"""

        # 两种碰撞方式:1.子弹和敌方飞机
        self.bombs.add(pygame.sprite.groupcollide(self.enemys, self.hero.bullets, True, True))
        for enemy_bomb in self.bombs:
            self.num += 2
            print(self.num)
            self.bomb(enemy_bomb)
            self.music.bomb_music()
            self.bombs.remove(enemy_bomb)

        # 2.英雄飞机和敌方飞机之间
        e = pygame.sprite.spritecollide(self.hero, self.enemys, True)
        if len(e) > 0:
            self.num = 0
            self.music.bomb_music()
            time.sleep(1)
            self.hero.kill()
            self.game_over()

    def show_index(self):
        """展示首页"""

        # 首页精灵
        self.index = game_sprites.Index("./images/shou_ye_1.jpg")
        self.resources.add(self.index)

        while True:
            self.resources.draw(self.screen)
            self.resources.update()
            pygame.display.update()
            # 键盘事件监听
            key_down = pygame.key.get_pressed()
            event_list = pygame.event.get()
            if len(event_list) > 0:
                # print(event_list)

                for event in event_list:
                    # 如果当前事件为QUIT事件
                    if event.type == pygame.QUIT:
                        # 卸载所有资源，退出程序
                        pygame.quit()
                        exit()
            if key_down[pygame.K_a]:
                print("游戏开始...")
                self.resources.empty()
                return self.start()

    def game_over(self):
        """结束界面"""
        game_over_bg = pygame.image.load("./images/game_over_bg.jpg")
        self.screen.blit(game_over_bg, (0, 0))
        self.screen.blit(self.score, (160, 200))
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 150 <= event.pos[0] <= 400 and 450 <= event.pos[1] <= 550:
                        self.resources.empty()
                        self.enemys.empty()
                        self.start()
                    elif 150 <= event.pos[0] <= 400 and 550 <= event.pos[1] <= 650:
                        pygame.quit()
                        exit()
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

    def check_event(self):
        """监听所有事件"""

        # 隔一段时间创建一家敌方飞机
        event_list = pygame.event.get()
        if len(event_list) > 0:
            for event in event_list:
                # 如果当前事件为QUIT事件
                if event.type == pygame.QUIT:
                    # 卸载所有资源，退出程序
                    pygame.quit()
                    exit()
                if event.type == ENEMY_CREATE:
                    print("创建一家敌方飞机...")
                    enemy = game_sprites.EnemySprite()
                    # 添加到敌方飞机精灵组中
                    self.enemys.add(enemy)

        # 键盘监听
        key_down = pygame.key.get_pressed()

        if key_down[pygame.K_LEFT]:
            print("飞机向左移动<<<")
            self.hero.rect.x -= 5
        if key_down[pygame.K_RIGHT]:
            print("飞机向右移动>>>")
            self.hero.rect.x += 5
        if key_down[pygame.K_UP]:
            print("飞机向上移动^^^")
            self.hero.rect.y -= 5
        if key_down[pygame.K_DOWN]:
            print("飞机向下移动vvv")
            self.hero.rect.y += 5
        if key_down[pygame.K_SPACE]:
            self.hero.fire()
            self.music.bullet_music()
            print("子弹发射",self.hero.bullets)

    def bomb(self, enemy):
        """子弹爆炸效果"""
        for img_path in ["./images/bomb1.png", "./images/bomb2.png", "./images/bomb3.png"]:
            image = pygame.image.load(img_path)
            self.screen.blit(image, (enemy.rect.x + 20, enemy.rect.y))
            pygame.display.update()
            # self.bombs.draw(self.screen)

    def start(self):
        print("游戏开始...")
        # 刷新游戏帧率
        self.clock.tick(24)
        self.create_scene()
        self.music.back_music()

        while True:

            # 调用分数方法
            self.fen_shu()
            # 更新绘制、渲染精灵组
            self.update_scene()
            # 事件监听
            self.check_event()
            # 碰撞检测
            self.check_collide()
            # 游戏更新展示
            pygame.display.update()

