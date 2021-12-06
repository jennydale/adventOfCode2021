# Advent of Code 2021, Dec 4
# BINGO

test_input = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
""".splitlines()

colbingotest = """
2 7 21 17 24  4
 3 4 16 15  9 19
 2 5  8 23 26 20
 2 9 11 13  6  5
2 11  0 12  3  7
"""

BINGO_SIZE = 5


def is_bingo(card, called_numbers):
    # Check rows
    for row in card:
        if set(row).issubset(called_numbers):
            print('ROW BINGO', row, called_numbers)
            return True

    # Check columns
    columns = list(map(list, zip(*card)))
    for col in columns:
        if set(col).issubset(called_numbers):
            print('COL BINGO', col)
            return True

    return False


def get_uncalled_sum(card, called_numbers):
    uncalled_card_numbers = [num for row in card for num in row if num not in (called_numbers)]
    return sum(uncalled_card_numbers)


if __name__ == '__main__':
    with open('../inputs/aoc_dec04.txt') as f:
        input = f.read().split("\n")

    # input = test_input
    numbers = [int(n) for n in input[0].split(',')]
    # print(numbers)
    cards_str = [input[i:i + BINGO_SIZE] for i in range(2, len(input), BINGO_SIZE+1)]
    cards = [[[int(n) for n in line.split()] for line in card] for card in cards_str]
    # print('cards', cards)

    bingo = False
    round = BINGO_SIZE
    winning_cards = []
    while len(winning_cards) < len(cards) and round < len(numbers):
        called_numbers = set(numbers[:round])
        for (card_num, card) in enumerate(cards):
            # print(f"checking {card_num}, {card}, {winning_cards}, {called_numbers}")
            if card_num in winning_cards:
                print(f'Card {card_num} already won, skipping...')
                # This card already won!
                continue

            bingo = is_bingo(card, called_numbers)
            if bingo:
                uncalled_sum = get_uncalled_sum(card, called_numbers)
                winning_number = numbers[round-1]
                print(f"BINGO on card {card_num}!", card, winning_number)
                answer = uncalled_sum * winning_number
                print(f"uncalled_sum {uncalled_sum}, winning number {winning_number}")
                print(f"ANSWER IS {answer}")
                winning_cards.append(card_num)
                break
        else:
            print(f'no match with {numbers[round-1]}, calling another number')
            round += 1

        if round > len(numbers):
            print("THIS IS IMPOSSIBLE, NO BINGO!")
            break
