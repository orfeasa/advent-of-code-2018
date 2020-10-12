from typing import Generator, Dict, List, Set


def read_input(filename: str) -> Generator[str, None, None]:
    with open(filename) as f:
        for line in f:
            yield line.strip()


def calculate_checksum(input_filename: str) -> int:
    # exactly two of any letter
    # exactly three of any letter
    count_2s = 0
    count_3s = 0
    for line in read_input(input_filename):
        char_dict = create_char_dict(line)
        if 2 in char_dict.values():
            count_2s += 1
        if 3 in char_dict.values():
            count_3s += 1
    return count_2s * count_3s


def create_char_dict(line: str) -> Dict:
    char_dict: Dict[str, int] = {}
    for char in line:
        char_dict.setdefault(char, 0)
        char_dict[char] += 1
    return char_dict


def load_input(input_filename: str) -> List[str]:
    codes: List[str] = []
    with open(input_filename) as f:
        for code in f.readlines():
            codes.append(code.strip())

    return codes


def find_common_in_correct_ID(input_filename: str) -> str:

    codes = load_input(input_filename)

    # assuming all lines have the same length
    # for each character index
    for char_ind in range(len(codes[0])):
        # create sub-list of strings without char in that index
        # fmt: off
        temp_codes = [code[:char_ind] + code[char_ind + 1:] for code in codes]

        set_of_codes: Set[str] = set()
        for temp_code in temp_codes:
            if temp_code in set_of_codes:
                return temp_code
            else:
                set_of_codes.add(temp_code)

    return ""


if __name__ == "__main__":
    filename = "input"
    print("Part 1: ", calculate_checksum(filename))
    print("Part 2: ", find_common_in_correct_ID(filename))
