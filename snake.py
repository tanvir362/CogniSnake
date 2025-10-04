from collections import deque
import os
import time
import msvcrt
from constants import WIDTH, HEIGHT, STEP

class Snake:
    """
    Represents the snake, including its body and target.
    Provides movement and collision checking.
    """
    def __init__(self, body, target):
        """Initialize the snake with a body (deque of positions) and a target (tuple)."""
        self.body = deque(body)
        self.target = target

    def check_valid_move(self, direction):
        """Check if moving in the given direction is valid (no collision, in bounds)."""
        head_x, head_y = self.body[0]
        step_x, step_y = STEP[direction]
        new_head = (head_x + step_x, head_y + step_y)
        if new_head in self.body:
            return False
        if not (0 <= new_head[0] < WIDTH and 0 <= new_head[1] < HEIGHT):
            return False
        return True

    def move(self, direction):
        """Move the snake in the given direction (in-place)."""
        if direction == "W":
            return
        head_x, head_y = self.body[0]
        step_x, step_y = STEP[direction]
        new_head = (head_x + step_x, head_y + step_y)
        self.body.appendleft(new_head)
        self.body.pop()


# evaluate how near the snake is to the target
def score(head, target):
    """Return a score based on the distance from head to target. Higher is better."""
    head_x, head_y = head
    target_x, target_y = target
    dist = abs(head_x - target_x) + abs(head_y - target_y)
    # dist = ((head_x - target_x) ** 2 + (head_y - target_y) ** 2) ** 0.5
    return 1/dist if dist != 0 else float('inf')  # closer is better, avoid div by zero


def simulate(snake, depth):
    """
    Simulate the best move for the snake up to a given depth.
    Returns (score, direction) where direction is the best first move.
    Mutates snake in-place but restores state after recursion.
    """
    if snake.body[0] == snake.target:
        return 9999, 'W'
    
    if depth == 0:
        return score(snake.body[0], snake.target), 'W'

    best_score = float('-inf')
    best_direction = ''
    for direction in STEP.keys():
        if direction == 'W':
            continue
        if not snake.check_valid_move(direction):
            continue
        
        tail = snake.body[-1]
        snake.move(direction)
        current_score, _ = simulate(snake, depth-1)
        if current_score > best_score:
            best_score = current_score
            best_direction = direction
        snake.body.append(tail)  # restore tail
        snake.body.popleft()    # restore head
    return best_score-1, best_direction
        
            


def draw_snake(body, target):
    """Render the snake and target to the terminal."""
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if (j, i) == body[0]:
                print('O', end='')
            elif (j, i) in body:
                print('#', end='')
            elif (j, i) == target:
                print('X', end='')
            else:
                print('.', end='')
        print()


if __name__ == '__main__':
    snake = Snake(
        body=[
            (8, 6), (8, 7), (9, 7), (10, 7), (10, 6), 
            (10, 5), (9, 5), (8, 5), (7, 5), (6, 5), 
            (5, 5), (4, 5), (3, 5), (2, 5), (1, 5)
        ], 
        target=(8, 4)
    )

    paused = False
    while snake.body[0] != snake.target:
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
        snake.move(step)
        draw_snake(snake.body, snake.target)

