

#from elmts.plyrs import Player
from typing import Final, Tuple
from PIL import Image

Bside: Final[str] = "black"
Wside: Final[str] = "white"
Shared: Final[str] = "void"

class piece:
    def __init__(self, texture: Image.Image, pos: Tuple[int, int], side) -> None:
        self.side = side
        self.weight = None
        self.texture = texture
        self.pos = pos


class Void(piece):

    def __init__(self, texture: Image.Image, pos: Tuple[int, int], side) -> None:
        piece.__init__(self, texture, pos, side)

class Pawn(piece):

    def __init__(self, texture: Image.Image, pos: Tuple[int, int], side) -> None:
        piece.__init__(self, texture, pos, side)
        self.weight = 1/6


    def nextMoves(self, board) -> Tuple[int, int]:
        np = ()
        if self.currpos[0]:
            if board.view[self.currpos[0]-1][self.currpos[1]].name == "":
                np+=(self.currpos[0]-1, self.currpos[1]),
                if (self.currpos[0] == 6) and (board.view[self.currpos[0]-2][self.currpos[1]].name == ""):
                    np+=(self.currpos[0]-2, self.currpos[1]),
            if board.view[self.currpos[0]-1][self.currpos[1]+1].name != "":
                if board.view[self.currpos[0]-1][self.currpos[1]+1].name[1] != self.side[0]: np+=(self.currpos[0]-1, self.currpos[1]+1),
            if board.view[self.currpos[0]-1][self.currpos[1]-1].name != "":
                if board.view[self.currpos[0]-1][self.currpos[1]-1].name[1] != self.side[0]: np+=(self.currpos[0]-1, self.currpos[1]-1),
        else: np = None,
        return np
                



class Rook(piece):

    def __init__(self, texture: Image.Image, pos: tuple, side) -> None:
        piece.__init__(self, texture, pos, side)
        self.weight = 1/3


class Knight(piece):

    def __init__(self, texture: Image.Image, pos: tuple, side) -> None:
        piece.__init__(self, texture, pos, side)
        self.weight = 2/3

class Bishop(piece):

    def __init__(self, texture: Image.Image, pos: tuple, side) -> None:
        piece.__init__(self, texture, pos, side)
        self.weight = .5

class Queen(piece):

    def __init__(self, texture: Image.Image, pos: tuple, side) -> None:
        piece.__init__(self, texture, pos, side)
        self.weight = 5/6

class King(piece):

    def __init__(self, texture: Image.Image, pos: tuple, side) -> None:
        piece.__init__(self, texture, pos, side)
        self.weight = 1


