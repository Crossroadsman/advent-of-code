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

    # every increment of address 2 by 1 increases output by 1
    # every increment of address 1 by 1 increases output by 432000

    program[1] = 0
    program[2] = 0

    computed = intcode_computer.compute(program)
    base_value = computed[0]

    target_value = 19690720

    target_multiple = (target_value - base_value) // 432000

    program[1] = target_multiple
    computed = intcode_computer.compute(program)

    remaining_difference = target_value - computed[0]
    #print(f'remaining difference: {remaining_difference}')

    program[2] = remaining_difference
    computed = intcode_computer.compute(program)
    print(computed)

    noun = computed[1]
    verb = computed[2]

    print(f'noun,verb: {noun},{verb}')
    print(f'100 x noun + verb = {(100 * noun) + verb}')

