from sys import stdin


def answers(people: list):
    return len(set(''.join(people)))


def main():
    people = stdin.read().split("\n\n")
    print(sum(answers(person.split()) for person in people))


if __name__ == '__main__':
    main()
