# Advent of Code 2021, Dec 3

def is_match(diagnostic, val, index):
    return diagnostic[index] == val


def get_rating(strings, is_gamma):
    idx = 0
    filtered_list = strings
    while len(filtered_list) > 1:
        rate = get_rate(filtered_list, is_gamma)
        filtered_list = [d for d in filtered_list if is_match(d, rate[idx], idx)]
        # print('get_rating', idx, rate, filtered_list)
        idx += 1

    return filtered_list[0]


def get_most_common_at_idx(values, idx):
    one_count = len([d for d in values if d[idx] == '1'])
    return '1' if one_count >= (len(values) / 2) else '0'


def invert(rate_str):
    return ''.join(['1' if d == '0' else '0' for d in rate_str])


def get_rate(values, is_gamma):
    """
    get gamma or epsilon rate
    """
    str_len = len(values[0])
    gamma = ''.join([get_most_common_at_idx(values, i) for i in range(str_len)])
    return gamma if is_gamma else invert(gamma)


def get_power(values):
    gamma = get_rate(values, True)
    epsilon = get_rate(values, False)
    power = int(gamma, 2) * int(epsilon, 2)
    # print('gamma', gamma, 'epsilon', epsilon, int(gamma, 2), int(epsilon, 2), power)
    return power


if __name__ == '__main__':
    with open('../inputs/aoc_dec03.txt') as f:
        diagnostics = f.readlines()

    # # Test data
    # diagnostics = ['00100\n',
    #                '11110\n',
    #                '10110\n',
    #                '10111\n',
    #                '10101\n',
    #                '01111\n',
    #                '00111\n',
    #                '11100\n',
    #                '10000\n',
    #                '11001\n',
    #                '00010\n',
    #                '01010\n']

    diagnostics = [d.strip('\n') for d in diagnostics]

    power = get_power(diagnostics)
    print(f'Power is {power}')

    o2_generator_rating = get_rating(diagnostics, True)
    co2_scrubber_rating = get_rating(diagnostics, False)
    life_support_rating = int(o2_generator_rating, 2) * int(co2_scrubber_rating, 2)
    # print(f'o2_generator_rating {o2_generator_rating}, co2_scrubber_rating {co2_scrubber_rating}')
    print(f'Life Support Rating is {life_support_rating}')

