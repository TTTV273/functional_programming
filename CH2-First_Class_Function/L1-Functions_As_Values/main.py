def file_to_prompt(file, to_string):
    # TODO(human) - Implement this function
    # Step 1: Call the to_string function with the file parameter
    content = to_string(file)
    # Step 2: Wrap the result in markdown code blocks with triple backticks
    # Remember: ```\n{content}\n```
    return f"```\n{content}\n```"
