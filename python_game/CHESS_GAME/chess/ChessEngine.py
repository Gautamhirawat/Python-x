'''
This class is responsible for storing all th info about the current state of a chess game . It will also be responsible for determining the valid moves at the current state . It will also keep a move log.
'''
class GameState():
    def __init__(self):
        # Board is 8X8 2d list , each  element of teh list has 2 character ,
        # first char shows the color 'b' or 'w'
        # second char shows the type of piece 'K','Q','B','N','R' or 'p'
        # "--" represent empty space
        self.board = [
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bp","bp","bp","bp","bp","bp","bp","bp"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["wp","wp","wp","wp","wp","wp","wp","wp"],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"]
        ]
        self.whitetomove = True
        self.moveLog = []
        
