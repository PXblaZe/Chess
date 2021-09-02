
from PIL import Image, ImageFilter, ImageDraw

def border_glow(image: Image, filter: str) -> Image: 
    img = image.convert("RGBA")
    cpy = img.copy()
    pxls = img.getdata()
    npxls = list()
    for r, g, b, a in pxls: 
        if filter.lower() == "red":
            npxls.append((r, 0, 0, round(a+a*.2)))
        elif filter.lower() == "green":
            npxls.append((0, g, 0, round(a+a*.2)))
        elif filter.lower() == "blue":
            npxls.append((0, 0, b, round(a+a*.2)))
        else:
            raise ValueError('filter takes only "red", "green" or "blue" as its values')
    img.putdata(npxls)
    bimg = img.filter(ImageFilter.BLUR)
    new = Image.new("L", cpy.size, 0)
    di = ImageDraw.Draw(new)
    di.rectangle((10, 10, cpy.width-10, cpy.height-10), 255)
    bn = new.filter(ImageFilter.BLUR)
    bimg.paste(cpy, (0, 0), bn)
    return bimg

def _paste(im1, im2):
    cp = im1.copy()
    cpd = cp.convert("RGBA").getdata()
    imd = im2.convert("RGBA").resize(cp.size).getdata()
    nd = []
    for c, i in zip(cpd, imd):
        if (not i[3]) or not (i[0] or i[1] or i[2]):
            nd.append(c)
        else: nd.append(i)
    cp.putdata(nd)
    return cp.copy()

def paste(background_img: Image, foreground_img: Image, glow_mode = ""):
    if glow_mode.lower() not in ("r", "g", "b", ""): 
        raise ValueError('glow_mode only takes "r", "g", "b" as its values')
    img = foreground_img.convert("RGBA").resize(background_img.size)
    imgd = img.getdata()
    cpy = background_img.convert("RGBA")
    datas = cpy.getdata()
    newData = []
    if not glow_mode:
        cpy = _paste(cpy, img)
    else:
        '''
        ci = Image.new("RGBA", background_img.size, (0, 0 ,0 ,0))
        cid = []
        for pi, pc in zip(imgd, datas):
            if pi[3]:
                if glow_mode.lower() == 'r': 
                    cid.append((pc[0], 0, 0, pc[3]))
                elif glow_mode.lower() == 'g': 
                    cid.append((0, pc[1], 0, pc[3]))
                else: cid.append((0, 0, pc[2], pc[3]))
            else: cid.append((0, 0, 0, 0))
        else: print(pi+pc)
        ci.putdata(cid)
        ci.show()
        bci = ci.filter(ImageFilter.GaussianBlur(10))
        bci.show()
        cpy = _paste(cpy, bci)
    return cpy.copy()
        '''
        bi = img.convert("1")
        b = bi.filter(ImageFilter.GaussianBlur(10))
        b.show()
        cpy.paste(img.resize((60, 60)), (7, 7), b)
        return cpy.copy()

b = Image.open('box.png')
f = Image.open("images\\chess.png")


i = paste(b, f, glow_mode="r")
i.show()


def chance(x: int, y: int) -> bool: pass