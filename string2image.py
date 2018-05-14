from PIL import Image, ImageDraw, ImageFont, ImageOps, ImageEnhance, ImageFilter
import unicodedata
import os
import numpy as np
# from conf import Conf
import sys
sys.path.append("../")


def save_image(yomi, font, prefix, processing=None, pos=(0, 0), rad=None):
    image = Image.new(
        'RGB', (Conf.pict_height, Conf.pict_width), (255, 255, 255))

    draw = ImageDraw.Draw(image)
    draw.text(pos, yomi, font=font, fill='#000000')

    if processing is not None:
        image = processing(image)
    if rad is not None:
        image = image.rotate(rad)
    print("save " + Conf.save_dir + yomi + "_" + prefix + ".png")
    bytes_yomi = yomi.encode("UTF-8").hex()
    image.save(Conf.save_dir + bytes_yomi + "_" + prefix + ".png", 'PNG')


def is_exist(yomi):
    return os.path.isfile(Conf.save_dir + yomi + '.png')


def contrast_50(img):
    img = ImageEnhance.Contrast(img)
    img = img.enhance(0.5)
    return img


def sharpness_2(img):
    img = ImageEnhance.Sharpness(img)
    img = img.enhance(2.0)  # シャープ画像
    return img


def sharpness_0(img):
    img = ImageEnhance.Sharpness(img)
    img = img.enhance(0.0)  # ボケ画像
    return img


def gaussian_bluer(img):
    img = img.filter(ImageFilter.GaussianBlur(3.0))
    return img


def erosion(img):  # 縮小
    img = img.filter(ImageFilter.MinFilter())
    return img


def dilation(img):  # 膨張
    img = img.filter(ImageFilter.MaxFilter())
    return img


def string2image(inp, font_file=None):
    yomi_str = inp
    if font_file is None:
        font_file = Conf.font_file

    if unicodedata.east_asian_width(inp) in 'FWA':  # 全角のとき
        font = ImageFont.truetype(
            font_file, Conf.font_size, encoding='unic')
    else:
        font = ImageFont.truetype(
            font_file, Conf.font_size_en, encoding='unic')

    img_pos = [(0, 0), (0, 3), (0, 6), (3, 0), (6, 0), (3, 3), (6, 6)]
    for i in range(len(img_pos)):
        prefix = str(i)
        if not is_exist(yomi_str + "_" + prefix):
            save_image(yomi_str, font, prefix, pos=img_pos[i])

    prefix = "flip"
    if not is_exist(yomi_str + "_" + prefix):
        save_image(yomi_str, font, prefix, processing=ImageOps.flip)

    prefix = "mirror"
    if not is_exist(yomi_str + "_" + prefix):
        save_image(yomi_str, font, prefix, processing=ImageOps.mirror)

    prefix = "rotate_90"
    if not is_exist(yomi_str + "_" + prefix):
        save_image(yomi_str, font, prefix, rad=90)

    prefix = "rotate_180"
    if not is_exist(yomi_str + "_" + prefix):
        save_image(yomi_str, font, prefix, rad=180)

    prefix = "contrast_50"
    if not is_exist(yomi_str + "_" + prefix):
        save_image(yomi_str, font, prefix,
                   processing=contrast_50)

    prefix = "sharpness_0"
    if not is_exist(yomi_str + "_" + prefix):
        save_image(yomi_str, font, prefix,
                   processing=sharpness_0)

    prefix = "sharpness_2"
    if not is_exist(yomi_str + "_" + prefix):
        save_image(yomi_str, font, prefix,
                   processing=sharpness_2)

    prefix = "gaussianblur"
    if not is_exist(yomi_str + "_" + prefix):
        save_image(yomi_str, font, prefix,
                   processing=gaussian_bluer)

    prefix = "erosion"
    if not is_exist(yomi_str + "_" + prefix):
        save_image(yomi_str, font, prefix,
                   processing=erosion)

    prefix = "dilation"
    if not is_exist(yomi_str + "_" + prefix):
        save_image(yomi_str, font, prefix,
                   processing=dilation)


def main():
    inp = "b"
    for value in inp:
        string2image(value)


if __name__ == '__main__':
    from conf import Conf
    main()
else:
    from string2image.conf import Conf
