def file_to_list(filename: str) -> [str]:
    with open(filename, 'r') as fh:
        text_list = fh.readlines()

    # need to strip trailing newlines or any other whitespace
    text_list = [x.strip() for x in text_list]

    return text_list


def strs_to_ints(ss: [str]) -> [int]:
    return [int(x) for x in ss]

