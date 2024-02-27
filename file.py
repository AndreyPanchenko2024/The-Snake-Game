import pygame
import sys
import random
RED = (224, 0, 0)
size_block = 20
WHITE = (255, 255, 255)
BLUE = (204, 255, 255)
FRAME_COLOR = (0, 255, 204)
Count_blocks = 20
Indent = 1
HEADER_Indet = 70
HEADER_COLOR = (0, 254, 153)
SNAKE_COLOR = (11, 22, 209)
size = [size_block * Count_blocks + 2 * size_block + Indent * Count_blocks,
        size_block * Count_blocks + 2 * size_block + Indent * Count_blocks + HEADER_Indet]



screen = pygame.display.set_mode(size) # Вывод экрана размером 600 на 800

pygame.display.set_caption('Змейка') # Зоголовок программы
timer = pygame.time.Clock()
class SnakeBlock:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def is_inside(self):
        return  0 <= self.x < Count_blocks and 0 <= self.y <Count_blocks
    
    def __eq__(self, other):  #магический метол сравнения eq
        return isinstance(other, SnakeBlock) and self.x == other.x and self.y == other.y
#Задачём рандомные координаты клубнике которую съела змейка(координаты после съедания имеются ввиду)
def get_random_empty_block():
    x = random.randint(0, Count_blocks - 1)
    y = random.randint(0, Count_blocks - 1)
    empty_block = SnakeBlock(x, y)
    while empty_block in snake_blocks:
        empty_block.x = random.randint(0, Count_blocks - 1)
        empty_block.y = random.randint(0, Count_blocks - 1)
    return empty_block

def draw_block(color, row, c):
    pygame.draw.rect(screen, color, [size_block + Count_blocks * c + (Indent * c), 
                                    HEADER_Indet + size_block + Count_blocks * row + (Indent * row), size_block, size_block])

snake_blocks = [SnakeBlock(9, 8), SnakeBlock(9, 9), SnakeBlock(9, 10)]
strawberry = get_random_empty_block()
d_row = 0
d_col = 1

while True:

    for event in pygame.event.get(): # цикл по происходящим событиям в окне игры
        if event.type == pygame.QUIT:
            print('exit')
            pygame.quit()
            sys.exit()
        # Движение вниз, вверх, влево и вправо и изменение значений переменых впоследствии этого
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and d_col != 0:
                d_row = 1
                d_col = 0
            elif event.key == pygame.K_UP and d_col != 0:
                d_row = -1
                d_col = 0
            elif event.key == pygame.K_RIGHT and d_row != 0:
                d_row = 0
                d_col = 1
            elif event.key == pygame.K_LEFT and d_row != 0:
                d_row = 0
                d_col = -1
      


    screen.fill(FRAME_COLOR)  # Заполнение цветом
    pygame.draw.rect(screen, HEADER_COLOR, [0, 0, size[0], HEADER_Indet])
    
    #Проверка на чётность и нечётность для определения цвета
    for row in range(Count_blocks):
        for c in range(Count_blocks):
            if (row + c) % 2 == 0:
                color = BLUE
            else:
                color = WHITE

            draw_block(color, row, c)

    head = snake_blocks[-1]
    #В случае столкновения змейки со стенкой будет вызвана строка crash и программа будет завершена
    if not head.is_inside():
            print('crash')
            pygame.quit()
            sys.exit()

    for block in snake_blocks:
        draw_block(SNAKE_COLOR, block.x, block.y)

    draw_block(RED, strawberry.x, strawberry.y)
    
    if strawberry == head:
        snake_blocks.append(strawberry)
        strawberry = get_random_empty_block()

    new_head = SnakeBlock(head.x + d_row, head.y + d_col)
    snake_blocks.append(new_head)
    snake_blocks.pop(0)

    pygame.display.flip() # Этот метод применяет всё , что произошло на экране
    timer.tick(2)
