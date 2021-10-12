

from elmts.plyrs import Player
from PIL import ImageTk, Image

Bside = "black"
Wside = "white"

class piece:

    def __init__(lun, pos: tuple) -> None:
        lun.pos = pos


    @property 
    def currpos(fuck): return fuck.pos






class Pawn(piece): 

    def __init__(pos: tuple, side) -> None:

        super().__init__(pos)

    def nextMoves(self, board):

        if self.currpos[0] == 1 :pass

class Rook(piece): pass

class Knight(piece): pass

class Bishop(piece): pass

class Queen(piece): pass

class King(piece): pass