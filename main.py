from PIL.ImageFilter import BuiltinFilter
from utils import *
from PIL import ImageTk, Image
import tkinter as tkr
app = tkr.Tk()
app.title("Chess")
app.iconphoto(True, ImageTk.PhotoImage(file="images/chess.ico"))
app.geometry("770x660")
app.wm_resizable(0, 0)
correctionW = 20.704225352112676
correctionH = 19.718309859154928
bgt = Image.open("images/table-wdn.png").resize((770, 660))
boardimg = Image.open("images/Set1b.png").resize((575, 577))
bgt.paste(boardimg, (98, 10))
bgi = ImageTk.PhotoImage(bgt)
c = tkr.Canvas(app, width=770, height=660)
c.pack(anchor="nw")
c.create_image(0, 0, anchor="nw", image=bgi)
boxdim = {"w": round((boardimg.width-(2*correctionW))/8), "h": round((boardimg.height-(2*correctionH))/8)}
bf = tkr.Frame(app, width=boxdim["w"]*8, height=boxdim["h"]*8)
c.create_window(98+correctionW, 10+correctionH, anchor="nw", window=bf)
idx2bi = dict()
b_corr = 1.0307692307692307
ibox = tuple([[[None, None, None] for j in range(8)] for i in range(8)])
imgd = Image.open("images/chess.png").resize((boxdim["w"], boxdim["h"]))
select_mode = True
def ichange(i, j): 
    global select_mode
    if select_mode and chance(i, j): 
        box: Image = ibox[i][j][0]
        cpy = box.convert("RGBA")
        cpy = paste(cpy, imgd, "g")
        acsklj = ImageTk.PhotoImage(cpy)
        idx2bi[i, j][0].config(image=acsklj)
        idx2bi[i, j][1] = acsklj
def on_hover(i, j): 
    phi = paste(ibox[i][j][0], ibox[i][j][1], glow_mode="g")
    ibox[i][j][2] = ImageTk.PhotoImage(phi)
    idx2bi[i,j][0].config(image=ibox[i][j][2]) if chance(i, j) else ...
def off_hover(i, j): idx2bi[i,j][0].config(image=idx2bi[i,j][1])
for i in range(8):
    for j in range(8):
        ibox[i][j] = [boardimg.crop((round(correctionW+(j*boxdim["w"])), round(correctionH+(i*boxdim["h"])), round(correctionW+((j+1)*boxdim["w"])), round(correctionH+((i+1)*boxdim["h"])))), imgd, None]
        timg = ImageTk.PhotoImage(paste(ibox[i][j][0], ibox[i][j][1]))
        idx2bi[i,j] = [tkr.Button(bf, width=boxdim["w"]/b_corr, height=boxdim["h"]/b_corr, image=timg, borderwidth=0, command=lambda r=i, clm=j: ichange(r, clm)), timg]
        idx2bi[i,j][0].grid(row=i, column=j)
        idx2bi[i,j][0].bind("<Enter>", lambda e, i=i, j=j: on_hover(i,j))
        idx2bi[i,j][0].bind("<Leave>", lambda e, i=i, j=j: off_hover(i,j))
app.mainloop()