import os


class Conf():
    font_size = 28
    font_size_en = 32
    pict_height = 28
    pict_width = 28
    run_dir_path = os.path.dirname(os.path.abspath(__file__))

    font_file = run_dir_path + '/RictyDiminished-Regular.ttf'
    font_file = run_dir_path + '/hiragino_maru_go_ProN_W4.ttc'
    save_dir = run_dir_path + "/image/"
