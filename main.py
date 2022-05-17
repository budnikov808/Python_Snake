import pygame
import random
from os import path #позволяет внедрядь в код сторонние файлы
import time
pygame.init()

WIDTH = 800
HEIGHT = 800

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT)) # в данной переменной параметры ширины и высоты дисплея
pygame.display.set_caption('Змейка на PyGame')
img_dir = path.join(path.dirname(__file__), 'C:/Users/User/Desktop/Python/Программы/Змейка/') #прописывается путь к изображению
bg = pygame.image.load(path.join(img_dir, 'foliage.png')).convert() #картинка становится фоном
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT)) #растягиваем картинку по ширине и высоте
bg_rect = bg.get_rect() #картинка становится слоем

xcor = WIDTH/2 #координаты
ycor = HEIGHT/2
x = 0
y = 0
snake_speed = 10
clock = pygame.time.Clock()
font_style = pygame.font.SysFont(None, 50)

def message (msg, color):
    mes = font_style.render(msg, True, color)
    screen.blit(mes, [WIDTH/2.5, HEIGHT/2])

foodx = round(random.randrange(0, WIDTH-10)/10)*10 #случайные точки координат для отображения зеленого квадрата
foody = round(random.randrange(0, HEIGHT-10)/10)*10

snake_body = []
length = 1

def new_block (snake_body):
    for x in snake_body:
        pygame.draw.rect(screen, BLACK, [x[0], x[1], 10, 10])

run = True
while run:
    for event in pygame.event.get(): #pygame.event.get() хранит в себе события библиотеки
        if event.type  == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN: # событие нажания на клавишу
            if event.key == pygame.K_LEFT:
                x = -10
                y = 0
            if event.key == pygame.K_RIGHT:
                x = 10
                y = 0
            if event.key == pygame.K_UP:
                x = 0
                y = -10
            if event.key == pygame.K_DOWN:
                x = 0
                y = 10
    if xcor >= WIDTH or xcor < 0 or ycor >= HEIGHT or ycor < 0:
        run = False
    xcor += x
    ycor += y
    screen.fill(BLUE)  # закрасит дисплей желаемым цветом
    screen.blit(bg, bg_rect) #размещаем слой
    #pygame.draw.rect(screen, RED, (xcor, ycor, 10, 10)) #прописали "змейку"
    pygame.draw.rect(screen, WHITE, (foodx, foody, 10, 10)) #отображение "еды"
    snake_head = [] #список для координат головы змеи
    snake_head.append(xcor)
    snake_head.append(ycor)
    snake_body.append(snake_head)
    if len(snake_body) > length:
        del snake_body[0]
        new_block(snake_body)
    pygame.display.update()
    if xcor == foodx and ycor == foody:
        foodx = round(random.randrange(0, WIDTH - 10) / 10) * 10
        foody = round(random.randrange(0, HEIGHT - 10) / 10) * 10
        length += 1
    '''if length > 1:
        for z in snake_body[::-1]:
            if z == snake_head:
                run = False'''
    pygame.display.flip()  # переворачивает экран
    clock.tick(snake_speed)

message('GAME OVER', RED)
pygame.display.update()
time.sleep(2)
pygame.quit()
quit()