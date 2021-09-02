from utils import *
from PIL import ImageTk, Image
import tkinter as tkr
app = tkr.Tk()
app.title("Chess")
app.iconbitmap("images/chess.ico")
app.geometry("770x660")
app.wm_resizable(0, 0)
correctionW = 20.704225352112676
correctionH = 19.718309859154928
bgt = Image.open(r"images\table-wdn.png").resize((770, 660))
boardimg = Image.open(r"images\Set1b.png").resize((575, 577))
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
ibox = tuple([[None for j in range(8)] for i in range(8)])
select_mode = True
def ichange(i, j): 
    global select_mode
    if select_mode and chance(i, j):
        pass
    box: Image = ibox[i][j]
    imgd = Image.open(r"images\chess.png").resize((boxdim["w"], boxdim["h"])).getdata()
    cpy = box.convert("RGBA")
    datas = cpy.getdata()
    newData = []
    for item1, item2 in zip(imgd, datas):
        if item1[3] == 0 : newData.append(item2)
        else: newData.append(item1) 
    cpy.putdata(newData)
    cpy = border_glow(cpy, "red")
    acsklj = ImageTk.PhotoImage(cpy)
    idx2bi[i, j][0].config(image=acsklj)
    idx2bi[i, j][1] = acsklj
for i in range(8):
    for j in range(8):
        ibox[i][j] = boardimg.crop((round(correctionW+(j*boxdim["w"])), round(correctionH+(i*boxdim["h"])), round(correctionW+((j+1)*boxdim["w"])), round(correctionH+((i+1)*boxdim["h"]))))
        timg = ImageTk.PhotoImage(ibox[i][j])
        idx2bi[i, j] = [tkr.Button(bf, width=boxdim["w"]/b_corr, height=boxdim["h"]/b_corr, image=timg, borderwidth=0, command=lambda r=i, clm=j: ichange(r, clm)), timg]
        idx2bi[i, j][0].grid(row=i, column=j)

app.mainloop()