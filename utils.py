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

def _paste(imb, imf, frompxls = (0, 0)) -> Image:
    cp = imb.copy()
    cpd = cp.convert("RGBA").getdata()
    imd = imf.convert("RGBA").resize(cp.size).getdata()
    nd = []
    for i in range(cp.height):
        for j in range(cp.width):
            bp = imb.getpixel((j,i))
            if i<frompxls[1] or j<frompxls[0]: nd.append(bp)
            else:
                fp = (0,0,0,0) if i>=imf.height+frompxls[1] or j>=imf.width+frompxls[0] else imf.getpixel((j-frompxls[0],i-frompxls[1])) 
                if (fp[0]==0 and fp[1]==0 and fp[2]==0) or fp[3]==0: nd.append(bp)
                else: nd.append(fp)
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
        ci.putdata(cid)
        sci = img.resize(tuple([round(i*.8) for i in img.size]))
        itd = _paste(cpy, ci)
        cpy = _paste(itd, sci, tuple([round(i*.09) for i in img.size]))
    return cpy.copy()


b = Image.open('box.png')
f = Image.open("images\\chess.png")


#i = paste(b, f, glow_mode="")
i = paste(b, f, glow_mode="g")
i.show()


def chance(x: int, y: int) -> bool: pass