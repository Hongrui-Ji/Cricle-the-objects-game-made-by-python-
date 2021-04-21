import sys
import pygame
import maingame
import Rules_description

#定义一个类来收纳每个选项
def options():
    class Option:
        hovered = False
        clicked = False

        def __init__(self, text, pos):
            self.text = text
            self.pos = pos
            self.set_rect()
            self.draw()

        def draw(self):
            self.set_rend()
            screen.blit(self.rend, self.rect)

        def set_rend(self):
            self.rend = menu_font.render(self.text, True, self.get_color())  #渲染函数

        def get_color(self):
            if self.hovered:
                if self.clicked:
                    return (255, 0, 0)  #点击时为红色
                else:
                    return (255, 255, 255)  #悬停时为白色
            else:
                return (100, 100, 100)   #默认为灰色

        def set_rect(self):
            self.set_rend()
            self.rect = self.rend.get_rect()
            self.rect.topleft = self.pos

        def new_window(self):
            if self.clicked:
                screen.fill((159, 182, 205))
            else:
                pass

    pygame.init()
    screen = pygame.display.set_mode((1080, 720))
    pygame.display.set_caption('Menu')
    menu_font = pygame.font.SysFont('arial', 40)

    #定义选项中的元素
    options = [Option("Difficulty-Normal",(400,250)),Option("Difficulty-Devil",(400,300)),Option("Rules and Description", (400, 350)),Option("Exit", (400, 400))]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()  #按下esc退出

        #pygame.event.pump()
        screen.fill((0, 0, 0))#背景设置为黑色

        #对第一个option执行操作
        for option in options:
            if options[0].rect.collidepoint(pygame.mouse.get_pos()):
                options[0].hovered = True #悬停时改为True,从而改变颜色
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    options[0].clicked = True
                    maingame.main1()  #点击时bool为True,并且运行main1()

                else:
                    options[0].clicked = False  #没有点击则为false
            else:
                options[0].hovered = False
                options[0].clicked = False   #没有悬停时，两个都为false。

        #对第二个option执行操作
            if options[1].rect.collidepoint(pygame.mouse.get_pos()):
                options[1].hovered = True
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    options[1].clicked = True
                    maingame.main2()     #运行main2()
                else:
                    options[1].clicked = False
            else:
                options[1].hovered = False
                options[1].clicked = False

        #对第三个optionn执行操作
            if options[2].rect.collidepoint(pygame.mouse.get_pos()):
                options[2].hovered = True
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    options[2].clicked = True
                    Rules_description.rules()   #跳转值rule界面

                else:
                    options[2].clicked = False
            else:
                options[2].hovered = False
                options[2].clicked = False

            if options[3].rect.collidepoint(pygame.mouse.get_pos()):
                options[3].hovered = True
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    options[3].clicked = True
                    pygame.quit()
                    sys.exit()    #直接退出
                else:
                    options[3].clicked = False
            else:
                options[3].hovered = False
                options[3].clicked = False

            #对每一个option执行渲染操作使其显示再屏幕上
            options[0].draw()
            options[1].draw()
            options[2].draw()
            options[3].draw()
            option.new_window()
        pygame.display.update()
