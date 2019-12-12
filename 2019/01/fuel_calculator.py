from file_handling import file_to_list, strs_to_ints


def calculate_from_mass(mass: int, fuel_so_far: int=0) -> int:
    """recursive computation because fuel also has mass"""

    fuel_from_mass = (mass // 3) - 2

    if fuel_from_mass < 0:
       return fuel_so_far

    return calculate_from_mass(
        mass=fuel_from_mass,
        fuel_so_far=fuel_so_far + fuel_from_mass
    )


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

