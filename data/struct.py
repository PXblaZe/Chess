from utils import paste
from PIL import ImageTk
import data.Packs as Packs
from typing import Callable
import elmts.pieces as pieces
from tkinter import Canvas, Frame, Button


class Box(Button):

    def __init__(self, win, size, func: Callable, *data) -> None:
        self.bg = data[0]
        self.look = data[1]
        self.hover = data[2]
        Button.__init__(self, win, width=size[0], height=size[1], image=self.look, borderwidth=0, command=func)

    def __call__(self, index: int = None):
        return (self.bg, self.look, self.hover) if index==None else (self.bg, self.look, self.hover)[index]


class Board(Frame):
    def __init__(self, pack: Packs.load, player_side = pieces.Bside): 
        Frame.__init__(self, pack.win, width=pack.box_dim[0]*8, height=pack.box_dim[1]*8)    
        self.pack(anchor="nw")    
        self.view = tuple([[None for _ in range(8)] for __ in range(8)])
        def on_hover(i, j): self.view[i][j].config(image=self.view[i][j].hover)
        def off_hover(i, j): self.view[i][j].config(image=self.view[i][j].look)
        for _ in range(2):
            if player_side == pieces.Bside:
                for pc in pack.Wpieces:
                    if pc == "rook":
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]), round(pack.corrB[1]), round(pack.corrB[0]+pack.box_dim[0]), round(pack.corrB[1]+pack.box_dim[1])))
                        self.view[0][0] = Box(self, pack.box_dim, ..., 
                            ImageTk.PhotoImage(bi),
                            ImageTk.PhotoImage(paste(bi, pack.Wpieces[pc])),
                            ImageTk.PhotoImage(paste(bi, pack.Wpieces[pc]))
                        )
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(7*pack.box_dim[0])), round(pack.corrB[1]), round(pack.corrB[0]+(8*pack.box_dim[0])), round(pack.corrB[1]+pack.box_dim[1])))
                        self.view[0][7] = Box(self, pack.box_dim, ..., 
                            ImageTk.PhotoImage(bi),
                            ImageTk.PhotoImage(paste(bi, pack.Wpieces[pc])),
                            ImageTk.PhotoImage(paste(bi, pack.Wpieces[pc]))
                        )
                        self.view[0][0].grid(row=0, column=0)
                        self.view[0][0].bind("<Enter>", lambda e, i=0, j=0: on_hover(i,j))
                        self.view[0][0].bind("<Leave>", lambda e, i=0, j=0: off_hover(i,j))
                        self.view[0][7].grid(row=0, column=7)
                        self.view[0][7].bind("<Enter>", lambda e, i=0, j=7: on_hover(i,j))
                        self.view[0][7].bind("<Leave>", lambda e, i=0, j=7: off_hover(i,j))
                    elif pc == "knight": 
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+pack.box_dim[0]), round(pack.corrB[1]), round(pack.corrB[0]+(2*pack.box_dim[0])), round(pack.corrB[1]+pack.box_dim[1])))
                        self.view[0][1] = Box(self, pack.box_dim, ..., 
                            ImageTk.PhotoImage(bi),
                            ImageTk.PhotoImage(paste(bi, pack.Wpieces[pc])),
                            ImageTk.PhotoImage(paste(bi, pack.Wpieces[pc]))
                        )
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(6*pack.box_dim[0])), round(pack.corrB[1]), round(pack.corrB[0]+(7*pack.box_dim[0])), round(pack.corrB[1]+pack.box_dim[1])))
                        self.view[0][6] = Box(self, pack.box_dim, ..., 
                            ImageTk.PhotoImage(bi),
                            ImageTk.PhotoImage(paste(bi, pack.Wpieces[pc])),
                            ImageTk.PhotoImage(paste(bi, pack.Wpieces[pc]))
                        )
                        self.view[0][1].grid(row=0, column=1)
                        self.view[0][1].bind("<Enter>", lambda e, i=0, j=1: on_hover(i,j))
                        self.view[0][1].bind("<Leave>", lambda e, i=0, j=1: off_hover(i,j))
                        self.view[0][6].grid(row=0, column=6)
                        self.view[0][6].bind("<Enter>", lambda e, i=0, j=6: on_hover(i,j))
                        self.view[0][6].bind("<Leave>", lambda e, i=0, j=6: off_hover(i,j))
                    elif pc == "bishop":
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(2*pack.box_dim[0])), round(pack.corrB[1]), round(pack.corrB[0]+(3*pack.box_dim[0])), round(pack.corrB[1]+pack.box_dim[1])))
                        self.view[0][2] = Box(self, pack.box_dim, ..., 
                            ImageTk.PhotoImage(bi),
                            ImageTk.PhotoImage(paste(bi, pack.Wpieces[pc])),
                            ImageTk.PhotoImage(paste(bi, pack.Wpieces[pc]))
                        )
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(5*pack.box_dim[0])), round(pack.corrB[1]), round(pack.corrB[0]+(6*pack.box_dim[0])), round(pack.corrB[1]+pack.box_dim[1])))
                        self.view[0][5] = Box(self, pack.box_dim, ..., 
                            ImageTk.PhotoImage(bi),
                            ImageTk.PhotoImage(paste(bi, pack.Wpieces[pc])),
                            ImageTk.PhotoImage(paste(bi, pack.Wpieces[pc]))
                        )
                        self.view[0][2].grid(row=0, column=2)
                        self.view[0][2].bind("<Enter>", lambda e, i=0, j=2: on_hover(i,j))
                        self.view[0][2].bind("<Leave>", lambda e, i=0, j=2: off_hover(i,j))
                        self.view[0][5].grid(row=0, column=5)
                        self.view[0][5].bind("<Enter>", lambda e, i=0, j=5: on_hover(i,j))
                        self.view[0][5].bind("<Leave>", lambda e, i=0, j=5: off_hover(i,j))
                    elif pc == "king":
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(4*pack.box_dim[0])), round(pack.corrB[1]), round(pack.corrB[0]+(5*pack.box_dim[0])), round(pack.corrB[1]+pack.box_dim[1])))
                        self.view[0][4] = Box(self, pack.box_dim, ..., 
                            ImageTk.PhotoImage(bi),
                            ImageTk.PhotoImage(paste(bi, pack.Wpieces[pc])),
                            ImageTk.PhotoImage(paste(bi, pack.Wpieces[pc]))
                        )
                        self.view[0][4].grid(row=0, column=4)
                        self.view[0][4].bind("<Enter>", lambda e, i=0, j=4: on_hover(i,j))
                        self.view[0][4].bind("<Leave>", lambda e, i=0, j=4: off_hover(i,j))
                    elif pc == "queen":
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(3*pack.box_dim[0])), round(pack.corrB[1]), round(pack.corrB[0]+(4*pack.box_dim[0])), round(pack.corrB[1]+pack.box_dim[1])))
                        self.view[0][3] = Box(self, pack.box_dim, ..., 
                            ImageTk.PhotoImage(bi),
                            ImageTk.PhotoImage(paste(bi, pack.Wpieces[pc])),
                            ImageTk.PhotoImage(paste(bi, pack.Wpieces[pc]))
                        )
                        self.view[0][3].grid(row=0, column=3)
                        self.view[0][3].bind("<Enter>", lambda e, i=0, j=3: on_hover(i,j))
                        self.view[0][3].bind("<Leave>", lambda e, i=0, j=3: off_hover(i,j))
                else:
                    for j in range(8):
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(j*pack.box_dim[0])), round(pack.corrB[1]+pack.box_dim[1]), round(pack.corrB[0]+((j+1)*pack.box_dim[0])), round(pack.corrB[1]+(2*pack.box_dim[1]))))
                        self.view[1][j] = Box(self, pack.box_dim, ..., 
                            ImageTk.PhotoImage(bi),
                            ImageTk.PhotoImage(paste(bi, pack.Wpieces["pawn"])),
                            ImageTk.PhotoImage(paste(bi, pack.Wpieces["pawn"]))
                        )
                        self.view[1][j].grid(row=1, column=j)
                        self.view[1][j].bind("<Enter>", lambda e, i=1, j=j: on_hover(i,j))
                        self.view[1][j].bind("<Leave>", lambda e, i=1, j=j: off_hover(i,j))
                for pc in pack.Bpieces:
                    if pc == "rook":
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]), round(pack.corrB[1]+(7*pack.box_dim[1])), round(pack.corrB[0]+pack.box_dim[0]), round(pack.corrB[1]+(8*pack.box_dim[1]))))
                        self.view[7][0] = Box(self, pack.box_dim, ..., 
                            ImageTk.PhotoImage(bi),
                            ImageTk.PhotoImage(paste(bi, pack.Bpieces[pc])),
                            ImageTk.PhotoImage(paste(bi, pack.Bpieces[pc], glow_mode="g"))
                        )
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(7*pack.box_dim[0])), round(pack.corrB[1]+(7*pack.box_dim[1])), round(pack.corrB[0]+(8*pack.box_dim[0])), round(pack.corrB[1]+(8*pack.box_dim[1]))))
                        self.view[7][7] = Box(self, pack.box_dim, ..., 
                            ImageTk.PhotoImage(bi),
                            ImageTk.PhotoImage(paste(bi, pack.Bpieces[pc])),
                            ImageTk.PhotoImage(paste(bi, pack.Bpieces[pc], glow_mode="g"))
                        )
                        self.view[7][0].grid(row=7, column=0)
                        self.view[7][0].bind("<Enter>", lambda e, i=7, j=0: on_hover(i,j))
                        self.view[7][0].bind("<Leave>", lambda e, i=7, j=0: off_hover(i,j))
                        self.view[7][7].grid(row=7, column=7)
                        self.view[7][7].bind("<Enter>", lambda e, i=7, j=7: on_hover(i,j))
                        self.view[7][7].bind("<Leave>", lambda e, i=7, j=7: off_hover(i,j))
                    elif pc == "knight": 
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+pack.box_dim[0]), round(pack.corrB[1]+(7*pack.box_dim[1])), round(pack.corrB[0]+(2*pack.box_dim[0])), round(pack.corrB[1]+(8*pack.box_dim[1]))))
                        self.view[7][1] = Box(self, pack.box_dim, ..., 
                            ImageTk.PhotoImage(bi),
                            ImageTk.PhotoImage(paste(bi, pack.Bpieces[pc])),
                            ImageTk.PhotoImage(paste(bi, pack.Bpieces[pc], glow_mode="g"))
                        )
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(6*pack.box_dim[0])), round(pack.corrB[1]+(7*pack.box_dim[1])), round(pack.corrB[0]+(7*pack.box_dim[0])), round(pack.corrB[1]+(8*pack.box_dim[1]))))
                        self.view[7][6] = Box(self, pack.box_dim, ..., 
                            ImageTk.PhotoImage(bi),
                            ImageTk.PhotoImage(paste(bi, pack.Bpieces[pc])),
                            ImageTk.PhotoImage(paste(bi, pack.Bpieces[pc], glow_mode="g"))
                        )
                        self.view[7][1].grid(row=7, column=1)
                        self.view[7][1].bind("<Enter>", lambda e, i=7, j=1: on_hover(i,j))
                        self.view[7][1].bind("<Leave>", lambda e, i=7, j=1: off_hover(i,j))
                        self.view[7][6].grid(row=7, column=6)
                        self.view[7][6].bind("<Enter>", lambda e, i=7, j=6: on_hover(i,j))
                        self.view[7][6].bind("<Leave>", lambda e, i=7, j=6: off_hover(i,j))
                    elif pc == "bishop":
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(2*pack.box_dim[0])), round(pack.corrB[1]+(7*pack.box_dim[1])), round(pack.corrB[0]+(3*pack.box_dim[0])), round(pack.corrB[1]+(8*pack.box_dim[1]))))
                        self.view[7][2] = Box(self, pack.box_dim, ..., 
                            ImageTk.PhotoImage(bi),
                            ImageTk.PhotoImage(paste(bi, pack.Bpieces[pc])),
                            ImageTk.PhotoImage(paste(bi, pack.Bpieces[pc], glow_mode="g"))
                        )
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(5*pack.box_dim[0])), round(pack.corrB[1]+(7*pack.box_dim[1])), round(pack.corrB[0]+(6*pack.box_dim[0])), round(pack.corrB[1]+(8*pack.box_dim[1]))))
                        self.view[7][5] = Box(self, pack.box_dim, ..., 
                            ImageTk.PhotoImage(bi),
                            ImageTk.PhotoImage(paste(bi, pack.Bpieces[pc])),
                            ImageTk.PhotoImage(paste(bi, pack.Bpieces[pc], glow_mode="g"))
                        )
                        self.view[7][2].grid(row=7, column=2)
                        self.view[7][2].bind("<Enter>", lambda e, i=7, j=2: on_hover(i,j))
                        self.view[7][2].bind("<Leave>", lambda e, i=7, j=2: off_hover(i,j))
                        self.view[7][5].grid(row=7, column=5)
                        self.view[7][5].bind("<Enter>", lambda e, i=7, j=5: on_hover(i,j))
                        self.view[7][5].bind("<Leave>", lambda e, i=7, j=5: off_hover(i,j))
                    elif pc == "king":
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(4*pack.box_dim[0])), round(pack.corrB[1])+(7*pack.box_dim[1]), round(pack.corrB[0]+(5*pack.box_dim[0])), round(pack.corrB[1]+(8*pack.box_dim[1]))))
                        self.view[7][4] = Box(self, pack.box_dim, ..., 
                            ImageTk.PhotoImage(bi),
                            ImageTk.PhotoImage(paste(bi, pack.Bpieces[pc])),
                            ImageTk.PhotoImage(paste(bi, pack.Bpieces[pc], glow_mode="g"))
                        )
                        self.view[7][4].grid(row=7, column=4)
                        self.view[7][4].bind("<Enter>", lambda e, i=7, j=4: on_hover(i,j))
                        self.view[7][4].bind("<Leave>", lambda e, i=7, j=4: off_hover(i,j))
                    elif pc == "queen":
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(3*pack.box_dim[0])), round(pack.corrB[1]+(7*pack.box_dim[1])), round(pack.corrB[0]+(4*pack.box_dim[0])), round(pack.corrB[1]+(8*pack.box_dim[1]))))
                        self.view[7][3] = Box(self, pack.box_dim, ..., 
                            ImageTk.PhotoImage(bi),
                            ImageTk.PhotoImage(paste(bi, pack.Bpieces[pc])),
                            ImageTk.PhotoImage(paste(bi, pack.Bpieces[pc], glow_mode="g"))
                        )
                        self.view[7][3].grid(row=7, column=3)
                        self.view[7][3].bind("<Enter>", lambda e, i=7, j=3: on_hover(i,j))
                        self.view[7][3].bind("<Leave>", lambda e, i=7, j=3: off_hover(i,j))
                else:
                    for j in range(8):
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(j*pack.box_dim[0])), round(pack.corrB[1]+(6*pack.box_dim[1])), round(pack.corrB[0]+((j+1)*pack.box_dim[0])), round(pack.corrB[1]+(7*pack.box_dim[1]))))
                        self.view[6][j] = Box(self, pack.box_dim, ..., 
                            ImageTk.PhotoImage(bi),
                            ImageTk.PhotoImage(paste(bi, pack.Bpieces["pawn"])),
                            ImageTk.PhotoImage(paste(bi, pack.Bpieces["pawn"], glow_mode="g"))
                        )
                        self.view[6][j].grid(row=6, column=j)
                        self.view[6][j].bind("<Enter>", lambda e, i=6, j=j: on_hover(i,j))
                        self.view[6][j].bind("<Leave>", lambda e, i=6, j=j: off_hover(i,j))
            elif player_side == pieces.Wside: 
                for pc in pack.Bpieces:
                    if pc == "rook":
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]), round(pack.corrB[1]), round(pack.corrB[0]+pack.box_dim[0]), round(pack.corrB[1]+pack.box_dim[1])))
                        self.view[0][0] = Box(self, pack.box_dim, ..., 
                            ImageTk.PhotoImage(bi),
                            ImageTk.PhotoImage(paste(bi, pack.Bpieces[pc])),
                            ImageTk.PhotoImage(paste(bi, pack.Bpieces[pc]))
                        )
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(7*pack.box_dim[0])), round(pack.corrB[1]), round(pack.corrB[0]+(8*pack.box_dim[0])), round(pack.corrB[1]+pack.box_dim[1])))
                        self.view[0][7] = Box(self, pack.box_dim, ..., 
                            ImageTk.PhotoImage(bi),
                            ImageTk.PhotoImage(paste(bi, pack.Bpieces[pc])),
                            ImageTk.PhotoImage(paste(bi, pack.Bpieces[pc]))
                        )
                        self.view[0][0].grid(row=0, column=0)
                        self.view[0][0].bind("<Enter>", lambda e, i=0, j=0: on_hover(i,j))
                        self.view[0][0].bind("<Leave>", lambda e, i=0, j=0: off_hover(i,j))
                        self.view[0][7].grid(row=0, column=7)
                        self.view[0][7].bind("<Enter>", lambda e, i=0, j=7: on_hover(i,j))
                        self.view[0][7].bind("<Leave>", lambda e, i=0, j=7: off_hover(i,j))
                    elif pc == "knight": 
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+pack.box_dim[0]), round(pack.corrB[1]), round(pack.corrB[0]+(2*pack.box_dim[0])), round(pack.corrB[1]+pack.box_dim[1])))
                        self.view[0][1] = Box(self, pack.box_dim, ..., 
                            ImageTk.PhotoImage(bi),
                            ImageTk.PhotoImage(paste(bi, pack.Bpieces[pc])),
                            ImageTk.PhotoImage(paste(bi, pack.Bpieces[pc]))
                        )
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(6*pack.box_dim[0])), round(pack.corrB[1]), round(pack.corrB[0]+(7*pack.box_dim[0])), round(pack.corrB[1]+pack.box_dim[1])))
                        self.view[0][6] = Box(self, pack.box_dim, ..., 
                            ImageTk.PhotoImage(bi),
                            ImageTk.PhotoImage(paste(bi, pack.Bpieces[pc])),
                            ImageTk.PhotoImage(paste(bi, pack.Bpieces[pc]))
                        )
                        self.view[0][1].grid(row=0, column=1)
                        self.view[0][1].bind("<Enter>", lambda e, i=0, j=1: on_hover(i,j))
                        self.view[0][1].bind("<Leave>", lambda e, i=0, j=1: off_hover(i,j))
                        self.view[0][6].grid(row=0, column=6)
                        self.view[0][6].bind("<Enter>", lambda e, i=0, j=6: on_hover(i,j))
                        self.view[0][6].bind("<Leave>", lambda e, i=0, j=6: off_hover(i,j))
                    elif pc == "bishop":
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(2*pack.box_dim[0])), round(pack.corrB[1]), round(pack.corrB[0]+(3*pack.box_dim[0])), round(pack.corrB[1]+pack.box_dim[1])))
                        self.view[0][2] = Box(self, pack.box_dim, ..., 
                            ImageTk.PhotoImage(bi),
                            ImageTk.PhotoImage(paste(bi, pack.Bpieces[pc])),
                            ImageTk.PhotoImage(paste(bi, pack.Bpieces[pc]))
                        )
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(5*pack.box_dim[0])), round(pack.corrB[1]), round(pack.corrB[0]+(6*pack.box_dim[0])), round(pack.corrB[1]+pack.box_dim[1])))
                        self.view[0][5] = Box(self, pack.box_dim, ..., 
                            ImageTk.PhotoImage(bi),
                            ImageTk.PhotoImage(paste(bi, pack.Bpieces[pc])),
                            ImageTk.PhotoImage(paste(bi, pack.Bpieces[pc]))
                        )
                        self.view[0][2].grid(row=0, column=2)
                        self.view[0][2].bind("<Enter>", lambda e, i=0, j=2: on_hover(i,j))
                        self.view[0][2].bind("<Leave>", lambda e, i=0, j=2: off_hover(i,j))
                        self.view[0][5].grid(row=0, column=5)
                        self.view[0][5].bind("<Enter>", lambda e, i=0, j=5: on_hover(i,j))
                        self.view[0][5].bind("<Leave>", lambda e, i=0, j=5: off_hover(i,j))
                    elif pc == "king":
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(4*pack.box_dim[0])), round(pack.corrB[1]), round(pack.corrB[0]+(5*pack.box_dim[0])), round(pack.corrB[1]+pack.box_dim[1])))
                        self.view[0][4] = Box(self, pack.box_dim, ..., 
                            ImageTk.PhotoImage(bi),
                            ImageTk.PhotoImage(paste(bi, pack.Bpieces[pc])),
                            ImageTk.PhotoImage(paste(bi, pack.Bpieces[pc]))
                        )
                        self.view[0][4].grid(row=0, column=4)
                        self.view[0][4].bind("<Enter>", lambda e, i=0, j=4: on_hover(i,j))
                        self.view[0][4].bind("<Leave>", lambda e, i=0, j=4: off_hover(i,j))
                    elif pc == "queen":
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(3*pack.box_dim[0])), round(pack.corrB[1]), round(pack.corrB[0]+(4*pack.box_dim[0])), round(pack.corrB[1]+pack.box_dim[1])))
                        self.view[0][3] = Box(self, pack.box_dim, ..., 
                            ImageTk.PhotoImage(bi),
                            ImageTk.PhotoImage(paste(bi, pack.Bpieces[pc])),
                            ImageTk.PhotoImage(paste(bi, pack.Bpieces[pc]))
                        )
                        self.view[0][3].grid(row=0, column=3)
                        self.view[0][3].bind("<Enter>", lambda e, i=0, j=3: on_hover(i,j))
                        self.view[0][3].bind("<Leave>", lambda e, i=0, j=3: off_hover(i,j))
                else:
                    for j in range(8):
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(j*pack.box_dim[0])), round(pack.corrB[1]+pack.box_dim[1]), round(pack.corrB[0]+((j+1)*pack.box_dim[0])), round(pack.corrB[1]+(2*pack.box_dim[1]))))
                        self.view[1][j] = Box(self, pack.box_dim, ..., 
                            ImageTk.PhotoImage(bi),
                            ImageTk.PhotoImage(paste(bi, pack.Bpieces["pawn"])),
                            ImageTk.PhotoImage(paste(bi, pack.Bpieces["pawn"]))
                        )
                        self.view[1][j].grid(row=1, column=j)
                        self.view[1][j].bind("<Enter>", lambda e, i=1, j=j: on_hover(i,j))
                        self.view[1][j].bind("<Leave>", lambda e, i=1, j=j: off_hover(i,j))
                for pc in pack.Wpieces:
                    if pc == "rook":
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]), round(pack.corrB[1]+(7*pack.box_dim[1])), round(pack.corrB[0]+pack.box_dim[0]), round(pack.corrB[1]+(8*pack.box_dim[1]))))
                        self.view[7][0] = Box(self, pack.box_dim, ..., 
                            ImageTk.PhotoImage(bi),
                            ImageTk.PhotoImage(paste(bi, pack.Wpieces[pc])),
                            ImageTk.PhotoImage(paste(bi, pack.Wpieces[pc], glow_mode="g"))
                        )
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(7*pack.box_dim[0])), round(pack.corrB[1]+(7*pack.box_dim[1])), round(pack.corrB[0]+(8*pack.box_dim[0])), round(pack.corrB[1]+(8*pack.box_dim[1]))))
                        self.view[7][7] = Box(self, pack.box_dim, ..., 
                            ImageTk.PhotoImage(bi),
                            ImageTk.PhotoImage(paste(bi, pack.Wpieces[pc])),
                            ImageTk.PhotoImage(paste(bi, pack.Wpieces[pc], glow_mode="g"))
                        )
                        self.view[7][0].grid(row=7, column=0)
                        self.view[7][0].bind("<Enter>", lambda e, i=7, j=0: on_hover(i,j))
                        self.view[7][0].bind("<Leave>", lambda e, i=7, j=0: off_hover(i,j))
                        self.view[7][7].grid(row=7, column=7)
                        self.view[7][7].bind("<Enter>", lambda e, i=7, j=7: on_hover(i,j))
                        self.view[7][7].bind("<Leave>", lambda e, i=7, j=7: off_hover(i,j))
                    elif pc == "knight": 
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+pack.box_dim[0]), round(pack.corrB[1]+(7*pack.box_dim[1])), round(pack.corrB[0]+(2*pack.box_dim[0])), round(pack.corrB[1]+(8*pack.box_dim[1]))))
                        self.view[7][1] = Box(self, pack.box_dim, ..., 
                            ImageTk.PhotoImage(bi),
                            ImageTk.PhotoImage(paste(bi, pack.Wpieces[pc])),
                            ImageTk.PhotoImage(paste(bi, pack.Wpieces[pc], glow_mode="g"))
                        )
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(6*pack.box_dim[0])), round(pack.corrB[1]+(7*pack.box_dim[1])), round(pack.corrB[0]+(7*pack.box_dim[0])), round(pack.corrB[1]+(8*pack.box_dim[1]))))
                        self.view[7][6] = Box(self, pack.box_dim, ..., 
                            ImageTk.PhotoImage(bi),
                            ImageTk.PhotoImage(paste(bi, pack.Wpieces[pc])),
                            ImageTk.PhotoImage(paste(bi, pack.Wpieces[pc], glow_mode="g"))
                        )
                        self.view[7][1].grid(row=7, column=1)
                        self.view[7][1].bind("<Enter>", lambda e, i=7, j=1: on_hover(i,j))
                        self.view[7][1].bind("<Leave>", lambda e, i=7, j=1: off_hover(i,j))
                        self.view[7][6].grid(row=7, column=6)
                        self.view[7][6].bind("<Enter>", lambda e, i=7, j=6: on_hover(i,j))
                        self.view[7][6].bind("<Leave>", lambda e, i=7, j=6: off_hover(i,j))
                    elif pc == "bishop":
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(2*pack.box_dim[0])), round(pack.corrB[1]+(7*pack.box_dim[1])), round(pack.corrB[0]+(3*pack.box_dim[0])), round(pack.corrB[1]+(8*pack.box_dim[1]))))
                        self.view[7][2] = Box(self, pack.box_dim, ..., 
                            ImageTk.PhotoImage(bi),
                            ImageTk.PhotoImage(paste(bi, pack.Wpieces[pc])),
                            ImageTk.PhotoImage(paste(bi, pack.Wpieces[pc], glow_mode="g"))
                        )
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(5*pack.box_dim[0])), round(pack.corrB[1]+(7*pack.box_dim[1])), round(pack.corrB[0]+(6*pack.box_dim[0])), round(pack.corrB[1]+(8*pack.box_dim[1]))))
                        self.view[7][5] = Box(self, pack.box_dim, ..., 
                            ImageTk.PhotoImage(bi),
                            ImageTk.PhotoImage(paste(bi, pack.Wpieces[pc])),
                            ImageTk.PhotoImage(paste(bi, pack.Wpieces[pc], glow_mode="g"))
                        )
                        self.view[7][2].grid(row=7, column=2)
                        self.view[7][2].bind("<Enter>", lambda e, i=7, j=2: on_hover(i,j))
                        self.view[7][2].bind("<Leave>", lambda e, i=7, j=2: off_hover(i,j))
                        self.view[7][5].grid(row=7, column=5)
                        self.view[7][5].bind("<Enter>", lambda e, i=7, j=5: on_hover(i,j))
                        self.view[7][5].bind("<Leave>", lambda e, i=7, j=5: off_hover(i,j))
                    elif pc == "king":
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(4*pack.box_dim[0])), round(pack.corrB[1])+(7*pack.box_dim[1]), round(pack.corrB[0]+(5*pack.box_dim[0])), round(pack.corrB[1]+(8*pack.box_dim[1]))))
                        self.view[7][4] = Box(self, pack.box_dim, ..., 
                            ImageTk.PhotoImage(bi),
                            ImageTk.PhotoImage(paste(bi, pack.Wpieces[pc])),
                            ImageTk.PhotoImage(paste(bi, pack.Wpieces[pc], glow_mode="g"))
                        )
                        self.view[7][4].grid(row=7, column=4)
                        self.view[7][4].bind("<Enter>", lambda e, i=7, j=4: on_hover(i,j))
                        self.view[7][4].bind("<Leave>", lambda e, i=7, j=4: off_hover(i,j))
                    elif pc == "queen":
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(3*pack.box_dim[0])), round(pack.corrB[1]+(7*pack.box_dim[1])), round(pack.corrB[0]+(4*pack.box_dim[0])), round(pack.corrB[1]+(8*pack.box_dim[1]))))
                        self.view[7][3] = Box(self, pack.box_dim, ..., 
                            ImageTk.PhotoImage(bi),
                            ImageTk.PhotoImage(paste(bi, pack.Wpieces[pc])),
                            ImageTk.PhotoImage(paste(bi, pack.Wpieces[pc], glow_mode="g"))
                        )
                        self.view[7][3].grid(row=7, column=3)
                        self.view[7][3].bind("<Enter>", lambda e, i=7, j=3: on_hover(i,j))
                        self.view[7][3].bind("<Leave>", lambda e, i=7, j=3: off_hover(i,j))
                else:
                    for j in range(8):
                        bi = pack.iBoard.copy().crop((round(pack.corrB[0]+(j*pack.box_dim[0])), round(pack.corrB[1]+(6*pack.box_dim[1])), round(pack.corrB[0]+((j+1)*pack.box_dim[0])), round(pack.corrB[1]+(7*pack.box_dim[1]))))
                        self.view[6][j] = Box(self, pack.box_dim, ..., 
                            ImageTk.PhotoImage(bi),
                            ImageTk.PhotoImage(paste(bi, pack.Wpieces["pawn"])),
                            ImageTk.PhotoImage(paste(bi, pack.Wpieces["pawn"], glow_mode="g"))
                        )
                        self.view[6][j].grid(row=6, column=j)
                        self.view[6][j].bind("<Enter>", lambda e, i=6, j=j: on_hover(i,j))
                        self.view[6][j].bind("<Leave>", lambda e, i=6, j=j: off_hover(i,j))
            else:
                raise ValueError()

            for i in range(4):
                for j in range(8):
                    bi = pack.iBoard.crop((round(pack.corrB[0]+(j*pack.box_dim[0])), round(pack.corrB[1]+((i+2)*pack.box_dim[1])), round(pack.corrB[0]+((j+1)*pack.box_dim[0])), round(pack.corrB[1]+((i+3)*pack.box_dim[1]))))
                    self.view[i+2][j] = Box(self, pack.box_dim, ..., 
                        ImageTk.PhotoImage(bi),
                        ImageTk.PhotoImage(bi),
                        ImageTk.PhotoImage(bi)
                    ) 
                    self.view[i+2][j].grid(row=i+2, column=j)
                    self.view[i+2][j].bind("<Enter>", lambda e, i=i+2, j=j: on_hover(i,j))
                    self.view[i+2][j].bind("<Leave>", lambda e, i=i+2, j=j: off_hover(i,j))


class Table(Canvas):

    def __init__(self, pack: Packs.load):    
        Canvas.__init__(self, pack.win, width=pack.win.winfo_screenwidth(), height=pack.win.winfo_screenheight())
        self.pack(anchor="nw")
        im1 = pack.iTable.copy()
        im2 = pack.iBoard.copy()
        self.pzcod = ((im1.width*.2) + pack.corrB[0], (im1.height*.05) + pack.corrB[1])
        im1.paste(im2, (round(im1.width*.2), round(im1.height*.05)))
        self.look = ImageTk.PhotoImage(im1)
        self.create_image(0, 0, anchor="nw", image=self.look)

    def initBoard(self, board):
        self.create_window(self.pzcod[0], self.pzcod[1], anchor="nw", window=board)
        
