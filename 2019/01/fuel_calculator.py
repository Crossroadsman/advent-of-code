from file_handling import file_to_list, strs_to_ints


def calculate_from_mass(mass: int) -> int:
    fuel_required = (mass // 3) - 2
    return fuel_required


def calculate_from_modules(modules: [int]) -> int:
    return sum(
        [calculate_from_mass(x) for x in modules]
    )



if __name__ == "__main__":

    filename = 'input.txt'
    inputs = strs_to_ints(
       file_to_list(filename)
    )

    print(calculate_from_modules(inputs))

