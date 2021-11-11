from utils import paste
from typing import Tuple
import data.Packs as Packs
import elmts.pieces as pieces
from PIL import Image, ImageTk
from tkinter import Canvas, Frame, Button


class Box(Button):

    def __init__(self, win: Frame, pos: Tuple[int, int], background_img: Image.Image, piece: pieces.piece) -> None:
        self.bgi = background_img
        self.piece = piece
        self.look = ImageTk.PhotoImage(paste(self.bgi, self.piece.texture)) if piece.side!=pieces.Shared else ImageTk.PhotoImage(self.bgi)
        self.hover = ImageTk.PhotoImage(paste(self.bgi, self.piece.texture, glow_mode="g")) if piece.side==win.player_side else ImageTk.PhotoImage(paste(self.bgi, self.piece.texture))
        Button.__init__(self, win, image=self.look, borderwidth=0, command=self.piece)
        self.grid(row=pos[0], column=pos[1])
        self.bind("<Enter>", lambda e: self.config(image=self.look if self.piece.side==pieces.Shared else self.hover))
        self.bind("<Leave>", lambda e: self.config(image=self.look))


class Board(Frame):
    def __init__(self, pack: Packs.load, player_side = pieces.Bside): 
        Frame.__init__(self, pack.win, width=pack.box_dim[0]*8, height=pack.box_dim[1]*8)    
        self.pack(anchor="nw")    
        self.player_side =player_side
        self.view = tuple([[None for _ in range(8)] for __ in range(8)])
        for _ in range(2):
            if self.player_side == pieces.Bside:
                for pc in pack.Wpieces:
                    if pc == "rook":
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]), round(pack.corrB[1]), round(pack.corrB[0]+pack.box_dim[0]), round(pack.corrB[1]+pack.box_dim[1])))
                        self.view[0][0] = Box(self, (0,0), bi, pieces.Rook(pack.Wpieces[pc], (0,0), pieces.Wside))
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(7*pack.box_dim[0])), round(pack.corrB[1]), round(pack.corrB[0]+(8*pack.box_dim[0])), round(pack.corrB[1]+pack.box_dim[1])))
                        self.view[0][7] = Box(self, (0,7), bi, pieces.Rook(pack.Wpieces[pc], (0,7), pieces.Wside))
                    elif pc == "knight": 
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+pack.box_dim[0]), round(pack.corrB[1]), round(pack.corrB[0]+(2*pack.box_dim[0])), round(pack.corrB[1]+pack.box_dim[1])))
                        self.view[0][1] = Box(self, (0,1), bi, pieces.Knight(pack.Wpieces[pc], (0,1), pieces.Wside))
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(6*pack.box_dim[0])), round(pack.corrB[1]), round(pack.corrB[0]+(7*pack.box_dim[0])), round(pack.corrB[1]+pack.box_dim[1])))
                        self.view[0][6] = Box(self, (0,6), bi, pieces.Knight(pack.Wpieces[pc], (0,6), pieces.Wside))
                    elif pc == "bishop":
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(2*pack.box_dim[0])), round(pack.corrB[1]), round(pack.corrB[0]+(3*pack.box_dim[0])), round(pack.corrB[1]+pack.box_dim[1])))
                        self.view[0][2] = Box(self, (0,2), bi, pieces.Bishop(pack.Wpieces[pc], (0,2), pieces.Wside))
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(5*pack.box_dim[0])), round(pack.corrB[1]), round(pack.corrB[0]+(6*pack.box_dim[0])), round(pack.corrB[1]+pack.box_dim[1])))
                        self.view[0][5] = Box(self, (0,5), bi, pieces.Bishop(pack.Wpieces[pc], (0,5), pieces.Wside))
                    elif pc == "king":
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(4*pack.box_dim[0])), round(pack.corrB[1]), round(pack.corrB[0]+(5*pack.box_dim[0])), round(pack.corrB[1]+pack.box_dim[1])))
                        self.view[0][4] = Box(self, (0,4), bi, pieces.King(pack.Wpieces[pc], (0,4), pieces.Wside))
                    elif pc == "queen":
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(3*pack.box_dim[0])), round(pack.corrB[1]), round(pack.corrB[0]+(4*pack.box_dim[0])), round(pack.corrB[1]+pack.box_dim[1])))
                        self.view[0][3] = Box(self, (0,3), bi, pieces.Queen(pack.Wpieces[pc], (0,3), pieces.Wside))
                else:
                    for j in range(8):
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(j*pack.box_dim[0])), round(pack.corrB[1]+pack.box_dim[1]), round(pack.corrB[0]+((j+1)*pack.box_dim[0])), round(pack.corrB[1]+(2*pack.box_dim[1]))))
                        self.view[1][j] = Box(self, (1,j), bi, pieces.Pawn(pack.Wpieces["pawn"], (1,j), pieces.Wside))
                for pc in pack.Bpieces:
                    if pc == "rook":
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]), round(pack.corrB[1]+(7*pack.box_dim[1])), round(pack.corrB[0]+pack.box_dim[0]), round(pack.corrB[1]+(8*pack.box_dim[1]))))
                        self.view[7][0] = Box(self, (7,0), bi, pieces.Rook(pack.Bpieces[pc], (7,0), pieces.Bside))
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(7*pack.box_dim[0])), round(pack.corrB[1]+(7*pack.box_dim[1])), round(pack.corrB[0]+(8*pack.box_dim[0])), round(pack.corrB[1]+(8*pack.box_dim[1]))))
                        self.view[7][7] = Box(self, (7,7), bi, pieces.Rook(pack.Bpieces[pc], (7,7), pieces.Bside))
                    elif pc == "knight": 
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+pack.box_dim[0]), round(pack.corrB[1]+(7*pack.box_dim[1])), round(pack.corrB[0]+(2*pack.box_dim[0])), round(pack.corrB[1]+(8*pack.box_dim[1]))))
                        self.view[7][1] = Box(self, (7,1), bi, pieces.Knight(pack.Bpieces[pc], (7,1), pieces.Bside))
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(6*pack.box_dim[0])), round(pack.corrB[1]+(7*pack.box_dim[1])), round(pack.corrB[0]+(7*pack.box_dim[0])), round(pack.corrB[1]+(8*pack.box_dim[1]))))
                        self.view[7][6] = Box(self, (7,6), bi, pieces.Knight(pack.Bpieces[pc], (7,6), pieces.Bside))
                    elif pc == "bishop":
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(2*pack.box_dim[0])), round(pack.corrB[1]+(7*pack.box_dim[1])), round(pack.corrB[0]+(3*pack.box_dim[0])), round(pack.corrB[1]+(8*pack.box_dim[1]))))
                        self.view[7][2] = Box(self, (7,2), bi, pieces.Bishop(pack.Bpieces[pc], (7,2), pieces.Bside))
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(5*pack.box_dim[0])), round(pack.corrB[1]+(7*pack.box_dim[1])), round(pack.corrB[0]+(6*pack.box_dim[0])), round(pack.corrB[1]+(8*pack.box_dim[1]))))
                        self.view[7][5] = Box(self, (7,5), bi, pieces.Bishop(pack.Bpieces[pc], (7,5), pieces.Bside))
                    elif pc == "king":
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(4*pack.box_dim[0])), round(pack.corrB[1])+(7*pack.box_dim[1]), round(pack.corrB[0]+(5*pack.box_dim[0])), round(pack.corrB[1]+(8*pack.box_dim[1]))))
                        self.view[7][4] = Box(self, (7,4), bi, pieces.King(pack.Bpieces[pc], (7,4), pieces.Bside))
                    elif pc == "queen":
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(3*pack.box_dim[0])), round(pack.corrB[1]+(7*pack.box_dim[1])), round(pack.corrB[0]+(4*pack.box_dim[0])), round(pack.corrB[1]+(8*pack.box_dim[1]))))
                        self.view[7][3] = Box(self, (7,3), bi, pieces.Queen(pack.Bpieces[pc], (7,3), pieces.Bside))
                else:
                    for j in range(8):
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(j*pack.box_dim[0])), round(pack.corrB[1]+(6*pack.box_dim[1])), round(pack.corrB[0]+((j+1)*pack.box_dim[0])), round(pack.corrB[1]+(7*pack.box_dim[1]))))
                        self.view[6][j] = Box(self, (6,j), bi, pieces.Pawn(pack.Bpieces["pawn"], (6,j), pieces.Bside))
            elif self.player_side == pieces.Wside: 
                for pc in pack.Bpieces:
                    if pc == "rook":
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]), round(pack.corrB[1]), round(pack.corrB[0]+pack.box_dim[0]), round(pack.corrB[1]+pack.box_dim[1])))
                        self.view[0][0] = Box(self, (0,0), bi, pieces.Rook(pack.Bpieces[pc], (0,0), pieces.Bside))
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(7*pack.box_dim[0])), round(pack.corrB[1]), round(pack.corrB[0]+(8*pack.box_dim[0])), round(pack.corrB[1]+pack.box_dim[1])))
                        self.view[0][7] = Box(self, (0,7), bi, pieces.Rook(pack.Bpieces[pc], (0,7), pieces.Bside))
                    elif pc == "knight": 
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+pack.box_dim[0]), round(pack.corrB[1]), round(pack.corrB[0]+(2*pack.box_dim[0])), round(pack.corrB[1]+pack.box_dim[1])))
                        self.view[0][1] = Box(self, (0,1), bi, pieces.Knight(pack.Bpieces[pc], (0,1), pieces.Bside))
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(6*pack.box_dim[0])), round(pack.corrB[1]), round(pack.corrB[0]+(7*pack.box_dim[0])), round(pack.corrB[1]+pack.box_dim[1])))
                        self.view[0][6] = Box(self, (0,6), bi, pieces.Knight(pack.Bpieces[pc], (0,3), pieces.Bside))
                    elif pc == "bishop":
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(2*pack.box_dim[0])), round(pack.corrB[1]), round(pack.corrB[0]+(3*pack.box_dim[0])), round(pack.corrB[1]+pack.box_dim[1])))
                        self.view[0][2] = Box(self, (0,2), bi, pieces.Bishop(pack.Bpieces[pc], (0,2), pieces.Bside))
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(5*pack.box_dim[0])), round(pack.corrB[1]), round(pack.corrB[0]+(6*pack.box_dim[0])), round(pack.corrB[1]+pack.box_dim[1])))
                        self.view[0][5] = Box(self, (0,5), bi, pieces.Bishop(pack.Bpieces[pc], (0,5), pieces.Bside))
                    elif pc == "king":
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(4*pack.box_dim[0])), round(pack.corrB[1]), round(pack.corrB[0]+(5*pack.box_dim[0])), round(pack.corrB[1]+pack.box_dim[1])))
                        self.view[0][4] = Box(self, (0,4), bi, pieces.King(pack.Bpieces[pc], (0,4), pieces.Bside))
                    elif pc == "queen":
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(3*pack.box_dim[0])), round(pack.corrB[1]), round(pack.corrB[0]+(4*pack.box_dim[0])), round(pack.corrB[1]+pack.box_dim[1])))
                        self.view[0][3] = Box(self, (0,3), bi, pieces.Queen(pack.Bpieces[pc], (0,3), pieces.Bside))
                else:
                    for j in range(8):
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(j*pack.box_dim[0])), round(pack.corrB[1]+pack.box_dim[1]), round(pack.corrB[0]+((j+1)*pack.box_dim[0])), round(pack.corrB[1]+(2*pack.box_dim[1]))))
                        self.view[1][j] = Box(self, (1,j), bi, pieces.Pawn(pack.Bpieces["pawn"], (1,j), pieces.Bside))
                for pc in pack.Wpieces:
                    if pc == "rook":
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]), round(pack.corrB[1]+(7*pack.box_dim[1])), round(pack.corrB[0]+pack.box_dim[0]), round(pack.corrB[1]+(8*pack.box_dim[1]))))
                        self.view[7][0] = Box(self, (7,0), bi, pieces.Rook(pack.Wpieces[pc], (7,0), pieces.Wside))
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(7*pack.box_dim[0])), round(pack.corrB[1]+(7*pack.box_dim[1])), round(pack.corrB[0]+(8*pack.box_dim[0])), round(pack.corrB[1]+(8*pack.box_dim[1]))))
                        self.view[7][7] = Box(self, (7,7), bi, pieces.Rook(pack.Wpieces[pc], (7,7), pieces.Wside))
                    elif pc == "knight": 
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+pack.box_dim[0]), round(pack.corrB[1]+(7*pack.box_dim[1])), round(pack.corrB[0]+(2*pack.box_dim[0])), round(pack.corrB[1]+(8*pack.box_dim[1]))))
                        self.view[7][1] = Box(self, (7,1), bi, pieces.Knight(pack.Wpieces[pc], (7,1), pieces.Wside))
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(6*pack.box_dim[0])), round(pack.corrB[1]+(7*pack.box_dim[1])), round(pack.corrB[0]+(7*pack.box_dim[0])), round(pack.corrB[1]+(8*pack.box_dim[1]))))
                        self.view[7][6] = Box(self, (7,6), bi, pieces.Knight(pack.Wpieces[pc], (7,6), pieces.Wside))
                    elif pc == "bishop":
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(2*pack.box_dim[0])), round(pack.corrB[1]+(7*pack.box_dim[1])), round(pack.corrB[0]+(3*pack.box_dim[0])), round(pack.corrB[1]+(8*pack.box_dim[1]))))
                        self.view[7][2] = Box(self, (7,2), bi, pieces.Bishop(pack.Wpieces[pc], (7,2), pieces.Wside))
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(5*pack.box_dim[0])), round(pack.corrB[1]+(7*pack.box_dim[1])), round(pack.corrB[0]+(6*pack.box_dim[0])), round(pack.corrB[1]+(8*pack.box_dim[1]))))
                        self.view[7][5] = Box(self, (7,5), bi, pieces.Bishop(pack.Wpieces[pc], (7,5), pieces.Wside))
                    elif pc == "king":
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(4*pack.box_dim[0])), round(pack.corrB[1])+(7*pack.box_dim[1]), round(pack.corrB[0]+(5*pack.box_dim[0])), round(pack.corrB[1]+(8*pack.box_dim[1]))))
                        self.view[7][4] = Box(self, (7,4), bi, pieces.King(pack.Wpieces[pc], (7,4), pieces.Wside))
                    elif pc == "queen":
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(3*pack.box_dim[0])), round(pack.corrB[1]+(7*pack.box_dim[1])), round(pack.corrB[0]+(4*pack.box_dim[0])), round(pack.corrB[1]+(8*pack.box_dim[1]))))
                        self.view[7][3] = Box(self, (7,3), bi, pieces.Queen(pack.Wpieces[pc], (7,3), pieces.Wside))
                else:
                    for j in range(8):
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(j*pack.box_dim[0])), round(pack.corrB[1]+(6*pack.box_dim[1])), round(pack.corrB[0]+((j+1)*pack.box_dim[0])), round(pack.corrB[1]+(7*pack.box_dim[1]))))
                        self.view[6][j] = Box(self, (6,j), bi, pieces.Pawn(pack.Wpieces["pawn"], (6,j), pieces.Wside))
            else: raise ValueError()
            for i in range(4):
                for j in range(8):
                    bi = pack.iBoard.crop((round(pack.corrB[0]+(j*pack.box_dim[0])), round(pack.corrB[1]+((i+2)*pack.box_dim[1])), round(pack.corrB[0]+((j+1)*pack.box_dim[0])), round(pack.corrB[1]+((i+3)*pack.box_dim[1]))))
                    self.view[i+2][j] = Box(self, (i+2,j), bi, pieces.Void(bi, (i,j), pieces.Shared))


class Table(Canvas):

    def __init__(self, pack: Packs.load):    
        Canvas.__init__(self, pack.win, width=pack.win.winfo_screenwidth(), height=pack.win.winfo_screenheight())
        self.pack(anchor="nw")
        im1 = pack.iTable.copy()
        im2 = pack.iBoard.copy()
        self.pzcod = ((im1.width*.2) + pack.corrB[0], (im1.height*.05) + pack.corrB[1])
        im1.paste(im2, (round(im1.width*.2), round(im1.height*.05)))
        self.look = ImageTk.PhotoImage(im1)
        self.create_image(0, 0, anchor="nw", image=self.look, )

    def initBoard(self, board: Board):
        self.create_window(self.pzcod[0], self.pzcod[1], anchor="nw", window=board)
        