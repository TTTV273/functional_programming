def doc_format_checker_and_converter(conversion_function, valid_formats):
    # STEP 1: This is the OUTER function (the factory)
    # It receives parameters that will be "remembered" by the inner function
    # conversion_function = a function like capitalize_content or reverse_content
    # valid_formats = a list like [".txt", ".md"] of allowed file extensions

    # STEP 2: Define the INNER function (the product that gets returned)
    # This inner function will be called later: checker_converter(filename, content)
    def checker_converter(filename, content):
        # STEP 3: Use the parameters from the outer function (closure)
        # We need to access conversion_function and valid_formats from outer scope

        # STEP 4: Do the actual work (validation + conversion)
        # TODO: Get file extension from filename (hint: use .split('.'))
        extension = filename.split(".")[-1]
        # extension_with_dot = "." + filename.split(".")[-1]
        # TODO: Check if extension is in valid_formats
        if extension in valid_formats:
            # TODO: If valid, return conversion_function(content)
            return conversion_function(content)
        # TODO: If invalid, raise ValueError('invalid file format')
        else:
            raise ValueError("invalid file format")
        pass

    # STEP 5: Return the inner function (NOT call it!)
    # This gives the caller a customized function to use later
    return checker_converter


# Don't edit below this line


def capitalize_content(content):
    return content.upper()


def reverse_content(content):
    return content[::-1]
