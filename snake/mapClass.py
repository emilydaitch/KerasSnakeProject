from colorDict import colors

class MapPixel:
    'map pixel and properties- foodPresent, snakePresent'
		
    def __init__(self):
        self.foodPresent = False
        self.snakePresent = False
	
    def putFood(self):
        self.foodPresent = True
		
    def putSnake(self):
        self.snakePresent = True	

class MapClass:
    'snake territory (map class)'
	
    columns = 10
    rows = 10
    food = [0, 0]
	
    def __init__(self, rows, columns, pygame, snakeTerritory):
        self.rows = rows
        self.columns = columns
        self.board = [[MapPixel() for _ in range(rows)] for _ in range(columns)]
        self.pygame = pygame
        self.snakeTerritory = snakeTerritory
		
    def placeFood(self, row, column):
        self.food = [row, column]
        self.board[row][column].putFood()
        self.pygame.draw.rect(self.snakeTerritory, colors.get('green'), (5 + 40*row + 10*row, 5 + 40*column + 10*column, 40, 40))
		
    def placeSnake(self, row, column):
        self.board[row][column].putSnake()