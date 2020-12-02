from sys import stdin


def find_three_nums(inp: list, count: int):
    for i in range(len(inp) - 2):
        for j in range(i+1, len(inp) - 1):
            for k in range(j + 1, len(inp)):
                if inp[i] + inp[j] + inp[k] == count:
                    return inp[i] * inp[j] * inp[k]


def main():
    inps = list(map(int, stdin.readlines()))
    print(find_three_nums(inps, 2020))


if __name__ == '__main__':
    main()
