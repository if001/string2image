import string2image

def main():
    with open("./gomi.txt") as f:
        for word in f.read():
            string2image.string2image(word)

if __name__ == '__main__':
   main()
