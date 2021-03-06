from str2img import string2image


def main():

    with open("../aozora_data/files/files_all_rnp.txt") as f:
        word_list = list(set(list(f.read())))

    if '\n' in word_list:
        word_list.remove('\n')
    if ' ' in word_list:
        word_list.remove(' ')
    if '' in word_list:
        word_list.remove('')

    for word in word_list:
        string2image(word, "./RictyDiminished-Regular.ttf")


if __name__ == '__main__':
    main()
