# Advent of Code 2021, Dec 7
# Crab Alignment

def get_fuel(distance):
    return sum(range(distance + 1))


if __name__ == '__main__':
    with open('../inputs/aoc_dec07.txt') as f:
        crabs_input = f.readline()

    # Test Input
    # crabs_input = "16,1,2,0,4,2,7,1,2,14"

    crabs = [int(position) for position in crabs_input.split(',')]
    max_position = max(crabs)
    min_fuel = 99999999999999
    alignment_position = 0

    for i in range(max_position):
        fuel = sum(get_fuel(abs(i - crab_position)) for crab_position in crabs)

        # print(f"Power at {i} is {fuel}")
        if fuel < min_fuel:
            print(f"Found a better position: {i}! Power here is {fuel}")
            alignment_position = i
            min_fuel = fuel
            # NOTE: once numbers start getting bigger we could stop looking.
            # Will leave that as an exercise for the reader. :)

    print(f"Position {alignment_position} is where it's at! Join the crab party! Fuel cost: {min_fuel}")