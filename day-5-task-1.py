from sys import stdin


def seat_id(boarding_pass: str):
    return int(boarding_pass.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1'), 2)


def main():
    tickets = stdin.read().split()
    print(max((seat_id(ticket) for ticket in tickets)))


if __name__ == '__main__':
    main()
