import pygame
from random import randint
from board import Board

RED = pygame.Color("red")
BLACK = pygame.Color("black")
WHITE = pygame.Color("white")
FPS = 10


class MineSweeper(Board):
    def __init__(self, width, height, count_mines):
        self.width = width
        self.height = height
        self.board = []
        self.board = [[randint(-1, 10) for _ in range(height)] for _ in range(width)]
        for x in range(width):
            for y in range(height):
                count = sum([i.count(10) for i in self.board])
                if count <= count_mines:
                    if self.board[x][y] != 10:
                        self.board[x][y] = -1
                else:
                    self.board[x][y] = -1
        self.matrix = []
        self.left = 20
        self.top = 10
        self.cell_size = 30

    def render(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[x][y] == 10:
                    pygame.draw.rect(screen, RED, (self.cell_size * x + self.left,
                                                   self.top + self.cell_size * y,
                                                   self.cell_size, self.cell_size))
                elif self.board[x][y] == -1:
                    pygame.draw.rect(screen, WHITE, (self.cell_size * x + self.left,
                                                     self.top + self.cell_size * y,
                                                     self.cell_size, self.cell_size),
                                     1)
                else:
                    neighbours = self.get_neighbours(x, y)
                    count = neighbours.count(10)
                    font = pygame.font.Font(None, 25)
                    text = font.render(str(count), 1, pygame.Color("green"))
                    screen.blit(text, (self.cell_size * x + 22,
                                       12 + self.cell_size * y))
                pygame.draw.rect(screen, WHITE, (self.cell_size * x + self.left,
                                                 self.top + self.cell_size * y,
                                                 self.cell_size, self.cell_size),
                                 1)

    def get_neighbours(self, x, y):
        m = self.board
        first, second, third, \
        fourth, sixth, \
        seventh, eighth, nineth = \
            m[x - 1][y - 1], m[x][y - 1], \
            m[x + 1][y - 1], m[x - 1][y], \
            m[x + 1][y], \
            m[x - 1][y + 1], m[x][y + 1], \
            m[x + 1][y + 1]
        neighbours = [first, second, third, fourth,
                      sixth, seventh, eighth, nineth]
        return neighbours

    def open_cell(self, pos):
        x, y = self.get_cell(pos)
        self.board[x][y] = 1


if __name__ == '__main__':
    pygame.init()
    size = w, h = 400, 600
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Дедушка Сапёра")
    clock = pygame.time.Clock()
    # Вводится кол-во клеток по ширине и высоте, затем количество бомб на плоскости
    board = MineSweeper(12, 19, 25)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.open_cell(event.pos)
        screen.fill(BLACK)
        board.render()
        pygame.display.flip()
        clock.tick(FPS)
