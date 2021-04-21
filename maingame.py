import sys
import pygame
import time
import options

#Normal难度
def main1():
    direction = ''  # 用来标记图片运动方向，当为空串时，表示不运动
    SCREEN_HEIGHT = 720 # 游戏窗口高
    SCREEN_WIDTH = 1080  # 游戏窗口宽
    STEP = 50  # 图片每次运动的跨度（单位：像素）
    STEP1 = 75

    pygame.init()  # 初始化pygame模块
    playSurface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # 设置游戏窗口尺寸，并获得画布表面
    #原点在左上方
    pygame.display.set_caption('套圈圈')  # 设置游戏窗口标题

    white =255,255,255
    myfont = pygame.font.SysFont('arial',60)#定义自己的字体
    myfont1 = pygame.font.SysFont('arial',30)
    #文本+字体+颜色

    #定义奖励文字
    noaward = myfont.render("You get nothing",True,white)
    restart = myfont1.render("(Press r to restart)",True,white)
    award1  = myfont.render("You get the Bottled cola",True,white)
    award2  = myfont.render("You get the Canned cola", True, white)
    award3  = myfont.render("You get the Canned Pepsi", True, white)
    award4  = myfont.render("You get the Milk tea", True, white)
    award5  = myfont.render("You get the Thermos cup", True, white)
    award6  = myfont.render("You get the Plastic cup", True, white)
    award7  = myfont.render("You get the Basketball", True, white)
    award8  = myfont.render("You get the Football", True, white)
    award9  = myfont.render("You get the Apple", True, white)
    award10 = myfont.render("You get the Toy Bear", True, white)
    award11 = myfont.render("You get the Mouse", True, white)
    award12 = myfont.render("You get the Little cash", True, white)
    award13 = myfont.render("You get the Much money", True, white)
    award14 = myfont.render("You get the Casio", True, white)
    award15 = myfont.render("You get the Normal watch", True, white)
    award16 = myfont.render("You get the Ipone", True, white)



    #定义圈
    img = pygame.image.load("圈.png")  # 加载一个图片对象
    img = pygame.transform.smoothscale(img,(100,100))
    imgX = SCREEN_WIDTH / 2 - img.get_width() // 2  # 游戏开始时图片左上角的X坐标（水平坐标）
    imgY = SCREEN_HEIGHT-img.get_height()//2 # 游戏开始时图片左上角的Y坐标（垂直坐标）

    #以下为第一排的物品
    object1 = pygame.image.load("可乐瓶子.png")
    object2 = pygame.image.load("可乐罐装.png")
    object3 = pygame.image.load("可口可乐汽水.png")
    object4 = pygame.image.load("奶茶.png")
    object1=pygame.transform.smoothscale(object1,(100,100))
    object2 = pygame.transform.smoothscale(object2, (100, 100))
    object3 = pygame.transform.smoothscale(object3, (100, 100))
    object4 = pygame.transform.smoothscale(object4, (100, 100))
    object1X = SCREEN_WIDTH - object1.get_width() - 4*STEP
    object1Y = SCREEN_HEIGHT - object1.get_height()-2*STEP
    object2X = object1X - 245
    object2Y = object1Y
    object3X = object2X - 245
    object3Y = object1Y
    object4X = object3X - 245
    object4Y = object1Y

    #以下为第二排的物品
    object5 = pygame.image.load("儿童水杯.png")
    object6 = pygame.image.load("水杯.png")
    object7 = pygame.image.load("篮球.png")
    object8 = pygame.image.load("足球.png")
    object5 = pygame.transform.smoothscale(object5, (100, 100))
    object6 = pygame.transform.smoothscale(object6, (100, 100))
    object7 = pygame.transform.smoothscale(object7, (100, 100))
    object8 = pygame.transform.smoothscale(object8, (100, 100))
    object5X = SCREEN_WIDTH - object1.get_width() - 2*STEP
    object5Y = object1Y - 155
    object6X = object5X - 245
    object6Y = object5Y
    object7X = object6X - 245
    object7Y = object5Y
    object8X = object7X - 245
    object8Y = object5Y

    #以下为第三排物品
    object9 = pygame.image.load("苹果.png")
    object10 = pygame.image.load("公仔.png")
    object11 = pygame.image.load("鼠标.png")
    object12 = pygame.image.load("钱.png")
    object9 = pygame.transform.smoothscale(object9, (100, 100))
    object10 = pygame.transform.smoothscale(object10, (100, 100))
    object11 = pygame.transform.smoothscale(object11, (100, 100))
    object12 = pygame.transform.smoothscale(object12, (100, 100))
    object9X = SCREEN_WIDTH - object1.get_width()
    object9Y = object1Y - 155*2
    object10X = object9X - 245
    object10Y = object9Y
    object11X = object10X - 245
    object11Y = object9Y
    object12X = object11X - 245
    object12Y = object9Y
    #以下为第四排物品
    object13 = pygame.image.load("一袋钱.png")
    object14 = pygame.image.load("高级手表.png")
    object15 = pygame.image.load("手表.png")
    object16 = pygame.image.load("手机.png")
    object13 = pygame.transform.smoothscale(object13, (100, 100))
    object14 = pygame.transform.smoothscale(object14, (100, 100))
    object15 = pygame.transform.smoothscale(object15, (100, 100))
    object16 = pygame.transform.smoothscale(object16, (100, 100))
    object13X = SCREEN_WIDTH - object1.get_width() - STEP
    object13Y = object1Y - 155*3
    object14X = object13X - 245
    object14Y = object13Y
    object15X = object14X - 245
    object15Y = object13Y
    object16X = object15X - 245
    object16Y = object13Y

    playSurface.fill((135,206,235))  # 设置游戏窗口背景色为天蓝色
    playSurface.blit(img, (imgX, imgY))  # 将img对象画到(imgX,imgY)点上。只是画到缓冲区，需要调用flip才能显示
    pygame.display.flip()  # 将绘图缓冲区刷到屏幕，用户就可以看见


    while True:  # 游戏一直处于‘死’循环中
        for event in pygame.event.get():  # 监听事件
            if event.type == pygame.QUIT:  # 事件：点击游戏窗口右上方的X
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # 事件：当用户按键
                if event.key == pygame.K_ESCAPE:
                    options.options()
                if event.key == pygame.K_w:  # 按键为“上”方向键
                    direction = 'up'
                if event.key == pygame.K_d:  # 按键为“右”方向键
                    direction = 'right'
                if event.key == pygame.K_RETURN: #按键为“回车”键
                    direction = 'finish'
                if event.key == pygame.K_r:
                    main1()

        if direction == 'up':
            imgY -= STEP1
            if imgY < 0:  # 如果顶天，就返回
                imgY = 0
                direction = 'down'
        elif direction == 'down':
            imgY += STEP1
            if imgY + img.get_height() > SCREEN_HEIGHT:  # 如果触底，就返回
                imgY = SCREEN_HEIGHT - img.get_height()
                direction = 'up'
        elif direction == 'left':
            imgX -= STEP1
            if imgX < 0:  # 如果左碰壁，就折返向右
                imgX = 0
                direction = 'right'
        elif direction == 'right':
            imgX += STEP1
            if imgX + img.get_width() > SCREEN_WIDTH:  # 如果右碰壁，就折返向左
                imgX = SCREEN_WIDTH - img.get_width()
                direction = 'left'

        playSurface.fill((135,206,235))
        playSurface.blit(img, (imgX, imgY))   #刷新图标

        #第一排
        playSurface.blit(object1,(object1X,object1Y))
        playSurface.blit(object2,(object2X,object2Y))
        playSurface.blit(object3, (object3X, object3Y))
        playSurface.blit(object4, (object4X, object4Y))
        #第二排
        playSurface.blit(object5, (object5X, object5Y))
        playSurface.blit(object6, (object6X, object6Y))
        playSurface.blit(object7, (object7X, object7Y))
        playSurface.blit(object8, (object8X, object8Y))
        #第三排
        playSurface.blit(object9, (object9X, object9Y))
        playSurface.blit(object10, (object10X, object10Y))
        playSurface.blit(object11, (object11X, object11Y))
        playSurface.blit(object12, (object12X, object12Y))
        #第四排
        playSurface.blit(object13, (object13X, object13Y))
        playSurface.blit(object14, (object14X, object14Y))
        playSurface.blit(object15, (object15X, object15Y))
        playSurface.blit(object16, (object16X, object16Y))

        pygame.display.flip()

        #判断圈中的是什么物体
        if direction == 'finish':
            if imgX>object1X-50 and imgX<object1X+50 and imgY>object1Y-50 and imgY<object1Y+50:
                playSurface.blit(award1,(300,610))
                playSurface.blit(restart,(480,680))
            elif imgX>object2X-50 and imgX<object2X+50 and imgY>object2Y-50 and imgY<object2Y+50:
                playSurface.blit(award3,(300,610))
                playSurface.blit(restart,(480,680))
            elif imgX>object3X-50 and imgX<object3X+50 and imgY>object3Y-50 and imgY<object3Y+50:
                playSurface.blit(award2,(300,610))
                playSurface.blit(restart,(480,680))
            elif imgX>object4X-50 and imgX<object4X+50 and imgY>object4Y-50 and imgY<object4Y+50:
                playSurface.blit(award4,(300,610))
                playSurface.blit(restart,(480,680))
            elif imgX>object5X-50 and imgX<object5X+50 and imgY>object5Y-50 and imgY<object5Y+50:
                playSurface.blit(award5,(300,610))
                playSurface.blit(restart,(480,680))
            elif imgX>object6X-50 and imgX<object6X+50 and imgY>object6Y-50 and imgY<object6Y+50:
                playSurface.blit(award6,(300,610))
                playSurface.blit(restart,(480,680))
            elif imgX>object7X-50 and imgX<object7X+50 and imgY>object7Y-50 and imgY<object7Y+50:
                playSurface.blit(award7,(300,610))
                playSurface.blit(restart,(480,680))
            elif imgX>object8X-50 and imgX<object8X+50 and imgY>object8Y-50 and imgY<object8Y+50:
                playSurface.blit(award8,(300,610))
                playSurface.blit(restart,(480,680))
            elif imgX>object9X-50 and imgX<object9X+50 and imgY>object9Y-50 and imgY<object9Y+50:
                playSurface.blit(award9,(300,610))
                playSurface.blit(restart,(480,680))
            elif imgX>object10X-50 and imgX<object10X+50 and imgY>object10Y-50 and imgY<object10Y+50:
                playSurface.blit(award10,(300,610))
                playSurface.blit(restart,(480,680))
            elif imgX>object11X-50 and imgX<object11X+50 and imgY>object11Y-50 and imgY<object11Y+50:
                playSurface.blit(award11,(300,610))
                playSurface.blit(restart,(480,680))
            elif imgX>object12X-50 and imgX<object12X+50 and imgY>object12Y-50 and imgY<object12Y+50:
                playSurface.blit(award12,(300,610))
                playSurface.blit(restart,(480,680))
            elif imgX>object13X-50 and imgX<object13X+50 and imgY>object13Y-50 and imgY<object13Y+50:
                playSurface.blit(award13,(300,610))
                playSurface.blit(restart,(480,680))
            elif imgX>object14X-50 and imgX<object14X+50 and imgY>object14Y-50 and imgY<object14Y+50:
                playSurface.blit(award14,(300,610))
                playSurface.blit(restart,(480,680))
            elif imgX>object15X-50 and imgX<object15X+50 and imgY>object15Y-50 and imgY<object15Y+50:
                playSurface.blit(award15,(300,610))
                playSurface.blit(restart,(480,680))
            elif imgX>object16X-50 and imgX<object16X+50 and imgY>object16Y-50 and imgY<object16Y+50:
                playSurface.blit(award16,(300,610))
                playSurface.blit(restart,(480,680))

            else:
                playSurface.blit(noaward,(playSurface.get_height()-300,610))
                playSurface.blit(restart, (480, 680))
            pygame.display.flip()


        pygame.display.flip()
        time.sleep(0.1)

