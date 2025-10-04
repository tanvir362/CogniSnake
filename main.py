import time
import pygame
from snake import Snake, simulate
from constants import WIDTH, HEIGHT, STEP

pygame.init()

screen = pygame.display.set_mode((WIDTH*10, HEIGHT*10))
pygame.display.set_caption("CogniSnake")


def main():
    clock = pygame.time.Clock()
    snake = Snake(
        body=[
            (8, 6), (8, 7), (9, 7), (10, 7), (10, 6), 
            (10, 5), (9, 5), (8, 5), (7, 5), (6, 5), 
            (5, 5), (4, 5), (3, 5), (2, 5), (1, 5)
        ], 
        target=(65, 35)
    )

    run = True
    while run:
        clock.tick(60)
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = False

        mouse_x, mouse_y = pygame.mouse.get_pos()
        snake.target = (mouse_x // 10, mouse_y // 10)

        score, direction = simulate(snake, depth=11)
        if direction and snake.check_valid_move(direction):
            temp_head_x, temp_head_y = snake.body[0]
            dx, dy = STEP[direction]
            temp_head = (temp_head_x + dx, temp_head_y + dy)
            snake.move(direction, grow=(temp_head == snake.target))

        # Draw snake
        for segment in snake.body:
            pygame.draw.rect(screen, (0, 255, 0), (segment[0]*10, segment[1]*10, 10, 10))
        
        if snake.target != snake.body[0]:
            pygame.draw.rect(screen, (255, 0, 0), (snake.target[0]*10, snake.target[1]*10, 10, 10))

        pygame.display.update()

    pygame.quit()





if __name__ == '__main__':
    main()

    