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
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    trees = 1
    for slope in slopes:
        count = travel(*slope, lines)
        print(count)
        trees *= count
    print(trees)

if __name__ == '__main__':
    main()
