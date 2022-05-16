import pygame as pg
from objects import *
import sys

class Game:
    def __init__(self):
        pg.init()
        self.WIN_SIZE = 750
        self.TILE_SIZE = 50
        self.screen = pg.display.set_mode([self.WIN_SIZE] * 2)
        self.clock = pg.time.Clock()
        self.FPS = 60
        self.grid_color = [50, 50, 50] #rgb
        self.new_game()

    def draw_grid(self):
        # draws grid, line by line, for each axis
        [pg.draw.line(self.screen, self.grid_color, (x, 0), (x, self.WIN_SIZE)) for x in range(0, self.WIN_SIZE, self.TILE_SIZE)]
        [pg.draw.line(self.screen, self.grid_color, (0, y), (self.WIN_SIZE, y)) for y in range(0, self.WIN_SIZE, self.TILE_SIZE)]        
    
    def new_game(self):
        self.snake = Snake(self)
        self.food = Food(self)

    def update(self):
        self.snake.update()
        pg.display.flip()
        self.clock.tick(self.FPS)

    def draw(self):
        self.screen.fill("black")
        self.draw_grid()
        self.food.draw()
        self.snake.draw()

    def check_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            self.snake.control(event) # snake movement controls

    def run(self):
        while True:
            self.check_event()
            self.update()
            self.draw()

if __name__ == "__main__":
    game = Game()
    game.run()