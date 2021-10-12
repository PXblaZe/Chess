
from data import Packs, struct
from tkinter import Tk
from PIL import ImageTk, Image
from elmts.pieces import *


if __name__ == "__main__":

    pk = Packs.load(Tk(), set=1)
    tbl = struct.Table(pk)
    brd = struct.Board(pk)
    tbl.initBoard(brd)
    
    pk.win.mainloop()
