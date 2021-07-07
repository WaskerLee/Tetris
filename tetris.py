import pygame
import sys
import time

pygame.init()


# 定义主窗口的尺寸
win_width = 480
win_height = 853
background_image = 'images/bg.png'

# 俄罗斯游戏窗口的内容
class Tetris(object):
    def __init__(self):
        pass

    def run(self):
        print('I am running.')

# 游戏主窗口
class Game(object):
    def __init__(self, screen_width, screen_height, background_image):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.background_image = background_image

    def run(self):
        tetris = Tetris()
        # 定义窗口对象
        win_main = pygame.display.set_mode((self.screen_width, self.screen_height))

        # 加载logo图片
        background = pygame.image.load(self.background_image)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

                # 判断按键被按下
                if event.type == pygame.KEYDOWN:
                    tetris.run()

            win_main.blit(background, (0, 0))
            pygame.display.flip()
            time.sleep(1)


if '__main__' == __name__:
    game = Game(win_width, win_height, background_image)
    game.run()


