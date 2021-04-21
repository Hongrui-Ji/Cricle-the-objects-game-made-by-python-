import sys
import pygame
import options

def rules():  #Rule界面
    SCREEN_HEIGHT = 720
    SCREEN_WIDTH = 1080
    pygame.init()
    playSurface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Rules and descriptionn')

    # 定义标题和文本两种字体
    white =255,255,255
    titlefont = pygame.font.SysFont('arial',40)
    wordfont = pygame.font.SysFont('arial',30)

    # 定义规则文字
    rule = titlefont.render("Rules:",True,white)
    ruledetails1 = wordfont.render('You can press \"W\" to move upward and \"D\" to move rightward',True,white)
    ruledetails2 = wordfont.render('then press \"Enter\" to stop moving and you can get whatever you circle!',True,white)

    # 定义建议文字
    Tips = titlefont.render("Tips:",True,white)
    tips1 = wordfont.render("\"Normal\" is easy and \"Devil\" is really devil!",True,white)

    # 定义描述文字
    Description  = titlefont.render('Description:',True,white)
    Description1 = wordfont.render('Originally Made by Hongrui Ji',True,white)
    Description2 = wordfont.render('Contact me if you want to use for Commercial: hongruiji0515@gmail.com',True,white)
    Description3 = wordfont.render('This project isn\'t completed, you can contact me to make it better!',True,white)
    escword = wordfont.render("(press \"ESC\" to go back to menu)",True,white)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()  #按下X退出窗口
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    options.options()  #按下esc返回option界面
        playSurface.fill((135, 206, 235))  # 设置游戏窗口背景色为天蓝色
        playSurface.blit(rule, (30, 30))
        playSurface.blit(ruledetails1,(130,100))
        playSurface.blit(ruledetails2,(130,150))
        playSurface.blit(Tips,(30,180))
        playSurface.blit(tips1,(130,250))
        playSurface.blit(Description,(30,350))
        playSurface.blit(Description1,(130,400))
        playSurface.blit(Description2,(130,450))
        playSurface.blit(Description3,(130,500))
        playSurface.blit(escword,(380,680))
        pygame.display.flip()  # 将文字刷新到屏幕

