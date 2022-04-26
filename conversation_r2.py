from distutils.command import config
from fileinput import filename


def read_file(filename):
    con = []
    with open(filename, 'r', encoding='utf-8-sig') as f:
        for line in f:
            line = line.strip()
            con.append(line)
    return con


def convert(cons):
    allen_word_count = 0
    allen_stick_count = 0
    allen_image_count = 0
    Viki_word_count = 0
    Viki_stick_count = 0
    Viki_image_count = 0
    for line in cons:
        cons = line.split(' ')
        name = cons[1]
        if name == 'Allen':
            if cons[2] == '貼圖':
                allen_stick_count += 1
            elif cons[2] == '圖片':
                allen_image_count += 1
            else:
                for m in cons[2:]:
                    allen_word_count += len(m)
        elif name == 'Viki':
            if cons[2] == '貼圖':
                Viki_stick_count += 1
            elif cons[2] == '圖片':
                Viki_image_count += 1
            else:
                for m in cons[2:]:
                    Viki_word_count += len(m)
    print('allen說了:', allen_word_count, '個字')
    print('allen傳了:', allen_stick_count, '個貼圖')
    print('allen傳了:', allen_image_count, '個圖片')
    print('Viki說了:', Viki_word_count, '個字')
    print('Viki傳了:', Viki_stick_count, '個貼圖')
    print('Viki傳了:', Viki_image_count, '個圖片')


def write_file(filename, cons):
    with open(filename, 'w', encoding='utf-8-sig') as f:
        for line in cons:
            f.write(line + '\n')


def main():
    cons = read_file('LINE-Viki.txt')
    convert(cons)
    #write_file('output.txt', cons)


main()
