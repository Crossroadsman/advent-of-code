def calibrate(filename: str) -> int:
    text_list = file_to_list(filename)
    int_list = strs_to_ints(text_list)
    frequency = 0
    for n in int_list:
        frequency += n
    return frequency


def file_to_list(filename: str) -> [str]:
    fh = open(filename, 'r')
    text_list = fh.readlines()
    text_list = [x.strip() for x in text_list if x != '\n']
    fh.close()

    return text_list

def strs_to_ints(ss: [str]) -> [int]:
    output = [int(x) for x in ss]
    return output
