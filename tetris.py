import time

import pygame
import numpy as np
from enum import Enum

# 40 x 10, but 20 x 10 seen
# T S Z L rL square

window_width = 1000
window_height = 1000
square_size = 40
colors = [(255, 0, 0), (0, 255, 0)]
score = 0

lrotations = np.asarray([[[0, 0, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0]],
                         [[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 1, 1], [0, 1, 0, 0]],
                         [[0, 0, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0]],
                         [[0, 0, 0, 0], [0, 0, 0, 1], [0, 1, 1, 1], [0, 0, 0, 0]]])

rlrotations = np.asarray([[[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 0, 0], [0, 1, 0, 0]],
                          [[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 1, 1], [0, 0, 0, 1]],
                          [[0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 1, 1, 0]],
                          [[0, 0, 0, 0], [0, 1, 0, 0], [0, 1, 1, 1], [0, 0, 0, 0]]])

zrotations = np.asarray([[[0, 0, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1], [0, 0, 0, 0]],
                         [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 1], [0, 0, 1, 0]],
                         [[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1]],
                         [[0, 0, 0, 0], [0, 0, 1, 0], [0, 1, 1, 0], [0, 1, 0, 0]]])

srotations = np.asarray([[[0, 0, 0, 0], [0, 0, 1, 1], [0, 1, 1, 0], [0, 0, 0, 0]],
                         [[0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 1, 1], [0, 0, 0, 1]],
                         [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 1, 1], [0, 1, 1, 0]],
                         [[0, 0, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 0]]])

trotations = np.asarray([[[0, 0, 0, 0], [0, 0, 1, 0], [0, 1, 1, 1], [0, 0, 0, 0]],
                         [[0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 1, 1], [0, 0, 1, 0]],
                         [[0, 0, 0, 0], [0, 0, 0, 0], [0, 1, 1, 1], [0, 0, 1, 0]],
                         [[0, 0, 0, 0], [0, 0, 1, 0], [0, 1, 1, 0], [0, 0, 1, 0]]])

irotations = np.asarray([[[0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0]],
                         [[0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 1, 0]],
                         [[0, 0, 0, 0], [0, 0, 0, 0], [1, 1, 1, 1], [0, 0, 0, 0]],
                         [[0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0], [0, 1, 0, 0]]])
