import itertools
from copy import deepcopy
import cv2
from a_cv_imwrite_imread_plus import save_cv_image

import PILasOPENCV as Image
import PILasOPENCV as ImageDraw
import PILasOPENCV as ImageFont
import numpy as np
from PIL import Image as Image__


def get_perfect_fontsize(
    biggesttext,
    begin_with_size,
    max_size,
    abstand_oben_links,
    fontart="arial.ttf",
    border=20,
):
    fontsize = begin_with_size
    font = None
    width, height = max_size[0] * 2, max_size[1] * 2
    abziehen = 1
    while width >= max_size[0] or height >= max_size[1]:
        font = ImageFont.truetype(fontart, fontsize)
        width, height = ImageFont.getsize(f"|{biggesttext}|", font)[:2]
        width = width + border + abstand_oben_links[0]
        height += border
        fontsize -= abziehen
    return font


def cycle_iter(iter1, iter2):
    iter1 = [list(x) for x in iter1]
    for i in iter1:
        i.reverse()
    iter2 = [list(x) for x in iter2]
    for i in iter2:
        i.reverse()
    looplist = [(x, y) for x, y in zip(iter1, itertools.cycle(iter2))]
    return looplist


def create_text_images(textlist, textcolor, backgroundcolor, border, font):
    textundfont = cycle_iter(textlist, textcolor)
    textundfontbackground = cycle_iter(textlist, backgroundcolor)
    allpicsx = []

    for ini, wrappedtext in enumerate(textlist.splitlines()):
        textcol = textundfont[ini][1]
        backcol = textundfontbackground[ini][1]
        width, height = ImageFont.getsize(f"|{wrappedtext}|", font)[:2]
        width += border
        height += border
        im = Image.new("RGB", (width, height), backcol)
        draw = ImageDraw.Draw(im)

        draw.text((border // 2, border // 2), wrappedtext, font=font, fill=textcol)
        allpicsx.append(deepcopy(im))
    return allpicsx


def fit_text_in_box(
    text,
    textcolor,
    backgroundcolor,
    transparent=True,
    filepath=None,
    maximalx=1200,
    maximaly=300,
    columns=3,
    fontart="arial.ttf",
    fontborder=4,
    distance_upper_left=(1, 1),
):
    backgroundcolortmp = []
    for b in backgroundcolor:
        if b != (0, 0, 0):
            backgroundcolortmp.append(b)
        else:
            backgroundcolortmp.append((0, 0, 1))
    textcolortmp = []
    for b in textcolor:
        if b != (0, 0, 0):
            textcolortmp.append(b)
        else:
            textcolortmp.append((3, 3, 3))
    textcolor = textcolortmp.copy()

    backgroundcolor = backgroundcolortmp.copy()
    rammsteintextall = text.strip()
    textaslines = rammsteintextall.splitlines()
    gesplittet = np.array_split(textaslines, columns)
    linelength = len(gesplittet[0])
    minyzeile = maximaly // linelength
    longestelement = [(len(x), x) for x in textaslines]
    longestelement.sort()
    longestelement = longestelement[-1][-1]
    font = get_perfect_fontsize(
        longestelement,
        begin_with_size=minyzeile * 2,
        max_size=(maximalx // columns, minyzeile),
        fontart=fontart,
        border=fontborder,
        abstand_oben_links=distance_upper_left,
    )

    allefertig = []
    for ini, rammsteintext in enumerate(gesplittet):
        alstext = "\n".join(rammsteintext.tolist())
        allebilder = create_text_images(
            alstext,
            textcolor=textcolor,
            backgroundcolor=backgroundcolor,
            border=1,
            font=font,
        )
        alle = [x.getim() for x in allebilder]

        longest = 0
        for li in alle:
            for bildliste in li:
                neueliste = bildliste.tolist()
                if len(neueliste) > longest:
                    longest = len(neueliste)
        allepicsrightganz = []
        for li in alle:
            allepicsright = []

            for bildliste in li:
                neueliste = bildliste.tolist()
                while len(neueliste) < longest:
                    neueliste.append([0, 0, 0])
                allepicsright.append(neueliste.copy())
            if any(allepicsright):
                allepicsrightganz.append(allepicsright.copy())
        allepicsrightganz = [x for x in allepicsrightganz if any(x)]
        fertig = np.vstack(allepicsrightganz)
        allefertig.append(fertig.copy())
    ymax = 0
    xmax = 0
    for li in allefertig:
        xw = li.shape[1]
        yw = li.shape[0]
        if ymax < yw:
            ymax = yw
        if xmax < xw:
            xmax = xw
    allcvimages = []
    for li in allefertig:
        img1 = cv2.copyMakeBorder(
            li.copy(),
            0,
            ymax - li.shape[0],
            0,
            xmax - li.shape[1],
            borderType=cv2.BORDER_CONSTANT,
            value=(0, 0, 0, 0),
        )
        allcvimages.append(img1.copy())
    result = cv2.hconcat(allcvimages)
    ymissing = (maximaly - result.shape[0]) // 2
    xmissing = (maximalx - result.shape[1]) // 2
    image = cv2.copyMakeBorder(
        result,
        ymissing,
        ymissing,
        xmissing,
        xmissing,
        cv2.BORDER_CONSTANT,
        None,
        value=0,
    )

    if transparent:
        img = Image__.fromarray(image.astype(np.uint8))
        imga = img.convert("RGBA")

        imga = np.asarray(imga)
        r, g, b, a = np.rollaxis(imga, axis=-1)
        r_m = r != 0
        g_m = g != 0
        b_m = b != 0
        a = a * ((r_m == 1) | (g_m == 1) | (b_m == 1))
        image = np.array(
            Image__.fromarray(np.dstack([r, g, b, a]).astype(np.uint8), "RGBA")
        )
    if filepath is not None:

        save_cv_image(filepath, image)
    return image
