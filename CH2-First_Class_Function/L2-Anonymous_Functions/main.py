def file_type_getter(file_extension_tuples):
    # TODO(human) - Implement this function
    # Step 1: Create an empty dictionary to map extensions to file types
    extension_map = {}
    # Step 2: Loop through file_extension_tuples
    #   For each (file_type, extensions) tuple:
    #     Loop through the extensions list
    #     Add each extension to the dictionary with file_type as value
    for file_type, extensions in file_extension_tuples:
        for extension in extensions:
            extension_map[extension] = file_type
    # Step 3: Return a lambda function that takes an extension and returns
    #         the file type using dict.get(extension, "Unknown")
    return lambda extension: extension_map.get(extension, "Unknown")
