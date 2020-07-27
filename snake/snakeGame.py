import pygame
import queue
import time

from mapClass import MapPixel
from mapClass import MapClass
from snake import SnakeClass
from colorDict import colors

displayWidth = 500;
displayHeight = 500;
snakeTerritory = pygame.display.set_mode((displayWidth,displayHeight))
snakeTerritory.fill(colors.get('black'))
gameMap = MapClass(10, 10, pygame, snakeTerritory)
clock = pygame.time.Clock()
pygame.init()
	    
class GameClass:
    def leftKey():
        snake.left()
    def rightKey():
        snake.right()
    def upKey():
        snake.up()
    def downKey():
        snake.down()
        
    def displayMessage(message, height):
        font = pygame.font.Font('freesansbold.ttf',20)
        text = font.render(message, True, colors.get('white'))
        textBox = text.get_rect()
        textBox.center = (int(displayWidth/2),int(height))
        snakeTerritory.blit(text, textBox)

        pygame.display.update()
    
    def startScreen():
        GameClass.displayMessage('Feed the snake! Avoid walls and yourself : )', 100)
        GameClass.displayMessage('Press the spacebar key to begin!', 200)
        GameClass.displayMessage('If you kill the snake, press spacebar to try again!', 300)

    def initializeGame():
        snakeTerritory.fill(colors.get('black'))
        snake.gameOver = False
        snake.drawSnake(pygame, snakeTerritory)
		
        # draw and instantiate map
        for i in range(10):
            for j in range(10):
                gameMap.board[i][j] = MapPixel()
                pygame.draw.rect(snakeTerritory, colors.get('white'), (5 + 40*i + 10*i, 5 + 40*j + 10*j, 40, 40))
        gameMap.placeFood(5,5)

    def setNewGameState():
        global positionQueue
        positionQueue = queue.Queue()
        positionQueue.put([0,0])
        positionQueue.put([0,1])
        positionQueue.put([0,2])
        positionQueue.put([0,3])

        global snake
        snake = SnakeClass(4, positionQueue, 1, 0, 1, 'red', gameMap, [0,3])

    def step():
        snake.moveSnake()
        
    def distanceToFood():  
        distanceVector = [] # [distance in direction snake goes, distance in left/up, distance in right/down]
        if(snake.xVelocity == 0 and snake.yVelocity == -1): #up
            if(gameMap.food[1] > snake.head[1]):
                return gameMap.food[1] - snake.head[1] #above
            if(gameMap.food[0] > snake.head[0]):
                return gameMap.food[0] - snake.head[0] #right
            if(gameMap.food[0] < snake.head[0]):
                return snake.head[0] - gameMap.food[0] #left
        if(snake.xVelocity == 0 and snake.yVelocity == 1): #down
            if(gameMap.food[1] < snake.head[1]):
                return snake.head[1] - gameMap.food[1] #below
            if(gameMap.food[0] > snake.head[0]):
                return gameMap.food[0] - snake.head[0] #right
            if(gameMap.food[0] < snake.head[0]):
                return snake.head[0] - gameMap.food[0] #left
        if(snake.xVelocity == 1 and snake.yVelocity == 0): #right
            if(gameMap.food[0] > snake.head[0]):
                return gameMap.food[0] - snake.head[0] #right 
            if(gameMap.food[1] < snake.head[1]):
                return snake.head[1] - gameMap.food[1] #below
            if(gameMap.food[1] > snake.head[1]):
                return gameMap.food[1] - snake.head[1] #above
        if(snake.xVelocity == -1 and snake.yVelocity == 0): #left
            if(gameMap.food[0] < snake.head[0]):
                return snake.head[0] - gameMap.food[0] #left
            if(gameMap.food[1] < snake.head[1]):
                return snake.head[1] - gameMap.food[1] #below
            if(gameMap.food[1] > snake.head[1]):
                return gameMap.food[1] - snake.head[1] #above
                
    def distanceToWall(directionGoing, turnDirection):
        if(directionGoing == "up"):
            if(turnDirection == 'straight'):
                return (snake.head[1])  
            if(turnDirection == 'left'):
                return (snake.head[0])
            if(turnDirection == 'right'):
                return (9 -snake.head[0])
                
        if(directionGoing == "down"):
            if(turnDirection == 'straight'):
                return (9 -snake.head[1])   
            if(turnDirection == 'left'):
                return (snake.head[0])
            if(turnDirection == 'right'):
                return (9 - snake.head[0]) 
                
        if(directionGoing == "left"):
            if(turnDirection == 'straight'):
                return (snake.head[0])   
            if(turnDirection == 'up'):
                return (snake.head[1])
            if(turnDirection == 'down'):
                return (9 -snake.head[1])
                
        if(directionGoing == "right"):
            if(turnDirection == 'straight'):
                return (9 - snake.head[0]) 
            if(turnDirection == 'up'):
                return (snake.head[1])
            if(turnDirection == 'down'):
                return (9 - snake.head[1])        

    def gameLoop():
        list = ['right', 'straight', 'straight', 'up', 'straight', 'straight', 'left', 'straight', 'straight', 'down', 'straight', 'straight']
        counter = 0
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
        
            keyinput = pygame.key.get_pressed()     
            if (keyinput[pygame.K_SPACE] and snake.gameOver):
                snake.gameOver = False
                GameClass.initializeGame()
                GameClass.setNewGameState()
            if(not snake.gameOver):
                GameClass.distanceToFood() # TODO use threads
                print(list[counter]);
                if list[counter] == 'left':
                    GameClass.leftKey()
                elif list[counter] == 'right':
                    GameClass.rightKey()
                elif list[counter] == 'up':
                    GameClass.upKey()
                elif list[counter] == 'down':
                    GameClass.downKey()
                    
                counter = counter + 1
                if counter == 12:
                    counter = 0
                
                if keyinput[pygame.K_LEFT] or keyinput[pygame.K_a]:
                    GameClass.leftKey()
                elif keyinput[pygame.K_RIGHT] or keyinput[pygame.K_d]:
                    GameClass.rightKey()
                elif keyinput[pygame.K_UP] or keyinput[pygame.K_w]:
                    GameClass.upKey()
                elif keyinput[pygame.K_DOWN] or keyinput[pygame.K_s]:
                    GameClass.downKey()
                elif keyinput[pygame.K_ESCAPE]:
                    raise SystemExit   
                snake.drawSnake(pygame, snakeTerritory)
                pygame.display.flip()
                GameClass.step()
                clock.tick(8)	

GameClass.startScreen()
GameClass.setNewGameState()
snake.gameOver = True	
GameClass.gameLoop();	