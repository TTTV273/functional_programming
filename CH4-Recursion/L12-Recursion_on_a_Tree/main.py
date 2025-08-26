def list_files(parent_directory, current_filepath=""):
    """
    Recursively scan file system (nested dictionaries) and return list of filepaths.

    Args:
        parent_directory: Dict where subdirs have dict values, files have None values
        current_filepath: Current path string (e.g. "/Documents")

    Returns:
        List of all filepaths in the directory tree
    """

    # Step 1: Create an empty list to store the file paths
    # TODO: Create a variable to hold our list of file paths (like total = 0 in L8)
    file_paths = []

    # Step 2: Use a for-loop to iterate through the keys of the parent_directory dictionary
    # TODO: Loop through parent_directory (hint: use .items() to get both key and value)
    for key, value in parent_directory.items():
        # Step 2.1: Use the key to create a new file path by concatenating "/" and the key
        # TODO: Create new_path by combining current_filepath + "/" + key
        new_path = f"{current_filepath}/{key}"
        # Step 2.2: If the value is None, the key is a filename - append the new file path
        # TODO: Check if value is None (this means it's a file)
        # If so, append new_path to your file paths list
        # if value is None:
        if value == None:
            file_paths.append(new_path)

        # Step 2.3: Otherwise, value is a child directory - recursively call list_files
        # TODO: Check if value is a dictionary (this means it's a subdirectory)
        # If so, call list_files(value, new_path) and extend your results
        else:
            file_paths.extend(list_files(value, new_path))

    # Step 3: Return the list of file paths
    # TODO: Return your collected file paths
    return file_paths
