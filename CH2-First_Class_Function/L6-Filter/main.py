def remove_invalid_lines(document):
    """
    Remove lines that start with '-' character using filter function.
    Preserve all other lines and trailing newlines.
    """
    # TODO(human): Implement the filter logic here
    # Split the document into lines, filter out lines starting with '-',
    # then join back with newlines. Use filter() with a lambda function.
    split_document = filter(lambda x: not x.startswith("-"), document.split("\n"))
    return "\n".join(split_document)
