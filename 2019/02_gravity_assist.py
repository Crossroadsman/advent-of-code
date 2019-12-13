from file_handling import file_handling
from intcode_computer import intcode_computer


FILENAME = '02_input.txt'


if __name__ == "__main__":

    filename = FILENAME

    string_list = file_handling.file_to_list(
        filename=FILENAME,
        multiline=False
    )
    program = file_handling.strs_to_ints(string_list)

    # restore 1202 program alarm state
    program[1] = 12
    program[2] = 2

    computed = intcode_computer.compute(program)

    print(computed)
