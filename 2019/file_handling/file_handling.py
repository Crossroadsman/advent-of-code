def file_to_list(filename: str, multiline=True) -> [str]:
    with open(filename, 'r') as fh:
        if multiline:
            text_list = fh.readlines()

        else:
            text = fh.readline()
            text_list = text.split(',')

    # need to strip trailing newlines or any other whitespace
    text_list = [x.strip() for x in text_list]

    return text_list


def strs_to_ints(ss: [str]) -> [int]:
    return [int(x) for x in ss]

