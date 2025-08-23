def add_format(default_formats, new_format):
    copy_default_formats = default_formats.copy()
    copy_default_formats[new_format] = True
    return copy_default_formats


def remove_format(default_formats, old_format):
    copy_default_formats = default_formats.copy()
    copy_default_formats[old_format] = False
    return copy_default_formats
