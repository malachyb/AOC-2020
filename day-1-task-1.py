from sys import stdin


def find_sum(nums: set, count: int):
    for i in nums:
        if count - i in nums:
            return i * (count - i)


def main():
    inp = set(map(int, stdin.readlines()))
    print(find_sum(inp, 2020))

if __name__ == '__main__':
    main()
