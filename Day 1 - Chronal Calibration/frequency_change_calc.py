if __name__ == "__main__":
    input_file = "input.txt"
    sum = 0
    sums = set()
    frequency_changes = []

    with open(input_file) as f:
        for line in f.readlines():
            frequency_changes.append(int(line))

    duplicate_found = False
    last_sum = 0
    while not (duplicate_found):
        for change in frequency_changes:
            last_sum += change
            if last_sum not in sums:
                sums.add(last_sum)
            else:
                print(f"First frequency repeated: {last_sum}")
                print(f"Sums checked: {len(sums)}")
                duplicate_found = True
                break
