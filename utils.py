from PIL import Image
from typing import Literal, Tuple

def Kded(image: Image.Image, xy: Tuple[int, int], sharp: int = 50) -> bool:
    if isinstance(image, Image.Image) and isinstance(xy, tuple): pass
    else: raise ValueError("Invalid Argument(s).")
    sum = abs(((-2*image.getpixel((xy[0]-1, xy[1]-1)))) + (2*image.getpixel((xy[0]+1, xy[1]+1))))
    if sum<sharp: return False
    else: return True

def Kved(image: Image.Image, xy: Tuple[int, int],  sharp: int = 50) -> bool:
    if isinstance(image, Image.Image) and isinstance(xy, tuple): pass
    else: raise ValueError("Invalid Argument(s).")
    suml = (-1*image.getpixel((xy[0]-1, xy[1]-1))) + (-2*image.getpixel((xy[0]-1, xy[1]))) + (-1*image.getpixel((xy[0]-1, xy[1]+1)))
    sumr = image.getpixel((xy[0]+1, xy[1]-1)) + 2*image.getpixel((xy[0]+1, xy[1])) + image.getpixel((xy[0]+1, xy[1]+1))
    sum = suml + sumr
    if sum < sharp: return False
    else: return True

def Khed(image: Image.Image, xy: Tuple[int, int], sharp: int = 50) -> bool:
    if isinstance(image, Image.Image) and isinstance(xy, tuple): pass
    else: raise ValueError("Invalid Argument(s).")
    sumu = (-1*image.getpixel((xy[0]-1, xy[1]-1))) + (-2*image.getpixel((xy[0], xy[1]-1))) + (-1*image.getpixel((xy[0]+1, xy[1]-1)))
    sumb = image.getpixel((xy[0]-1, xy[1]+1)) + 2*image.getpixel((xy[0], xy[1]+1)) + image.getpixel((xy[0]+1, xy[1]+1))
    sum = sumu + sumb
    if sum < sharp: return False
    else: return True

def _paste(imb: Image.Image, imf: Image.Image, frompxls: Tuple[int, int] = (0, 0)) -> Image.Image:
    imb = imb.convert("RGBA")
    imf = imf.convert("RGBA")
    cp = imb.copy()
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

def paste(background_img: Image.Image, foreground_img: Image.Image, glow_mode: Literal['r', 'b', 'g',''] = "", rescalef: float = .8):
    if glow_mode.lower() not in ("r", "g", "b", ""): 
        raise ValueError('glow_mode only takes "r", "g", "b" as its values')
    img = foreground_img.convert("RGBA").resize(background_img.size)
    cpy = background_img.convert("RGBA")
    sci = img.resize(tuple([round(i*rescalef) for i in img.size]))
    if not glow_mode:
        cpy = _paste(cpy, sci, (round((cpy.width-sci.width)/2), round((cpy.height-sci.height)/2)))
    else:
        imgd = img.getdata()
        datas = cpy.getdata()
        ci = Image.new("RGBA", background_img.size, (0, 0 ,0 ,0))
        cid = []
        for pi, pc in zip(imgd, datas):
            if pi[3]:
                if glow_mode.lower() == 'r': 
                    cid.append((255, 0, 0, 255))
                elif glow_mode.lower() == 'g': 
                    cid.append((0, 255, 0, 255))
                else: cid.append((0, 0, 255, 255))
            else: cid.append((0, 0, 0, 0))
        ci.putdata(cid)
        itd = _paste(cpy, ci)
        cpy = _paste(itd, sci, frompxls=(round((itd.width-sci.width)/2), round((itd.height-sci.height)/2)))
    return cpy.copy()


