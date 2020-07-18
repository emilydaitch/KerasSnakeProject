import copy

from colorDict import colors
from random import randrange

class SnakeClass:
    'slithery little snake (snake class)'
	
    bodySegmentCount = 0
    head = []
    tail = []
		
    def __init__(self, length, position, speed, xVelocity, yVelocity, color, _map, head=[0,0]):
        self.bodySegmentCount = length
        self.position = position
        self.speed = speed
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity
        self.color = color
        self._map = _map
        self.head = head
        self.tailToRemove = [0,0]
        self.needToGrow = False
        self.gameOver = False
		
    def growSnake(self):
        self.needToGrow = True
	
    def tryToEat(self):
        if(self._map.board[self.head[0]][self.head[1]].foodPresent):
            self.growSnake()
            self._map.board[self.head[0]][self.head[1]].foodPresent = False
            self._map.placeFood(randrange(0, 9), randrange(0, 9))
	
    def up(self):
        if(self.yVelocity != 1):
            self.xVelocity = 0
            self.yVelocity = -1
    def down(self):
        if(self.yVelocity != -1):
            self.xVelocity = 0
            self.yVelocity = 1
    def right(self):
        if(self.xVelocity != -1):
            self.xVelocity = 1
            self.yVelocity = 0
    def left(self):
        if(self.xVelocity != 1):
            self.xVelocity = -1
            self.yVelocity = 0
			
    def checkSelfCollision(self):
        if(self._map.board[self.head[0] + self.xVelocity][self.head[1] + + self.yVelocity].snakePresent):
            self._map.board[self.head[0]][self.head[1]].foodPresent = False
            return True
        return False
		
    def moveSnake(self):
        if(self.head[0] + self.xVelocity > 9 or self.head[0] + self.xVelocity < 0):
            self.gameOver = True
        elif(self.head[1] + self.yVelocity > 9 or self.head[1] + self.yVelocity < 0):
            self.gameOver = True
        elif(self.checkSelfCollision()):
            self.gameOver = True
        else:
            self.tryToEat();
            if(not self.needToGrow):
                self.tailToRemove = self.position.get()
            self.position.put([self.head[0] + self.xVelocity, self.head[1] + self.yVelocity])
            self._map.placeSnake(self.head[0] + self.xVelocity, self.head[1] + self.yVelocity)
            self.head = [self.head[0] + self.xVelocity, self.head[1] + self.yVelocity]

    def drawSnake(self, pygame, snakeTerritory):
        if(not self.needToGrow):
            self._map.board[self.tailToRemove[0]][self.tailToRemove[1]].snakePresent = False
            pygame.draw.rect(snakeTerritory, colors.get('white'), (5 + 50*self.tailToRemove[0], 5 + 50*self.tailToRemove[1], 40, 40))
        else:
            self.needToGrow = False
        copyQueue = copy.deepcopy(self.position.queue)
        while copyQueue:
            segment = copyQueue.pop()
            self._map.placeSnake(segment[0], segment[1])
            pygame.draw.rect(snakeTerritory, colors.get('blue'), (5 + 40*segment[0] + 10*segment[0], 5 + 40*segment[1] + 10*segment[1], 40, 40))