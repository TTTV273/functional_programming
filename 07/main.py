def hex_to_rgb(hex_color):
    # Fixed function with proper validation and hex conversion
    # Check if input is a string first
    if not isinstance(hex_color, str):
        raise Exception("not a hex color string")
    
    # Now we know it's a string, safe to check length and hex validity
    if not is_hexadecimal(hex_color) or len(hex_color) != 6:
        raise Exception("not a hex color string")

    # Current broken implementation:
    r = int(hex_color[:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:], 16)
    return r, g, b


# Don't edit below this line


def is_hexadecimal(hex_string):
    try:
        int(hex_string, 16)
        return True
    except Exception:
        return False
