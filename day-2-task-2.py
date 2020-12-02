from sys import stdin


def check_password(first, second, char, string: str):
    return (string[first] == char) != (string[second] == char)



def main():
    valid = 0
    for line in stdin:
        rule, password = line.split(':')
        nums, char = rule.split()
        first, second = map(int, nums.split('-'))
        if check_password(first, second, char, password):
            valid += 1
    print(valid)


if __name__ == '__main__':
    main()