squarerotations = np.asarray([[[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]],
                              [[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]],
                              [[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]],
                              [[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]])


class ShapeType(Enum):
    T = 0
    S = 1
    Z = 2
    L = 3
    rL = 4
    Square = 5
    I = 6


def get_random_shapetype():
    random_number = np.random.randint(0, 7, size=1)
    match random_number:

        case 1:  # L
            return ShapeType.L
        case 2:  # rL
            return ShapeType.rL

        case 3:  # z
            return ShapeType.Z

        case 4:  # s
            return ShapeType.S
        case 5:  # t
            return ShapeType.T
        case 6:
            return ShapeType.I

        case 0:  # square
            return ShapeType.Square


class Shape:
    x = 0
    y = 4

    def __init__(self):
        self.type = get_random_shapetype()
        self.state = self.init_state()
        self.rotations = self.init_rotations()
        self.color = self.init_color()
        self.index = 0

    def init_state(self):

        match self.type:

            case ShapeType.L:  # L
                return lrotations[0]
            case ShapeType.rL:  # rL
                return rlrotations[0]
            case ShapeType.Z:  # z
                return zrotations[0]
            case ShapeType.S:  # s
                return srotations[0]
            case ShapeType.T:  # t
                return trotations[0]

            case ShapeType.I:
                return irotations[0]
            case ShapeType.Square:  # square
                return squarerotations[0]

    def init_color(self):

        match self.type:
            case ShapeType.L:
                return (220, 120, 60)
            case ShapeType.rL:
                return (255, 0, 255)
            case ShapeType.Z:
                return (0, 255, 255)
            case ShapeType.S:
                return (0, 0, 255)
            case ShapeType.T:
                return (255, 0, 0)
            case ShapeType.I:
                return (255, 255, 0)
            case ShapeType.Square:
                return (0, 255, 0)

    def changeindex(self, clockwise):
        self.index += clockwise
        if self.index > 3:
            self.index = 0
        elif self.index < 0:
            self.index = 3

    def rotate(self, clockwise):
        self.changeindex(clockwise)
        self.state = self.rotations[self.index]

    def init_rotations(self):

        match self.type:
            case ShapeType.L:
                return lrotations
            case ShapeType.rL:
                return rlrotations
            case ShapeType.Z:
                return zrotations
            case ShapeType.S:
                return srotations
            case ShapeType.T:
                return trotations
            case ShapeType.I:
                return irotations
            case ShapeType.Square:
                return squarerotations


color_dt = np.dtype("3u1")
background_color = np.asarray((210, 230, 255), dtype=color_dt)
false_mask = np.asarray((np.zeros((40, 10), "u1")))
false_mask = false_mask.reshape(40, 10, 1)  # I need to force this shape
color_mask = np.full((40, 10), background_color, dtype=color_dt)
game_state_mask = np.concatenate([false_mask, color_mask], axis=2)
print(game_state_mask.dtype)
print(game_state_mask.shape)
game_state = np.copy(game_state_mask)

pygame.init()


def draw_game(self):
    y = 100
    for row in game_state[20::][:]:
        x = 100
        for square in row:
            pygame.draw.rect(self.screen, (square[1:4]), pygame.Rect((x, y), (square_size - 1, square_size - 1)))
            x += square_size
        y += square_size


def is_collision(shape):
    for row in range(0, 4):
        for column in range(0, 4):
            if shape.state[row][column] != 1:
                continue
            if (row + shape.x) > 38:
                return True
            if game_state[row + shape.x + 1][column + shape.y][0] == 1:
                return True

    return False


def check_rows():
    fullrowindex = []
    for row in range(39, 19, -1):
        isfull = True
        for column in range(0, 10):
            if game_state[row][column][0] == 0:
                isfull = False
        if isfull:
            fullrowindex.append(row)

    for x in fullrowindex:
        for column in range(0, 10):
            game_state[x][column][0] = 0
            game_state[x][column][1:4] = background_color

    # TODO gravity is too strong         
    if len(fullrowindex) > 0:
        for x in range(0, 20):
            for row in range(38, 19, -1):
                for column in range(0, 10):

                    if game_state[row + 1][column][0] == 0 and game_state[row][column][0] == 1:
                        game_state[row + 1][column][0] = 1
                        game_state[row][column][0] = 0
                        game_state[row + 1][column][1:4] = game_state[row][column][1:4]
                        game_state[row][column][1:4] = background_color


def update_gamestate(shape):
    for row in range(0, 4):
        for column in range(0, 4):
            if shape.state[row][column] == 1:
                game_state[row + shape.x][column + shape.y][1:4] = shape.color


def update_shapestate(shape, direction):
    for row in range(3, -1, -1):

        if direction == -1:
            columns = range(0, 4, 1)
        else:
            columns = range(3, -1, -1)
        for column in columns:
            if shape.state[row][column] == 1:
                game_state[row + shape.x][column + shape.y + direction][1:4] = shape.color
                game_state[row + shape.x][column + shape.y][1:4] = background_color


def update_shape_rotation(shape, clockwise):
    shape.changeindex(-clockwise)
    for row in range(0, 4):
        for column in range(0, 4):
            if shape.state[row][column] == 0 and shape.rotations[shape.index][row][column] == 1:
                if game_state[row + shape.x][column + shape.y][0] == 0:
                    game_state[row + shape.x][column + shape.y][1:4] = background_color
            elif shape.state[row][column] == 1:
                game_state[row + shape.x][column + shape.y][1:4] = shape.color
    shape.changeindex(clockwise)


def canrotate(shape, clockwise):
    shape.changeindex(clockwise)
    possiblestate = shape.rotations[shape.index]
    for row in range(0, 4):
        for column in range(0, 4):
            if possiblestate[row][column] != 1:
                continue
            if not (-1 < column + shape.y < 10 and row + shape.x < 40):
                shape.changeindex(-clockwise)
                return False
            if game_state[row + shape.x][column + shape.y][0] == 1:
                shape.changeindex(-clockwise)
                return False
    shape.changeindex(-clockwise)
    return True


def canmove(shape, direction):
    for row in range(0, 4):
        for column in range(0, 4):
            if shape.state[row][column] != 1:
                continue
            if (column + shape.y + direction > 9) or (column + shape.y + direction < 0) or \
                    game_state[row + shape.x][column + shape.y + direction][0] == 1:
                return False
    return True


def player_action(shape):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_q] and canrotate(shape, -1):
        shape.rotate(-1)
        update_shape_rotation(shape, -1)
    if keys[pygame.K_e] and canrotate(shape, 1):
        shape.rotate(1)
        update_shape_rotation(shape, 1)
    if keys[pygame.K_RIGHT]:
        if canmove(shape, 1):
            update_shapestate(shape, 1)
            shape.y += 1

    if keys[pygame.K_LEFT]:
        if canmove(shape, -1):
            update_shapestate(shape, -1)
            shape.y += -1


class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((window_width, window_height))
        self.running = True

        self.shape = None
        self.has_shape = False
        self.clock = pygame.time.Clock()
        self.play()

    def play(self):
        counter = 2
        while self.running:
            # quits the game if user closes the window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            if not self.has_shape:
                self.shape = Shape()
                self.has_shape = True
                update_gamestate(self.shape)

            player_action(self.shape)
            if counter == 2:
                self.drop_shape()
                check_rows()
                counter = 0
            if self.has_shape:
                if self.is_game_over():
                    self.running = False
                    time.sleep(2)
            self.screen.fill((0, 0, 30))
            draw_game(self)
            pygame.display.flip()
            counter += 1
            self.clock.tick(15)
        pygame.quit()

    def drop_shape(self):

        if is_collision(self.shape):
            for row in range(0, 4):
                for column in range(0, 4):
                    if self.shape.state[row][column] == 1:
                        game_state[row + self.shape.x][column + self.shape.y][0] = 1

            self.has_shape = False
            self.shape = None
            return

        for row in range(3, -1, -1):
            for column in range(3, -1, -1):
                if self.shape.state[row][column] == 1:
                    game_state[row + self.shape.x + 1][column + self.shape.y][1:4] = self.shape.color
                    game_state[row + self.shape.x][column + self.shape.y][1:4] = background_color

        self.shape.x += 1

    def is_game_over(self):
        for square in game_state[19][:]:
            if square[0] == 1:
                return True
        return False


game = Game()
