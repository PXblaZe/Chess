from PIL import Image
#from elmts.plyrs import Player
from typing import Final, Tuple, Literal, List

Bside: Final[str]  = "black"
Wside: Final[str]  = "white"
Shared: Final[str] = "void"

class piece:
    def __init__(self, texture: Image.Image, pos: Tuple[int, int], side) -> None:
        self.pos: tuple = pos
        self.texture: Image.Image = texture
        self.side: Literal['black', 'white', 'void'] = side


class Void(piece):

    def __init__(self, texture: Image.Image, pos: Tuple[int, int], side) -> None:
        piece.__init__(self, texture, pos, side)
        self.weight: Final[float] = .0

    def __call__(self, board, box):
        pass
        

class Pawn(piece):

    def __init__(self, texture: Image.Image, pos: Tuple[int, int], side) -> None:
        piece.__init__(self, texture, pos, side)
        self.weight: Final[float] = 1/6

    def nexts(self, board) -> List[Tuple[int, int, bool]]: 
        new = list()
        if self.pos[0]==6 and isinstance(board.view[4][self.pos[1]].piece, Void):
            new.append((4, self.pos[1], False))
        if self.pos[0]-1>-1 and isinstance(board.view[self.pos[0]-1][self.pos[1]].piece, Void):
            new.append((self.pos[0]-1, self.pos[1], False))
        if self.pos[0]-1>-1 and self.pos[1]-1>-1 and board.view[self.pos[0]-1][self.pos[1]-1].piece.side not in [self.side, Shared]:
            new.append((self.pos[0]-1, self.pos[1]-1, True))
        if self.pos[1]+1<8 and self.pos[0]-1>-1 and board.view[self.pos[0]-1][self.pos[1]+1].piece.side not in [self.side, Shared]:
            new.append((self.pos[0]-1, self.pos[1]+1, True))
        return new

    def __call__(self, board, box): 
        moves = self.nexts(board)
        print(moves)


class Rook(piece):

    def __init__(self, texture: Image.Image, pos: tuple, side) -> None:
        piece.__init__(self, texture, pos, side)
        self.weight: Final[float] = 1/3

    def nexts(self, board) -> List[Tuple[int, int, bool]]:
        new = list()
        for i in range(self.pos[1]+1, 8): 
            c = board.view[self.pos[0]][i].piece.side
            if c == self.side: break
            elif c not in [self.side, Shared]:
                new.append((self.pos[0], i, True)); break
            new.append((self.pos[0], i, False))
        for i in range(self.pos[0]-1, -1, -1):
            c = board.view[i][self.pos[1]].piece.side
            if c == self.side: break
            elif c not in [self.side, Shared]:
                new.append((i, self.pos[1], True)); break
            new.append((i, self.pos[1], False))
        for i in range(self.pos[1]-1, -1, -1):
            c = board.view[self.pos[0]][i].piece.side
            if c == self.side: break
            elif c not in [self.side, Shared]:
                new.append((self.pos[0], i, True)); break
            new.append((self.pos[0], i, False))
        for i in range(self.pos[0]+1, 8): 
            c = board.view[i][self.pos[1]].piece.side
            if c == self.side: break
            elif c not in [self.side, Shared]:
                new.append((i, self.pos[1], True)); break
            new.append((i, self.pos[1], False))
        return new

    def __call__(self, board, box): 
        moves = self.nexts(board)
        print(moves)


class Knight(piece):

    def __init__(self, texture: Image.Image, pos: tuple, side) -> None:
        piece.__init__(self, texture, pos, side)
        self.weight: Final[float] = 2/3
    
    def nexts(self, board) -> List[Tuple[int, int, bool]]:
        n1, n2 = self.pos
        points = [
            (n1-2, n2+1), (n1-1, n2+2), (n1+1, n2+2),
            (n1+2, n2+1), (n1+2, n2-1), (n1+1, n2-2),
            (n1-1, n2-2), (n1-2, n2-1) 
        ]; new = list()
        for i in range(8):
            if points[i][0] in range(8) and points[i][1] in range(8) :
                p1, p2 = points[i]
                c = board.view[p1][p2].piece
                if self.side == c.side: pass
                elif isinstance(c, Void): new.append(points[i]+(False,))
                else: new.append(points[i]+(True,))
        return new

    def __call__(self, board, box): 
        moves = self.nexts(board)
        print(moves)
        

