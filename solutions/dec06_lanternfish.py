# Advent of Code 2021, Dec 6
# Lanternfish

DAYS = 256
CYCLE_LEN = 7
MAX_TIMER = 9


if __name__ == '__main__':
    with open('../inputs/aoc_dec06.txt') as f:
        starting_fish = f.readline()

    # Test Input
    # starting_fish = "3,4,3,1,2"
    fish = [int(timer) for timer in starting_fish.split(',')]

    # ---------------------------------------------------------
    # This worked fine for Part 1, not so much for Part 2!
    # ---------------------------------------------------------

    # day = 0
    # while day < DAYS:
    #     # Count expired timers
    #     num_new_fish = sum(f == 0 for f in fish)
    #     print(f"Adding {num_new_fish} new fish")
    #     # Adjust timers
    #     fish = [6 if timer == 0 else timer - 1 for timer in fish]
    #     # Add new fish with timers of 8
    #     fish.extend([8] * num_new_fish)
    #     # New day!
    #     day += 1
    #     print(f'After {day:2} days: ', fish)
    #
    # print(f"After {DAYS} days, we have {len(fish)} fish!")

    # ---------------------------------------------------------
    # A better solution was required to solve Part 2!
    # ---------------------------------------------------------

    # Initialize fish counts { timer: fish_count_at timer }
    fish_counts = {i: sum(f == i for f in fish) for i in range(MAX_TIMER)}

    day = 0
    while day < DAYS:
        # print(f"day {day}")
        new_fish = fish_counts[0]

        # Shift fish down so fish that were at timer 3 are now at timer 2
        fish_counts = {i-1: count for (i, count) in fish_counts.items() if i > 0}

        # Add new fish with long timer
        fish_counts[MAX_TIMER-1] = new_fish

        # Reset timers for the fish that just spawned (they get added to whatever other fish already are at timer 6)
        fish_counts[CYCLE_LEN-1] += new_fish

        # print('fish_counts2', fish_counts)
        day += 1

    print(f"After {DAYS} days, we have {sum(fish_counts.values())} lanternfish!")
