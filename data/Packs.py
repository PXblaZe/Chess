import os, sys
from PIL import Image
from tkinter import Tk
from utils import Kded, Khed, Kved

dirI = os.path.abspath("images/")+"/"

class load():

    def __init__(self, win, set: int):
        if not isinstance(set, int) or not isinstance(win, Tk):
            raise ValueError("Invalid Argument(s).")
        def close_app(e): self.win.withdraw(); sys.exit()
        self.win = win
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
        
        self.corrB = (x, y)
        self.box_dim = (round(((self.iBoard.width)-(2*self.corrB[0]))/8), round(((self.iBoard.height)-(2*self.corrB[1]))/8))
        self.Bpieces = {
            "pawn": Image.open(dirI+f"s{self.set}pawnB.png").resize(self.box_dim),
            "knight": Image.open(dirI+f"s{self.set}knightB.png").resize(self.box_dim),
            "bishop": Image.open(dirI+f"s{self.set}bishopB.png").resize(self.box_dim),
            "rook": Image.open(dirI+f"s{self.set}rookB.png").resize(self.box_dim),
            "queen": Image.open(dirI+f"s{self.set}queenB.png").resize(self.box_dim),
            "king": Image.open(dirI+f"s{self.set}kingB.png").resize(self.box_dim)
        }
        self.Wpieces = {
            "pawn": Image.open(dirI+f"s{self.set}pawnW.png").resize(self.box_dim),
            "knight": Image.open(dirI+f"s{self.set}knightW.png").resize(self.box_dim),
            "bishop": Image.open(dirI+f"s{self.set}bishopW.png").resize(self.box_dim),
            "rook": Image.open(dirI+f"s{self.set}rookW.png").resize(self.box_dim),
            "queen": Image.open(dirI+f"s{self.set}queenW.png").resize(self.box_dim),
            "king": Image.open(dirI+f"s{self.set}kingW.png").resize(self.box_dim)
        }
