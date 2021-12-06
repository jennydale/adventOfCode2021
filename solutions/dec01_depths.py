# Advent of Code 2021, Dec 1

def make_sums(depths):
    sums = [d + depths[i+1] + depths[i+2] for (i,d) in enumerate(depths[:-2])]
    print(f'Sums: {sums}')
    return sums


def count_increases(depths):
    sums = make_sums(depths)
    increases = [d for (idx,d) in enumerate(sums[:-1]) if sums[idx+1] > d]
    return len(increases)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open('../inputs/aoc_dec01.txt') as f:
        readings = [int(reading) for reading in f.readlines()]

    # readings = [199,200,208,210,200,207,240,269,260,263]
    answer = count_increases(readings)
    print(f'Looks like we have {answer} increases!')
