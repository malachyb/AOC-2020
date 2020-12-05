from sys import stdin


def seat_id(boarding_pass: str):
    row_id = boarding_pass[:7]
    column_id = boarding_pass[7:]
    row = int(row_id.replace('F', '0').replace('B', '1'), 2)
    column = int(column_id.replace('L', '0').replace('R', '1'), 2)
    return row * 8 + column


def main():
    tickets = stdin.read().split()
    seats = sorted(seat_id(ticket) for ticket in tickets)
    for i, id in enumerate(seats):
        if seats[i+1] != id + 1:
            print(id + 1)
            break


if __name__ == '__main__':
    main()
