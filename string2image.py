from PIL import Image, ImageDraw, ImageFont, ImageOps
import unicodedata
import os

from conf import Conf


def save_image(inp, yomi, font, prefix, processing=None, pos=(0, 0)):
    image = Image.new(
        'RGB', (Conf.pict_height, Conf.pict_width), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    draw.text(pos, inp, font=font, fill='#000000')
    if processing is not None:
        image = processing(image)
    print("save " + Conf.save_dir + yomi + "_" + prefix + ".png")
    image.save(Conf.save_dir + yomi + "_" + prefix + ".png", 'PNG')


def is_exist(yomi):
    return os.path.isfile(Conf.save_dir + yomi + '.png')


def string2image(inp):
    yomi_str = inp
    if unicodedata.east_asian_width(inp) in 'FWA':  # 全角のとき
        font = ImageFont.truetype(
            Conf.font_file, Conf.font_size, encoding='unic')
    else:
        font = ImageFont.truetype(
            Conf.font_file, Conf.font_size_en, encoding='unic')

    prefix = "flip"
    if not is_exist(yomi_str + "_" + prefix):
        save_image(inp, yomi_str, font, prefix, processing=ImageOps.flip)

    prefix = "mirror"
    if not is_exist(yomi_str + "_" + prefix):
        save_image(inp, yomi_str, font, prefix, processing=ImageOps.mirror)

    img_pos = [(0, 0), (0, 3), (3, 0), (3, 3)]
    for i in range(len(img_pos)):
        prefix = str(i)
        if not is_exist(yomi_str + "_" + prefix):
            save_image(inp, yomi_str, font, prefix, pos=img_pos[i])


def string2image2(inp):
    yomi_str = inp
    if unicodedata.east_asian_width(inp) in 'FWA':  # 全角のとき
        font = ImageFont.truetype(
            Conf.font_file, Conf.font_size, encoding='unic')
    else:
        font = ImageFon t.truetype(
            Conf.font_file, Conf.font_size_en, encoding='unic')

    if not is_exist(yomi_str + "_0"):
        prefix = "flip"
        save_image(inp, yomi_str, font, prefix, processing=ImageOps.flip)

        prefix = "mirror"
        save_image(inp, yomi_str, font, prefix, processing=ImageOps.mirror)

        img_pos = [(0, 0), (0, 3), (3, 0), (3, 3)]
        for i in range(len(img_pos)):
            prefix = str(i)
            save_image(inp, yomi_str, font, prefix, pos=img_pos[i])


def main():
    inp = "b"
    for value in inp:
        string2image(value)


if __name__ == '__main__':
    main()
