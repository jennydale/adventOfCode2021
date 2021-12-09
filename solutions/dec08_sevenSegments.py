# Advent of Code 2021, Dec 8
# Seven Segment Search
# https://adventofcode.com/2021/day/8


# test_puzzle_input = """
# be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
# edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
# fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
# fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
# aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
# fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
# dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
# bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
# egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
# gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
# """

# test_puzzle_input = """acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"""


def is_1478(coded_value):
    """
    Return true if the coded_value has a unique number of segments (representing a 1, 4, 7, or 8)
    """
    return len(coded_value) in (2, 3, 4, 7)


def get_easy_part_of_map(inputs):
    """
    Figure out 1, 4, 7, 8
    """
    len_2_value = {
        2: '1',
        3: '7',
        4: '4',
        7: '8'
    }
    return {value: len_2_value.get(len(value), None) for value in inputs}


def is_digit_subset(digit, other_digit):
    """
    Return True if segments in digit are a subset of segments in other_digit
    """
    return set(digit).issubset(set(other_digit))


def invert_dict(inp_dict):
    return {v: k for k, v in inp_dict.items()}


def alphabetize(inp):
    return "".join(sorted(inp))


def get_decoder_ring(digit_map):
    """
    Turn our map into something we can use on alphabetized values
    """
    return {alphabetize(k): v for k, v in digit_map.items()}


def decode(coded_values, decoder):
    """
    Alphabetize the coded values and see what digits they map to, then convert that to an int
    """
    return int(''.join([decoder[alphabetize(v)] for v in coded_values.split()]))


def process_input_row(row):
    """
    Figure out full map for the input, and decode the output
    """
    (signal_input_str, output_digits) = row.split("|")
    signal_input = signal_input_str.split()

    # First fill in 1, 4, 7, 8
    value_2_digit = get_easy_part_of_map(signal_input)
    digit_2_value = invert_dict(value_2_digit)

    two_and_five = []
    for inp in signal_input:
        if len(inp) == 6:
            # It's a '0', '6', or '9'
            if is_digit_subset(digit_2_value['4'], inp):
                # If it overlaps with '4' it's a '9'
                value_2_digit[inp] = '9'
            elif is_digit_subset(digit_2_value['1'], inp):
                # If it overlaps with '1' then it's a '0'
                value_2_digit[inp] = '0'
            else:
                # '6' doesn't overlap with '4' or '1'
                value_2_digit[inp] = '6'
        elif len(inp) == 5:
            # It's a '2', '3', or '5'
            if is_digit_subset(digit_2_value['7'], inp):
                # If it overlaps with '7' it's a '3'
                value_2_digit[inp] = '3'
            else:
                # We'll figure these out later
                two_and_five.append(inp)

    # Should have everything except '2' and '5' at this point
    digit_2_value = invert_dict(value_2_digit)

    # Figure out what segment b is mapping to -- it's the one that's in '9' but not in '3'
    segment_b = next(iter(set(digit_2_value['9']) - set(digit_2_value['3'])))

    # Now we can figure out '2' and '5'
    for inp in two_and_five:
        value_2_digit[inp] = '5' if segment_b in inp else '2'

    # print('We have a full map!', decoder_ring)
    output = decode(output_digits, get_decoder_ring(value_2_digit))
    print(f"{output_digits}: {output}")
    return output


if __name__ == '__main__':
    with open('../inputs/aoc_dec08.txt') as f:
        puzzle_input = f.read().split("\n")

    # puzzle_input = test_puzzle_input.splitlines()

    # ---------------------------------------
    # Part 1
    # ---------------------------------------
    count_1478 = 0
    for input_row in puzzle_input:
        if "|" not in input_row:
            # Maybe this is blank line at the end or something
            continue

        (_, output_digitz) = input_row.split("|")
        count_1478 += len([s for s in output_digitz.split() if is_1478(s)])

    print(f"Count of 1,4,7,8 is: {count_1478}\n\n")

    # ---------------------------------------
    # Part 2
    # ---------------------------------------
    grand_total = 0
    for input_row in puzzle_input:
        if "|" not in input_row:
            # Maybe this is blank line at the end or something
            continue

        grand_total += process_input_row(input_row)

    print(f"\nWe have a grand total of {grand_total}")
