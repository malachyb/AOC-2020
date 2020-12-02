from sys import stdin


def check_password(low, high, char, string: str):
    return low <= string.count(char) <= high


def main():
    valid = 0
    for line in stdin:
        rule, password = line.split(':')
        nums, char = rule.split()
        low, high = map(int, nums.split('-'))
        if check_password(low, high, char, password):
            valid += 1
    print(valid)


if __name__ == '__main__':
    main()
