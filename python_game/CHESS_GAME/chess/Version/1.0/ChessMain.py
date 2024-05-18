'''
This is our main driver file .It will be responsible for handling user input and displaying the current GameState object . 
'''

import pygame as p 
from ChessEngine import GameState


WIDTH = HEIGHT = 512
DIMENSION = 8
SQ_SIZE = HEIGHT//DIMENSION
MAX_FPS = 15
IMAGES = {}
Version = 0.1

'''
Initialise A SINGLE DICTIONARY OF IMAGES THIS WILL BE CALLED EXACTLY ONCES , it for the purpose so that it dont consume much memory while loading images. 
'''

def loadimages():
     pieces = ["bR","bN","bB","bQ","bK","bp","wR","wN","wB","wQ","wK","wp"]
     for piece in pieces:
         IMAGES[piece] = p.transform.scale(p.image.load(f"CHESS_GAME/chess/images/{piece}.png"),(SQ_SIZE,SQ_SIZE))
     #CHESS_GAME/chess/images/bB.png
    #Note from this we can access an image by saying 'IMAGES['wp']'

'''
Main driver for the code . This will handel user input and updating the graphics.
'''

def main():
     p.init()
     screen = p.display.set_mode((WIDTH,HEIGHT))
     clock = p.time.Clock()
     screen.fill(p.Color("white"))
     gs = GameState()
     loadimages()
     running = True
     while running:
          for e in p.event.get():
               if e.type == p.QUIT:
                    running = False
          drawGameState(screen,gs)
          clock.tick(MAX_FPS)
          p.display.flip()

'''
Responsible for all the graphics within a current game state 
'''

def drawGameState(screen , gs):
     drawBoard(screen) # draw square on board
     #later to add highlighting or move suggestion 
     drawPieces(screen,gs.board) #draw pieces on top of squares

'''
draw teh squares on the board.
the top left square is always light color no matter what perspective you are playing 
'''

def drawBoard(screen):
     colors = [p.Color((255, 255, 240)),p.Color((107, 143, 59))]
     for r in range(DIMENSION):
          for c in range(DIMENSION):
               color = colors[( ( r + c ) % 2 )]
               p.draw.rect(screen,color,p.Rect(c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE))

'''
Draw the pieces on the board using the current state.board
'''

def drawPieces(screen,board):
     for r in range(DIMENSION):
          for c in range(DIMENSION):
               piece = board[r][c]
               if piece != "--": #not empty square
                    screen.blit(IMAGES[piece],p.Rect(c*SQ_SIZE,r*SQ_SIZE,SQ_SIZE,SQ_SIZE))

if __name__ == "__main__":
     print(f"This is the {Version} version of the game ")
     main()
