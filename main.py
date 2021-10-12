from tkinter import Tk
import elmts.pieces as pieces
from data import Packs, struct
from PIL import ImageTk, Image


if __name__ == "__main__":

    pk = Packs.load(Tk(), set=1)
    tbl = struct.Table(pk)
    brd = struct.Board(pk)
    tbl.initBoard(brd)
    pk.win.mainloop()
