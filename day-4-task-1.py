from sys import stdin


def is_valid(passport: str):
    fields = passport.split()
    fields = set(map(lambda x: x.split(':')[0], fields))
    # print(1)
    return all(map(lambda x: x in fields, ['byr', 'ecl', 'eyr', 'hgt', 'iyr', 'pid', 'hcl']))


def main():
    passports = stdin.read().split("\n\n")
    valid = 0
    for passport in passports:
        # print(passport)
        valid += bool(is_valid(passport))
    print(valid)


if __name__ == '__main__':
    main()
