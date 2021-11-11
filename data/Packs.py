import os, sys
from PIL import Image
from tkinter import Tk
from typing import Dict, Final, Tuple
from utils import Kded, Khed, Kved

dirI: Final[str] = os.path.abspath("images/")+"/"

class load:

    def __init__(self, win: Tk, set: int):
        if not isinstance(set, int) or not isinstance(win, Tk):
            raise ValueError("Invalid Argument(s).")
        def close_app(e): self.win.withdraw(); sys.exit()
        self.win: Tk = win
        self.set: tuple = set
        self.win.title("Chess")
        if os.name=='nt': self.win.iconbitmap("images/chess.ico")
        self.win.attributes('-fullscreen', True)
        self.win.bind("<Escape>", close_app)
        self.iTable = Image.open(dirI+f"s{self.set}table.png").resize((self.win.winfo_screenwidth(), self.win.winfo_screenheight()))
        self.iBoard = Image.open(dirI+f"s{self.set}board.png").resize((round(self.iTable.width*.6), round(self.iTable.height*.8)))

        gcpy = self.iBoard.copy().convert("L")
        x = 1; y = 1
        while y<=51:
            if Kded(gcpy, (x, y), sharp=25) and Khed(gcpy, (x, y), sharp=25) and Kved(gcpy, (x, y), sharp=25): break
            elif Kded(gcpy, (x, y)) and Khed(gcpy, (x, y)): x-=1; continue
            elif Kded(gcpy, (x, y)) and Kved(gcpy, (x, y)): y-=1; continue
            y+=1; x=y
        else: 
            gcpy.close()
            if x>50 and y>50: x=y=0
        
        self.corrB: Final[Tuple[int, int]] = (x, y)
        self.box_dim: Final[Tuple[float, float]] = (((self.iBoard.width)-(2*self.corrB[0]))/8, ((self.iBoard.height)-(2*self.corrB[1]))/8)
        self.Bpieces: Final[Dict[str, Image.Image]] = {
            "pawn": Image.open(dirI+f"s{self.set}pawnB.png").resize(tuple(round(i) for i in self.box_dim)),
            "knight": Image.open(dirI+f"s{self.set}knightB.png").resize(tuple(round(i) for i in self.box_dim)),
            "bishop": Image.open(dirI+f"s{self.set}bishopB.png").resize(tuple(round(i) for i in self.box_dim)),
            "rook": Image.open(dirI+f"s{self.set}rookB.png").resize(tuple(round(i) for i in self.box_dim)),
            "queen": Image.open(dirI+f"s{self.set}queenB.png").resize(tuple(round(i) for i in self.box_dim)),
            "king": Image.open(dirI+f"s{self.set}kingB.png").resize(tuple(round(i) for i in self.box_dim))
        }
        self.Wpieces: Final[Dict[str, Image.Image]] = {
            "pawn": Image.open(dirI+f"s{self.set}pawnW.png").resize(tuple(round(i) for i in self.box_dim)),
            "knight": Image.open(dirI+f"s{self.set}knightW.png").resize(tuple(round(i) for i in self.box_dim)),
            "bishop": Image.open(dirI+f"s{self.set}bishopW.png").resize(tuple(round(i) for i in self.box_dim)),
            "rook": Image.open(dirI+f"s{self.set}rookW.png").resize(tuple(round(i) for i in self.box_dim)),
            "queen": Image.open(dirI+f"s{self.set}queenW.png").resize(tuple(round(i) for i in self.box_dim)),
            "king": Image.open(dirI+f"s{self.set}kingW.png").resize(tuple(round(i) for i in self.box_dim))
        }

class show:

    def __init__(self, win) -> None: pass
        