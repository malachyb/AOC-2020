from sys import stdin
import re


def is_valid(passport: str):
    fields = passport.split()
    passport = {}
    for field in fields:
        field, val = field.split(':')
        passport[field] = val
    if "hgt" in passport:
        hgt = passport["hgt"]
        if hgt[-2:] == "cm":
            hgt_min, hgt_max = 150, 193
        else:
            hgt_min, hgt_max = 59, 76
    return all(map(lambda x: x in passport, ['byr', 'ecl', 'eyr', 'hgt', 'iyr', 'pid', 'hcl'])) and (
                1920 <= int(passport["byr"]) <= 2002) and (2010 <= int(passport["iyr"]) <= 2020) and bool(
        re.fullmatch("\d+(cm|in)", hgt)) and (hgt_min <= int(hgt[:-2]) <= hgt_max) and bool(
        re.fullmatch("#[\da-f]{6}", passport["hcl"])) and (
                   passport["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]) and bool(
        re.fullmatch("\d{9}", passport["pid"])) and (2020 <= int(passport["eyr"]) <= 2030)


def main():
    passports = stdin.read().split("\n\n")
    valid = 0
    for passport in passports:
        # print(passport)
        valid += int(is_valid(passport))
    print(valid)


if __name__ == '__main__':
    main()