class Bishop(piece):

    def __init__(self, texture: Image.Image, pos: tuple, side) -> None:
        piece.__init__(self, texture, pos, side)
        self.weight: Final[float] = .5
    
    def nexts(self, board) -> List[Tuple[int, int, bool]]:
        new = list(); p1, p2 = self.pos
        fg1 = fg2 = fg3 = fg4 = True
        for i in range(p2+1, 8):
            f1 = (p1+p2-i, i); f4 = (p1+i-p2, i)
            if fg1 and f1[0] in range(p1):
                c1 = board.view[f1[0]][f1[1]].piece
                if c1.side == self.side: fg1 = False
                elif c1.side != Shared:
                    new.append(f1+(True,))
                else: new.append(f1+(False,))
            if fg4 and f4[0] in range(p1+1,8):
                c4 = board.view[f4[0]][f4[1]].piece
                if c4.side == self.side: fg4 = False
                elif c4.side != Shared:
                    new.append(f4+(True,))
                else: new.append(f4+(False,))
            if not fg1 and not fg4: break
        for i in range(p2-1, -1, -1):
            f2 = (p1+i-p2, i); f3 = (p1+p2-i, i, i)
            if fg2 and f2[0] in range(p1):
                c2 = board.view[f2[0]][f2[1]].piece
                if c2.side == self.side: fg2 = False
                elif c2.side != Shared:
                    new.append(f2+(True,))
                else: new.append(f2+(False,))
            if fg3 and f3[0] in range(p1+1,8):
                c3 = board.view[f3[0]][f3[1]].piece
                if c3.side == self.side: fg3 = False
                elif c3.side != Shared:
                    new.append(f3+(True,))
                else: new.append(f3+(False,))
            if not fg2 and not fg3: break
        return new

    def __call__(self, board, box): 
        moves = self.nexts(board)
        print(moves)


class Queen(piece):

    def __init__(self, texture: Image.Image, pos: tuple, side) -> None:
        piece.__init__(self, texture, pos, side)
        self.weight: Final[float] = 5/6

    def nexts(self, board) -> List[Tuple[int, int, bool]]:
        new = list(); p1, p2 = self.pos
        fg1 = fg2 = fg3 = fg4 = True
        for i in range(p2+1, 8):
            f1 = (p1+p2-i, i); f4 = (p1+i-p2, i)
            if fg1 and f1[0] in range(p1):
                c1 = board.view[f1[0]][f1[1]].piece
                if c1.side == self.side: fg1 = False
                elif c1.side != Shared:
                    new.append(f1+(True,))
                else: new.append(f1+(False,))
            if fg4 and f4[0] in range(p1+1,8):
                c4 = board.view[f4[0]][f4[1]].piece
                if c4.side == self.side: fg4 = False
                elif c4.side != Shared:
                    new.append(f4+(True,))
                else: new.append(f4+(False,))
            if not fg1 and not fg4: break
        for i in range(p2-1, -1, -1):
            f2 = (p1+i-p2, i); f3 = (p1+p2-i, i, i)
            if fg2 and f2[0] in range(p1):
                c2 = board.view[f2[0]][f2[1]].piece
                if c2.side == self.side: fg2 = False
                elif c2.side != Shared:
                    new.append(f2+(True,))
                else: new.append(f2+(False,))
            if fg3 and f3[0] in range(p1+1,8):
                c3 = board.view[f3[0]][f3[1]].piece
                if c3.side == self.side: fg3 = False
                elif c3.side != Shared:
                    new.append(f3+(True,))
                else: new.append(f3+(False,))
            if not fg2 and not fg3: break
        for i in range(self.pos[1]+1, 8): 
            c = board.view[self.pos[0]][i].piece.side
            if c == self.side: break
            elif c not in [self.side, Shared]:
                new.append((self.pos[0], i, True)); break
            new.append((self.pos[0], i, False))
        for i in range(self.pos[0]-1, -1, -1):
            c = board.view[i][self.pos[1]].piece.side
            if c == self.side: break
            elif c not in [self.side, Shared]:
                new.append((i, self.pos[1], True)); break
            new.append((i, self.pos[1], False))
        for i in range(self.pos[1]-1, -1, -1):
            c = board.view[self.pos[0]][i].piece.side
            if c == self.side: break
            elif c not in [self.side, Shared]:
                new.append((self.pos[0], i, True)); break
            new.append((self.pos[0], i, False))
        for i in range(self.pos[0]+1, 8): 
            c = board.view[i][self.pos[1]].piece.side
            if c == self.side: break
            elif c not in [self.side, Shared]:
                new.append((i, self.pos[1], True)); break
            new.append((i, self.pos[1], False))
        return new

    def __call__(self, board, box): 
        moves = self.nexts(board)
        print(moves)
    

class King(piece):

    def __init__(self, texture: Image.Image, pos: tuple, side) -> None:
        piece.__init__(self, texture, pos, side)
        self.weight: Final[float] = 1.0

    def nexts(self, board) -> List[Tuple[int, int, bool]]:
        k1, k2 = self.pos
        pts = [
            (k1-1, k2), (k1-1, k2+1), (k1, k2+1),
            (k1+1, k2+1), (k1+1, k2), (k1+1, k2-1),
            (k1, k2-1), (k1-1, k2-1)
        ]; new = list()
        for i in range(8):
            if pts[i][0] in range(8) and pts[i][1] in range(8): 
                p1, p2 = pts[i]
                c = board.view[p1][p2].piece
                if self.side == c.side: pass
                elif isinstance(c, Void): new.append(pts[i]+(False,))
                else: new.append(pts[i]+(True,))
        return new

    def __call__(self, board, box): 
        moves = self.nexts(board)
        print(moves)
