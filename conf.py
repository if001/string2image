import os
class Conf():
    font_size = 28
    pict_size = 28
    font_file = '/Users/issei/Library/Fonts/RictyDiminished-Regular.ttf'
    # font_file = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
    font_file = './RictyDiminished-Regular.ttf'
    run_dir_path = os.path.dirname(os.path.abspath(__file__))
    save_dir = run_dir_path + "/image/"

