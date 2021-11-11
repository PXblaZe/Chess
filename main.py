from tkinter import Tk
from data import Packs, struct


if __name__ == "__main__":
    pk = Packs.load(Tk(), set=1)
    tbl = struct.Table(pk)
    brd = struct.Board(pk)
    tbl.initBoard(brd)
    pk.win.mainloop()
