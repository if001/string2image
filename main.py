import string2image

def main():
    with open("../aozora_data/files/files_all_rnp.txt") as f:
        for word in f.read():
            if (word != "") or (word != " ") or (word != "\n"):
                string2image.string2image(word)

if __name__ == '__main__':
   main()
