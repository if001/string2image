from PIL import Image, ImageDraw, ImageFont
from conf import Conf

def save_image(inp, yomi):
    font = ImageFont.truetype(Conf.font_file,Conf.font_size, encoding='unic')
    # image = Image.new('RGBA', (Conf.pict_size, Conf.pict_size))
    image = Image.new('RGB', (Conf.pict_size, Conf.pict_size))
    draw = ImageDraw.Draw(image)

    # 引数: (文字列の左上のx座標, 文字列の左上のy座標)」「フォントの指定」「文字色」
    draw.text((0, 0), inp, font = font, fill='#000000')
    print("save " + Conf.save_dir + yomi + '.png')
    image.save(Conf.save_dir + yomi + '.png', 'PNG')


import os
def is_exist(yomi):
    return os.path.isfile(Conf.save_dir +  yomi + '.png')


from pykakasi import kakasi

def get_yomi(inp):
    k = kakasi()
    k.setMode('H', 'a')
    k.setMode('K', 'a')
    k.setMode('J', 'a')
    k.setMode('E', 'a')

    conv = k.getConverter()
    return conv.do(inp)

def string2image(inp):
    yomi_str = inp
    if is_exist(yomi_str):
        pass
        # print(Conf.save_dir + yomi_str + '.png' + " is already exist")
    else:
        save_image(inp, yomi_str)
    print(Conf.save_dir + yomi_str + '.png')

def main():
    inp = "a"
    for value in inp:
        string2image(value)


if __name__ == '__main__':
    main()
