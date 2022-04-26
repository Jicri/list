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
    for line in cons:
        cons = line.split(' ')
        # print(cons)
        name = cons[0][5:]
        time = cons[0][:5]
        print(name, time)


def write_file(filename, cons):
    with open(filename, 'w', encoding='utf-8-sig') as f:
        for line in cons:
            f.write(line + '\n')


def main():
    cons = read_file('3.txt')
    convert(cons)
    #write_file('output.txt', cons)


main()
