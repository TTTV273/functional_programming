default_commands = {}
default_formats = ["txt", "md", "html"]
saved_documents = {}

# Don't edit above this line


def add_custom_command(commands, new_command, function):
    # TODO(human): Fix input mutation - create .copy() before modifying
    commands_copy = commands.copy()
    commands_copy[new_command] = function
    return commands_copy


def add_format(formats, format):
    # TODO(human): Fix input mutation - create .copy() before modifying
    formats_copy = formats.copy()
    formats_copy.append(format)
    return formats_copy


def save_document(docs, file_name, doc):
    # TODO(human): Fix input mutation - create .copy() before modifying
    docs_copy = docs.copy()
    docs_copy[file_name] = doc
    return docs_copy


def add_line_break(line):
    # TODO(human): Fix side effect - remove print() and return the formatted string instead
    return line + "\n\n"
