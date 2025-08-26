def get_median_font_size(font_sizes):
    if font_sizes == []:
        return None
    sorted_font_sizes = sorted(font_sizes)
    middle_index = (len(font_sizes) - 1) // 2
    return sorted_font_sizes[middle_index]
