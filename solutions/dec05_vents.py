# Advent of Code 2021, Dec 5
# Vents
from collections import defaultdict

test_input = """
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""


def get_x_and_y(pt_str):
    return map(lambda x: int(x), pt_str.split(','))


if __name__ == '__main__':
    with open('../inputs/aoc_dec05.txt') as f:
        segments = f.read().split("\n")

    # segments = test_input.splitlines()
    # print('segments', segments)

    overlaps = 0
    vents = defaultdict(lambda: defaultdict(lambda: 0))
    for segment in segments:
        if not segment:
            continue
        pts = segment.split('->')
        (x1, y1) = get_x_and_y(pts[0])
        (x2, y2) = get_x_and_y(pts[1])

        if x1 == x2:
            # We found a vertical line segment!
            incr = 1 if y2 > y1 else -1
            for i in range(y1, y2 + incr, incr):
                vents[x1][i] += 1

                # If it's first overlap for the spot, count it!
                if vents[x1][i] == 2:
                    # print('overlap!', x1, y1, x2, y2, i)
                    overlaps += 1

        elif y1 == y2:
            # We found a horizontal line segment!
            incr = 1 if x2 > x1 else -1
            for i in range(x1, x2 + incr, incr):
                vents[i][y1] += 1

                # If it's first overlap for the spot, count it!
                if vents[i][y1] == 2:
                    overlaps += 1

        else:
            # Check for diagonals as well
            xdiff = x2 - x1
            ydiff = y2 - y1
            if abs(xdiff) == abs(ydiff):
                # print(f"diagonal! ({x1}, {y1}), ({x2}, {y2})")
                x_incr = 1 if x2 > x1 else -1
                y_incr = 1 if y2 > y1 else -1

                x_i = x1
                for y_i in range(y1, y2 + y_incr, y_incr):
                    vents[x_i][y_i] += 1

                    # If it's first overlap for the spot, count it!
                    if vents[x_i][y_i] == 2:
                        overlaps += 1

                    # Increment x as well
                    x_i += x_incr


    # print('vents', vents)
    print(f'We have {overlaps} overlaps')
