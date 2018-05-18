from PIL import Image
import plyvel
import numpy as np
import os
import sys
sys.path.append("../")
# モジュールとしてロード
from string2image.conf import Conf
from string2image.kvs import Image2Kvs

# main文からロード
# from conf import Conf
# from kvs import Image2Kvs


class Image2String():
    @classmethod
    def similarity(cls, vec1, vec2):
        return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

    @classmethod
    def exclude_extension(cls, st):
        return st.split(".")[0]

    @classmethod
    def extension(cls, st):
        return st.split(".")[1]

    @classmethod
    def load_image(cls, yomi):
        file_dir = Conf.run_dir_path + "/image/"
        img = Image.open(file_dir + yomi + "_0.png")
        img = img.convert("RGB")
        img = img.resize((28, 28))
        img = np.array(img)
        return img

    @classmethod
    def image2string(cls, img):
        dig_sim = 0
        label = ""
        img = img.flatten()
        file_dir = Conf.run_dir_path + "/image/"
        files = os.listdir(file_dir)
        db_name = "image.ldb"
        i2k = Image2Kvs(db_name)

        for fname in files:
            if cls.extension(fname) == "png" and (cls.exclude_extension(fname).split("_")[1] == "0"):
                yomi = cls.exclude_extension(fname).split("_")[0]
                load_img = i2k.get(yomi)
                sim = cls.similarity(img, load_img)
                if dig_sim < sim:
                    dig_sim = sim
                    label = bytes.fromhex(yomi).decode('utf-8')
        print("similarity:", dig_sim)
        return label


def all_save(db_name):
    image_file_dir = Conf.run_dir_path + "/image/"
    image_files = os.listdir(image_file_dir)

    i2k = Image2Kvs(db_name)

    for fname in image_files:
        if "_0" in Image2String.exclude_extension(fname):
            yomi = Image2String.exclude_extension(fname).split("_")[0]
            print(yomi)
            img = Image2String.load_image(yomi)
            img = img.flatten()
            if i2k.get(yomi) is None:
                i2k.put(yomi, img)


def main():
    all_save("image.ldb")


if __name__ == "__main__":
    main()
