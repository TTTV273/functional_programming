import copy


def css_styles(initial_styles):
    # TODO: Step 1 - Create a DEEP COPY of initial_styles to protect nested dictionaries
    # Hint: Use copy.deepcopy() instead of .copy() because we have nested dictionaries
    # The lesson explains why shallow copy (.copy()) won't work here
    initial_styles_deepcopy = copy.deepcopy(initial_styles)

    # TODO: Step 2 - Define the inner function add_style that takes 3 parameters
    # Parameters should be: selector (like "body"), property (like "color"), value (like "red")
    # This function needs to:
    # - Check if the selector exists in the copied styles dictionary
    # - If selector doesn't exist, create a new empty dictionary for it
    # - Add/update the property-value pair for that selector
    # - Return the updated styles dictionary
    def inner_func(selector, property, value):
        if selector not in initial_styles_deepcopy:
            initial_styles_deepcopy[selector] = {}
        initial_styles_deepcopy[selector][property] = value
        return initial_styles_deepcopy

    # TODO: Step 3 - Inside add_style function, implement the logic:
    # - Use an if statement to check if selector exists in the styles dict
    # - If not, initialize it as an empty dictionary: styles[selector] = {}
    # - Then set the property: styles[selector][property] = value
    # - Return the complete styles dictionary

    # TODO: Step 4 - Return the add_style function (not called, just the function itself)
    return inner_func
