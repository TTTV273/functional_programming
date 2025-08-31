def get_filter_cmd(filter_one, filter_two):
    # TODO: Step 1 - Add default parameter value "--one" to option parameter
    # Change the line below to: def filter_cmd(content, option="--one"):
    def filter_cmd(content, option="--one"):
        # TODO: Step 2 - Implement option handling logic
        # Use if/elif/else statements to handle different options:

        # TODO: Step 2a - If option == "--one":
        #   return filter_one(content)
        if option == "--one":
            return filter_one(content)

        # TODO: Step 2b - If option == "--two":
        #   return filter_two(content)
        elif option == "--two":
            return filter_two(content)

        # TODO: Step 2c - If option == "--three":
        #   Apply filter_one first, then filter_two to the result
        #   Example: result = filter_one(content)
        #            return filter_two(result)
        elif option == "--three":
            result = filter_one(content)
            return filter_two(result)

        # TODO: Step 2d - For any other option:
        #   raise Exception("invalid option")
        else:
            raise Exception("invalid option")

    return filter_cmd


# don't touch below this line


def replace_bad(text):
    return text.replace("bad", "good")


def replace_ellipsis(text):
    return text.replace("..", "...")


def fix_ellipsis(text):
    return text.replace("....", "...")
