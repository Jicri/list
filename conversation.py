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
    new = []
    for line in cons:
        if line == 'Allen':
            person = 'Allen'
            continue
        elif line == 'Tom':
            person = 'Tom'
            continue
        new.append(person + ':' + line)
    return new


def write_file(filename, cons):
    with open(filename, 'w', encoding='utf-8-sig') as f:
        for line in cons:
            f.write(line + '\n')


def main():
    cons = read_file('input.txt')
    cons = convert(cons)
    write_file('output.txt', cons)


main()
