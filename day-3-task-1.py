from sys import stdin


def travel(right: int, down: int, lines: list):
    i = 0
    trees = 0
    for line in lines[::down]:
        line = line.strip()
        if line[i] == '#':
            trees += 1
        i = (i + right) % len(line)
        print(i)
    return trees


def main():
    lines = stdin.readlines()
    print(travel(3, 1, lines))

if __name__ == '__main__':
    main()
