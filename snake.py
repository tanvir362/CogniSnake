from collections import deque
import os
import time
import msvcrt

WIDTH, HEIGHT = 70, 40
STEP = {'L': (-1, 0), 'R': (1, 0), 'U': (0, -1), 'D': (0, 1), 'W': (0, 0)}

snake = deque([(8, 6), (8, 7), (9, 7), (10, 7), (10, 6), (10, 5), (9, 5), (8, 5), (7, 5), (6, 5), (5, 5), (4, 5), (3, 5), (2, 5), (1, 5)])


def check_valid_move(snake, dir):
    head_x, head_y = snake[0]
    step_x, step_y = STEP[dir]
    new_head = (head_x + step_x, head_y + step_y)
    if new_head in snake:
        return False
    if not (0 <= new_head[0] < WIDTH and 0 <= new_head[1] < HEIGHT):
        return False
    return True

def move(snake, dir):
    head_x, head_y = snake[0]
    step_x, step_y = STEP[dir]
    new_head = (head_x + step_x, head_y + step_y)
    snake.appendleft(new_head)
    snake.pop()


# evaluate how near the snake is to a given target
def score(snake, target):
    head_x, head_y = snake[0]
    target_x, target_y = target
    dist = abs(head_x - target_x) + abs(head_y - target_y)
    # dist = ((head_x - target_x) ** 2 + (head_y - target_y) ** 2) ** 0.5

    return 1/dist  # closer is better    

target = (8, 4)

def simulate(snake, depth):
    if snake[0] == target:
        return 9999, ''
    
    if depth == 0:
        return score(snake, target), ''

    best_score = float('-inf')
    best_dir = ''
    for step in STEP.keys():
        if not check_valid_move(snake, step):
            continue
        tail = snake[-1]
        move(snake, step)
        current_score, _ = simulate(snake, depth - 1)
        if current_score > best_score:
            best_score = current_score
            best_dir = step

        snake.append(tail)  # restore tail
        snake.popleft()    # restore head

    return best_score-1, best_dir
        
            


def draw_snake():
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if (j, i) == snake[0]:
                print('O', end='')
            elif (j, i) in snake:
                print('#', end='')
            elif (j, i) == target:
                print('X', end='')
            else:
                print('.', end='')
        print()


if __name__ == '__main__':
    # zigzag and circular movement
    # steps = "R" * 20 + "D" * 5 + "L" * 20 + "D" * 5 + "R" * 20 + "D" * 5 + "L" * 20 + "U" * 15

    paused = False
    while snake[0] != target:
        # Check for spacebar press to toggle pause
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b' ':
                paused = not paused
        if paused:
            time.sleep(0.05)
            continue
        time.sleep(0.5)
        _, step = simulate(snake, 8)
        move(snake, step)
        draw_snake()

