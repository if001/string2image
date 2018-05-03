from PIL import Image, ImageDraw, ImageFont
from conf import Conf

def save_image(inp, yomi):
    font = ImageFont.truetype(Conf.font_file,Conf.font_size, encoding='unic')

    # 1文字にあたり、少しだけ位置をずらした画像を4つ生成する
    img_pos = [(0,0),(0,3),(3,0),(3,3)]
    for i in range(len(img_pos)):
        image = Image.new('RGB', (Conf.pict_size, Conf.pict_size), (255, 255, 255))
        draw = ImageDraw.Draw(image)
        draw.text(img_pos[i], inp, font = font, fill='#000000')
        print("save " + Conf.save_dir + yomi + "_" + str(i) + '.png')
        image.save(Conf.save_dir + yomi + "_" + str(i) + '.png', 'PNG')


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
        print(Conf.save_dir + yomi_str + '.png' + " is already exist")
    else:
        save_image(inp, yomi_str)

def main():
    inp = "あ"
    for value in inp:
        string2image(value)


if __name__ == '__main__':
    main()
