from sys import stdin


def answers(people: list):
    return len(set(chr(i) for i in range(ord('a'), ord('z') + 1)).intersection(*[set(person) for person in people]))


def main():
    people = stdin.read().split("\n\n")
    print(sum(answers(person.split()) for person in people))


if __name__ == '__main__':
    main()