#Devil难度
def main2():
    direction = ''  # 用来标记图片运动方向，当为空串时，表示不运动
    SCREEN_HEIGHT = 720  # 游戏窗口高
    SCREEN_WIDTH = 1080  # 游戏窗口宽
    STEP = 50  # 图片每次运动的跨度（单位：像素）
    STEP1 = 75

    pygame.init()  # 初始化pygame模块
    playSurface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # 设置游戏窗口尺寸，并获得画布表面
    # 原点在左上方
    pygame.display.set_caption('套圈圈')  # 设置游戏窗口标题

    white = 255, 255, 255
    myfont = pygame.font.SysFont('arial', 60)  # 定义自己的字体
    myfont1 = pygame.font.SysFont('arial', 30)
    # 文本+字体+颜色

    # 定义奖励文字
    noaward = myfont.render("You get nothing", True, white)
    restart = myfont1.render("(Press r to restart)", True, white)
    award1 = myfont.render("You get the Bottled cola", True, white)
    award2 = myfont.render("You get the Canned cola", True, white)
    award3 = myfont.render("You get the Canned Pepsi", True, white)
    award4 = myfont.render("You get the Milk tea", True, white)
    award5 = myfont.render("You get the Thermos cup", True, white)
    award6 = myfont.render("You get the Plastic cup", True, white)
    award7 = myfont.render("You get the Basketball", True, white)
    award8 = myfont.render("You get the Football", True, white)
    award9 = myfont.render("You get the Apple", True, white)
    award10 = myfont.render("You get the Toy Bear", True, white)
    award11 = myfont.render("You get the Mouse", True, white)
    award12 = myfont.render("You get the Little cash", True, white)
    award13 = myfont.render("You get the Much money", True, white)
    award14 = myfont.render("You get the Casio", True, white)
    award15 = myfont.render("You get the Normal watch", True, white)
    award16 = myfont.render("You get the Ipone", True, white)

    # 定义圈
    img = pygame.image.load("圈.png")  # 加载一个图片对象
    img = pygame.transform.smoothscale(img, (100, 100))
    imgX = SCREEN_WIDTH / 2 - img.get_width() // 2  # 游戏开始时图片左上角的X坐标（水平坐标）
    imgY = SCREEN_HEIGHT - img.get_height() // 2  # 游戏开始时图片左上角的Y坐标（垂直坐标）

    # 以下为第一排的物品
    object1 = pygame.image.load("可乐瓶子.png")
    object2 = pygame.image.load("可乐罐装.png")
    object3 = pygame.image.load("可口可乐汽水.png")
    object4 = pygame.image.load("奶茶.png")
    object1 = pygame.transform.smoothscale(object1, (100, 100))
    object2 = pygame.transform.smoothscale(object2, (100, 100))
    object3 = pygame.transform.smoothscale(object3, (100, 100))
    object4 = pygame.transform.smoothscale(object4, (100, 100))
    object1X = SCREEN_WIDTH - object1.get_width() - 4 * STEP
    object1Y = SCREEN_HEIGHT - object1.get_height() - 2 * STEP
    object2X = object1X - 245
    object2Y = object1Y
    object3X = object2X - 245
    object3Y = object1Y
    object4X = object3X - 245
    object4Y = object1Y

    # 以下为第二排的物品
    object5 = pygame.image.load("儿童水杯.png")
    object6 = pygame.image.load("水杯.png")
    object7 = pygame.image.load("篮球.png")
    object8 = pygame.image.load("足球.png")
    object5 = pygame.transform.smoothscale(object5, (100, 100))
    object6 = pygame.transform.smoothscale(object6, (100, 100))
    object7 = pygame.transform.smoothscale(object7, (100, 100))
    object8 = pygame.transform.smoothscale(object8, (100, 100))
    object5X = SCREEN_WIDTH - object1.get_width() - 2 * STEP
    object5Y = object1Y - 155
    object6X = object5X - 245
    object6Y = object5Y
    object7X = object6X - 245
    object7Y = object5Y
    object8X = object7X - 245
    object8Y = object5Y

    # 以下为第三排物品
    object9 = pygame.image.load("苹果.png")
    object10 = pygame.image.load("公仔.png")
    object11 = pygame.image.load("鼠标.png")
    object12 = pygame.image.load("钱.png")
    object9 = pygame.transform.smoothscale(object9, (100, 100))
    object10 = pygame.transform.smoothscale(object10, (100, 100))
    object11 = pygame.transform.smoothscale(object11, (100, 100))
    object12 = pygame.transform.smoothscale(object12, (100, 100))
    object9X = SCREEN_WIDTH - object1.get_width()
    object9Y = object1Y - 155 * 2
    object10X = object9X - 245
    object10Y = object9Y
    object11X = object10X - 245
    object11Y = object9Y
    object12X = object11X - 245
    object12Y = object9Y
    # 以下为第四排物品
    object13 = pygame.image.load("一袋钱.png")
    object14 = pygame.image.load("高级手表.png")
    object15 = pygame.image.load("手表.png")
    object16 = pygame.image.load("手机.png")
    object13 = pygame.transform.smoothscale(object13, (100, 100))
    object14 = pygame.transform.smoothscale(object14, (100, 100))
    object15 = pygame.transform.smoothscale(object15, (100, 100))
    object16 = pygame.transform.smoothscale(object16, (100, 100))
    object13X = SCREEN_WIDTH - object1.get_width() - STEP
    object13Y = object1Y - 155 * 3
    object14X = object13X - 245
    object14Y = object13Y
    object15X = object14X - 245
    object15Y = object13Y
    object16X = object15X - 245
    object16Y = object13Y

    playSurface.fill((135, 206, 235))  # 设置游戏窗口背景色为天蓝色
    playSurface.blit(img, (imgX, imgY))  # 将img对象画到(imgX,imgY)点上。只是画到缓冲区，需要调用flip才能显示
    pygame.display.flip()  # 将绘图缓冲区刷到屏幕，用户就可以看见

    while True:  # 游戏一直处于‘死’循环中
        for event in pygame.event.get():  # 监听事件
            if event.type == pygame.QUIT:  # 事件：点击游戏窗口右上方的X
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:  # 事件：当用户按键
                if event.key == pygame.K_ESCAPE:
                    options.options()
                if event.key == pygame.K_w:  # 按键为“上”方向键
                    direction = 'up'
                if event.key == pygame.K_d:  # 按键为“右”方向键
                    direction = 'right'
                if event.key == pygame.K_RETURN:  # 按键为“回车”键
                    direction = 'finish'
                if event.key == pygame.K_r:
                    main2()

        if direction == 'up':
            imgY -= STEP1
            if imgY < 0:  # 如果顶天，就返回
                imgY = 0
                direction = 'down'
        elif direction == 'down':
            imgY += STEP1
            if imgY + img.get_height() > SCREEN_HEIGHT:  # 如果触底，就返回
                imgY = SCREEN_HEIGHT - img.get_height()
                direction = 'up'
        elif direction == 'left':
            imgX -= STEP1
            if imgX < 0:  # 如果左碰壁，就折返向右
                imgX = 0
                direction = 'right'
        elif direction == 'right':
            imgX += STEP1
            if imgX + img.get_width() > SCREEN_WIDTH:  # 如果右碰壁，就折返向左
                imgX = SCREEN_WIDTH - img.get_width()
                direction = 'left'
        """elif direction == 'finish':
            if imgX>object1X-50 or imgX<object1X+50:
                playSurface.blit(award1,(50,100))
            else:
                playSurface.blit(noaward,(50,100))
            pygame.display.flip()"""

        playSurface.fill((135, 206, 235))
        playSurface.blit(img, (imgX, imgY))

        # 第一排
        playSurface.blit(object1, (object1X, object1Y))
        playSurface.blit(object2, (object2X, object2Y))
        playSurface.blit(object3, (object3X, object3Y))
        playSurface.blit(object4, (object4X, object4Y))
        # 第二排
        playSurface.blit(object5, (object5X, object5Y))
        playSurface.blit(object6, (object6X, object6Y))
        playSurface.blit(object7, (object7X, object7Y))
        playSurface.blit(object8, (object8X, object8Y))
        # 第三排
        playSurface.blit(object9, (object9X, object9Y))
        playSurface.blit(object10, (object10X, object10Y))
        playSurface.blit(object11, (object11X, object11Y))
        playSurface.blit(object12, (object12X, object12Y))
        # 第四排
        playSurface.blit(object13, (object13X, object13Y))
        playSurface.blit(object14, (object14X, object14Y))
        playSurface.blit(object15, (object15X, object15Y))
        playSurface.blit(object16, (object16X, object16Y))

        pygame.display.flip()
        if direction == 'finish':
            if imgX > object1X - 50 and imgX < object1X + 50 and imgY > object1Y - 50 and imgY < object1Y + 50:
                playSurface.blit(award1, (300, 610))
                playSurface.blit(restart, (480, 680))
            elif imgX > object2X - 50 and imgX < object2X + 50 and imgY > object2Y - 50 and imgY < object2Y + 50:
                playSurface.blit(award3, (300, 610))
                playSurface.blit(restart, (480, 680))
            elif imgX > object3X - 50 and imgX < object3X + 50 and imgY > object3Y - 50 and imgY < object3Y + 50:
                playSurface.blit(award2, (300, 610))
                playSurface.blit(restart, (480, 680))
            elif imgX > object4X - 50 and imgX < object4X + 50 and imgY > object4Y - 50 and imgY < object4Y + 50:
                playSurface.blit(award4, (300, 610))
                playSurface.blit(restart, (480, 680))
            elif imgX > object5X - 50 and imgX < object5X + 50 and imgY > object5Y - 50 and imgY < object5Y + 50:
                playSurface.blit(award5, (300, 610))
                playSurface.blit(restart, (480, 680))
            elif imgX > object6X - 50 and imgX < object6X + 50 and imgY > object6Y - 50 and imgY < object6Y + 50:
                playSurface.blit(award6, (300, 610))
                playSurface.blit(restart, (480, 680))
            elif imgX > object7X - 50 and imgX < object7X + 50 and imgY > object7Y - 50 and imgY < object7Y + 50:
                playSurface.blit(award7, (300, 610))
                playSurface.blit(restart, (480, 680))
            elif imgX > object8X - 50 and imgX < object8X + 50 and imgY > object8Y - 50 and imgY < object8Y + 50:
                playSurface.blit(award8, (300, 610))
                playSurface.blit(restart, (480, 680))
            elif imgX > object9X - 50 and imgX < object9X + 50 and imgY > object9Y - 50 and imgY < object9Y + 50:
                playSurface.blit(award9, (300, 610))
                playSurface.blit(restart, (480, 680))
            elif imgX > object10X - 50 and imgX < object10X + 50 and imgY > object10Y - 50 and imgY < object10Y + 50:
                playSurface.blit(award10, (300, 610))
                playSurface.blit(restart, (480, 680))
            elif imgX > object11X - 50 and imgX < object11X + 50 and imgY > object11Y - 50 and imgY < object11Y + 50:
                playSurface.blit(award11, (300, 610))
                playSurface.blit(restart, (480, 680))
            elif imgX > object12X - 50 and imgX < object12X + 50 and imgY > object12Y - 50 and imgY < object12Y + 50:
                playSurface.blit(award12, (300, 610))
                playSurface.blit(restart, (480, 680))
            elif imgX > object13X - 50 and imgX < object13X + 50 and imgY > object13Y - 50 and imgY < object13Y + 50:
                playSurface.blit(award13, (300, 610))
                playSurface.blit(restart, (480, 680))
            elif imgX > object14X - 50 and imgX < object14X + 50 and imgY > object14Y - 50 and imgY < object14Y + 50:
                playSurface.blit(award14, (300, 610))
                playSurface.blit(restart, (480, 680))
            elif imgX > object15X - 50 and imgX < object15X + 50 and imgY > object15Y - 50 and imgY < object15Y + 50:
                playSurface.blit(award15, (300, 610))
                playSurface.blit(restart, (480, 680))
            elif imgX > object16X - 50 and imgX < object16X + 50 and imgY > object16Y - 50 and imgY < object16Y + 50:
                playSurface.blit(award16, (300, 610))
                playSurface.blit(restart, (480, 680))

            else:
                playSurface.blit(noaward, (playSurface.get_height() - 300, 610))
                playSurface.blit(restart, (480, 680))
            pygame.display.flip()

        pygame.display.flip()
        time.sleep(0.02)
