# Advent of Code 2021, Dec 9
# Caves
import itertools


test_input = """
2199943210
3987894921
9856789892
8767896789
9899965678
"""


def get_neighbors(row_num, col_num):
    # Return list of tuples (rn, cn height)
    neighbors = []

    row = cave_map[row_num]
    if col_num > 0:
        # Neighbor to the left
        neighbors.append((row_num, col_num-1, row[col_num - 1]))
    if col_num < num_cols - 1:
        # Neighbor to the right
        neighbors.append((row_num, col_num +1, row[col_num + 1]))
    if row_num > 0:
        neighbors.append((row_num - 1, col_num, cave_map[row_num - 1][col_num]))
    if row_num < num_rows - 1:
        neighbors.append((row_num + 1, col_num, cave_map[row_num + 1][col_num]))
    return neighbors


def fill_basin_neighbors(rn, cn, basin_num):
    """
    Mark all points that share the given point's basin with the given basin number
    """
    # Get all neighbors of the given point
    immediate_neighbors = get_neighbors(rn, cn)

    # Find neighbors who aren't 9s and who aren't already filled
    new_basin_neighbors = [(r, c) for (r, c, h) in immediate_neighbors if h != 9 and not basins[r][c]]

    # Mark those new neighbors as being part of our basin, and fill *their* neighbors too.
    # Recursion is fun!
    neighbors = []
    for (rn, cn) in new_basin_neighbors:
        # print(f"found new neighbors for basin {basin_num}: ({rn}, {cn})")
        basins[rn][cn] = basin_num
        neighbors.extend(fill_basin_neighbors(rn, cn, basin_num))
    return neighbors


def is_local_min(row_num, col_num, height):
    return height < min([h for (_, _, h) in get_neighbors(row_num, col_num)])


def get_risk_level():
    low_points = get_low_points()
    return sum(height for (_, _, height) in low_points) + len(low_points)


def get_low_points():
    # Pretty sure I could make this all one line, but it'd be pretty hard to read that way!
    low_points = []
    for rn in range(len(cave_map)):
        for cn in range(len(cave_map[0])):
            height = cave_map[rn][cn]
            if is_local_min(rn, cn, height):
                low_points.append((rn, cn, height))

    return low_points


def fill_basins():
    """
    Fill in basin map with different basins having different number labels
    Return number of basins
    """
    basin_num = 1

    low_points = get_low_points()
    for (rn, cn, _) in low_points:
        basins[rn][cn] = basin_num
        fill_basin_neighbors(rn, cn, basin_num)
        basin_num += 1

    return len(low_points)


if __name__ == '__main__':
    with open('../inputs/aoc_dec09.txt') as f:
        cave_map_str = f.read().split("\n")

    # Test Input
    # cave_map_str = test_input.split("\n")

    cave_map = [[int(height) for height in r] for r in cave_map_str if r]
    # print(cave_map, "\n")
    num_rows = len(cave_map)
    num_cols = len(cave_map[0])

    # basin_map = [[0 if height == 9 else 1 for height in r] for r in cave_map]
    risk_level = get_risk_level()
    print(f"Risk level of the low points in this cave is {risk_level}\n")

    # This doesn't work! All the rows are the same list reference, so updating first row updates them all!
    # basins = [[0]*num_cols]*num_rows
    #
    # Take 2 on initializing list of lists for the basin map
    basins = []
    for i in range(num_rows):
        basins.append([0]*num_cols)

    # Fill in our basin map
    num_basins = fill_basins()

    # print(f"Final basin map:")
    # for r in range(num_rows):
    #     print(basins[r])

    # Count how many points are in each basin
    basin_sizes = []
    flat_basins = list(itertools.chain(*basins))
    for b in range(1, num_basins+1):
        basin_size = len([p for p in flat_basins if p == b])
        basin_sizes.append(basin_size)

    # Find biggest 3 basins and multiply their sizes together
    big_3 = sorted(basin_sizes)[-3:]
    print(f"Biggest 3 basins: {big_3}")
    answer = big_3[0] * big_3[1] * big_3[2]
    print(f"Multiplied together: {answer}")



