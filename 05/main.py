def format_line(line):
    # Apply transformations step by step for easier debugging
    # 1. Strip whitespace from beginning and end
    stripped = line.strip()
    # 2. Capitalize every character
    capitalized = stripped.upper()
    # 3. Remove any periods
    no_periods = capitalized.replace(".", "")
    # 4. Add ellipsis suffix (...)
    final = no_periods + "..."
    return final
