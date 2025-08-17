def change_bullet_style(document):
    lines_list = document.split("\n")
    convert_line_document = map(convert_line, lines_list)
    rejoined_document = "\n".join(convert_line_document)
    # new_document = list(rejoined_document)
    return rejoined_document


# Don't edit below this line


def convert_line(line):
    old_bullet = "-"
    new_bullet = "*"
    if len(line) > 0 and line[0] == old_bullet:
        return new_bullet + line[1:]
    return line

