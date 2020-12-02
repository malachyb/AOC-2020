from sys import stdin


def find_sum(nums: set, count: int):
    for i in nums:
        if count - i in nums:
            yield i * (count - i)


def main():
    inp = set(map(int, stdin.readlines()))
    for t in find_sum(inp, 2020):
        print(t)

if __name__ == '__main__':
    main()
