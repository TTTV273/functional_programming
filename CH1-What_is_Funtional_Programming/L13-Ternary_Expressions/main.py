def choose_parser(file_extension):
    return "markdown" if file_extension.lower() in ("markdown", "md") else "plaintext"
