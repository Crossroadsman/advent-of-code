from file_handling import file_handling
from wiring import wiring


FILENAME = '03_input.txt'


if __name__ == "__main__":

    filename = FILENAME

    string_list = file_handling.file_to_list(
        filename=FILENAME,
    )

    paths = [x.split(',') for x in string_list]

    print('---- PATH 1 ----')
    print(paths[0])
    print('---- PATH 2 ----')
    print(paths[1])

    overlaps = wiring.overlaps(paths[0], paths[1])

    print(overlaps)

    nearest = wiring.nearest_overlap(overlaps)

    print(nearest)

