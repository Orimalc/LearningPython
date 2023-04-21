import random
import time
import pygame
from enum import Enum

pygame.init()

# can malfunction is divisor is not fitting height and width
window_height = 800
window_width = 800
snake_size = window_width // 40

screen = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()
food_position = (window_width / 4, window_height / 2)
snake_head_position = (window_width / 2, window_height / 2)
snake_body = [(window_width / 2, window_height / 2),
              (window_width / 2 - snake_size, window_height / 2),
              (window_width / 2 - 2 * snake_size, window_height / 2)]
running = False
food_radius = snake_size / 2
score = 10


class Direction(Enum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3


snake_direction = Direction.RIGHT

if __name__ == "__main__":
    running = True


def draw_snake():
    for body in snake_body:
        pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(body, (snake_size - 1, snake_size - 1)))


def move_snake(direction):

    new_snake_head = None
    global snake_head_position

    if direction == Direction.UP:
        new_snake_head = (snake_head_position[0], snake_head_position[1] - snake_size)
    elif direction == Direction.DOWN:
        new_snake_head = (snake_head_position[0], snake_head_position[1] + snake_size)
    elif direction == Direction.LEFT:
        new_snake_head = (snake_head_position[0] - snake_size, snake_head_position[1])
    elif direction == Direction.RIGHT:
        new_snake_head = (snake_head_position[0] + snake_size, snake_head_position[1])

    snake_body.insert(0, new_snake_head)
    snake_head_position = new_snake_head


def update_direction():
    global snake_direction
    new_snake_direction = snake_direction
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and snake_direction != Direction.DOWN:
        new_snake_direction = Direction.UP
    elif keys[pygame.K_s] and snake_direction != Direction.UP:
        new_snake_direction = Direction.DOWN
    elif keys[pygame.K_a] and snake_direction != Direction.RIGHT:
        new_snake_direction = Direction.LEFT
    elif keys[pygame.K_d] and snake_direction != Direction.LEFT:
        new_snake_direction = Direction.RIGHT

    snake_direction = new_snake_direction


def eat_fruit():
    global food_position
    if snake_head_position == food_position:

        global score
        score += 10
        food_position = ((random.randint(snake_size, (window_width - snake_size) // snake_size) * snake_size,
                         random.randint(snake_size, (window_height - snake_size) // snake_size) * snake_size))
        return

    snake_body.pop()


def game_over():
    if (snake_head_position[0] < 0) or (snake_head_position[0] > window_width - snake_size):
        return True
    elif (snake_head_position[1] < 0) or (snake_head_position[1] > window_height - snake_size):
        return True
    for body in snake_body[1:]:
        if snake_head_position == body:
            return True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 30))
    pygame.draw.circle(screen, (255, 0, 0),
                       (food_position[0] + snake_size / 2, food_position[1] + snake_size / 2), food_radius)
    update_direction()
    move_snake(snake_direction)
    if game_over():
        time.sleep(1)
        break
    eat_fruit()
    draw_snake()
    pygame.display.flip()
    clock.tick(30)


print(score)
pygame.quit()
exit()
