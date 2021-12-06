# Advent of Code 2021, Dec 2

if __name__ == '__main__':
    depth = 0
    position = 0
    aim = 0

    with open('../inputs/aoc_dec02.txt') as f:
        moves = f.readlines()

    # Test data
    # moves = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']

    for move in moves:
        (direction, steps) = move.split()
        steps = int(steps)

        if direction == 'forward':
            position = position + steps
            depth = depth + (steps * aim)
        elif direction == 'down':
            aim = aim + steps
        elif direction == 'up':
            aim = aim - steps
        # print(f'new pos {position}, depth {depth}, aim {aim}')

    answer = depth * position

    print(f'Final position is depth {depth}, position {position}')
    print(f'Answer is {answer}')
