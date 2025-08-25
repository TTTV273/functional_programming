def sort_dates(dates):
    # TODO(human): Create a helper function to convert "MM-DD-YYYY" to "YYYY-MM-DD" for sorting
    # Then use sorted() with key parameter to sort chronologically
    # Example: sorted(dates, key=helper_function)
    return sorted(dates, key=date_to_sortable_format)


def date_to_sortable_format(date_str):
    # TODO(human): Split "MM-DD-YYYY" and rearrange to "YYYY-MM-DD"
    # This creates proper chronological ordering
    date_str_split = date_str.split("-")
    month = date_str_split[0]
    day = date_str_split[1]
    year = date_str_split[2]
    return f"{year}-{month}-{day}"
