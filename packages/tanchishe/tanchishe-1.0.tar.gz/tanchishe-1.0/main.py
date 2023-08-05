import pygame
import sys
import traceback
import snake
import food
from random import *
from pygame.locals import *

pygame.init()
pygame.mixer.init()
pygame.font.init()

bg_size = width, height = 500, 500
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption('贪吃蛇')

background = pygame.image.load('图片/贪吃蛇背景.png').convert()

stop_image1 = pygame.image.load('图片/暂停.png').convert_alpha()
stop_image2 = pygame.image.load('图片/暂停1.png').convert_alpha()
start_image1 = pygame.image.load('图片/继续.png').convert_alpha()
start_image2 = pygame.image.load('图片/继续1.png').convert_alpha()
stop_rect = stop_image1.get_rect()
stop_rect.left, stop_rect.top = width - stop_rect.width - 10, 10
stop_image = stop_image1

my_font = pygame.font.Font('font/daiyujianti.ttf', 30)

gameover_font = pygame.font.Font('font/daiyujianti.ttf',48)
again_image =pygame.image.load('图片/重新开始.png').convert_alpha()
again_rect = again_image.get_rect()

exit_image =pygame.image.load('图片/退出游戏.png').convert_alpha()
exit_rect = exit_image.get_rect()
icon_image =pygame.image.load('图片/贪吃蛇图标.png').convert_alpha()
icon_rect = icon_image.get_rect()

pygame.mixer.music.load('音效/Capo Productions - Inspire.ogg')
pygame.mixer.music.set_volume(0.2)

eat_sound = pygame.mixer.Sound('音效/吃食物.wav')
eat_sound.set_volume(0.2)
death_sound = pygame.mixer.Sound('音效/死亡.wav')
death_sound.set_volume(0.2)

#创建蛇尾集合
def add_snake(lists, rect, speed):
    e1= snake.Snake(bg_size, rect, speed)
    lists.append(e1)
    
def main():
    pygame.mixer.music.play(-1)
    head_snake = snake.My_Snake(bg_size)

    snakes =[]
    snakes.append(head_snake)

    foods = []
    foods.append(food.Food(bg_size))

    SNAKE_TIME = USEREVENT
    

    delay = 100

    food_i = 0  #食物图片索引
    num = 1    #蛇尾索引
    life_num = 1
    results = 0
    
    running = True
    stop = True    #切换暂停按钮
    recorded = False

    clock = pygame.time.Clock()   #导入帧率设置

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            #生成暂停按钮
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1 or stop_rect.collidepoint(event.pos):
                    stop = not stop
                    if stop:
                        pygame.mixer.music.pause()
                        pygame.mixer.pause()
                    else:
                        pygame.mixer.music.unpause()
                        pygame.mixer.unpause()

            elif event.type == MOUSEMOTION:
                if stop_rect.collidepoint(event.pos):
                    if stop:
                        stop_image = start_image2
                    else:
                        stop_image = stop_image2
                else:
                    if stop:
                        stop_image = start_image1
                    else:
                        stop_image = stop_image1

        screen.blit(background, (0, 0))    #背景图片

        if life_num and not stop:
    
            #绘制食物
            for each in foods:
                if each.active:
                    if not (delay % 5):
                        screen.blit(each.image[food_i], each.rect)
                        food_i = (food_i + 1) % 4
                else:
                    each.reset()
                    
            #食物蛇碰撞检测
            eat_down = pygame.sprite.spritecollide(head_snake, foods,\
                                        False, pygame.sprite.collide_mask)
            if eat_down:
                eat_sound.play()
                results += 1
                for each in foods:
                    each.active = False
                add_snake(snakes, snakes[num-1].rect, snakes[num-1].speed)
                num += 1

            #绘制蛇尾
            if(num > 1):
                for i in range(num - 1, 0, -1):
                    snakes[i].speed = snakes[i - 1].speed
                    snakes[i].move()
                    screen.blit(snakes[i].image, snakes[i].rect)

            #头尾碰撞检测
            for i in range(6, num):
                if head_snake.rect == snakes[i].rect:
                    life_num = 0
                    death_sound.play()

            #检测用户的键盘操作      一定要放在头前尾后！！！
            key_pressed = pygame.key.get_pressed()
            if key_pressed[K_w] or key_pressed[K_UP]:
                head_snake.moveUp()

            if key_pressed[K_s] or key_pressed[K_DOWN]:
                head_snake.moveDown()

            if key_pressed[K_a] or key_pressed[K_LEFT]:
                head_snake.moveLeft()

            if key_pressed[K_d] or key_pressed[K_RIGHT]:
                head_snake.moveRight()

            #绘制蛇头    
            head_snake.move()
            screen.blit(head_snake.image, head_snake.rect)

            #绘制得分
            screen.blit(my_font.render('results ：%d' % results, True,\
                                       [255, 0, 0]), [20, 20])
            #绘制暂停按钮
            screen.blit(stop_image, stop_rect)

        elif life_num == 0:
            pygame.mixer.music.pause()
            
            if not recorded:
                with open('历史成绩.txt', 'r') as f:
                    record_results = int(f.read())

                if results > record_results:
                    with open('历史成绩.txt', 'w') as f:
                        f.write(str(results))
                        f.close()

            screen.blit(icon_image, [190, 170])
            screen.blit(again_image, [150, 300])
            screen.blit(exit_image, [150, 380])
            screen.blit(my_font.render('RECORD RESSULTS：%d' % \
                    record_results, True, [255, 0, 0]), [100, 80])  #在游戏屏幕打印历史成绩
            screen.blit(my_font.render('now results ：%d' % \
                    results, True, [255, 0, 0]), [150, 120])  #在游戏屏幕打印当前成绩

            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                if 150< pos[0] < 350 and\
                   310 < pos[1] < 370:
                    main()
                 #坐标经计算得出
                elif 150 < pos[0] < 350 and\
                     390 < pos[1] < 450:
                    pygame.quit()
                    sys.exit()
        
        delay -= 1
        if not delay:
            delay = 100

        pygame.display.flip()
        clock.tick(15)  #设置为30帧


if __name__ == '__main__':
    try:
        main()
    except SystemExit:
        pass
    except:
        traceback.print_exc()
        pygame.quit()
        input()
