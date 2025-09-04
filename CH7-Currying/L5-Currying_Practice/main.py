def create_markdown_image(alt_text):
    square_bracket_alt_text = "![" + alt_text + "]"

    def inner_func(url):
        replace_url_1 = url.replace("(", "%28")
        replace_url_2 = replace_url_1.replace(")", "%29")
        alt_text_url = square_bracket_alt_text + f"({replace_url_2})"

        def inner_most_func(title=None):
            if not title is None:
                return alt_text_url.replace(")", f' "{title}")')
            else:
                return alt_text_url

        return inner_most_func

    return inner_func
