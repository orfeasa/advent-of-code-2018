from typing import List, Optional


def read_input(input_file) -> List:
    frequency_changes = []

    with open(input_file) as f:
        for line in f.readlines():
            frequency_changes.append(int(line))
    return frequency_changes


def find_duplicate(frequency_changes) -> Optional[int]:
    sums = set()
    first_duplicate = None
    duplicate_found = False
    last_sum = 0
    while not (duplicate_found):
        for change in frequency_changes:
            last_sum += change
            if last_sum not in sums:
                sums.add(last_sum)
            else:
                first_duplicate = last_sum
                duplicate_found = True
                break

    return first_duplicate


if __name__ == "__main__":
    frequency_changes = read_input("input.txt")
    duplicate = find_duplicate(frequency_changes)
    if duplicate is not None:
        print(f"First frequency repeated: {duplicate}")
